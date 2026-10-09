# ASDify

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[Prova](#prova-senza-installare) · [Installazione](#installa-per-il-tuo-agente) · [Lingue](docs/LANGUAGES.md) · [Supporto](SUPPORT.md) · [Esempi d'uso](examples/recipes.md) · [Contribuisci](CONTRIBUTING.md)

Offri al tuo agente di IA una procedura di revisione ripetibile: individuare il punto principale, eliminare il superfluo e verificare che i dettagli importanti restino intatti. ASDify è una piccola skill portatile in Markdown per risposte, traduzioni, aggiornamenti, rapporti e documentazione negli agenti di programmazione e negli editor compatibili.

## Guarda la differenza

**Prima**

> Vorremmo sottolineare che i ricavi preliminari degli abbonamenti in Brasile sono cresciuti del 12% su base annua, esclusi i rimborsi. Questi dati non sono ancora stati sottoposti a revisione contabile.

**Dopo (`full`)**

> I ricavi preliminari degli abbonamenti in Brasile sono cresciuti del 12% su base annua, esclusi i rimborsi. I dati non sono ancora stati sottoposti a revisione contabile.

*Esempio editoriale illustrativo, non un risultato misurato su un modello.* Conserva il carattere preliminare, gli abbonamenti, il Brasile, il 12%, il confronto annuo, l'esclusione dei rimborsi e l'assenza di revisione contabile. [Altri esempi prima e dopo](examples/before-after.md).

## Prova senza installare

1. Apri [SKILL.md](skills/asdify/SKILL.md), copiane il contenuto e incollalo come istruzioni in una chat, per esempio ChatGPT o Claude web. La skill canonica è in inglese.
2. Invia questo prompt:

```text
Usa asdify full. Riscrivi questo aggiornamento per la direzione.
Restituisci solo il testo rivisto. Conserva tutti i fatti e le precisazioni.

Vorremmo sottolineare che i ricavi preliminari degli abbonamenti in Brasile
sono cresciuti del 12% su base annua, esclusi i rimborsi. Questi dati non sono
ancora stati sottoposti a revisione contabile.
```

La formulazione può variare; fatti e precisazioni devono restare intatti. È una prova manuale, senza installazione automatica. Consulta [un'esecuzione reale in Codex](docs/demos/codex-full-2026-10-08.md), con prompt, risultato e verifiche, in inglese.

## Installa per il tuo agente

| Metodo | Quando sceglierlo | Requisiti |
| --- | --- | --- |
| Skills CLI | Ricerca, più agenti e installazione gestita | Node.js/npm e rete per i download |
| Installatore locale | Copia controllata senza npm | Clone o ZIP estratto, Bash e strumenti POSIX |
| Copia manuale | Senza installatore, anche su Windows | Cartella completa e percorso documentato dall'agente |
| Istruzioni del progetto / regola Cursor | L'agente legge istruzioni persistenti | File di istruzioni o cartella di regole |
| Plugin Claude Code | Usi il gestore di plugin | Claude Code con supporto ai plugin |
| [Chat manuale](#prova-senza-installare) | Prova senza installazione | Chat che accetti istruzioni |

ASDify non richiede Node.js né npm. La Skills CLI facoltativa può chiedere conferma prima di scaricare il proprio pacchetto npm. Usa l'[installatore locale](INSTALL.md#local-installer) per evitare questo download; consulta l'[installazione della skill nativa di Cursor senza npm](INSTALL.md#cursor-without-nodejs-or-npm).

Usa la [Skills CLI](https://github.com/vercel-labs/skills) per trovare ASDify e installarlo:

```bash
npx skills add hevertonrodrigues/asdify --list
npx skills add hevertonrodrigues/asdify --skill asdify --agent claude-code
```

Sostituisci `claude-code` con l'[ID del tuo agente](docs/HARNESSES.md), come `codex`, `cursor`, `gemini-cli` o `opencode`. Esegui i comandi dal progetto di destinazione; aggiungi `--global` per un'installazione a livello utente, quando supportata. La [guida all'installazione](INSTALL.md) descrive ambiti, percorsi e rimozione.

Se preferisci l'installatore locale:

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
bash scripts/install.sh --list
bash scripts/install.sh --agent claude-code --scope user
```

Scegli un ID da `--list`. L'installatore copia dal clone la skill completa e i riferimenti, senza scaricare nulla. Rifiuta di sovrascrivere file esistenti se non passi `--force`.

Per le skill native di Cursor, l'ID locale è `cursor-skill`; `cursor` conserva il precedente adattatore di regole compatte del progetto. La Skills CLI usa `cursor` per le skill native. [Differenze e percorsi](INSTALL.md#cursor-native-skill-or-compact-rule).

La [tabella degli agenti](docs/HARNESSES.md) copre il registro di questa versione. I test di installazione e le sessioni reali sono registrati separatamente in [compatibilità](docs/COMPATIBILITY.md). Per altri agenti, usa il percorso documentato dal prodotto o la prova manuale sopra.

### Ambito e conferme

La CLI usa il progetto corrente per impostazione predefinita. `--global` sceglie l'utente; `--copy` richiede copie anziché collegamenti simbolici. Per più agenti usa `--agent claude-code cursor codex`. `--yes` prima di `skills` accetta il download npm; alla fine accetta le conferme della CLI:

```bash
DISABLE_TELEMETRY=1 npx --yes skills add hevertonrodrigues/asdify --skill asdify --agent cursor --global --copy --yes
```

I download necessari avvengono comunque. La CLI accetta anche una fonte locale: `npx skills add /path/to/asdify --skill asdify --agent cursor`. Consulta [tutte le opzioni](INSTALL.md#scope-copies-and-multiple-agents).

Senza Git, usa **Code → Download ZIP** su GitHub, estrai l'archivio ed esegui l'installatore da quella cartella. `--list` mostra le destinazioni; `--help` mostra le opzioni. Per la skill nativa di Cursor limitata a un progetto, esegui dal progetto di destinazione e sostituisci il percorso:

```bash
bash "/path/to/asdify/scripts/install.sh" --agent cursor-skill --scope project
```

La destinazione è `.agents/skills/asdify/`; `--scope user` usa `~/.cursor/skills/asdify/`. Controlla una copia esistente prima di usare `--force`. L'ID locale `cursor` installa la regola compatta; l'ID `cursor` della Skills CLI installa la skill nativa.

### Copia manuale e istruzioni persistenti

Copia tutta la cartella [skills/asdify/](skills/asdify/), inclusi `SKILL.md` e `references/`, nella [destinazione documentata](docs/HARNESSES.md). Crea le cartelle necessarie e controlla un'installazione esistente prima di sostituirla. Una volta ottenuti i file, non servono npm, Git o Bash.

Se l'agente legge istruzioni di progetto, integra [AGENTS.md](AGENTS.md) senza sostituire altre regole. Per Cursor, usa `bash "/path/to/asdify/scripts/install.sh" --agent cursor-rule --scope project` dal progetto di destinazione, oppure copia [cursor-rule.mdc](integrations/cursor-rule.mdc) in `.cursor/rules/asdify.mdc`. Gli adattatori compatti contengono meno dettagli della skill completa.

### Plugin Claude Code

Il repository include i manifesti del plugin e del marketplace. In una sessione di Claude Code:

```text
/plugin marketplace add hevertonrodrigues/asdify
/plugin install asdify@asdify
```

Scegli l'ambito nel gestore; è possibile anche usare un [clone locale](INSTALL.md#claude-code-plugin). I manifesti superano la validazione, ma un'installazione e attivazione reali del plugin non sono state verificate.

## Ambienti supportati

La [tabella completa](docs/HARNESSES.md) elenca **82 ID: 79 mappature di agenti e 3 ID di compatibilità**, con destinazioni, ambiti e fonti. Include Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, OpenCode, Windsurf, Cline, Continue e altri.

Su Windows, usa la CLI o la copia manuale. Lo script richiede Bash/POSIX; con WSL, installa dove l'agente legge i suoi file. La matrice automatizzata copre Linux/macOS; l'esecuzione su Windows non è stata verificata. Per agenti remoti o nel cloud, usa skill di progetto nel repository o il loro metodo di distribuzione documentato. `universal` è una convenzione di cartella, non una garanzia per ogni applicazione.

Dopo l'installazione apri una nuova sessione e chiedi `Usa asdify full`. In Cursor controlla **Customize → Skills**. Una copia riuscita non dimostra da sola l'attivazione; consulta [compatibilità](docs/COMPATIBILITY.md).

## Aggiornamento e rimozione

| Metodo | Aggiornare | Rimuovere |
| --- | --- | --- |
| Skills CLI | `npx skills update asdify` | `npx skills remove asdify --agent <id>`; aggiungi `--global` per l'utente |
| Installatore locale | Ottieni i file aggiornati, controlla e ripeti con lo stesso agente/ambito e `--force` | Rimuovi solo la cartella o regola ASDify indicata |
| Copia manuale / istruzioni | Controlla e sostituisci la cartella o il testo ASDify | Rimuovi solo quella cartella o quelle istruzioni |
| Plugin Claude Code | Usa l'aggiornamento del gestore | Disattiva o disinstalla `asdify@asdify` |

Nella Skills CLI, aggiungi `--global` anche per aggiornare un'installazione utente. Le cartelle condivise interessano tutti gli agenti che le leggono. Conserva le modifiche personali prima di sostituire una copia. [Comandi e percorsi](INSTALL.md#removal-and-updates).

## Come lavora ASDify

Identifica il lettore, segna ciò che va conservato, applica la minima modifica utile e controlla il significato. Mantieni numeri, date, condizioni, incertezze e termini tecnici necessari. Lascia invariato ciò che è già chiaro. Non inventare consigli, decisioni o scadenze durante una riscrittura.

| Modalità | Quando usarla | Cosa cambia |
| --- | --- | --- |
| `lite` | Vuoi una revisione leggera | La formulazione; conserva struttura, ordine e tono. |
| `full` · predefinita | Vuoi una risposta più chiara | La formulazione e la struttura, quando utile. |
| `ultra` | Il testo contiene introduzioni o sezioni inutili | Revisione più intensa, con le stesse regole di conservazione. |

Richiedi una modalità con `Usa asdify lite`, `full` o `ultra`. `asdify off` disattiva questo flusso facoltativo, nel rispetto delle altre istruzioni dell'agente. Le modalità sono istruzioni; il supporto dei comandi nativi varia.

## Lingue e traduzione

Sono disponibili READMEs e casi di regressione in inglese, portoghese brasiliano, spagnolo, francese, tedesco, giapponese, cinese semplificato, italiano e russo. Installa la stessa skill canonica per tutte le lingue; non servono pacchetti linguistici. Le riscritture mantengono la lingua originale salvo richiesta di traduzione.

```text
Usa asdify full. Traduci in italiano (it).
Restituisci solo la traduzione. Conserva tutti i fatti e le precisazioni.

Preliminary subscription revenue grew 12% year over year in Brazil,
excluding refunds. These figures are unaudited.
```

Specifica la lingua o la variante di destinazione. La traduzione conserva significato, identificatori, segnaposto e formato richiesto, adattando grammatica e registro. Consulta gli [esempi multilingue](examples/multilingual.md) e la [copertura linguistica e il supporto](docs/LANGUAGES.md). La qualità dipende dal modello dell'agente; i test del pacchetto non la verificano.

## Applicazioni pratiche

| Attività | Cosa proteggere | Prompt completo |
| --- | --- | --- |
| Aggiornamento per la direzione | Stato, responsabili, scadenze provvisorie e condizioni | [`full` · EN](examples/recipes.md#1-executive-update-en) |
| Raccomandazione tecnica | Identificatori, attore, sequenza e raccomandazione rispetto a obbligo | [`lite` · PT-BR](examples/recipes.md#2-technical-recommendation-pt-br) |
| Documento decisionale denso | Stime, esclusioni e approvazioni necessarie | [`ultra` · EN](examples/recipes.md#3-dense-decision-brief-en) |
| Messaggio già chiaro | Formulazione originale, se non servono modifiche | [Nessuna modifica · EN](examples/recipes.md#4-leave-clear-text-alone-en) |

## Verifica e supporto

Nello studio di 900 casi con una versione fissa della skill, `full` ha superato il **98,33%** dei controlli automatici rigorosi, contro il **93,22%** senza la skill.

Una risposta più breve che modifica un fatto importante non supera la valutazione. Il repository include casi di riscrittura e traduzione in nove lingue, una griglia per la revisione umana e un [protocollo di valutazione riproducibile](benchmarks/README.md). Il [protocollo multilingue dei modi](benchmarks/multilingual-modes/README.md) prevede, per il confronto iniziale, 100 nuovi casi in ciascuna delle nove lingue (900 in totale): `lite`, `full`, `ultra` e `off` vengono confrontati con un controllo senza istruzioni ASDify, per 3.600 prove dei modi e 4.500 risposte complessive, controllo incluso. Sono previste due revisioni in cieco per ogni risposta, con modelli della stessa famiglia del modello che le genera. **L'affidabilità generale e i miglioramenti di qualità su larga scala restano da dimostrare.** Consulta i [risultati e gli archivi](benchmarks/results/README.md), la [verifica del pacchetto](docs/VERIFICATION.md) e la [compatibilità](docs/COMPATIBILITY.md).

| Problema | Dove chiedere aiuto |
| --- | --- |
| Conferma npm, ID, percorso, sovrascrittura o rilevamento | [Diagnosi](INSTALL.md#troubleshooting) · [Segnalazione di installazione](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md) |
| Fatti persi, obblighi cambiati, lingua errata o contenuto inventato | [Modifica del significato](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) |
| README tradotto errato o obsoleto | [Traduzione della documentazione](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml) |
| Nuova lingua, agente, esempio o miglioramento | [Richiesta](https://github.com/hevertonrodrigues/asdify/issues/new?template=feature_request.md) · [Contribuire](CONTRIBUTING.md) |
| Vulnerabilità o informazioni private | [Sicurezza e segnalazione privata](SECURITY.md) |

Includi comando o prompt, risultato effettivo, versioni del sistema/agente, modalità, ambito e lingue di origine/destinazione se pertinenti. Rimuovi le informazioni private. Il testo già chiaro può restare uguale. Consulta [SUPPORT.md](SUPPORT.md) e [supporto linguistico](docs/LANGUAGES.md). Problemi di account, fatturazione o servizio dell'agente spettano al suo fornitore.

Le guide complementari collegate sono in inglese, salvo gli esempi indicati in PT-BR. Questa traduzione non ha ancora ricevuto una revisione indipendente da parte di un madrelingua italiano.

[Roadmap](docs/ROADMAP.md) · [Registro delle modifiche](CHANGELOG.md) · [Licenza MIT](LICENSE)
