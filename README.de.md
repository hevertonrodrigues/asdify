# ASDify

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[Ausprobieren](#ohne-installation-ausprobieren) · [Installation](#für-deinen-agenten-installieren) · [Sprachen](docs/LANGUAGES.md) · [Support](SUPPORT.md) · [Anwendungsbeispiele](examples/recipes.md) · [Mitwirken](CONTRIBUTING.md)

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

| Weg | Wann wählen | Voraussetzungen |
| --- | --- | --- |
| Skills CLI | Suche, mehrere Agenten und verwaltete Installation | Node.js/npm und Netzwerk für Downloads |
| Lokaler Installer | Geprüfte Kopien ohne npm | Klon oder entpacktes ZIP, Bash und POSIX-Werkzeuge |
| Manuelle Kopie | Ohne Installer, auch unter Windows | Vollständiger Ordner und dokumentierter Zielpfad |
| Projektanweisungen / Cursor-Regel | Der Agent liest dauerhafte Anweisungen | Anweisungsdatei oder Regelverzeichnis |
| Claude-Code-Plugin | Du nutzt die Plugin-Verwaltung | Claude Code mit Plugin-Unterstützung |
| [Manueller Chat](#ohne-installation-ausprobieren) | Versuch ohne Installation | Chat, der Anweisungen annimmt |

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

### Geltungsbereich und Bestätigungen

Die CLI verwendet standardmäßig das aktuelle Projekt. `--global` wählt den Benutzerbereich; `--copy` erstellt Kopien statt symbolischer Links. Für mehrere Agenten verwende `--agent claude-code cursor codex`. `--yes` vor `skills` bestätigt den npm-Download; am Ende bestätigt es die Installation durch die CLI:

```bash
DISABLE_TELEMETRY=1 npx --yes skills add hevertonrodrigues/asdify --skill asdify --agent cursor --global --copy --yes
```

Benötigte Dateien werden weiterhin heruntergeladen. Auch eine lokale Quelle ist möglich: `npx skills add /path/to/asdify --skill asdify --agent cursor`. Siehe [alle Optionen](INSTALL.md#scope-copies-and-multiple-agents).

Ohne Git kannst du auf GitHub **Code → Download ZIP** wählen, das Archiv entpacken und den Installer dort ausführen. `--list` zeigt Ziele, `--help` zeigt Optionen. Für einen nativen Cursor-Skill nur im Projekt führe diesen Befehl im Zielprojekt aus und ersetze den Quellpfad:

```bash
bash "/path/to/asdify/scripts/install.sh" --agent cursor-skill --scope project
```

Das Ziel ist `.agents/skills/asdify/`; `--scope user` nutzt `~/.cursor/skills/asdify/`. Prüfe eine bestehende Kopie vor `--force`. Die lokale ID `cursor` installiert die kompakte Regel; die Skills-CLI-ID `cursor` installiert den nativen Skill.

### Manuelle Kopie und dauerhafte Anweisungen

Kopiere den gesamten Ordner [skills/asdify/](skills/asdify/), einschließlich `SKILL.md` und `references/`, an das [dokumentierte Ziel](docs/HARNESSES.md). Erstelle nötige Verzeichnisse und prüfe bestehende Installationen vor dem Ersetzen. Sobald die Dateien vorliegen, brauchst du weder npm noch Git oder Bash.

Liest der Agent Projektanweisungen, ergänze [AGENTS.md](AGENTS.md), ohne andere Regeln zu ersetzen. Für Cursor nutze `bash "/path/to/asdify/scripts/install.sh" --agent cursor-rule --scope project` im Zielprojekt oder kopiere [cursor-rule.mdc](integrations/cursor-rule.mdc) nach `.cursor/rules/asdify.mdc`. Die kompakten Adapter enthalten weniger Details als der vollständige Skill.

### Claude-Code-Plugin

Das Repository enthält Plugin- und Marketplace-Manifeste. In einer Claude-Code-Sitzung:

```text
/plugin marketplace add hevertonrodrigues/asdify
/plugin install asdify@asdify
```

Wähle den Geltungsbereich in der Verwaltung; auch ein [lokaler Klon](INSTALL.md#claude-code-plugin) ist möglich. Die Manifeste bestehen die Validierung; eine echte Plugin-Installation und Aktivierung wurden noch nicht geprüft.

## Unterstützte Umgebungen

Die [vollständige Tabelle](docs/HARNESSES.md) umfasst **82 IDs: 79 Agentenzuordnungen und 3 Kompatibilitäts-IDs**, mit Zielen, Geltungsbereichen und Quellen. Dazu gehören Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, OpenCode, Windsurf, Cline, Continue und weitere.

Unter Windows nutze die CLI oder kopiere manuell. Das Skript benötigt Bash/POSIX; mit WSL installiere dort, wo der Agent seine Dateien liest. Die automatisierte Matrix deckt Linux/macOS ab; Windows-Ausführung wurde nicht geprüft. Für entfernte oder Cloud-Agenten nutze Projekt-Skills im Repository oder deren dokumentierten Verteilungsweg. `universal` ist eine Ordnerkonvention, keine Garantie für jede Anwendung.

Starte nach der Installation eine neue Sitzung und fordere `Nutze asdify full` an. Prüfe in Cursor **Customize → Skills**. Erfolgreiches Kopieren allein beweist keine Aktivierung; siehe [Kompatibilität](docs/COMPATIBILITY.md).

## Aktualisieren und entfernen

| Weg | Aktualisieren | Entfernen |
| --- | --- | --- |
| Skills CLI | `npx skills update asdify` | `npx skills remove asdify --agent <id>`; für Benutzerinstallation `--global` ergänzen |
| Lokaler Installer | Aktuelle Dateien holen, prüfen und mit gleichem Agenten/Geltungsbereich sowie `--force` erneut installieren | Nur den angezeigten ASDify-Ordner oder die Regel entfernen |
| Manuelle Kopie / Anweisungen | Ordner oder ASDify-Text prüfen und ersetzen | Nur diesen Ordner oder diese Anweisungen entfernen |
| Claude-Code-Plugin | Aktualisierung in der Verwaltung nutzen | `asdify@asdify` deaktivieren oder deinstallieren |

Bei der Skills CLI nutze `--global` auch zum Aktualisieren einer Benutzerinstallation. Geteilte Verzeichnisse betreffen alle Agenten, die sie lesen. Sichere eigene Änderungen vor dem Ersetzen. [Befehle und Pfade](INSTALL.md#removal-and-updates).

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

| Problem | Hilfe |
| --- | --- |
| npm-Bestätigung, ID, Pfad, Überschreiben oder Erkennung | [Fehlersuche](INSTALL.md#troubleshooting) · [Installationsbericht](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md) |
| Verlorene Fakten, geänderte Pflicht, falsche Sprache oder erfundener Inhalt | [Bedeutungsänderung](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) |
| Fehlerhaftes oder veraltetes übersetztes README | [Dokumentationsübersetzung](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml) |
| Neue Sprache, neuer Agent, Beispiel oder Verbesserung | [Anfrage](https://github.com/hevertonrodrigues/asdify/issues/new?template=feature_request.md) · [Mitwirken](CONTRIBUTING.md) |
| Schwachstelle oder private Angaben | [Sicherheitsrichtlinie und private Meldung](SECURITY.md) |

Nenne Befehl oder Prompt, tatsächliche Ausgabe, System-/Agentenversionen, Modus, Geltungsbereich und gegebenenfalls Ausgangs-/Zielsprache. Entferne private Informationen. Klarer Text darf unverändert bleiben. Siehe [SUPPORT.md](SUPPORT.md) und [Sprachsupport](docs/LANGUAGES.md). Probleme mit Konto, Abrechnung oder Agentendienst gehören zum jeweiligen Anbieter.

Die verlinkten ergänzenden Anleitungen sind auf Englisch, außer den als PT-BR markierten Beispielen. Diese Übersetzung wurde noch nicht unabhängig von einer Person mit Deutsch als Muttersprache geprüft.

[Roadmap](docs/ROADMAP.md) · [Änderungsverlauf](CHANGELOG.md) · [MIT-Lizenz](LICENSE)
