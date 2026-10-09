# ASDify

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[试用](#无需安装即可试用) · [安装](#为你的智能体安装) · [语言](docs/LANGUAGES.md) · [支持](SUPPORT.md) · [使用示例](examples/recipes.md) · [参与贡献](CONTRIBUTING.md)

为你的AI智能体提供一套可重复使用的编辑流程：找出重点，删除空话，检查重要细节是否保留。ASDify是一项小巧、可移植的Markdown技能，适用于兼容的编程智能体和编辑器中的回答、翻译、进展更新、报告和文档。

## 看看修改效果

**修改前**

> 我们想强调的是，巴西的初步订阅收入同比增长12%，不包括退款。这些数据尚未经审计。

**修改后（`full`）**

> 巴西的初步订阅收入同比增长12%，不包括退款。这些数据尚未经审计。

*这是用于说明编辑原则的示例，并非测得的模型输出。* 它保留了初步数据、订阅收入、巴西、12%、同比、排除退款以及未经审计这些信息。[查看更多修改前后示例](examples/before-after.md)。

## 无需安装即可试用

1. 打开[SKILL.md](skills/asdify/SKILL.md)，复制内容，并作为指令粘贴到ChatGPT或Claude网页版等聊天中。权威版本的技能文件使用英语。
2. 发送以下提示词：

```text
使用asdify full，为管理层改写这段进展更新。
只返回改写后的文本。保留所有事实和限定条件。

我们想强调的是，巴西的初步订阅收入同比增长12%，不包括退款。
这些数据尚未经审计。
```

措辞可以不同，但事实和限定条件必须保留。这是手动试用，不会自动安装技能。[一次真实的Codex运行记录](docs/demos/codex-full-2026-10-08.md)提供了提示词、输出及保留信息的检查结果，内容为英语。

## 为你的智能体安装

| 方法 | 适用场景 | 所需条件 |
| --- | --- | --- |
| Skills CLI | 查找技能、选择多个智能体并管理安装 | Node.js/npm及下载所需的网络 |
| 本地安装脚本 | 无需npm，进行带检查的文件复制 | 克隆或已解压的ZIP、Bash、POSIX工具 |
| 手动复制 | 无需安装器，也适用于Windows | 完整技能文件夹和智能体规定的路径 |
| 项目指令／Cursor规则 | 智能体读取持久指令 | 指令文件或规则目录 |
| Claude Code插件 | 使用插件管理器 | 支持插件的Claude Code |
| [手动聊天](#无需安装即可试用) | 不安装即可试用 | 能接收指令的聊天界面 |

ASDify本身不需要Node.js或npm。可选的Skills CLI可能会在下载其npm包前要求确认。使用[本地安装脚本](INSTALL.md#local-installer)即可避免这项下载；也可参阅[无需npm的Cursor原生技能安装方法](INSTALL.md#cursor-without-nodejs-or-npm)。

使用[Skills CLI](https://github.com/vercel-labs/skills)查找并安装ASDify：

```bash
npx skills add hevertonrodrigues/asdify --list
npx skills add hevertonrodrigues/asdify --skill asdify --agent claude-code
```

将`claude-code`替换为你的[智能体ID](docs/HARNESSES.md)，例如`codex`、`cursor`、`gemini-cli`或`opencode`。在目标项目中运行；如支持用户级安装，可添加`--global`。有关安装范围、路径和卸载，请参阅[安装指南](INSTALL.md)。

如果更愿意使用本地安装脚本：

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
bash scripts/install.sh --list
bash scripts/install.sh --agent claude-code --scope user
```

从`--list`中选择ID。脚本从克隆的仓库复制完整技能和参考文件，不进行下载。除非传入`--force`，否则拒绝覆盖现有文件。

对于Cursor原生技能，本地ID为`cursor-skill`；`cursor`保留早期的精简项目规则适配器。Skills CLI使用`cursor`安装原生技能。[查看区别和路径](INSTALL.md#cursor-native-skill-or-compact-rule)。

[智能体表](docs/HARNESSES.md)列出了本版本注册表中的目标。安装测试和实际会话分别记录在[兼容性说明](docs/COMPATIBILITY.md)中。对于表中没有的智能体，使用其文档指定的技能路径，或使用上述手动试用方法。

### 安装范围和确认

CLI默认安装到当前项目。`--global`选择用户范围；`--copy`使用文件复制而非符号链接。多个智能体可用`--agent claude-code cursor codex`。放在`skills`之前的`--yes`接受npm下载确认；末尾的`--yes`接受CLI自身的安装确认：

```bash
DISABLE_TELEMETRY=1 npx --yes skills add hevertonrodrigues/asdify --skill asdify --agent cursor --global --copy --yes
```

需要时仍会下载文件。CLI也接受本地来源：`npx skills add /path/to/asdify --skill asdify --agent cursor`。参阅[全部选项](INSTALL.md#scope-copies-and-multiple-agents)。

没有Git时，可在GitHub选择**Code → Download ZIP**，解压后在该目录运行脚本。`--list`显示目标；`--help`显示选项。只在某个项目安装Cursor原生技能时，从目标项目运行以下命令，并替换源路径：

```bash
bash "/path/to/asdify/scripts/install.sh" --agent cursor-skill --scope project
```

目标为`.agents/skills/asdify/`；`--scope user`使用`~/.cursor/skills/asdify/`。先检查现有副本，再使用`--force`。本地ID `cursor`安装精简规则；Skills CLI的ID `cursor`安装原生技能。

### 手动复制和持久指令

将整个[skills/asdify/](skills/asdify/)文件夹，包括`SKILL.md`和`references/`，复制到[文档规定的目标](docs/HARNESSES.md)。按需创建父目录，并在替换前检查已有安装。取得文件后，无需npm、Git或Bash。

如果智能体读取项目指令，可合并[AGENTS.md](AGENTS.md)，保留其他规则。对于Cursor，在目标项目运行`bash "/path/to/asdify/scripts/install.sh" --agent cursor-rule --scope project`，或将[cursor-rule.mdc](integrations/cursor-rule.mdc)复制到`.cursor/rules/asdify.mdc`。精简适配器的内容少于完整技能。

### Claude Code插件

仓库包含插件和插件市场清单。在Claude Code会话中运行：

```text
/plugin marketplace add hevertonrodrigues/asdify
/plugin install asdify@asdify
```

在管理器中选择安装范围；也可使用[本地克隆](INSTALL.md#claude-code-plugin)。清单通过了结构验证，但尚未验证实际的插件安装与激活。

## 支持的环境

[完整表格](docs/HARNESSES.md)列出**82个ID：79个智能体映射和3个兼容ID**，包括目标路径、范围和信息来源。涵盖Claude Code、Cursor、Codex、Gemini CLI、GitHub Copilot、OpenCode、Windsurf、Cline、Continue等。

在Windows上使用CLI或手动复制。脚本需要Bash/POSIX环境；使用WSL时，应安装到智能体读取文件的环境。自动测试矩阵覆盖Linux/macOS，尚未验证Windows执行。远程或云端智能体应使用检出的项目技能或其文档规定的分发机制。`universal`是文件夹约定，不保证任何应用都能发现技能。

安装后，打开新会话并要求`使用asdify full`。在Cursor中查看**Customize → Skills**。成功复制文件并不等于已激活；参阅[兼容性记录](docs/COMPATIBILITY.md)。

## 更新与移除

| 方法 | 更新 | 移除 |
| --- | --- | --- |
| Skills CLI | `npx skills update asdify` | `npx skills remove asdify --agent <id>`；用户安装添加`--global` |
| 本地脚本 | 获取更新文件，检查后以相同智能体和范围加`--force`重新运行 | 只删除脚本显示的ASDify文件夹或规则 |
| 手动复制／指令 | 检查并替换ASDify文件夹或文本 | 只删除该文件夹或这些指令 |
| Claude Code插件 | 使用管理器的更新操作 | 禁用或卸载`asdify@asdify` |

使用Skills CLI更新用户安装时，也应添加`--global`。共享目录的更改会影响所有读取它的智能体。替换前保留自己的修改。参阅[管理命令和路径](INSTALL.md#removal-and-updates)。

## ASDify如何编辑

确定读者，标记必须保留的信息，进行最小的有效修改，再检查含义。保留数字、日期、条件、不确定性和必要的技术术语。已经清楚的文本保持原样。改写时不要编造建议、决定或截止时间。

| 模式 | 适用场景 | 修改内容 |
| --- | --- | --- |
| `lite` | 只需轻微修改 | 修改措辞，保留结构、顺序和语气。 |
| `full` · 默认 | 需要更清楚的回答 | 在有帮助时修改措辞和结构。 |
| `ultra` | 存在多余的开场或章节 | 更积极地精简，但遵守相同的信息保留规则。 |

通过`使用asdify lite`、`full`或`ultra`指定模式。`asdify off`关闭这套可选编辑流程，但仍须遵守智能体的其他指令。模式是指令；原生命令支持因产品而异。

## 语言与翻译

仓库提供英语、巴西葡萄牙语、西班牙语、法语、德语、日语、简体中文、意大利语和俄语的README及回归测试输入。所有语言使用同一个权威版本的技能，无需语言包。除非要求翻译，改写会保留原文语言。

```text
使用asdify full，翻译成简体中文（zh-CN）。
只返回译文。保留所有事实和限定条件。

Preliminary subscription revenue grew 12% year over year in Brazil,
excluding refunds. These figures are unaudited.
```

请指定目标语言或地区、文字变体。翻译会保留含义、标识符、占位符和指定格式，同时调整语法和语体。参阅[多语言示例](examples/multilingual.md)以及[语言覆盖与支持](docs/LANGUAGES.md)。翻译质量取决于智能体使用的模型；软件包测试不会验证翻译质量。

## 实际应用

| 任务 | 需要保留的内容 | 完整提示词 |
| --- | --- | --- |
| 管理层进展更新 | 状态、负责人、暂定期限和条件 | [`full` · 英语](examples/recipes.md#1-executive-update-en) |
| 技术建议 | 标识符、执行者、步骤顺序、建议与义务的区别 | [`lite` · PT-BR](examples/recipes.md#2-technical-recommendation-pt-br) |
| 内容密集的决策简报 | 估计值、排除项和审批要求 | [`ultra` · 英语](examples/recipes.md#3-dense-decision-brief-en) |
| 已经清楚的消息 | 无需修改时保留原文 | [不修改示例 · 英语](examples/recipes.md#4-leave-clear-text-alone-en) |

## 验证与支持

在使用固定技能版本的900案例研究中，`full`通过严格自动评估的比例为**98.33%**，不使用技能的对照组为**93.22%**。

如果更短的回答改变了重要事实，就不能通过评估。[四种模式的研究](benchmarks/multilingual-modes/README.md)为九种输出语言各使用100个新案例，将相同的900个不同案例分别用于`lite`、`full`、`ultra`、`off`及不使用技能的对照条件，共计3,600次模式测试和4,500份回答。评审由与生成模型同一系列的模型进行两轮盲评。参阅[已记录的测试](benchmarks/results/README.md)和[可复现的评估流程](benchmarks/README.md)。案例为合成文本，部分场景结构在不同语言中重复，因此不能将所有观察结果视为相互独立。**普遍可靠性和广泛的质量提升仍未得到证明。** [软件包验证](docs/VERIFICATION.md)和[兼容性说明](docs/COMPATIBILITY.md)涵盖其他检查。

| 问题 | 获取帮助 |
| --- | --- |
| npm确认、ID、路径、覆盖或技能发现 | [排查指南](INSTALL.md#troubleshooting) · [安装报告](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md) |
| 事实丢失、义务变化、语言错误或编造内容 | [含义变化报告](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) |
| README误译或信息过时 | [文档翻译报告](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml) |
| 新语言、智能体、示例或改进 | [功能请求](https://github.com/hevertonrodrigues/asdify/issues/new?template=feature_request.md) · [贡献步骤](CONTRIBUTING.md) |
| 漏洞或私密信息 | [安全政策及私密报告](SECURITY.md) |

请提供命令或提示词、实际输出、系统及智能体版本、模式、范围，以及相关的源语言和目标语言。删除私密信息。已经清楚的文本可以保持不变。参阅[SUPPORT.md](SUPPORT.md)和[语言支持](docs/LANGUAGES.md)。账户、账单及智能体服务问题应联系其提供方。

链接的补充指南使用英语，标注PT-BR的示例除外。本译文尚无中文母语者独立审阅的记录。

[路线图](docs/ROADMAP.md) · [更新日志](CHANGELOG.md) · [MIT许可证](LICENSE)
