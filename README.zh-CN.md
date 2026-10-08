# ASDify

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[试用](#无需安装即可试用) · [安装](#为你的智能体安装) · [语言](docs/LANGUAGES.md) · [使用示例](examples/recipes.md) · [参与贡献](CONTRIBUTING.md)

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

如果更短的回答改变了重要事实，就不能通过评估。仓库包含九种语言的改写和翻译回归测试输入、人工评审标准及[可复现的评估流程](benchmarks/README.md)。**尚未证明真实模型的输出质量有所提升。** 参阅[软件包验证](docs/VERIFICATION.md)和[兼容性说明](docs/COMPATIBILITY.md)。

发现条件丢失、数字变化或编造承诺时，请附上原文、实际输出、源语言和目标语言，[报告含义变化](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml)。本README的错误请通过[文档翻译表单](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml)报告。贡献步骤见[CONTRIBUTING.md](CONTRIBUTING.md)。

链接的补充指南使用英语，标注PT-BR的示例除外。本译文尚无中文母语者独立审阅的记录。

[路线图](docs/ROADMAP.md) · [更新日志](CHANGELOG.md) · [MIT许可证](LICENSE)
