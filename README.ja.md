# ASDify

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[試す](#インストールせずに試す) · [インストール](#エージェントにインストールする) · [言語](docs/LANGUAGES.md) · [サポート](SUPPORT.md) · [活用例](examples/recipes.md) · [貢献する](CONTRIBUTING.md)

AIエージェントに、要点を見つけ、不要な表現を削り、重要な情報が残っているか確認する編集手順を与えます。ASDifyは、対応するコーディングエージェントやエディターで、回答、翻訳、進捗報告、レポート、文書を整えるための、小さく持ち運びやすいMarkdownスキルです。

## 編集の例

**編集前**

> お伝えしたいのは、ブラジルのサブスクリプション売上の速報値が、返金分を除き、前年比12%増加したという点です。この数値はまだ監査されていません。

**編集後（`full`）**

> ブラジルのサブスクリプション売上の速報値は、返金分を除き、前年比12%増加しました。この数値はまだ監査されていません。

*編集方針を示す例であり、モデルで測定した結果ではありません。* 速報値、サブスクリプション売上、ブラジル、12%、前年比、返金分の除外、未監査という情報を保持しています。[ほかの編集例](examples/before-after.md)。

## インストールせずに試す

1. [SKILL.md](skills/asdify/SKILL.md)を開き、内容をコピーして、ChatGPTやClaudeのWeb版などのチャットに指示として貼り付けます。正本のスキルは英語です。
2. 次のプロンプトを送ります。

```text
asdify fullを使って、この進捗報告を経営陣向けに書き直してください。
書き直した本文だけを返してください。すべての事実と留保を保持してください。

お伝えしたいのは、ブラジルのサブスクリプション売上の速報値が、
返金分を除き、前年比12%増加したという点です。
この数値はまだ監査されていません。
```

表現は変わっても、事実と留保は残す必要があります。これは手動の試用であり、スキルは自動インストールされません。[Codexでの実行記録](docs/demos/codex-full-2026-10-08.md)には、プロンプト、出力、情報の保持を確認した結果が英語で掲載されています。

## エージェントにインストールする

| 方法 | 適した場面 | 必要なもの |
| --- | --- | --- |
| Skills CLI | スキルの検索、複数エージェントの選択、インストール管理 | Node.js/npmとダウンロード用のネットワーク |
| ローカルインストーラー | npmを使わず、確認付きでコピーしたい | クローンまたは展開済みZIP、Bash、POSIXツール |
| 手動コピー | Windowsを含め、インストーラーを使いたくない | 完全なスキルフォルダーと製品が定めるパス |
| プロジェクトの指示／Cursorルール | エージェントが永続的な指示を読む | 指示ファイルまたはルールのディレクトリ |
| Claude Codeプラグイン | プラグイン管理を使いたい | プラグイン対応のClaude Code |
| [手動チャット](#インストールせずに試す) | インストールせずに試したい | 指示を受け付けるチャット |

ASDify自体にNode.jsやnpmは不要です。任意のSkills CLIでは、npmパッケージのダウンロード前に確認が表示されることがあります。このダウンロードを避けるには[ローカルインストーラー](INSTALL.md#local-installer)を使ってください。[npmを使わないCursorのネイティブスキルのインストール](INSTALL.md#cursor-without-nodejs-or-npm)も参照できます。

[Skills CLI](https://github.com/vercel-labs/skills)でASDifyを探し、インストールできます。

```bash
npx skills add hevertonrodrigues/asdify --list
npx skills add hevertonrodrigues/asdify --skill asdify --agent claude-code
```

`claude-code`を、`codex`、`cursor`、`gemini-cli`、`opencode`などの[エージェントID](docs/HARNESSES.md)に置き換えてください。対象プロジェクトから実行します。対応している場合、`--global`を追加するとユーザー全体の設定にインストールできます。適用範囲、パス、削除方法は[インストールガイド](INSTALL.md)を参照してください。

ローカルのインストーラーを使う場合：

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
bash scripts/install.sh --list
bash scripts/install.sh --agent claude-code --scope user
```

`--list`に表示されるIDを選びます。このインストーラーは、クローンしたリポジトリからスキル本体と参照文書をコピーします。ダウンロードは行いません。`--force`を指定しない限り、既存ファイルを上書きしません。

Cursorのネイティブスキルでは、ローカルIDは`cursor-skill`です。`cursor`は従来の簡略版プロジェクトルール用アダプターを維持します。Skills CLIでは、ネイティブスキルのIDに`cursor`を使います。[違いとパス](INSTALL.md#cursor-native-skill-or-compact-rule)を参照してください。

[エージェント一覧](docs/HARNESSES.md)は、このバージョンのレジストリに含まれる対象を示します。インストールの検証と実際のセッションは、[互換性](docs/COMPATIBILITY.md)で別々に記録します。一覧にないエージェントでは、その製品が定めるスキルのパスか、上の手動試用を使ってください。

### 適用範囲と確認

CLIは既定で現在のプロジェクトにインストールします。`--global`はユーザー単位、`--copy`はシンボリックリンクではなくコピーを選びます。複数の対象には`--agent claude-code cursor codex`を使います。`skills`の前の`--yes`はnpmのダウンロード確認、末尾の`--yes`はCLIのインストール確認を受け入れます。

```bash
DISABLE_TELEMETRY=1 npx --yes skills add hevertonrodrigues/asdify --skill asdify --agent cursor --global --copy --yes
```

必要な場合のダウンロードは引き続き行われます。ローカルのファイルも指定できます：`npx skills add /path/to/asdify --skill asdify --agent cursor`。[全オプション](INSTALL.md#scope-copies-and-multiple-agents)を参照してください。

Gitを使わない場合は、GitHubの**Code → Download ZIP**から取得し、展開したフォルダーでインストーラーを実行します。`--list`は対象一覧、`--help`は使い方を表示します。Cursorのネイティブスキルをプロジェクトだけに入れるには、対象プロジェクトから次を実行し、ソースのパスを置き換えてください。

```bash
bash "/path/to/asdify/scripts/install.sh" --agent cursor-skill --scope project
```

保存先は`.agents/skills/asdify/`です。`--scope user`では`~/.cursor/skills/asdify/`になります。既存のコピーを確認してから`--force`を使ってください。ローカルIDの`cursor`は簡略ルール、Skills CLIの`cursor`はネイティブスキルをインストールします。

### 手動コピーと永続的な指示

[skills/asdify/](skills/asdify/)フォルダー全体を、`SKILL.md`と`references/`を含めて[規定の保存先](docs/HARNESSES.md)にコピーします。必要な親フォルダーを作り、既存のインストールを確認してから置き換えてください。ファイルを取得済みなら、npm、Git、Bashは不要です。

プロジェクトの指示を読むエージェントでは、ほかのルールを残して[AGENTS.md](AGENTS.md)を統合します。Cursorでは対象プロジェクトから`bash "/path/to/asdify/scripts/install.sh" --agent cursor-rule --scope project`を使うか、[cursor-rule.mdc](integrations/cursor-rule.mdc)を`.cursor/rules/asdify.mdc`へコピーします。簡略版アダプターは、完全なスキルより情報が少なくなります。

### Claude Codeプラグイン

リポジトリにはプラグインとマーケットプレイスのマニフェストがあります。Claude Codeのセッション内で実行します。

```text
/plugin marketplace add hevertonrodrigues/asdify
/plugin install asdify@asdify
```

管理画面で適用範囲を選びます。[ローカルのクローン](INSTALL.md#claude-code-plugin)も使えます。マニフェストは検証に合格していますが、実際のプラグインのインストールと有効化は未検証です。

## 対応環境

[完全な一覧](docs/HARNESSES.md)には、**79件のエージェント対応と3件の互換ID、合計82個のID**があり、保存先、適用範囲、情報源を示しています。Claude Code、Cursor、Codex、Gemini CLI、GitHub Copilot、OpenCode、Windsurf、Cline、Continueなどを含みます。

WindowsではCLIか手動コピーを使ってください。スクリプトにはBash/POSIX環境が必要です。WSLでは、エージェントがファイルを読む環境にインストールします。自動検証はLinux/macOSを対象とし、Windowsでの実行は未検証です。リモートやクラウドのエージェントでは、チェックアウト内のプロジェクトスキルか、製品が定める配布方法を使います。`universal`はフォルダーの慣習であり、すべてのアプリでの検出を保証しません。

インストール後は新しいセッションで`asdify fullを使ってください`と依頼します。Cursorでは**Customize → Skills**を確認できます。コピーの成功だけでは有効化を証明できません。[互換性の記録](docs/COMPATIBILITY.md)を参照してください。

## 更新と削除

| 方法 | 更新 | 削除 |
| --- | --- | --- |
| Skills CLI | `npx skills update asdify` | `npx skills remove asdify --agent <id>`。ユーザー単位なら`--global`を追加 |
| ローカルインストーラー | 更新ファイルを取得して確認し、同じ対象と範囲で`--force`を付けて再実行 | 表示されたASDifyフォルダーかルールだけを削除 |
| 手動コピー／指示 | ASDifyフォルダーか指示を確認して置き換える | そのフォルダーか指示だけを削除 |
| Claude Codeプラグイン | 管理画面の更新操作を使う | `asdify@asdify`を無効化またはアンインストール |

Skills CLIでユーザー単位のインストールを更新する際も`--global`を追加します。共有フォルダーの変更は、それを読むすべてのエージェントに影響します。置き換える前に独自の編集を保存してください。[管理コマンドとパス](INSTALL.md#removal-and-updates)を参照してください。

## ASDifyの編集方針

読者を確認し、残すべき情報を特定し、必要最小限の編集を行い、意味を確認します。数値、日付、条件、不確実性、必要な専門用語を保持します。すでに明確な文章はそのままにします。書き直す際に、求められていない助言、決定、期限を作りません。

| モード | 適した場面 | 変更内容 |
| --- | --- | --- |
| `lite` | 軽い修正をしたい | 表現を修正し、構成、順序、語調を保持します。 |
| `full`・既定 | より明確な回答にしたい | 必要に応じて表現と構成を修正します。 |
| `ultra` | 不要な導入や節がある | 同じ保持ルールの下で、より積極的に削ります。 |

`asdify lite`、`full`、`ultra`を使うよう指示します。`asdify off`は、エージェントのほかの指示に従いつつ、この任意の編集手順を無効にします。モードは指示であり、ネイティブコマンドへの対応は製品によって異なります。

## 言語と翻訳

英語、ブラジルポルトガル語、スペイン語、フランス語、ドイツ語、日本語、簡体字中国語、イタリア語、ロシア語のREADMEと回帰テスト用入力を用意しています。どの言語でも同じ正本のスキルをインストールします。言語パックは不要です。翻訳を求めない限り、書き直しでは原文の言語を保持します。

```text
asdify fullを使って、日本語（ja）に翻訳してください。
翻訳文だけを返してください。すべての事実と留保を保持してください。

Preliminary subscription revenue grew 12% year over year in Brazil,
excluding refunds. These figures are unaudited.
```

翻訳先の言語や地域・表記の指定を明示してください。翻訳では意味、識別子、プレースホルダー、指定された書式を保持し、文法と文体を調整します。[多言語の例](examples/multilingual.md)と[対応言語・サポート](docs/LANGUAGES.md)を参照してください。翻訳品質はエージェントのモデルに依存し、パッケージのテストでは検証しません。

## 活用例

| 作業 | 保持する情報 | 完全なプロンプト |
| --- | --- | --- |
| 経営陣への進捗報告 | 状況、担当、暫定的な期限、条件 | [`full`・英語](examples/recipes.md#1-executive-update-en) |
| 技術的な推奨 | 識別子、行為者、順序、推奨と義務の違い | [`lite`・PT-BR](examples/recipes.md#2-technical-recommendation-pt-br) |
| 情報量の多い意思決定資料 | 見積もり、除外条件、承認要件 | [`ultra`・英語](examples/recipes.md#3-dense-decision-brief-en) |
| すでに明確なメッセージ | 変更が不要な場合の原文 | [変更しない例・英語](examples/recipes.md#4-leave-clear-text-alone-en) |

## 検証とサポート

固定版のスキルを使った900ケースの研究では、自動評価の厳格な基準を満たした割合は`full`が**98.33%**、スキルなしが**93.22%**でした。

短くなっても、重要な事実が変われば評価に不合格となります。[4モードの研究](benchmarks/multilingual-modes/README.md)では、9つの出力言語それぞれに新規100ケースを用意し、同じ900ケースを`lite`、`full`、`ultra`、`off`と、スキルを使わない対照条件で実行します。モード別のテストは計3,600件、対照を含む回答は4,500件で、生成モデルと同じ系列のモデルによるブラインド評価を2回行います。[記録済みのテスト](benchmarks/results/README.md)と[再現可能な評価手順](benchmarks/README.md)を参照してください。ケースは人工的に作成され、一部のシナリオ構成が言語間で共通するため、すべての観測を独立したものとして扱うことはできません。**一般的な信頼性や幅広い品質向上は、まだ実証されていません。** [パッケージの検証](docs/VERIFICATION.md)と[互換性](docs/COMPATIBILITY.md)は別の確認を扱います。

| 問題 | 相談先 |
| --- | --- |
| npmの確認、ID、パス、上書き、スキルの検出 | [トラブル対応](INSTALL.md#troubleshooting)・[インストール報告](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md) |
| 事実の欠落、義務の変更、言語の間違い、情報の捏造 | [意味の変更の報告](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) |
| READMEの誤訳や古い情報 | [文書翻訳の報告](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml) |
| 言語、エージェント、例、動作の改善 | [機能の提案](https://github.com/hevertonrodrigues/asdify/issues/new?template=feature_request.md)・[貢献手順](CONTRIBUTING.md) |
| 脆弱性や非公開の情報 | [セキュリティ方針と非公開の報告](SECURITY.md) |

コマンドまたはプロンプト、実際の出力、OSとエージェントのバージョン、モード、適用範囲、必要に応じて原文と翻訳先の言語を記載します。個人情報や非公開情報は除いてください。すでに明確な文章は変更されないことがあります。[SUPPORT.md](SUPPORT.md)と[言語サポート](docs/LANGUAGES.md)を参照してください。アカウント、請求、エージェントのサービス障害は、その提供元に問い合わせてください。

リンク先の補足ガイドは、PT-BRと明記した例を除き英語です。この翻訳について、日本語を母語とする人による独立したレビューはまだ記録されていません。

[ロードマップ](docs/ROADMAP.md) · [変更履歴](CHANGELOG.md) · [MITライセンス](LICENSE)
