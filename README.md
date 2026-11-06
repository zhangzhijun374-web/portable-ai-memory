# Portable AI Memory

**A portable, user-owned memory system for AI assistants.**

Organize long-term context from conversations, documents, and project files into a structured archive that can be reviewed, updated, backed up, and reused across compatible AI tools.

> Your context should belong to you—not to a single AI account.

[简体中文](#简体中文) · [English](#english)

---

## 简体中文

### 为什么需要它？

换一个 AI 助手时，用户经常需要重新介绍自己的背景、偏好和项目。重要决定散落在聊天记录里，旧信息与新信息容易冲突，而平台内置记忆通常不能直接迁移。

Portable AI Memory 把这个过程变成一套可重复的工作流：

**收集资料 → 提取长期信息 → 分类去重 → 隐私检查 → 建立档案 → 持续更新 → 备份迁移**

它不是聊天记录的简单压缩，也不是某个平台 Memory 的替代品。它生成的是用户自己掌握的、可阅读和可编辑的长期上下文档案。

### 核心能力

- 从用户提供的聊天导出、文件和项目资料中提取长期上下文。
- 将个人背景、偏好、项目、决策、流程和待办分开管理。
- 为信息标注来源、可信度、时效和核验状态。
- 检测重复信息和相互冲突的记录。
- 更新现有档案并保留变更历史。
- 生成 Markdown 档案、JSON manifest 和 ZIP 备份。
- 为切换 AI 账号或平台准备迁移说明和启动提示词。
- 通过隐私规则避免将凭证和不必要的敏感信息写入档案。

### 安装

本项目遵循 Agent Skills 的 `SKILL.md` 目录格式。不同 AI 客户端的安装入口和能力可能不同，请以目标客户端当前文档为准。

**在 Codex 仓库级使用：**

将本项目的 Skill 文件夹放入目标仓库的：

```text
.agents/skills/portable-ai-memory/
```

至少保留 `SKILL.md`；建议同时保留 `references/` 和 `templates/`。

**全局使用：**

部分兼容客户端支持用户级 Skill 目录。请查看对应客户端的官方说明，不要假定所有客户端使用相同路径。

**ChatGPT / Codex：**

当前 OpenAI 文档说明，Skills 以 `SKILL.md` 加可选资源组成；独立 Skill 和通过插件分发的 Skill，其可用入口有所不同。参考：
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Agent Skills overview](https://agentskills.io/home)

### 快速使用

安装后，可以这样请求：

```text
请使用 Portable AI Memory，基于我提供的历史对话和项目文件，
为我建立一套长期记忆档案。

请先检查资料范围和隐私风险，再提取稳定背景、长期偏好、
项目状态、关键决策和待确认事项。

输出模块化 Markdown 文件、来源登记、更新日志和 ZIP 备份。
不要把计划写成已完成事实，也不要编造缺失信息。
```

常用任务：

```text
/bootstrap  根据当前可用资料建立新档案
/update     将新项目进展合并到现有档案
/migrate    为切换 AI 账号准备迁移包
/audit      检查档案的冲突、过期信息和隐私风险
/selective  只整理某个项目或时间范围
```

以上是建议的任务表达方式，不是所有客户端都支持的真实命令。

### 档案结构

推荐的个人档案结构：

```text
memory/
├── README.md
├── manifest.json
├── profile.md
├── preferences.md
├── projects/
├── workflows/
├── decisions/
├── status/
├── sources/
└── CHANGELOG.md
```

可以从 `templates/` 复制模板开始。不要为了凑齐目录而创建没有实际内容的文件。

### 重要原则

1. 用户拥有自己的记忆文件。
2. 不假定 AI 能访问用户的全部历史聊天。
3. 重要信息保留来源和核验状态。
4. 不把计划、推测或旧版本结果写成当前事实。
5. 不保存密码、API Key、令牌或私钥。
6. 未经用户明确同意，不把个人档案公开到 GitHub。
7. 文件迁移不等于平台账号、订阅或内部 Memory 迁移。

### 项目结构

- `SKILL.md`：核心工作流。
- `references/`：方法论、数据模型、隐私和迁移说明。
- `templates/`：可复用的记忆档案模板。
- `examples/`：完全虚构的示例档案。
- `scripts/`：本地结构检查和 ZIP 打包脚本。
- `tests/`：人工评估用例。

### 贡献

欢迎提交问题、改进模板、补充平台适配说明和测试案例。请勿在 Issue 或 Pull Request 中提交真实聊天记录、私人档案、账号导出或密钥。

详见 [CONTRIBUTING.md](CONTRIBUTING.md)、[PRIVACY.md](PRIVACY.md)、[PUBLISHING.md](PUBLISHING.md) 和 [中文设计方法论](references/design-methodology.zh-CN.md)。

---

## English

### What is Portable AI Memory?

Portable AI Memory is an Agent Skill for turning scattered conversations, documents, and project files into a structured, user-owned memory archive.

It helps people preserve useful context across AI tools without treating any platform's internal memory as the only source of truth.

### Workflow

**Collect → Extract → Classify → Deduplicate → Review privacy → Structure → Validate → Update → Export**

### Features

- Extract durable user and project context from available sources.
- Separate profile, preferences, projects, decisions, workflows, and tasks.
- Track provenance, confidence, freshness, and verification status.
- Detect duplicates and conflicts without silently overwriting history.
- Generate portable Markdown archives and JSON manifests.
- Prepare migration handoffs for another AI account or platform.
- Apply privacy-first rules and exclude credentials.

### Quick start

Install the skill in a directory supported by your AI client, then ask:

```text
Use Portable AI Memory to build a portable archive from the
conversation exports and project files I provide.

Separate confirmed facts, current plans, historical information,
and items that need verification. Preserve source references.
Review privacy risks before writing files.

Create modular Markdown files, a source register, a changelog,
and a ZIP backup. Do not invent missing information.
```

### Compatibility

The project follows the Agent Skills folder convention. Compatibility depends on each host's implementation and available file tools. A shared `SKILL.md` does not guarantee identical behavior across every AI product.

### Privacy

Do not publish real personal memory archives, chat exports, credentials, or private project documents. The included example data is synthetic.

---

## License

MIT. See [LICENSE](LICENSE).
