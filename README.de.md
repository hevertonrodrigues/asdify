# ASDify

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[Ausprobieren](#ohne-installation-ausprobieren) · [Installation](#für-deinen-agenten-installieren) · [Sprachen](docs/LANGUAGES.md) · [Anwendungsbeispiele](examples/recipes.md) · [Mitwirken](CONTRIBUTING.md)

Gib deinem KI-Agenten einen wiederholbaren Ablauf zum Überarbeiten: den Kern finden, Fülltext entfernen und prüfen, ob die wichtigen Details erhalten bleiben. ASDify ist ein kleiner, portabler Markdown-Skill für Antworten, Übersetzungen, Statusmeldungen, Berichte und Dokumentation in unterstützten Programmieragenten und Editoren.

## Den Unterschied sehen

**Vorher**

> Wir möchten darauf hinweisen, dass der vorläufige Abonnementumsatz in Brasilien im Jahresvergleich um 12% gestiegen ist, ohne Berücksichtigung von Rückerstattungen. Diese Zahlen sind noch nicht geprüft.

**Nachher (`full`)**

> Der vorläufige Abonnementumsatz in Brasilien stieg im Jahresvergleich um 12%, ohne Berücksichtigung von Rückerstattungen. Die Zahlen sind noch nicht geprüft.

*Redaktionelles Beispiel zur Veranschaulichung, kein gemessenes Modellergebnis.* Vorläufiger Stand, Abonnements, Brasilien, 12%, Jahresvergleich, ausgeschlossene Rückerstattungen und fehlende Prüfung bleiben erhalten. [Weitere Vorher-Nachher-Beispiele](examples/before-after.md).

## Ohne Installation ausprobieren

1. Öffne [SKILL.md](skills/asdify/SKILL.md), kopiere den Inhalt und füge ihn als Anweisungen in einen Chat ein, etwa ChatGPT oder Claude im Web. Der kanonische Skill ist auf Englisch.
2. Sende diesen Prompt:

```text
Nutze asdify full. Überarbeite diese Statusmeldung für die Geschäftsleitung.
Gib nur den überarbeiteten Text zurück. Erhalte alle Fakten und Einschränkungen.

Wir möchten darauf hinweisen, dass der vorläufige Abonnementumsatz
in Brasilien im Jahresvergleich um 12% gestiegen ist, ohne Berücksichtigung
von Rückerstattungen. Diese Zahlen sind noch nicht geprüft.
```

Die Formulierung kann variieren; Fakten und Einschränkungen müssen erhalten bleiben. Dies ist ein manueller Versuch ohne automatische Skill-Installation. Ein [echter Codex-Durchlauf](docs/demos/codex-full-2026-10-08.md) zeigt Prompt, Ausgabe und Prüfungen auf Englisch.

## Für deinen Agenten installieren

ASDify benötigt weder Node.js noch npm. Die optionale Skills CLI kann vor dem Download ihres npm-Pakets um Bestätigung bitten. Mit dem [lokalen Installer](INSTALL.md#local-installer) vermeidest du diesen Download; siehe auch die [Installation des nativen Cursor-Skills ohne npm](INSTALL.md#cursor-without-nodejs-or-npm).

Nutze die [Skills CLI](https://github.com/vercel-labs/skills), um ASDify zu finden und zu installieren:

```bash
npx skills add hevertonrodrigues/asdify --list
npx skills add hevertonrodrigues/asdify --skill asdify --agent claude-code
```

Ersetze `claude-code` durch deine [Agenten-ID](docs/HARNESSES.md), zum Beispiel `codex`, `cursor`, `gemini-cli` oder `opencode`. Führe die Befehle im Zielprojekt aus; füge `--global` für eine benutzerweite Installation hinzu, wenn unterstützt. Die [Installationsanleitung](INSTALL.md) erklärt Geltungsbereiche, Pfade und Entfernung.

Falls du den lokalen Installer bevorzugst:

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
bash scripts/install.sh --list
bash scripts/install.sh --agent claude-code --scope user
```

Wähle eine ID aus `--list`. Dieser Installer kopiert den vollständigen Skill mit Referenzen aus dem Klon, ohne Downloads. Bestehende Dateien werden nur mit `--force` überschrieben.

Für native Cursor-Skills lautet die lokale ID `cursor-skill`; `cursor` behält den bisherigen kompakten Projektregel-Adapter bei. Die Skills CLI verwendet `cursor` für native Skills. [Unterschiede und Pfade](INSTALL.md#cursor-native-skill-or-compact-rule).

Die [Agententabelle](docs/HARNESSES.md) deckt den Registerstand dieser Version ab. Installationstests und echte Sitzungen werden unter [Kompatibilität](docs/COMPATIBILITY.md) getrennt erfasst. Für andere Agenten verwende ihren dokumentierten Skill-Pfad oder den manuellen Versuch oben.

## Wie ASDify überarbeitet

Bestimme den Leser, markiere unverzichtbare Angaben, mache die kleinste hilfreiche Änderung und prüfe die Bedeutung. Erhalte Zahlen, Daten, Bedingungen, Unsicherheit und notwendige Fachbegriffe. Lass bereits klaren Text stehen. Erfinde beim Überarbeiten keine Ratschläge, Entscheidungen oder Fristen.

| Modus | Wann verwenden | Was sich ändert |
| --- | --- | --- |
| `lite` | Du willst leichte Korrekturen | Formulierung; Aufbau, Reihenfolge und Ton bleiben erhalten. |
| `full` · Standard | Du willst eine klarere Antwort | Formulierung und Aufbau, wenn hilfreich. |
| `ultra` | Unnötige Einleitungen oder Abschnitte stören | Stärkere Kürzung mit denselben Erhaltungsregeln. |

Fordere einen Modus mit `Nutze asdify lite`, `full` oder `ultra` an. `asdify off` deaktiviert diesen optionalen Ablauf unter den übrigen Agentenanweisungen. Modi sind Anweisungen; die Unterstützung nativer Befehle variiert.

## Sprachen und Übersetzung

READMEs und Regressionseingaben gibt es für Englisch, brasilianisches Portugiesisch, Spanisch, Französisch, Deutsch, Japanisch, vereinfachtes Chinesisch, Italienisch und Russisch. Installiere für alle denselben kanonischen Skill; Sprachpakete sind nicht nötig. Beim Überarbeiten bleibt die Ausgangssprache erhalten, sofern du keine Übersetzung anforderst.

```text
Nutze asdify full. Übersetze ins Deutsche (de).
Gib nur die Übersetzung zurück. Erhalte alle Fakten und Einschränkungen.

Preliminary subscription revenue grew 12% year over year in Brazil,
excluding refunds. These figures are unaudited.
```

Nenne die Zielsprache oder Sprachvariante. Die Übersetzung erhält Bedeutung, Bezeichner, Platzhalter und gewünschtes Format und passt Grammatik und Register an. Siehe [mehrsprachige Beispiele](examples/multilingual.md) sowie [Sprachabdeckung und Support](docs/LANGUAGES.md). Die Qualität hängt vom Modell des Agenten ab; Pakettests prüfen sie nicht.

## Anwenden

| Aufgabe | Was erhalten bleiben muss | Vollständiger Prompt |
| --- | --- | --- |
| Statusmeldung für die Geschäftsleitung | Stand, Zuständigkeit, vorläufige Fristen und Bedingungen | [`full` · EN](examples/recipes.md#1-executive-update-en) |
| Technische Empfehlung | Bezeichner, Akteur, Reihenfolge und Empfehlung gegenüber Pflicht | [`lite` · PT-BR](examples/recipes.md#2-technical-recommendation-pt-br) |
| Dichte Entscheidungsvorlage | Schätzungen, Ausschlüsse und erforderliche Freigaben | [`ultra` · EN](examples/recipes.md#3-dense-decision-brief-en) |
| Bereits klare Nachricht | Originalformulierung, wenn keine Änderung hilft | [Unverändert · EN](examples/recipes.md#4-leave-clear-text-alone-en) |

## Prüfung und Support

Eine kürzere Antwort, die eine wesentliche Tatsache verändert, besteht die Bewertung nicht. Das Repository enthält Überarbeitungs- und Übersetzungsfälle in neun Sprachen, einen menschlichen Bewertungsmaßstab und ein [reproduzierbares Bewertungsverfahren](benchmarks/README.md). **Qualitätsgewinne mit echten Modellen sind noch nicht nachgewiesen.** Siehe [Paketprüfung](docs/VERIFICATION.md) und [Kompatibilität](docs/COMPATIBILITY.md).

Eine Bedingung fehlt, eine Zahl wurde verändert oder ein Versprechen erfunden? [Melde die Bedeutungsänderung](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) mit Quelle, tatsächlicher Ausgabe sowie Ausgangs- und Zielsprache. Für Fehler in diesem README nutze das [Formular für Dokumentationsübersetzungen](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml). Hinweise zum Mitwirken stehen in [CONTRIBUTING.md](CONTRIBUTING.md).

Die verlinkten ergänzenden Anleitungen sind auf Englisch, außer den als PT-BR markierten Beispielen. Diese Übersetzung wurde noch nicht unabhängig von einer Person mit Deutsch als Muttersprache geprüft.

[Roadmap](docs/ROADMAP.md) · [Änderungsverlauf](CHANGELOG.md) · [MIT-Lizenz](LICENSE)
