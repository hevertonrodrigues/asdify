# ASDify

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[試す](#インストールせずに試す) · [インストール](#エージェントにインストールする) · [言語](docs/LANGUAGES.md) · [活用例](examples/recipes.md) · [貢献する](CONTRIBUTING.md)

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

短くなっても、重要な事実が変われば評価に不合格となります。リポジトリには、9言語の書き直し・翻訳の回帰テスト用入力、人による評価基準、[再現可能な評価手順](benchmarks/README.md)があります。**実際のモデルで品質が向上するという比較結果は、まだ確立されていません。** [パッケージの検証](docs/VERIFICATION.md)と[互換性](docs/COMPATIBILITY.md)を参照してください。

条件の欠落、数値の変更、根拠のない約束を見つけた場合は、原文、実際の出力、原文と翻訳先の言語を添えて[意味の変更を報告](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml)してください。このREADMEの誤訳には[文書翻訳の報告フォーム](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml)を使います。貢献の手順は[CONTRIBUTING.md](CONTRIBUTING.md)を参照してください。

リンク先の補足ガイドは、PT-BRと明記した例を除き英語です。この翻訳について、日本語を母語とする人による独立したレビューはまだ記録されていません。

[ロードマップ](docs/ROADMAP.md) · [変更履歴](CHANGELOG.md) · [MITライセンス](LICENSE)
