# ASDify

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[Prova](#prova-senza-installare) · [Installazione](#installa-per-il-tuo-agente) · [Lingue](docs/LANGUAGES.md) · [Esempi d'uso](examples/recipes.md) · [Contribuisci](CONTRIBUTING.md)

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

Una risposta più breve che modifica un fatto importante non supera la valutazione. Il repository include casi di riscrittura e traduzione in nove lingue, una griglia di revisione umana e un [protocollo di valutazione riproducibile](benchmarks/README.md). **Non sono ancora stati dimostrati miglioramenti di qualità con modelli reali.** Consulta la [verifica del pacchetto](docs/VERIFICATION.md) e la [compatibilità](docs/COMPATIBILITY.md).

Hai trovato una condizione persa, un numero cambiato o una promessa inventata? [Segnala la modifica del significato](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) con la fonte, il risultato effettivo e le lingue di origine e destinazione. Per errori in questo README usa il [modulo per la traduzione della documentazione](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml). Consulta [CONTRIBUTING.md](CONTRIBUTING.md) per contribuire.

Le guide complementari collegate sono in inglese, salvo gli esempi indicati in PT-BR. Questa traduzione non ha ancora ricevuto una revisione indipendente da parte di un madrelingua italiano.

[Roadmap](docs/ROADMAP.md) · [Registro delle modifiche](CHANGELOG.md) · [Licenza MIT](LICENSE)
