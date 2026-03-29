# Dingyi X Operator

[English README](README.md)

> 面向 Codex、Claude Code 和 OpenClaw 的跨平台 X/Twitter 运营 skill。

[![Release](https://img.shields.io/github/v/release/fuyalan126/dingyi-x-operator)](https://github.com/fuyalan126/dingyi-x-operator/releases)
[![License](https://img.shields.io/github/license/fuyalan126/dingyi-x-operator)](LICENSE)
[![Platforms](https://img.shields.io/badge/platform-Codex%20%7C%20Claude%20Code%20%7C%20OpenClaw-111827)](README.md)

`dingyi-x-operator` 是一个偏重信号质量、审美判断和声誉安全的 X/Twitter 运营 agent。

适合谁：

- 不想把 X 做成低质自动化互动的 founder、builder、operator
- 想用 AI 帮自己做回复、原创帖子、资料改写和配图规划的人
- 正在使用 Codex、Claude Code、OpenClaw 作为 agent 运行环境的用户

它能做什么：

- 找出值得互动的高质量推文
- 起草更具体、更像真人的回复
- 规划原创帖子和线程
- 把外部资料转换成适合 X 的内容
- 在中英文之间做内容适配
- 判断帖子是否需要配图，并输出视觉 brief
- 通过 `opencli` 执行已经确认过的动作

## 快速开始

把对应平台的 adapter 复制到你的 skills 目录：

```bash
# Codex
cp -R "/path/to/repo/dingyi-x-operator/codex" "$HOME/.codex/skills/dingyi-x-operator"

# Claude Code
cp -R "/path/to/repo/dingyi-x-operator/claude-code" "$HOME/.claude/skills/dingyi-x-operator"

# OpenClaw
cp -R "/path/to/repo/dingyi-x-operator/openclaw" "/path/to/openclaw/skills/dingyi-x-operator"
```

然后用下面两个模板开始配置本地状态：

- `dingyi-x-operator/templates/PROFILE.example.md`
- `dingyi-x-operator/templates/MEMORY.example.md`

## 这个仓库是什么

这个仓库采用了“单一真源 + 多端适配”的结构，兼容：

- Codex
- Claude Code
- OpenClaw

共享的核心逻辑在：

- [`dingyi-x-operator/core/SKILL.md`](dingyi-x-operator/core/SKILL.md)

各平台的可安装入口在：

- [`dingyi-x-operator/codex/SKILL.md`](dingyi-x-operator/codex/SKILL.md)
- [`dingyi-x-operator/claude-code/SKILL.md`](dingyi-x-operator/claude-code/SKILL.md)
- [`dingyi-x-operator/openclaw/SKILL.md`](dingyi-x-operator/openclaw/SKILL.md)

这样做的好处是：

- `core/` 保持唯一真源
- 每个平台都有一份可独立安装的完整 skill
- 以后更新时可以从共享核心重新生成各端副本

## 仓库结构

```text
dingyi-x-operator/
  core/
    SKILL.md
    references/
  codex/
    SKILL.md
    agents/openai.yaml
  claude-code/
    SKILL.md
  openclaw/
    SKILL.md
  templates/
    PROFILE.example.md
    MEMORY.example.md
marketing/
  release-kit.md
  banner-brief.md
```

## 核心依赖

要执行真实的 X 操作，至少需要：

- `opencli`
- 正在运行的 Chrome
- OpenCLI 浏览器桥接扩展
- 一个已经登录 X 的浏览器会话

如果你的环境支持，下面这些辅助 skill 也很有价值：

- `social-media-strategist`
- `content-creator`
- `twitter-engager`
- `baoyu-url-to-markdown`
- `baoyu-translate`

## 安装方式

推荐做法：把对应平台的 adapter 复制或软链接到你的 skills 目录。

这样做的原因：

- 每个平台入口在运行时都是自包含的
- 不强依赖 symlink 才能工作
- 共享的 `core/` 更新后，可以通过脚本重新生成 adapter

### Codex

```bash
cp -R "/path/to/repo/dingyi-x-operator/codex" "$HOME/.codex/skills/dingyi-x-operator"
```

### Claude Code

```bash
cp -R "/path/to/repo/dingyi-x-operator/claude-code" "$HOME/.claude/skills/dingyi-x-operator"
```

### OpenClaw

把 `openclaw/` 目录安装到你的 OpenClaw skills 路径即可。

示例：

```bash
cp -R "/path/to/repo/dingyi-x-operator/openclaw" "/path/to/openclaw/skills/dingyi-x-operator"
```

如果你更喜欢软链接，当然也可以。

## 自定义配置

不要把真实账号的运行记忆、偏好设置或本地私密状态提交到仓库里。

建议从下面两个模板开始：

- [`dingyi-x-operator/templates/PROFILE.example.md`](dingyi-x-operator/templates/PROFILE.example.md)
- [`dingyi-x-operator/templates/MEMORY.example.md`](dingyi-x-operator/templates/MEMORY.example.md)

常见的本地放置位置包括：

- `$X_OPERATOR_STATE_DIR/PROFILE.md`
- `$X_OPERATOR_STATE_DIR/MEMORY.md`
- `.x-operator/PROFILE.md`
- `.x-operator/MEMORY.md`
- `~/.x-operator/PROFILE.md`
- `~/.x-operator/MEMORY.md`
- `.dingyi-x-operator/PROFILE.md`
- `.dingyi-x-operator/MEMORY.md`
- `~/.dingyi-x-operator/PROFILE.md`
- `~/.dingyi-x-operator/MEMORY.md`

对新安装用户，更推荐：

- 使用 `.x-operator/` 或 `~/.x-operator/`
- 如果你有多个项目或多个账号，优先使用 `X_OPERATOR_STATE_DIR`
- `dingyi-x-operator` 旧路径只作为兼容回退保留

## 设计原则

- 重质量，不重数量
- 公开操作默认先出 shortlist，再执行
- 写操作前先做 preflight 检查
- 发帖前必须确认最终文案
- 配图规划是内建能力
- 出图只是可选执行层，不是这个 agent 的核心定义

## 内置参考资料

核心 skill 自带这些可复用参考文件：

- execution modes
- profile template
- memory template
- output templates
- visual strategy

## 发布素材

仓库还带了两份轻量发布素材：

- [`marketing/release-kit.md`](marketing/release-kit.md)
- [`marketing/banner-brief.md`](marketing/banner-brief.md)

## 维护方式

如果你修改了 `core/` 里的共享内容，可以用下面这条命令重新生成三端 adapter：

```bash
python3 dingyi-x-operator/scripts/build_adapters.py
```

## 许可证

本仓库使用 [MIT License](LICENSE)。

## 贡献说明

贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 暂未包含

- 安装脚本
- CI 工作流
- 发布自动化

这些可以等仓库结构稳定后再补。
