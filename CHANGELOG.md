# 更新日志

本文件依据 git tag 历史整理，版本号遵循[语义化版本](https://semver.org/lang/zh-CN/)。
新提交合入后请在 `## [Unreleased]` 下记录，发布时随版本 tag 归档。

## [Unreleased]

## [4.0.12] - 2026-06-25
- feat(metadata): 补充网易云登录/登出命令冷却声明

## [4.0.11] - 2026-06-24
- fix sing callback task key mismatch
- feat(knowledge): 声明 knowledge_sources FAQ 供 LLM 注入

## [4.0.10] - 2026-06-21
- fix(chat): route drunk chat through unified llm submit

## [4.0.9] - 2026-06-21
- fix: align sing play callback request ids

## [4.0.8] - 2026-06-19
- docs(assets): 更新头像资源并改用 PyPI 版本徽章
- fix(sing): 补充媒体请求诊断并提升纯唱歌命中优先级
- chore(assets): 替换品牌头像为透明背景版本
- chore(release): 发布 4.0.8

## [4.0.7] - 2026-06-19
- chore(release): 4.0.2 同步 README 进 PyPI 包
- migrate: src.* → pallas.api.* / pallas.product.* / pallas.core.*
- release: bump to 4.0.3 for pallas import migration
- docs(readme): 更新官方扩展安装命令
- docs(readme): 统一官方插件卡片模板
- fix(ai-media): 修复 4.0 主仓兼容与任务回调问题
- chore(release): 发布 4.0.7

## [4.0.6] - 2026-06-19
- docs(ai-media): 统一文档与元数据
- fix(sing): 修复 AI 媒体插件 task_id 回调断链
- chore(release): 发布 4.0.3
- chore(release): 发布 4.0.6

## [4.0.5] - 2026-06-18
- docs(readme): 统一官方插件卡片模板

## [4.0.4] - 2026-06-18
- docs(readme): 更新官方扩展安装命令

## [4.0.3] - 2026-06-18
- migrate: src.* → pallas.api.* / pallas.product.* / pallas.core.*
- release: bump to 4.0.3 for pallas import migration

## [4.0.2] - 2026-06-18
- fix(sing): 移除 ncm_login 未使用的 PluginMetadata 导入
- chore: ruff format ai-media 插件源码
- docs(readme): 添加 Pallas-Bot hero 图
- chore(release): 4.0.2 同步 README 进 PyPI 包

## [4.0.1] - 2026-06-17
- feat: Pallas-Bot 4.0 官方扩展首包
- fix(build): 修正 hatch wheel 的 src 包路径
- feat(release): PyPI 发版 workflow 与 4.0.1
