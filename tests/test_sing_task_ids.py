from __future__ import annotations

import sys
import types
from pathlib import Path

import importlib

import pytest


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


def _install_stub(name: str, module: types.ModuleType) -> None:
    sys.modules[name] = module


def _bootstrap_stub_modules() -> None:
    nonebot = types.ModuleType("nonebot")
    nonebot.logger = types.SimpleNamespace(info=lambda *a, **k: None, warning=lambda *a, **k: None)
    nonebot.on_message = lambda *a, **k: types.SimpleNamespace(handle=lambda: (lambda fn: fn), finish=None)
    _install_stub("nonebot", nonebot)

    adapters = types.ModuleType("nonebot.adapters")
    adapters.Bot = object
    adapters.Event = object
    _install_stub("nonebot.adapters", adapters)

    ob11 = types.ModuleType("nonebot.adapters.onebot.v11")
    ob11.GroupMessageEvent = object
    ob11.permission = types.SimpleNamespace(GROUP=object())
    _install_stub("nonebot.adapters.onebot.v11", ob11)

    plugin = types.ModuleType("nonebot.plugin")
    plugin.PluginMetadata = lambda **kwargs: kwargs
    _install_stub("nonebot.plugin", plugin)

    rule = types.ModuleType("nonebot.rule")
    rule.Rule = lambda fn: fn
    _install_stub("nonebot.rule", rule)

    typing_mod = types.ModuleType("nonebot.typing")
    typing_mod.T_State = dict
    _install_stub("nonebot.typing", typing_mod)

    ulid = types.ModuleType("ulid")
    ulid.ULID = lambda: "local-request-id"
    _install_stub("ulid", ulid)

    cmd_defaults = types.ModuleType("src.features.cmd_perm.metadata_defaults")
    cmd_defaults.PLUGIN_EXTRA_VERSION = "4.0.1"
    cmd_defaults.PLUGIN_HOMEPAGE = "https://example.com"
    cmd_defaults.PLUGIN_MENU_TEMPLATE = "default"
    _install_stub("src.features.cmd_perm.metadata_defaults", cmd_defaults)

    cmd_text = types.ModuleType("src.features.cmd_perm.metadata_text")
    cmd_text.SCENE_GROUP = "group"
    cmd_text.SCENE_PRIVATE = "private"
    cmd_text.join_usage = lambda *lines: "\n".join(lines)
    cmd_text.usage_line = lambda text, desc: f"{text}: {desc}"
    _install_stub("src.features.cmd_perm.metadata_text", cmd_text)

    config_mod = types.ModuleType("src.foundation.config")
    config_mod.GroupConfig = object
    config_mod.TaskManager = types.SimpleNamespace(add_task=None, remove_task=None)
    _install_stub("src.foundation.config", config_mod)

    db_mod = types.ModuleType("src.foundation.db")
    db_mod.SingProgress = lambda **kwargs: types.SimpleNamespace(**kwargs)
    _install_stub("src.foundation.db", db_mod)

    utils_mod = types.ModuleType("src.shared.utils")
    utils_mod.HTTPXClient = types.SimpleNamespace(get=None, post=None)
    _install_stub("src.shared.utils", utils_mod)

    sing_config = types.ModuleType("pallas_plugin_sing.config")
    sing_config.get_sing_config = lambda: types.SimpleNamespace(
        sing_enable=True,
        sing_endpoint="/api/sing",
        play_endpoint="/api/play",
        request_endpoint="/api/request",
        sing_length=120,
        sing_speakers={"牛牛": "pallas"},
    )
    sing_config.sing_server_url = lambda cfg=None: "http://127.0.0.1:9099"
    _install_stub("pallas_plugin_sing.config", sing_config)

    ncm_login = types.ModuleType("pallas_plugin_sing.ncm_login")
    ncm_login.get_song_id = None
    ncm_login.get_song_title = None
    _install_stub("pallas_plugin_sing.ncm_login", ncm_login)


_bootstrap_stub_modules()

sing_mod = importlib.import_module("pallas_plugin_sing")  # noqa: E402


class DummyMatcher:
    def __init__(self) -> None:
        self.finished: list[str] = []

    async def finish(self, message: str) -> None:
        self.finished.append(message)


class DummyConfig:
    def __init__(self, group_id: int, cooldown: int = 10) -> None:
        self.group_id = group_id
        self.cooldown = cooldown
        self.updated_progress = None

    async def refresh_cooldown(self, _key: str) -> None:
        return None

    async def update_sing_progress(self, progress) -> None:
        self.updated_progress = progress


class DummyResponse:
    def __init__(self, task_id: str) -> None:
        self._task_id = task_id

    def json(self) -> dict[str, str]:
        return {"task_id": self._task_id}


@pytest.mark.asyncio
async def test_sync_task_id_alias_moves_task_to_remote_id(monkeypatch: pytest.MonkeyPatch) -> None:
    added: list[tuple[str, dict]] = []
    removed: list[str] = []

    async def fake_add_task(task_id: str, payload: dict) -> None:
        added.append((task_id, dict(payload)))

    async def fake_remove_task(task_id: str) -> None:
        removed.append(task_id)

    monkeypatch.setattr(sing_mod.TaskManager, "add_task", fake_add_task)
    monkeypatch.setattr(sing_mod.TaskManager, "remove_task", fake_remove_task)
    payload = {
        "bot_id": "123456",
        "group_id": 42,
        "task_type": "sing",
        "start_time": 1000.0,
    }

    await sing_mod.sync_task_id_alias("local-request-id", "remote-task-id", payload)

    assert removed == ["local-request-id"]
    assert [task_id for task_id, _ in added] == ["remote-task-id"]
    assert added[0][1]["task_type"] == "sing"
