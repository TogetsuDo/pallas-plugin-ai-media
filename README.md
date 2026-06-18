<p align="center">
  <img src="./assets/brand-avatar.png" width="220" height="220" alt="唱歌与酒后聊天">
</p>

<h1 align="center">唱歌与酒后聊天 pallas-plugin-ai-media</h1>

<p align="center">提供牛牛唱歌与酒后聊天两组 AI 媒体能力。</p>

<p align="center">
  <img alt="官方插件" src="https://img.shields.io/badge/%E5%AE%98%E6%96%B9%E6%8F%92%E4%BB%B6-FE7D37">
  <img alt="控制台插件商店" src="https://img.shields.io/badge/%E6%8E%A7%E5%88%B6%E5%8F%B0-%E6%8F%92%E4%BB%B6%E5%95%86%E5%BA%97-4EA94B">
  <img alt="安装命令" src="https://img.shields.io/badge/uv%20sync%20--extra%20plugins--ai--media-586069">
</p>

## 安装方式

需已安装 [Pallas-Bot](https://github.com/PallasBot/Pallas-Bot) `4.0` 或更高版本，并部署 [Pallas-Bot-AI](https://github.com/PallasBot/Pallas-Bot-AI)。可在控制台插件商店安装，或执行 `uv sync --extra plugins-ai-media`。

## 怎么使用

### 牛牛唱歌

| 口令 / 触发 | 场景 | 说明 |
| --- | --- | --- |
| `牛牛唱歌 歌曲名 [key=±N]` | 群内 | AI 翻唱歌曲。 |
| `牛牛继续唱` / `牛牛接着唱` | 群内 | 续唱上一首歌。 |
| `牛牛点歌 歌曲名` | 群内 | 播放网易云原曲。 |
| `牛牛什么歌` / `牛牛哪首歌` / `牛牛啥歌` | 群内 | 查询当前歌曲。 |
| `网易云登录` / `网易云登出` | 私聊 | 管理网易云登录状态。 |

### 酒后聊天

| 口令 / 触发 | 场景 | 说明 |
| --- | --- | --- |
| `@牛牛` | 群内 | 醉酒时与牛牛聊天。 |
| `牛牛 + 文本` | 群内 | 醉酒时直接和牛牛搭话。 |

> 详细用法、限制条件和可用范围以帮助为主。

## 命令权限

| 命令 ID | 默认等级 |
| --- | --- |
| `sing.ncm_login` | superuser |
| `sing.ncm_logout` | superuser |

酒后聊天没有独立命令权限，是否触发取决于醉酒状态和消息内容。

## 配置项

> 可在控制台对应插件页中修改。

- 唱歌相关配置见 [`src/pallas_plugin_sing/config.py`](./src/pallas_plugin_sing/config.py)
- 酒后聊天相关配置见 [`src/pallas_plugin_chat/config.py`](./src/pallas_plugin_chat/config.py)

## 排障

| 现象 | 处理 |
| --- | --- |
| 唱歌无语音 | 检查 AI 服务、回调链路和唱歌服务地址。 |
| 点歌失败 | 检查网易云登录状态和歌曲可用性。 |
| 酒后聊天无回复 | 确认牛牛已喝酒，且聊天服务可达。 |

## 实现

源码位置：

- [`src/pallas_plugin_sing/`](./src/pallas_plugin_sing/)
- [`src/pallas_plugin_chat/`](./src/pallas_plugin_chat/)

关键文件：

- `src/pallas_plugin_sing/__init__.py`：注册唱歌、点歌、续唱和查歌名能力。
- `src/pallas_plugin_sing/ncm_login/__init__.py`：处理网易云短信登录与登出。
- `src/pallas_plugin_chat/__init__.py`：处理醉酒状态下的聊天触发和 AI 请求。

实现要点：

- 唱歌和酒后聊天共用同一个扩展包，但触发条件、调用链路和故障点不同。
- 唱歌会记录上一首歌的进度，支持继续唱下一段。
- 酒后聊天不会常驻触发，只有牛牛处于醉酒状态时才会进入这条路径。

## 相关链接

- [主仓唱歌文档](https://PallasBot.github.io/Pallas-Bot-Docs/plugins/sing)
- [主仓酒后聊天文档](https://PallasBot.github.io/Pallas-Bot-Docs/plugins/chat)
- [Pallas-Bot-AI](https://github.com/PallasBot/Pallas-Bot-AI)
