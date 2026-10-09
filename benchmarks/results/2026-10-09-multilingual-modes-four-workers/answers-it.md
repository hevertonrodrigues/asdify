# it: all source tasks and answers

Labels below are unblinded after review. Pass requires both meaning reviews and exact checks. A flagged answer is retained unchanged.

## modes-it-001 · already_clear

Source task:

> Controlla questa istruzione. Se è già chiara, restituiscila identica e senza commenti: « Riponi i pennelli nella scatola dopo averli lavati. »

### baseline: flagged

```text
« Riponi i pennelli nella scatola dopo averli lavati. »
```

Review notes: Returns the supplied clear instruction exactly. / Preserves the exact instruction and its source quotation framing.

### lite: flagged

```text
Riponi i pennelli nella scatola dopo averli lavati.
```

Review notes: Preserves the instruction's meaning but not its explicitly requested exact form. / Faithfully returns the already-clear instruction.

### full: flagged

```text
Riponi i pennelli nella scatola dopo averli lavati.
```

Review notes: Preserves the instruction's meaning but not its explicitly requested exact form. / Faithfully returns the already-clear instruction.

### ultra: flagged

```text
Riponi i pennelli nella scatola dopo averli lavati.
```

Review notes: Preserves the instruction's meaning but not its explicitly requested exact form. / Identical instruction text; both action and sequence preserved.

### off: flagged

```text
Riponi i pennelli nella scatola dopo averli lavati.
```

Review notes: Preserves the instruction's meaning but not its explicitly requested exact form. / Faithfully returns the already-clear instruction.

## modes-it-002 · permissions

Source task:

> Riscrivi in modo più diretto: I partecipanti possono portare un grembiule personale. Devono però usare gli occhiali forniti durante la dimostrazione. Il grembiule personale non è obbligatorio.

### baseline: pass

```text
Puoi portare un grembiule personale, ma non è obbligatorio. Durante la dimostrazione devi usare gli occhiali forniti.
```

### lite: pass

```text
I partecipanti possono portare un grembiule personale, ma non è obbligatorio. Durante la dimostrazione devono usare gli occhiali forniti.
```

### full: pass

```text
I partecipanti possono portare un grembiule personale, ma non è obbligatorio. Durante la dimostrazione devono usare gli occhiali forniti.
```

### ultra: pass

```text
I partecipanti possono portare un grembiule personale, ma non è obbligatorio. Durante la dimostrazione devono usare gli occhiali forniti.
```

### off: pass

```text
I partecipanti possono portare un grembiule personale, ma non è obbligatorio. Durante la dimostrazione devono usare gli occhiali forniti.
```

## modes-it-003 · conditions

Source task:

> Semplifica questa regola fittizia: Il cortile può essere aperto solo quando il passaggio è stato liberato e il referente ha dato il consenso. Liberare il passaggio, da solo, non autorizza l’apertura.

### baseline: pass

```text
Puoi aprire il cortile solo se il passaggio è libero e il referente ha dato il consenso. Il passaggio libero non basta.
```

### lite: pass

```text
Il cortile può essere aperto solo quando il passaggio è libero e il referente ha dato il consenso. Liberare il passaggio non basta per autorizzare l’apertura.
```

### full: pass

```text
Il cortile può essere aperto solo quando il passaggio è libero e il referente ha dato il consenso. Liberare il passaggio non basta per autorizzare l’apertura.
```

### ultra: pass

```text
Il cortile può essere aperto solo quando il passaggio è libero e il referente ha dato il consenso. Liberare il passaggio non basta.
```

### off: pass

```text
Il cortile può essere aperto solo se il passaggio è stato liberato e il referente ha dato il consenso. Liberare il passaggio non basta per autorizzare l’apertura.
```

## modes-it-004 · negation

Source task:

> Rendi chiaro il messaggio: Non annullare la prenotazione se manca il numero del tavolo. Il posto è già confermato. Devi aggiungere soltanto il numero quando verrà assegnato.

### baseline: pass

```text
La prenotazione è già confermata: non annullarla se manca il numero del tavolo. Aggiungi solo il numero quando verrà assegnato.
```

### lite: pass

```text
Non annullare la prenotazione se manca il numero del tavolo: il posto è già confermato. Devi solo aggiungere il numero quando verrà assegnato.
```

### full: pass

```text
Non annullare la prenotazione: il posto è già confermato anche senza il numero del tavolo. Devi solo aggiungere il numero quando verrà assegnato.
```

### ultra: pass

```text
Non annullare la prenotazione: il posto è già confermato, anche senza numero del tavolo. Devi solo aggiungere il numero quando verrà assegnato.
```

### off: pass

```text
Non annullare la prenotazione: il posto è già confermato, anche se manca il numero del tavolo. Devi solo aggiungere il numero quando verrà assegnato.
```

## modes-it-005 · exceptions

Source task:

> Riscrivi: Per prendere in prestito una borsa serve una cauzione. Le borse usate soltanto all’interno del laboratorio sono esenti. Se la borsa viene portata fuori, la cauzione diventa necessaria.

### baseline: pass

```text
Per prendere in prestito una borsa serve una cauzione, tranne se la usi solo all’interno del laboratorio. Se la porti fuori, devi versare la cauzione.
```

### lite: pass

```text
Per prendere in prestito una borsa serve una cauzione. La cauzione non serve se la borsa viene usata solo all’interno del laboratorio. Se viene portata fuori, la cauzione è necessaria.
```

### full: pass

```text
Per prendere in prestito una borsa serve una cauzione, salvo se viene usata solo all’interno del laboratorio. Se viene portata fuori, la cauzione è necessaria.
```

### ultra: pass

```text
Per prendere in prestito una borsa serve una cauzione, salvo se viene usata solo all’interno del laboratorio. Se viene portata fuori, la cauzione è necessaria.
```

### off: pass

```text
Per prendere in prestito una borsa serve una cauzione, salvo quando la borsa viene usata solo all’interno del laboratorio. Se viene portata fuori, la cauzione è necessaria.
```

## modes-it-006 · unknown_actor

Source task:

> Chiarisci senza attribuire azioni non indicate: Marta ha segnalato la pagina mancante lunedì. Il fascicolo è stato completato martedì. Mercoledì, Davide lo ha consegnato. Non sappiamo chi abbia aggiunto la pagina.

### baseline: pass

```text
Lunedì Marta ha segnalato la pagina mancante. Martedì il fascicolo è stato completato, ma non sappiamo chi abbia aggiunto la pagina. Mercoledì Davide ha consegnato il fascicolo.
```

### lite: pass

```text
Marta ha segnalato la pagina mancante lunedì. Il fascicolo è stato completato martedì. Mercoledì, Davide ha consegnato il fascicolo. Non sappiamo chi abbia aggiunto la pagina.
```

### full: pass

```text
Lunedì Marta ha segnalato la pagina mancante. Martedì il fascicolo è stato completato. Mercoledì Davide lo ha consegnato. Non sappiamo chi abbia aggiunto la pagina.
```

### ultra: pass

```text
Lunedì Marta ha segnalato la pagina mancante. Martedì il fascicolo è stato completato. Mercoledì Davide lo ha consegnato. Non sappiamo chi abbia aggiunto la pagina.
```

### off: pass

```text
Lunedì Marta ha segnalato la pagina mancante. Martedì il fascicolo è stato completato, ma non sappiamo chi abbia aggiunto la pagina. Mercoledì Davide ha consegnato il fascicolo.
```

## modes-it-007 · sequence

Source task:

> Scrivi tre passaggi: Salva prima la bozza, poi controlla gli importi con un collega e invia il preventivo soltanto dopo il controllo.

### baseline: pass

```text
1. Salva la bozza.
2. Controlla gli importi con un collega.
3. Invia il preventivo soltanto dopo il controllo.
```

### lite: pass

```text
1. Salva la bozza.
2. Controlla gli importi con un collega.
3. Invia il preventivo soltanto dopo il controllo.
```

### full: pass

```text
1. Salva la bozza.
2. Controlla gli importi con un collega.
3. Invia il preventivo soltanto dopo il controllo.
```

### ultra: pass

```text
1. Salva la bozza.
2. Controlla gli importi con un collega.
3. Invia il preventivo soltanto dopo il controllo.
```

### off: pass

```text
1. Salva la bozza.
2. Controlla gli importi con un collega.
3. Invia il preventivo soltanto dopo il controllo.
```

## modes-it-008 · uncertainty

Source task:

> Riscrivi con precisione: La vibrazione potrebbe dipendere dal supporto allentato. Non lo abbiamo verificato. Abbiamo provato il dispositivo soltanto senza carico, per dieci minuti.

### baseline: pass

```text
La vibrazione potrebbe dipendere dal supporto allentato, ma questa ipotesi non è stata verificata. Il dispositivo è stato provato soltanto senza carico, per dieci minuti.
```

### lite: pass

```text
La vibrazione potrebbe dipendere dal supporto allentato, ma non lo abbiamo verificato. Abbiamo provato il dispositivo soltanto senza carico, per dieci minuti.
```

### full: pass

```text
La vibrazione potrebbe dipendere dal supporto allentato, ma non lo abbiamo verificato. Abbiamo provato il dispositivo solo senza carico, per dieci minuti.
```

### ultra: pass

```text
La vibrazione potrebbe dipendere dal supporto allentato, ma non lo abbiamo verificato. Abbiamo provato il dispositivo solo senza carico, per dieci minuti.
```

### off: pass

```text
La vibrazione potrebbe dipendere dal supporto allentato, ma questa ipotesi non è stata verificata. Abbiamo provato il dispositivo soltanto senza carico, per dieci minuti.
```

## modes-it-009 · estimates

Source task:

> Accorcia senza promettere una data: Stimiamo da 3 a 5 giorni lavorativi per riordinare i fascicoli, se l’elenco arriva entro mercoledì. Non abbiamo stimato il tempo per ricostruire le etichette mancanti.

### baseline: pass

```text
Stimiamo 3–5 giorni lavorativi per riordinare i fascicoli, se l’elenco arriva entro mercoledì. La stima non include la ricostruzione delle etichette mancanti, i cui tempi non sono stati stimati.
```

### lite: pass

```text
Stimiamo 3–5 giorni lavorativi per riordinare i fascicoli, se l’elenco arriva entro mercoledì. Non abbiamo stimato il tempo per ricostruire le etichette mancanti.
```

### full: pass

```text
Stimiamo 3–5 giorni lavorativi per riordinare i fascicoli, se l’elenco arriva entro mercoledì. Il tempo per ricostruire le etichette mancanti non è stato stimato.
```

### ultra: pass

```text
Stimiamo 3–5 giorni lavorativi per riordinare i fascicoli, se l’elenco arriva entro mercoledì. Il tempo per ricostruire le etichette mancanti non è stato stimato.
```

### off: pass

```text
Stimiamo 3–5 giorni lavorativi per riordinare i fascicoli, se l’elenco arriva entro mercoledì. La stima non include la ricostruzione delle etichette mancanti, per cui non abbiamo stimato i tempi.
```

## modes-it-010 · numbers_units

Source task:

> Rendi più leggibile il prezzo: Il noleggio costa 27 € per giorno e per pannello. Il prezzo comprende il supporto ma non il montaggio. Anche una giornata iniziata viene conteggiata interamente.

### baseline: pass

```text
Noleggio: 27 € al giorno per pannello.
- Supporto incluso.
- Montaggio escluso.
- Ogni giornata iniziata viene conteggiata per intero.
```

### lite: pass

```text
Il noleggio costa 27 € al giorno per pannello. Il prezzo comprende il supporto, ma non il montaggio. Anche una giornata iniziata viene conteggiata per intero.
```

### full: pass

```text
Il noleggio costa 27 € al giorno per pannello. Il supporto è incluso; il montaggio è escluso. Ogni giornata iniziata viene conteggiata per intero.
```

### ultra: pass

```text
Il noleggio costa 27 € al giorno per pannello, supporto incluso e montaggio escluso. Ogni giornata iniziata si paga per intero.
```

### off: pass

```text
Il noleggio costa 27 € al giorno per ciascun pannello. Il supporto è incluso; il montaggio è escluso. Ogni giornata iniziata viene addebitata per intero.
```

## modes-it-011 · denominators

Source task:

> Spiega il risultato senza cambiare il denominatore: Su 88 richieste esaminate, 22 erano incomplete. Di queste 22, 4 erano arrivate via posta. Non è noto quante richieste totali siano arrivate via posta.

### baseline: pass

```text
Delle 88 richieste esaminate, 22 erano incomplete, pari al 25 %. Tra queste 22 richieste incomplete, 4 erano arrivate via posta: 4/22, circa il 18,2 %. Non conoscendo il totale delle richieste arrivate via posta, non si può calcolare quale percentuale di esse fosse incompleta.
```

### lite: pass

```text
Delle 88 richieste esaminate, 22 erano incomplete: il 25 %. Tra queste 22 richieste incomplete, 4 erano arrivate via posta, cioè circa il 18,2 %. Non è noto il totale delle richieste arrivate via posta, quindi non si può calcolare quale percentuale di esse fosse incompleta.
```

### full: pass

```text
Su 88 richieste esaminate, 22 erano incomplete: il 25 %. Tra queste 22, 4 erano arrivate via posta, cioè circa il 18,2 % delle richieste incomplete. Non è noto il totale delle richieste arrivate via posta, quindi non si può calcolare quale percentuale di queste fosse incompleta.
```

### ultra: pass

```text
22 richieste su 88 erano incomplete: il 25 %. Tra le 22 incomplete, 4 erano arrivate via posta. Non conoscendo il totale delle richieste arrivate via posta, non si può calcolare quale percentuale fosse incompleta.
```

### off: pass

```text
Su 88 richieste esaminate, 22 erano incomplete: il 25% del totale. Tra le 22 richieste incomplete, 4 erano arrivate via posta, cioè circa il 18,2% delle incomplete. Non è noto il numero totale delle richieste arrivate via posta, quindi non si può calcolare quale percentuale di queste fosse incompleta.
```

## modes-it-012 · sampling

Source task:

> Descrivi i limiti di questa rilevazione fittizia: 29 persone hanno risposto volontariamente all’uscita di una mostra, tra le 15 e le 16. Non sono state selezionate a caso e chi è uscito prima non è stato contattato.

### baseline: pass

```text
La rilevazione comprende solo 29 persone che hanno risposto volontariamente all’uscita tra le 15 e le 16. La partecipazione volontaria e l’assenza di selezione casuale possono introdurre distorsioni: chi ha risposto potrebbe differire da chi non ha partecipato. Inoltre, chi è uscito prima non è stato contattato. I risultati descrivono i rispondenti, ma non possono essere considerati rappresentativi di tutti i visitatori.
```

### lite: pass

```text
La rilevazione fittizia comprende 29 persone che hanno risposto volontariamente all’uscita della mostra, tra le 15 e le 16. Non sono state selezionate a caso: chi ha scelto di rispondere potrebbe avere opinioni diverse da chi non ha risposto. Inoltre, chi è uscito prima non è stato contattato. I risultati non possono quindi essere considerati rappresentativi di tutti i visitatori.
```

### full: pass

```text
La rilevazione fittizia include 29 persone che hanno risposto volontariamente all’uscita della mostra, tra le 15 e le 16. Il campione non è casuale: chi ha scelto di rispondere potrebbe avere opinioni diverse da chi non ha risposto. Inoltre, chi è uscito prima non è stato contattato. I risultati non possono quindi essere considerati rappresentativi di tutti i visitatori.
```

### ultra: pass

```text
La rilevazione fittizia include 29 persone che hanno risposto volontariamente all’uscita della mostra tra le 15 e le 16. Il campione non è casuale ed esclude chi è uscito prima, che non è stato contattato. I risultati non sono quindi generalizzabili a tutti i visitatori.
```

### off: pass

```text
La rilevazione fittizia comprende solo 29 persone che hanno risposto volontariamente all’uscita della mostra tra le 15 e le 16. Il campione non è casuale: chi ha scelto di rispondere potrebbe avere opinioni diverse da chi non ha partecipato. Inoltre, chi è uscito prima non è stato contattato. I risultati non possono quindi essere considerati rappresentativi di tutti i visitatori.
```

## modes-it-013 · calculation

Source task:

> Un gruppo compra 8 quaderni a 6,25 € ciascuno e paga 7 € di spedizione per l’intero ordine. Qual è il totale? Mostra il calcolo.

### baseline: pass

```text
8 × 6,25 € = 50 € per i quaderni.
50 € + 7 € di spedizione = 57 € totali.
```

### lite: pass

```text
Costo dei quaderni: 8 × 6,25 € = 50 €.
Totale, inclusi 7 € di spedizione per l’intero ordine: 50 € + 7 € = 57 €.
```

### full: pass

```text
Quaderni: 8 × 6,25 € = 50 €.
Spedizione per l’intero ordine: 7 €.
Totale: 50 € + 7 € = 57 €.
```

### ultra: pass

```text
Quaderni: 8 × 6,25 € = 50 €.
Totale, con 7 € di spedizione per l’intero ordine: 50 € + 7 € = 57 €.
```

### off: pass

```text
Costo dei quaderni: 8 × 6,25 € = 50 €.
Spedizione per l’intero ordine: 7 €.
Totale: 50 € + 7 € = 57 €.
```

## modes-it-014 · percentage_points

Source task:

> In un esempio fittizio, la quota passa dal 26 % al 34 %. Indica l’aumento in punti percentuali, non l’aumento relativo.

### baseline: pass

```text
L’aumento è di 8 punti percentuali: 34 % − 26 % = 8 punti percentuali.
```

### lite: pass

```text
Nell’esempio fittizio, l’aumento è di 8 punti percentuali: 34 % − 26 % = 8 punti percentuali.
```

### full: pass

```text
Nell’esempio fittizio, l’aumento è di 8 punti percentuali: 34 % − 26 % = 8 punti percentuali.
```

### ultra: pass

```text
Nell’esempio fittizio, l’aumento è di 8 punti percentuali: 34 % − 26 %.
```

### off: pass

```text
L’aumento è di 8 punti percentuali: 34% − 26% = 8 punti percentuali.
```

## modes-it-015 · conflicting_notes

Source task:

> Scrivi una nota di stato: Il modulo indica lo scaffale C, mentre il registro indica lo scaffale D. Le annotazioni hanno la stessa data. La posizione effettiva non è stata controllata.

### baseline: pass

```text
Nota di stato: il modulo indica lo scaffale C, mentre il registro indica lo scaffale D. Le annotazioni riportano la stessa data. La posizione effettiva non è stata controllata e resta da verificare.
```

### lite: pass

```text
Il modulo indica lo scaffale C, mentre il registro indica lo scaffale D. Le annotazioni hanno la stessa data. La posizione effettiva non è stata controllata, quindi la discrepanza resta irrisolta.
```

### full: pass

```text
La posizione resta da verificare: il modulo indica lo scaffale C, mentre il registro indica lo scaffale D. Le annotazioni hanno la stessa data. La posizione effettiva non è stata controllata.
```

### ultra: pass

```text
Posizione non verificata: il modulo indica lo scaffale C, il registro lo scaffale D. Le annotazioni hanno la stessa data; la posizione effettiva non è stata controllata.
```

### off: pass

```text
Nota di stato: il modulo indica lo scaffale C, mentre il registro indica lo scaffale D. Le annotazioni riportano la stessa data. La posizione effettiva non è stata controllata, quindi la discrepanza resta irrisolta.
```

## modes-it-016 · technical

Source task:

> Semplifica la guida: Se arriva HTTP 409, non ripetere automaticamente la richiesta PUT. Prima recupera la versione corrente. La ripetizione è ammessa solo dopo aver risolto il conflitto.

### baseline: pass

```text
Se ricevi HTTP 409, non ripetere automaticamente la richiesta PUT. Recupera prima la versione corrente e risolvi il conflitto. Solo dopo puoi ripetere la richiesta.
```

### lite: pass

```text
Se arriva HTTP 409, non ripetere automaticamente la richiesta PUT. Prima recupera la versione corrente e risolvi il conflitto. Solo allora puoi ripetere la richiesta.
```

### full: pass

```text
Se ricevi HTTP 409, non ripetere automaticamente la richiesta PUT. Prima recupera la versione corrente e risolvi il conflitto. Solo allora puoi ripetere la richiesta.
```

### ultra: pass

```text
Se ricevi HTTP 409, non ripetere automaticamente la richiesta PUT. Recupera prima la versione corrente. Puoi ripetere la richiesta solo dopo aver risolto il conflitto.
```

### off: pass

```text
Se ricevi HTTP 409, non ripetere automaticamente la richiesta PUT. Recupera prima la versione corrente e risolvi il conflitto. Solo allora puoi ripetere la richiesta.
```

## modes-it-017 · technical

Source task:

> Spiega questa configurazione: preview_days=10 riguarda soltanto le anteprime temporanee. I documenti originali non vengono rimossi. La modifica vale per le anteprime create dopo il salvataggio dell’impostazione.

### baseline: pass

```text
preview_days=10 imposta a 10 giorni la durata delle sole anteprime temporanee, senza rimuovere i documenti originali. Vale soltanto per le anteprime create dopo il salvataggio dell’impostazione.
```

### lite: pass

```text
preview_days=10 imposta a 10 giorni la durata delle sole anteprime temporanee. I documenti originali non vengono rimossi. La modifica si applica solo alle anteprime create dopo il salvataggio dell’impostazione.
```

### full: pass

```text
preview_days=10 imposta a 10 giorni la durata delle sole anteprime temporanee. I documenti originali non vengono rimossi. La modifica si applica solo alle anteprime create dopo il salvataggio dell’impostazione.
```

### ultra: pass

```text
preview_days=10 imposta a 10 giorni la durata delle sole anteprime temporanee create dopo il salvataggio dell’impostazione. I documenti originali non vengono rimossi.
```

### off: pass

```text
preview_days=10 imposta a 10 giorni la durata delle sole anteprime temporanee. I documenti originali non vengono rimossi. La modifica si applica soltanto alle anteprime create dopo il salvataggio dell’impostazione.
```

## modes-it-018 · summary

Source task:

> Riassumi per gli iscritti: L’incontro di giovedì inizia alle 17 come previsto. La visita al cortile non si farà perché il passaggio è occupato. Si terrà invece la presentazione in aula. La nuova data della visita non è ancora fissata.

### baseline: pass

```text
L’incontro di giovedì resta alle 17, con la presentazione in aula. La visita al cortile non si farà perché il passaggio è occupato; la nuova data non è ancora fissata.
```

### lite: pass

```text
L’incontro di giovedì inizia alle 17, come previsto. La visita al cortile non si farà perché il passaggio è occupato; al suo posto si terrà la presentazione in aula. La nuova data della visita non è ancora fissata.
```

### full: pass

```text
L’incontro di giovedì resta alle 17. La visita al cortile non si farà perché il passaggio è occupato: al suo posto si terrà la presentazione in aula. La nuova data della visita non è ancora fissata.
```

### ultra: pass

```text
L’incontro di giovedì resta alle 17. La presentazione in aula sostituisce la visita al cortile perché il passaggio è occupato. La nuova data della visita non è ancora fissata.
```

### off: pass

```text
L’incontro di giovedì inizierà alle 17, come previsto. Al posto della visita al cortile, annullata perché il passaggio è occupato, si terrà la presentazione in aula. La nuova data della visita non è ancora fissata.
```

## modes-it-019 · scope

Source task:

> Rispondi soltanto: posso restituire il gioco venerdì sera? Nota: i nuovi prestiti finiscono alle 18. Le restituzioni sono accettate allo sportello fino alle 20. La scatola esterna non è disponibile.

### baseline: flagged

```text
Sì, venerdì sera puoi restituire il gioco allo sportello fino alle 20. La scatola esterna non è disponibile.
```

Review notes: Omits the loan deadline, but it is nonmaterial to the narrow return question; the actionable answer is complete. / Omette il dettaglio sui prestiti, ma conserva tutte le condizioni necessarie per la restituzione richiesta.

### lite: flagged

```text
Sì, puoi restituire il gioco venerdì sera allo sportello fino alle 20. La scatola esterna non è disponibile.
```

Review notes: The omitted loan deadline does not affect this narrowly requested answer about returning the game. / Omette il dettaglio sui prestiti, ma risponde integralmente alla domanda circoscritta senza applicare alle restituzioni il limite delle 18.

### full: pass

```text
Sì, puoi restituire il gioco venerdì sera allo sportello fino alle 20. Il limite delle 18 riguarda solo i nuovi prestiti. La scatola esterna non è disponibile.
```

### ultra: pass

```text
Sì, venerdì puoi restituire il gioco allo sportello fino alle 20. Alle 18 terminano solo i nuovi prestiti. La scatola esterna non è disponibile.
```

### off: pass

```text
Sì, puoi restituire il gioco venerdì sera allo sportello entro le 20. Il limite delle 18 riguarda solo i nuovi prestiti. La scatola esterna non è disponibile.
```

## modes-it-020 · analysis

Source task:

> Questa osservazione prova che il nuovo volantino ha aumentato le iscrizioni? In una simulazione, le iscrizioni passano da 35 a 50 dopo la distribuzione, ma nello stesso periodo è stata ridotta anche la quota.

### baseline: pass

```text
No. Nella simulazione le iscrizioni aumentano da 35 a 50, ma nello stesso periodo diminuisce anche la quota. Non si può quindi attribuire l’aumento al solo nuovo volantino.
```

### lite: pass

```text
No. Nella simulazione, le iscrizioni passano da 35 a 50 dopo la distribuzione del volantino, ma nello stesso periodo è stata ridotta anche la quota. L’osservazione non permette di attribuire l’aumento al volantino.
```

### full: pass

```text
No. Nella simulazione, le iscrizioni passano da 35 a 50 dopo la distribuzione del volantino, ma nello stesso periodo è stata ridotta anche la quota. L’osservazione non permette di stabilire se l’aumento dipenda dal volantino, dalla quota ridotta o da entrambi.
```

### ultra: pass

```text
No. Nella simulazione, le iscrizioni salgono da 35 a 50 dopo la distribuzione del volantino, ma nello stesso periodo è stata ridotta anche la quota. Non si può attribuire l’aumento al solo volantino.
```

### off: pass

```text
No. Nella simulazione le iscrizioni aumentano da 35 a 50 dopo la distribuzione del volantino, ma nello stesso periodo è stata ridotta anche la quota. L’osservazione non permette di distinguere l’effetto del volantino da quello della riduzione della quota, né prova un aumento delle iscrizioni reali.
```

## modes-it-021 · voice

Source task:

> Accorcia il messaggio mantenendo il tu e un tono amichevole: Grazie per avermi prestato il libro. Lo terrò nella custodia fino a sabato, perché vuoi controllare insieme a me le pagine con gli appunti. Non l’ho ancora restituito.

### baseline: pass

```text
Grazie per il libro! Non te l’ho ancora restituito: lo tengo nella custodia fino a sabato, perché vuoi controllare con me le pagine con gli appunti.
```

### lite: pass

```text
Grazie per il libro! Lo terrò nella custodia fino a sabato, perché vuoi controllare con me le pagine con gli appunti. Non te l’ho ancora restituito.
```

### full: pass

```text
Grazie per il libro! Non te l’ho ancora restituito: lo terrò nella custodia fino a sabato, perché vuoi controllare con me le pagine con gli appunti.
```

### ultra: pass

```text
Grazie per il libro! Non te l’ho ancora restituito: lo terrò nella custodia fino a sabato, perché vuoi controllare con me le pagine con gli appunti.
```

### off: pass

```text
Grazie per il libro! Non te l’ho ancora restituito: lo terrò nella custodia fino a sabato, perché vuoi controllare con me le pagine con gli appunti.
```

## modes-it-022 · ambiguity

Source task:

> Segnala l’ambiguità senza risolverla: « Dopo aver parlato con Luca, Andrea ha modificato il suo progetto. » Non è chiaro di chi sia il progetto. Proponi le due letture possibili.

### baseline: pass

```text
«Il suo progetto» è ambiguo. Le due letture possibili sono:
- Andrea ha modificato il progetto di Andrea dopo aver parlato con Luca.
- Andrea ha modificato il progetto di Luca dopo aver parlato con lui.
```

### lite: pass

```text
«Il suo progetto» è ambiguo. Le due letture possibili sono:
- Dopo aver parlato con Luca, Andrea ha modificato il progetto di Andrea.
- Dopo aver parlato con Luca, Andrea ha modificato il progetto di Luca.
```

### full: pass

```text
«Il suo progetto» è ambiguo. Le due letture possibili sono:
- Dopo aver parlato con Luca, Andrea ha modificato il progetto di Andrea.
- Dopo aver parlato con Luca, Andrea ha modificato il progetto di Luca.
```

### ultra: pass

```text
«Il suo progetto» può indicare il progetto di Andrea o quello di Luca:
- Dopo aver parlato con Luca, Andrea ha modificato il proprio progetto.
- Dopo aver parlato con Luca, Andrea ha modificato il progetto di Luca.
```

### off: pass

```text
«Il suo progetto» è ambiguo. Le due letture possibili sono:
- Dopo aver parlato con Luca, Andrea ha modificato il progetto di Andrea.
- Dopo aver parlato con Luca, Andrea ha modificato il progetto di Luca.
```

## modes-it-023 · permissions

Source task:

> Semplifica questa regola associativa fittizia: Gli ospiti possono assistere alla prova aperta senza iscriversi. La riunione successiva è riservata ai soci. Assistere alla prova non dà accesso alla riunione.

### baseline: pass

```text
Gli ospiti possono assistere alla prova aperta senza iscriversi, ma non alla riunione successiva, riservata ai soci. Partecipare alla prova non dà accesso alla riunione.
```

### lite: pass

```text
Gli ospiti possono assistere alla prova aperta senza iscriversi. La riunione successiva è solo per i soci: assistere alla prova non dà accesso alla riunione.
```

### full: pass

```text
Gli ospiti possono assistere alla prova aperta senza iscriversi, ma questo non dà accesso alla riunione successiva, riservata ai soci.
```

### ultra: pass

```text
Gli ospiti possono assistere alla prova aperta senza iscriversi, ma non alla riunione successiva, riservata ai soci. Assistere alla prova non dà accesso alla riunione.
```

### off: pass

```text
Gli ospiti possono assistere alla prova aperta senza iscriversi, ma non alla riunione successiva, riservata ai soci. Partecipare alla prova non dà accesso alla riunione.
```

## modes-it-024 · conditions

Source task:

> Riscrivi: La spedizione è gratuita per ordini di almeno 75 € destinati alla zona Nord. Gli articoli fragili sono esclusi, anche oltre 75 €. Gli ordini per la zona Sud pagano sempre la spedizione.

### baseline: pass

```text
La spedizione è gratuita solo per ordini di almeno 75 € destinati alla zona Nord, esclusi gli articoli fragili. Per gli articoli fragili la spedizione si paga anche oltre 75 €. Per gli ordini destinati alla zona Sud si paga sempre.
```

### lite: pass

```text
La spedizione è gratuita per ordini di almeno 75 € destinati alla zona Nord. Gli articoli fragili sono esclusi dalla spedizione gratuita, anche oltre 75 €. Per gli ordini destinati alla zona Sud, la spedizione è sempre a pagamento.
```

### full: pass

```text
La spedizione è gratuita per gli ordini di almeno 75 € destinati alla zona Nord, esclusi gli articoli fragili. Per questi articoli, la spedizione si paga anche oltre 75 €. Per gli ordini destinati alla zona Sud, la spedizione si paga sempre.
```

### ultra: pass

```text
La spedizione è gratuita per ordini di almeno 75 € destinati alla zona Nord, esclusi gli articoli fragili, anche oltre 75 €. Per la zona Sud, la spedizione è sempre a pagamento.
```

### off: pass

```text
La spedizione è gratuita per gli ordini di almeno 75 € destinati alla zona Nord, esclusi gli articoli fragili. Per gli articoli fragili la spedizione resta a pagamento, anche oltre 75 €. Per gli ordini destinati alla zona Sud, la spedizione è sempre a pagamento.
```

## modes-it-025 · negation

Source task:

> Rendi più chiaro: La dicitura « in attesa » non conferma né rifiuta la richiesta. Significa soltanto che la decisione non è stata registrata. Non considerarla un’autorizzazione.

### baseline: pass

```text
«In attesa» significa soltanto che la decisione sulla richiesta non è stata registrata. Non indica né approvazione né rifiuto e non vale come autorizzazione.
```

### lite: pass

```text
La dicitura «in attesa» non conferma né rifiuta la richiesta: indica solo che la decisione non è stata registrata. Non considerarla un’autorizzazione.
```

### full: pass

```text
«In attesa» significa solo che la decisione non è stata registrata: non conferma né rifiuta la richiesta. Non considerarla un’autorizzazione.
```

### ultra: pass

```text
«In attesa» significa solo che la decisione non è stata registrata: non conferma né rifiuta la richiesta. Non considerarla un’autorizzazione.
```

### off: pass

```text
La dicitura «in attesa» significa solo che la decisione non è stata registrata: la richiesta non risulta né confermata né rifiutata. Non considerare questa dicitura un’autorizzazione.
```

## modes-it-026 · unknown_actor

Source task:

> Riscrivi la cronologia: Alle 9:05, Paolo ha lasciato la busta in segreteria. Alle 9:30, la busta è stata aperta. Alle 10, Sara ha registrato i documenti. Non è indicato chi abbia aperto la busta.

### baseline: pass

```text
Alle 9:05 Paolo ha lasciato la busta in segreteria. Alle 9:30 la busta è stata aperta, ma non è indicato da chi. Alle 10 Sara ha registrato i documenti.
```

### lite: pass

```text
Alle 9:05, Paolo ha lasciato la busta in segreteria. Alle 9:30, la busta è stata aperta, ma non è indicato da chi. Alle 10, Sara ha registrato i documenti.
```

### full: pass

```text
Alle 9:05 Paolo ha lasciato la busta in segreteria. Alle 9:30 la busta è stata aperta, ma non è indicato da chi. Alle 10 Sara ha registrato i documenti.
```

### ultra: pass

```text
9:05: Paolo ha lasciato la busta in segreteria.
9:30: la busta è stata aperta; non è indicato da chi.
10:00: Sara ha registrato i documenti.
```

### off: pass

```text
Alle 9:05 Paolo ha lasciato la busta in segreteria. Alle 9:30 la busta è stata aperta, ma non è indicato da chi. Alle 10 Sara ha registrato i documenti.
```

## modes-it-027 · uncertainty

Source task:

> Riassumi: Due dei sette cavi controllati avevano un rivestimento danneggiato. Gli altri diciotto cavi non sono stati esaminati. Non possiamo indicare una percentuale di danni per l’intero stock.

### baseline: pass

```text
Due dei sette cavi esaminati avevano il rivestimento danneggiato. Gli altri diciotto non sono stati controllati, quindi non è possibile indicare la percentuale di cavi danneggiati nell’intero stock.
```

### lite: pass

```text
Due dei sette cavi controllati avevano il rivestimento danneggiato. Gli altri diciotto non sono stati esaminati: non possiamo quindi indicare una percentuale di danni per l’intero stock.
```

### full: pass

```text
Due dei sette cavi controllati avevano il rivestimento danneggiato. Gli altri diciotto non sono stati esaminati: non è quindi possibile indicare la percentuale di cavi danneggiati nell’intero stock.
```

### ultra: pass

```text
Due dei sette cavi controllati avevano il rivestimento danneggiato. Gli altri diciotto non sono stati esaminati: non possiamo indicare la percentuale di danni nell’intero stock.
```

### off: pass

```text
Due dei sette cavi controllati avevano il rivestimento danneggiato. Gli altri diciotto non sono stati esaminati, quindi non è possibile indicare la percentuale di cavi danneggiati nell’intero stock.
```

## modes-it-028 · numbers_units

Source task:

> Riformula: Il recipiente ha una capacità di 900 mL. La linea a 700 mL indica il riempimento consigliato, non la capacità massima. Questi valori valgono soltanto per il campione mostrato.

### baseline: pass

```text
Per il solo campione mostrato, il recipiente ha una capacità massima di 900 mL; la linea a 700 mL indica invece il livello di riempimento consigliato.
```

### lite: pass

```text
Il recipiente ha una capacità di 900 mL. La linea a 700 mL indica il riempimento consigliato, non la capacità massima. Questi valori si riferiscono soltanto al campione mostrato.
```

### full: pass

```text
Il recipiente ha una capacità di 900 mL. La linea a 700 mL indica il riempimento consigliato, non la capacità massima. Entrambi i valori valgono solo per il campione mostrato.
```

### ultra: pass

```text
Per il solo campione mostrato, la capacità del recipiente è di 900 mL. La linea a 700 mL indica il riempimento consigliato, non la capacità massima.
```

### off: pass

```text
Il recipiente ha una capacità massima di 900 mL. La linea a 700 mL indica il livello di riempimento consigliato, non la capacità massima. Entrambi i valori si riferiscono soltanto al campione mostrato.
```

## modes-it-029 · calculation

Source task:

> Un turno dura dalle 7:50 alle 11:25 e dalle 12:15 alle 15:40. Quanto lavoro effettivo è stato svolto? Non contare la pausa.

### baseline: pass

```text
Il lavoro effettivo è stato di 7 ore: 3 ore e 35 minuti al mattino e 3 ore e 25 minuti al pomeriggio, esclusa la pausa.
```

### lite: pass

```text
Il lavoro effettivo è stato di 7 ore: 3 ore e 35 minuti al mattino e 3 ore e 25 minuti al pomeriggio, esclusa la pausa.
```

### full: pass

```text
Il lavoro effettivo è di 7 ore: 3 ore e 35 minuti al mattino e 3 ore e 25 minuti al pomeriggio, esclusa la pausa.
```

### ultra: pass

```text
7 ore di lavoro effettivo: 3 ore e 35 minuti al mattino e 3 ore e 25 minuti al pomeriggio, esclusa la pausa.
```

### off: pass

```text
Il lavoro effettivo è stato di 7 ore: 3 ore e 35 minuti al mattino e 3 ore e 25 minuti al pomeriggio, escludendo la pausa.
```

## modes-it-030 · sampling

Source task:

> Rendi prudente questa conclusione: Tutti i 14 intervistati preferiscono il corso serale. Sono stati scelti tra chi aveva già frequentato un corso serale. Le persone disponibili soltanto al mattino non sono state intervistate.

### baseline: pass

```text
Tutti i 14 intervistati preferiscono il corso serale, ma erano stati selezionati tra persone che ne avevano già frequentato uno. Poiché chi è disponibile soltanto al mattino non è stato intervistato, il risultato non può essere generalizzato a tutte le persone.
```

### lite: pass

```text
Tutti i 14 intervistati preferiscono il corso serale, ma sono stati scelti tra chi aveva già frequentato un corso serale. Le persone disponibili soltanto al mattino non sono state intervistate. Il risultato non può quindi essere generalizzato a tutte le persone interessate al corso.
```

### full: pass

```text
Tutti i 14 intervistati preferiscono il corso serale, ma sono stati scelti tra chi ne aveva già frequentato uno. Le persone disponibili solo al mattino non sono state intervistate. Il risultato non può quindi essere generalizzato a tutte le persone potenzialmente interessate al corso.
```

### ultra: pass

```text
Tutti i 14 intervistati preferiscono il corso serale, ma erano stati scelti tra chi ne aveva già frequentato uno. Le persone disponibili solo al mattino non sono state intervistate: il risultato non può essere generalizzato.
```

### off: pass

```text
Tutti i 14 intervistati preferiscono il corso serale, ma sono stati selezionati tra persone che avevano già frequentato un corso serale. Le persone disponibili soltanto al mattino non sono state intervistate. Il risultato descrive quindi le preferenze degli intervistati e non può essere generalizzato a tutte le persone potenzialmente interessate al corso.
```

## modes-it-031 · summary

Source task:

> Scrivi una breve consegna: Elisa ha etichettato le scatole dei colori, ma non quelle dei tessuti. L’elenco delle etichette mancanti è nel cassetto alto. La stampante è stata riavviata; non sappiamo da chi.

### baseline: pass

```text
Elisa ha etichettato le scatole dei colori; restano quelle dei tessuti. L’elenco delle etichette mancanti è nel cassetto alto. La stampante è stata riavviata, ma non sappiamo da chi.
```

### lite: pass

```text
Elisa ha etichettato le scatole dei colori, ma non quelle dei tessuti. L’elenco delle etichette mancanti è nel cassetto alto. La stampante è stata riavviata, ma non sappiamo da chi.
```

### full: pass

```text
Elisa ha etichettato le scatole dei colori, ma non quelle dei tessuti. L’elenco delle etichette mancanti è nel cassetto alto. La stampante è stata riavviata, ma non sappiamo da chi.
```

### ultra: pass

```text
Elisa ha etichettato le scatole dei colori, non quelle dei tessuti. L’elenco delle etichette mancanti è nel cassetto alto. La stampante è stata riavviata, ma non sappiamo da chi.
```

### off: pass

```text
Elisa ha etichettato le scatole dei colori, ma non quelle dei tessuti. L’elenco delle etichette mancanti è nel cassetto alto. La stampante è stata riavviata, ma non sappiamo da chi.
```

## modes-it-032 · analysis

Source task:

> Quale acquisto costa meno per avere esattamente 60 fogli? Il pacco A contiene 20 fogli e costa 11 €; il pacco B ne contiene 30 e costa 17 €. Non si vendono fogli singoli. Confronta le due opzioni.

### baseline: pass

```text
Per avere esattamente 60 fogli, servono 3 pacchi A a 33 € oppure 2 pacchi B a 34 €. Conviene acquistare 3 pacchi A: si risparmia 1 €.
```

### lite: pass

```text
Per avere esattamente 60 fogli:
- 3 pacchi A: 3 × 11 € = 33 €.
- 2 pacchi B: 2 × 17 € = 34 €.

Conviene acquistare 3 pacchi A: costano 1 € in meno.
```

### full: pass

```text
Il pacco A costa meno: 3 pacchi da 20 fogli costano 33 €. Con B, 2 pacchi da 30 fogli costano 34 €. Entrambe le opzioni danno esattamente 60 fogli; A fa risparmiare 1 €.
```

### ultra: pass

```text
Conviene il pacco A: 3 pacchi danno 60 fogli per 33 €. Con B servono 2 pacchi: 60 fogli per 34 €. A fa risparmiare 1 €; non si vendono fogli singoli.
```

### off: pass

```text
Per avere esattamente 60 fogli:
- Pacco A: 3 pacchi da 20 fogli costano 33 €.
- Pacco B: 2 pacchi da 30 fogli costano 34 €.

Conviene acquistare 3 pacchi A: si risparmia 1 €.
```

## modes-it-033 · conflicting_notes

Source task:

> Riassumi per la segreteria: L’avviso indica aula 2, il calendario indica aula 4. Entrambi fissano l’incontro al 13 marzo alle 16. L’assegnazione dell’aula non è ancora confermata.

### baseline: pass

```text
L’incontro è fissato al 13 marzo alle 16. L’aula non è ancora confermata: l’avviso indica l’aula 2, il calendario l’aula 4.
```

### lite: pass

```text
L’incontro è fissato al 13 marzo alle 16. L’avviso indica aula 2, il calendario aula 4: l’assegnazione dell’aula non è ancora confermata.
```

### full: pass

```text
L’incontro è fissato al 13 marzo alle 16. L’aula non è ancora confermata: l’avviso indica aula 2, il calendario aula 4.
```

### ultra: pass

```text
L’incontro è fissato al 13 marzo alle 16. L’aula non è ancora confermata: l’avviso indica aula 2, il calendario aula 4.
```

### off: pass

```text
L’incontro è fissato al 13 marzo alle 16 in entrambi i documenti, ma l’aula non è ancora confermata: l’avviso indica l’aula 2, mentre il calendario indica l’aula 4.
```

## modes-it-034 · voice

Source task:

> Accorcia conservando l’ironia gentile: Oggi la macchina del caffè ha scelto il silenzio. Fino al controllo del tecnico, usate pure il bollitore in cucina. Non sappiamo ancora quando tornerà a fare rumore.

### baseline: flagged

```text
La macchina del caffè oggi tace: in attesa del tecnico, usate il bollitore in cucina. Non sappiamo quando ritroverà la voce.
```

Review notes: Shortens effectively and keeps gentle irony, but changes permissive wording and weakens the inspection condition. / Shorter and playful, but weakens the inspection condition and changes permissive wording into a directive.

### lite: pass

```text
Oggi la macchina del caffè ha scelto il silenzio. Fino al controllo del tecnico, usate pure il bollitore in cucina. Non sappiamo quando tornerà a farsi sentire.
```

### full: pass

```text
Oggi la macchina del caffè ha scelto il silenzio. Fino al controllo del tecnico, usate pure il bollitore in cucina. Il ritorno al rumore resta un mistero.
```

### ultra: pass

```text
Oggi la macchina del caffè ha scelto il silenzio. Fino al controllo del tecnico, usate pure il bollitore in cucina. Non sappiamo quando tornerà a farsi sentire.
```

### off: pass

```text
La macchina del caffè oggi fa voto di silenzio. Fino al controllo del tecnico, usate pure il bollitore in cucina: non sappiamo quando tornerà a farsi sentire.
```

## modes-it-035 · scope

Source task:

> Quale documento manca? Rispondi in una frase. Sono presenti il modulo firmato e la ricevuta. Servono anche una foto dell’oggetto e, soltanto per oggetti presi in prestito, una liberatoria del proprietario. L’oggetto è di proprietà di chi presenta la richiesta.

### baseline: pass

```text
Manca la foto dell’oggetto; la liberatoria non serve perché l’oggetto appartiene a chi presenta la richiesta.
```

### lite: pass

```text
Manca la foto dell’oggetto; la liberatoria non serve perché l’oggetto è di proprietà di chi presenta la richiesta.
```

### full: pass

```text
Manca la foto dell’oggetto; la liberatoria non serve perché l’oggetto appartiene a chi presenta la richiesta.
```

### ultra: pass

```text
Manca la foto dell’oggetto: modulo firmato e ricevuta sono presenti, mentre la liberatoria del proprietario serve solo per oggetti in prestito, non per questo, che appartiene a chi presenta la richiesta.
```

### off: pass

```text
Manca la foto dell’oggetto; la liberatoria non serve perché l’oggetto è di proprietà di chi presenta la richiesta.
```

## modes-it-036 · ambiguity

Source task:

> Chiarisci senza interpretare la data: « La consegna è indicata per il 06/07; il formato della data non è noto. » Mantieni 06/07 e segnala che giorno e mese devono essere confermati.

### baseline: pass

```text
La consegna è indicata per il 06/07, ma il formato della data non è noto: giorno e mese devono essere confermati.
```

### lite: pass

```text
La consegna è indicata per il 06/07. Il formato della data non è noto: giorno e mese devono essere confermati.
```

### full: pass

```text
La consegna è indicata per il 06/07, ma il formato della data non è noto: giorno e mese devono essere confermati.
```

### ultra: pass

```text
La consegna è indicata per il 06/07. Il formato della data non è noto: giorno e mese devono essere confermati.
```

### off: pass

```text
La consegna è indicata per il 06/07, ma il formato della data non è noto: giorno e mese devono essere confermati.
```

## modes-it-037 · technical

Source task:

> Riscrivi per il collega: Prima di eseguire export_tags --type json, copia tags.db nella cartella copy/. L’esportazione contiene solo le etichette attive; un risultato vuoto non dimostra che il database sia vuoto.

### baseline: pass

```text
Prima di eseguire `export_tags --type json`, copia `tags.db` nella cartella `copy/`. L’esportazione include solo le etichette attive: un risultato vuoto non significa che il database sia vuoto.
```

### lite: pass

```text
Prima di eseguire export_tags --type json, copia tags.db nella cartella copy/. L’esportazione include solo le etichette attive: un risultato vuoto non significa che il database sia vuoto.
```

### full: pass

```text
Prima di eseguire export_tags --type json, copia tags.db nella cartella copy/. L’esportazione include solo le etichette attive. Un risultato vuoto non dimostra che il database sia vuoto.
```

### ultra: pass

```text
Prima di eseguire export_tags --type json, copia tags.db nella cartella copy/. L’esportazione include solo le etichette attive: un risultato vuoto non dimostra che il database sia vuoto.
```

### off: pass

```text
Prima di eseguire export_tags --type json, copia tags.db nella cartella copy/. L’esportazione include solo le etichette attive: se il risultato è vuoto, non significa necessariamente che il database sia vuoto.
```

## modes-it-038 · technical

Source task:

> Spiega: state=preview mostra le modifiche proposte. Per registrarle serve commit=yes. La sola anteprima non cambia i dati già salvati.

### baseline: pass

```text
`state=preview` mostra le modifiche proposte senza cambiare i dati già salvati. Per registrare le modifiche, serve `commit=yes`.
```

### lite: pass

```text
state=preview mostra le modifiche proposte. Per salvarle serve commit=yes. La sola anteprima non modifica i dati già salvati.
```

### full: pass

```text
state=preview mostra le modifiche proposte, ma non cambia i dati già salvati. Per registrare le modifiche serve commit=yes.
```

### ultra: pass

```text
state=preview mostra le modifiche proposte senza cambiare i dati già salvati. Per registrare le modifiche serve commit=yes.
```

### off: pass

```text
state=preview mostra le modifiche proposte, senza cambiare i dati già salvati. Per registrare le modifiche serve commit=yes.
```

## modes-it-039 · exceptions

Source task:

> Semplifica questa regola fittizia: Ogni tavolo ospita al massimo tre espositori. Un quarto può aiutare soltanto durante l’allestimento e deve uscire prima dell’apertura. Non può restare per vendere.

### baseline: pass

```text
Ogni tavolo può ospitare al massimo tre espositori. Un quarto può aiutare solo durante l’allestimento: deve uscire prima dell’apertura e non può restare per vendere.
```

### lite: pass

```text
Ogni tavolo può ospitare al massimo tre espositori. Un quarto può aiutare solo durante l’allestimento e deve uscire prima dell’apertura. Non può restare per vendere.
```

### full: pass

```text
Ogni tavolo può ospitare al massimo tre espositori. Un quarto può aiutare solo durante l’allestimento e deve uscire prima dell’apertura: non può restare per vendere.
```

### ultra: pass

```text
Ogni tavolo può ospitare al massimo tre espositori. Un quarto può aiutare solo durante l’allestimento: deve uscire prima dell’apertura e non può restare per vendere.
```

### off: pass

```text
Ogni tavolo può ospitare al massimo tre espositori. Un quarto può aiutare solo durante l’allestimento, deve uscire prima dell’apertura e non può restare per vendere.
```

## modes-it-040 · conditions

Source task:

> Rendi l’istruzione più diretta: Il coperchio può essere aperto soltanto dopo che il dispositivo è stato spento e si è raffreddato. Spegnerlo non basta. La regola vale anche per una semplice ispezione.

### baseline: pass

```text
Apri il coperchio solo dopo aver spento il dispositivo e averlo lasciato raffreddare. Spegnerlo non basta: devi aspettare che si raffreddi, anche per una semplice ispezione.
```

### lite: pass

```text
Apri il coperchio solo dopo aver spento il dispositivo e averlo lasciato raffreddare. Spegnerlo non basta. La regola vale anche per una semplice ispezione.
```

### full: pass

```text
Apri il coperchio solo dopo aver spento il dispositivo e averlo lasciato raffreddare. Spegnerlo non basta. Questa regola vale anche per una semplice ispezione.
```

### ultra: pass

```text
Apri il coperchio solo dopo aver spento il dispositivo e averlo lasciato raffreddare. Spegnerlo non basta. La regola vale anche per una semplice ispezione.
```

### off: pass

```text
Apri il coperchio solo dopo aver spento il dispositivo e averlo lasciato raffreddare. Spegnerlo non basta. Segui questa regola anche per una semplice ispezione.
```

## modes-it-041 · denominators

Source task:

> Correggi la frase « Il 60 % dei clienti vuole il nuovo orario ». Dati: lo vuole il 60 % delle 40 persone che hanno restituito il questionario volontario; i questionari distribuiti erano 250.

### baseline: pass

```text
Il nuovo orario è voluto dal 60 % delle 40 persone che hanno restituito il questionario volontario, cioè 24 persone, su 250 questionari distribuiti.
```

### lite: pass

```text
Il 60 % delle 40 persone che hanno restituito il questionario volontario vuole il nuovo orario; i questionari distribuiti erano 250.
```

### full: pass

```text
Il 60 % delle 40 persone che hanno restituito il questionario volontario vuole il nuovo orario. Erano stati distribuiti 250 questionari: il risultato non rappresenta necessariamente tutti i clienti.
```

### ultra: pass

```text
Il 60 % delle 40 persone che hanno restituito il questionario volontario vuole il nuovo orario. I questionari distribuiti erano 250.
```

### off: pass

```text
Il 60 % delle 40 persone che hanno restituito il questionario volontario vuole il nuovo orario. I questionari distribuiti erano 250: il risultato non rappresenta necessariamente tutti i clienti.
```

## modes-it-042 · estimates

Source task:

> Accorcia: La riparazione potrebbe costare 680 € se bisogna sostituire entrambi i rulli. Per ora è confermato solo il controllo da 55 €. Non è ancora noto se i rulli debbano essere cambiati.

### baseline: pass

```text
È confermato solo il controllo da 55 €. La riparazione potrebbe costare 680 € se occorre sostituire entrambi i rulli, ma non è ancora noto se sia necessario.
```

### lite: pass

```text
La riparazione potrebbe costare 680 € se occorre sostituire entrambi i rulli, ma non è ancora noto se vadano cambiati. Per ora è confermato solo il controllo da 55 €.
```

### full: pass

```text
È confermato solo il controllo da 55 €. La riparazione potrebbe costare 680 € se occorre sostituire entrambi i rulli; non è ancora noto se vadano cambiati.
```

### ultra: pass

```text
È confermato solo il controllo da 55 €. La riparazione potrebbe costare 680 € se occorre sostituire entrambi i rulli; non è ancora noto se vadano cambiati.
```

### off: pass

```text
È confermato solo il controllo da 55 €. La riparazione potrebbe costare 680 € se fosse necessario sostituire entrambi i rulli, ma non è ancora noto se vadano cambiati.
```

## modes-it-043 · percentage_points

Source task:

> In una tabella fittizia, la percentuale scende dal 63 % al 54 %. Di quanti punti percentuali diminuisce? Non calcolare la variazione relativa.

### baseline: pass

```text
63 − 54 = 9 punti percentuali.
```

### lite: pass

```text
Diminuisce di 9 punti percentuali: 63 − 54 = 9.
```

### full: pass

```text
Diminuisce di 9 punti percentuali: 63 − 54 = 9.
```

### ultra: pass

```text
63 − 54 = 9 punti percentuali.
```

### off: pass

```text
Diminuisce di 9 punti percentuali: 63 − 54 = 9.
```

## modes-it-044 · calculation

Source task:

> Per 6 confezioni servono 420 cm di cordino. Quanto ne serve per 9 confezioni, mantenendo lo stesso consumo? Mostra il calcolo in centimetri.

### baseline: pass

```text
420 cm ÷ 6 × 9 = 630 cm di cordino.
```

### lite: pass

```text
420 cm ÷ 6 × 9 = 630 cm di cordino.
```

### full: pass

```text
420 cm ÷ 6 × 9 = 630 cm di cordino.
```

### ultra: pass

```text
420 cm ÷ 6 × 9 = 630 cm di cordino.
```

### off: pass

```text
420 cm ÷ 6 × 9 = 630 cm di cordino.
```

## modes-it-045 · summary

Source task:

> Riassumi il cambiamento: Dal 10 gennaio, gli oggetti da riparare si consegnano alla porta sul retro. Il ritiro resta al banco principale. Anche gli appuntamenti fissati prima del 10 gennaio usano la nuova porta se la consegna avviene da quella data.

### baseline: pass

```text
Dal 10 gennaio, le consegne degli oggetti da riparare avvengono alla porta sul retro, anche per appuntamenti fissati prima di quella data. Il ritiro resta al banco principale.
```

### lite: pass

```text
Dal 10 gennaio, gli oggetti da riparare si consegnano alla porta sul retro, anche per appuntamenti fissati prima se la consegna avviene da quella data. Il ritiro resta al banco principale.
```

### full: pass

```text
Dal 10 gennaio, gli oggetti da riparare si consegnano alla porta sul retro, anche per appuntamenti fissati prima se la consegna avviene da quella data. Il ritiro resta al banco principale.
```

### ultra: pass

```text
Dal 10 gennaio, gli oggetti da riparare si consegnano alla porta sul retro, anche per appuntamenti fissati prima di quella data. Il ritiro resta al banco principale.
```

### off: pass

```text
Dal 10 gennaio, gli oggetti da riparare si consegnano alla porta sul retro, anche per appuntamenti fissati prima di quella data. Il ritiro resta al banco principale.
```

## modes-it-046 · permissions

Source task:

> Riscrivi questa clausola fittizia senza parere legale: Chi utilizza l’attrezzatura può terminare il prestito in qualsiasi momento. Deve riconsegnarla entro due giorni. La restituzione anticipata non dà diritto al rimborso dei giorni già pagati.

### baseline: flagged

```text
Chi utilizza l’attrezzatura può interrompere il prestito in qualsiasi momento e deve riconsegnarla entro due giorni dall’interruzione. La restituzione anticipata non dà diritto al rimborso dei giorni già pagati.
```

Review notes: Preserves the clause; explicitly connects the return deadline to the contextual termination event. / Preserves the core clause but resolves an unspecified deadline anchor as a definite condition.

### lite: pass

```text
Chi utilizza l’attrezzatura può terminare il prestito in qualsiasi momento. Deve restituirla entro due giorni. La restituzione anticipata non dà diritto al rimborso dei giorni già pagati.
```

### full: pass

```text
Chi utilizza l’attrezzatura può terminare il prestito in qualsiasi momento e deve riconsegnarla entro due giorni. La restituzione anticipata non dà diritto al rimborso dei giorni già pagati.
```

### ultra: pass

```text
Chi utilizza l’attrezzatura può terminare il prestito in qualsiasi momento e deve riconsegnarla entro due giorni. La restituzione anticipata non dà diritto al rimborso dei giorni già pagati.
```

### off: pass

```text
Chi utilizza l’attrezzatura può interrompere il prestito in qualsiasi momento e deve restituirla entro due giorni. La restituzione anticipata non dà diritto al rimborso dei giorni già pagati.
```

## modes-it-047 · unknown_actor

Source task:

> Rendi chiaro: Il permesso è stato dato prima che Irene prendesse in carico la pratica. Irene ha aggiunto soltanto una nota sullo stato attuale. Il testo non indica chi abbia dato il permesso.

### baseline: pass

```text
Il permesso era già stato dato quando Irene ha preso in carico la pratica. Irene ha aggiunto solo una nota sullo stato attuale. Il testo non specifica chi abbia dato il permesso.
```

### lite: pass

```text
Il permesso è stato dato prima che Irene prendesse in carico la pratica. Irene ha aggiunto solo una nota sullo stato attuale. Il testo non indica chi abbia dato il permesso.
```

### full: pass

```text
Il permesso è stato dato prima che Irene prendesse in carico la pratica, ma il testo non indica da chi. Irene ha aggiunto soltanto una nota sullo stato attuale.
```

### ultra: pass

```text
Il permesso è stato dato prima che Irene prendesse in carico la pratica, ma il testo non indica da chi. Irene ha aggiunto solo una nota sullo stato attuale.
```

### off: pass

```text
Il permesso era già stato dato quando Irene ha preso in carico la pratica. Irene ha aggiunto solo una nota sullo stato attuale. Il testo non specifica chi abbia dato il permesso.
```

## modes-it-048 · analysis

Source task:

> Perché « nessun problema nei turni osservati » è più preciso di « nessun problema nel servizio »? In questo esempio fittizio sono stati osservati soltanto i turni del mattino.

### baseline: pass

```text
«Nessun problema nei turni osservati» limita l’affermazione ai turni del mattino, gli unici osservati. «Nessun problema nel servizio» estende invece la conclusione anche ai turni non osservati.
```

### lite: pass

```text
«Nessun problema nei turni osservati» limita l’affermazione ai turni del mattino, gli unici osservati. «Nessun problema nel servizio» estende invece l’affermazione all’intero servizio, anche ai turni non osservati.
```

### full: pass

```text
«Nessun problema nei turni osservati» limita l’affermazione ai turni del mattino, gli unici osservati. «Nessun problema nel servizio» estende invece l’affermazione anche ai turni non osservati, per i quali non ci sono informazioni.
```

### ultra: pass

```text
«Nessun problema nei turni osservati» limita l’affermazione ai soli turni del mattino, quelli osservati. «Nessun problema nel servizio» la estende anche ai turni non osservati, senza elementi a sostegno.
```

### off: pass

```text
«Nessun problema nei turni osservati» limita l’affermazione ai turni del mattino, gli unici osservati. «Nessun problema nel servizio» estende invece la conclusione all’intero servizio, anche ai turni non osservati, sui quali non ci sono informazioni.
```

## modes-it-049 · negation

Source task:

> Semplifica: Non occorre sostituire tutta la domanda. Manca soltanto la firma nella seconda pagina. Le altre pagine già inviate restano valide.

### baseline: pass

```text
Basta aggiungere la firma nella seconda pagina: non serve sostituire tutta la domanda. Le altre pagine già inviate restano valide.
```

### lite: pass

```text
Non occorre sostituire tutta la domanda: manca solo la firma nella seconda pagina. Le altre pagine già inviate restano valide.
```

### full: pass

```text
Manca solo la firma nella seconda pagina. Non serve sostituire tutta la domanda: le altre pagine già inviate restano valide.
```

### ultra: pass

```text
Manca solo la firma nella seconda pagina: non occorre sostituire tutta la domanda. Le altre pagine già inviate restano valide.
```

### off: pass

```text
Non serve sostituire tutta la domanda: manca solo la firma sulla seconda pagina. Le altre pagine già inviate restano valide.
```

## modes-it-050 · voice

Source task:

> Scrivi un breve messaggio cortese usando solo questi elementi: devo rinunciare alla cena di venerdì; non voglio indicare il motivo; ringrazio per l’invito. Non proporre un altro giorno.

### baseline: pass

```text
Grazie per l’invito. Purtroppo devo rinunciare alla cena di venerdì.
```

### lite: pass

```text
Grazie per l’invito. Purtroppo devo rinunciare alla cena di venerdì.
```

### full: pass

```text
Grazie per l’invito. Devo rinunciare alla cena di venerdì; preferisco non indicare il motivo.
```

### ultra: pass

```text
Grazie per l’invito. Purtroppo devo rinunciare alla cena di venerdì.
```

### off: pass

```text
Grazie per l’invito. Purtroppo devo rinunciare alla cena di venerdì.
```

## modes-it-051 · ambiguity

Source task:

> Spiega la differenza tra « Puoi consegnare la chiave domani » e « Devi consegnare la chiave domani ». Non aggiungere altre scadenze.

### baseline: pass

```text
«Puoi consegnare la chiave domani» esprime una possibilità o un permesso, non un obbligo. «Devi consegnare la chiave domani» indica invece un obbligo.
```

### lite: pass

```text
«Puoi consegnare la chiave domani» indica una possibilità o un permesso, non un obbligo. «Devi consegnare la chiave domani» indica un obbligo.
```

### full: pass

```text
«Puoi consegnare la chiave domani» indica una possibilità o un permesso, non un obbligo. «Devi consegnare la chiave domani» indica un obbligo.
```

### ultra: pass

```text
«Puoi consegnare la chiave domani» indica un permesso o una possibilità, non un obbligo. «Devi consegnare la chiave domani» indica un obbligo.
```

### off: pass

```text
«Puoi consegnare la chiave domani» esprime un permesso o una possibilità, non un obbligo. «Devi consegnare la chiave domani» indica invece l’obbligo di consegnarla domani.
```

## modes-it-052 · conditions

Source task:

> Chiarisci: Si può chiedere un duplicato se il tesserino è perso oppure illeggibile. Basta uno dei due motivi. La richiesta non equivale all’approvazione del duplicato.

### baseline: pass

```text
Puoi chiedere un duplicato se il tesserino è perso oppure illeggibile: basta una delle due condizioni. Presentare la richiesta non significa che il duplicato sia approvato.
```

### lite: pass

```text
Si può chiedere un duplicato se il tesserino è perso oppure illeggibile: basta uno dei due motivi. La richiesta non equivale all’approvazione del duplicato.
```

### full: pass

```text
Puoi chiedere un duplicato se il tesserino è perso oppure illeggibile: basta una delle due condizioni. La richiesta non equivale all’approvazione del duplicato.
```

### ultra: pass

```text
Puoi chiedere un duplicato se il tesserino è perso o illeggibile: basta una delle due condizioni. La richiesta non implica l’approvazione del duplicato.
```

### off: pass

```text
Si può chiedere un duplicato se il tesserino è perso oppure illeggibile: è sufficiente uno solo dei due motivi. Presentare la richiesta non significa che il duplicato sia approvato.
```

## modes-it-053 · scope

Source task:

> Rispondi brevemente: posso portare la bici nell’atrio e, se no, dove deve restare? Regola fittizia: i passeggini sono ammessi nell’atrio; le biciclette devono restare nel cortile; le borse possono essere lasciate all’accoglienza.

### baseline: pass

```text
No, la bici non può essere portata nell’atrio: deve restare nel cortile.
```

### lite: pass

```text
No, la bici deve restare nel cortile.
```

### full: pass

```text
No, la bici non può entrare nell’atrio: deve restare nel cortile.
```

### ultra: pass

```text
No, la bici deve restare nel cortile.
```

### off: pass

```text
No, la bici non può essere portata nell’atrio: deve restare nel cortile.
```

## modes-it-054 · sampling

Source task:

> Scrivi una limitazione del test: Undici persone già formate hanno completato il montaggio in meno di otto minuti. Tutte avevano usato lo stesso kit in passato. Nessun principiante ha partecipato.

### baseline: pass

```text
Il test ha coinvolto solo undici persone già formate, tutte con esperienza dello stesso kit. Il montaggio in meno di otto minuti non dimostra quindi che i principianti, non inclusi nel test, possano ottenere lo stesso risultato.
```

### lite: pass

```text
Il test ha coinvolto solo undici persone già formate, tutte con esperienza dello stesso kit. Hanno completato il montaggio in meno di otto minuti, ma nessun principiante ha partecipato: il risultato non permette di valutare i tempi dei principianti.
```

### full: pass

```text
Il test non permette di valutare il montaggio da parte di principianti: le undici persone che lo hanno completato in meno di otto minuti erano già formate e avevano tutte usato lo stesso kit in passato. Nessun principiante ha partecipato.
```

### ultra: pass

```text
Il test ha coinvolto solo undici persone già formate, tutte con esperienza dello stesso kit: hanno completato il montaggio in meno di otto minuti. Non avendo partecipato principianti, il risultato non ne indica i tempi di montaggio.
```

### off: pass

```text
Il test ha coinvolto soltanto undici persone già formate, tutte con esperienza precedente sullo stesso kit, che hanno completato il montaggio in meno di otto minuti. Poiché non ha partecipato alcun principiante, il risultato non permette di valutare i tempi di montaggio di chi usa il kit per la prima volta.
```

## modes-it-055 · conflicting_notes

Source task:

> Prepara una nota per il registro: L’etichetta dichiara 90 pezzi, il conteggio manuale ne trova 89. Il sacchetto è stato richiuso. Nessun secondo conteggio è stato effettuato.

### baseline: pass

```text
L’etichetta dichiara 90 pezzi; il conteggio manuale ne ha rilevati 89, uno in meno rispetto al dichiarato. Il sacchetto è stato richiuso. Non è stato effettuato un secondo conteggio.
```

### lite: pass

```text
L’etichetta dichiara 90 pezzi; il conteggio manuale ne ha rilevati 89. Il sacchetto è stato richiuso. Non è stato effettuato un secondo conteggio.
```

### full: pass

```text
L’etichetta dichiara 90 pezzi; il conteggio manuale ne ha rilevati 89. Il sacchetto è stato richiuso. Non è stato effettuato un secondo conteggio.
```

### ultra: pass

```text
L’etichetta dichiara 90 pezzi; il conteggio manuale ne rileva 89. Il sacchetto è stato richiuso. Non è stato effettuato un secondo conteggio.
```

### off: pass

```text
L’etichetta dichiara 90 pezzi; il conteggio manuale ne ha rilevati 89, uno in meno rispetto al dichiarato. Il sacchetto è stato richiuso. Non è stato effettuato un secondo conteggio.
```

## modes-it-056 · numbers_units

Source task:

> Riscrivi: Il limite è 6 kg per scatola, compreso l’imballaggio. Ogni spedizione può avere al massimo quattro scatole. Non è un limite di 6 kg per tutta la spedizione.

### baseline: pass

```text
Ogni spedizione può contenere al massimo quattro scatole. Il limite di 6 kg, imballaggio compreso, si applica a ciascuna scatola, non all’intera spedizione.
```

### lite: pass

```text
Il limite è di 6 kg per scatola, compreso l’imballaggio. Ogni spedizione può contenere al massimo quattro scatole. Il limite di 6 kg non si applica all’intera spedizione.
```

### full: pass

```text
Il limite è di 6 kg per scatola, imballaggio compreso, non per l’intera spedizione. Ogni spedizione può contenere al massimo quattro scatole.
```

### ultra: pass

```text
Ogni spedizione può contenere al massimo quattro scatole, ciascuna fino a 6 kg, imballaggio compreso. Il limite di 6 kg vale per scatola, non per l’intera spedizione.
```

### off: pass

```text
Ogni scatola può pesare al massimo 6 kg, imballaggio compreso. Ogni spedizione può contenere al massimo quattro scatole. Il limite di 6 kg si applica a ciascuna scatola, non all’intera spedizione.
```

## modes-it-057 · technical

Source task:

> Rendi chiara la nota di versione: Dalla versione 1.8, include_old=false nasconde le schede vecchie senza eliminarle. I rapporti avviati prima dell’aggiornamento mantengono la loro impostazione fino alla fine.

### baseline: pass

```text
Dalla versione 1.8, include_old=false nasconde le schede vecchie, ma non le elimina. I rapporti avviati prima dell’aggiornamento mantengono l’impostazione precedente fino al completamento.
```

### lite: pass

```text
Dalla versione 1.8, include_old=false nasconde le schede vecchie senza eliminarle. I rapporti avviati prima dell’aggiornamento mantengono la loro impostazione fino al termine.
```

### full: pass

```text
Dalla versione 1.8, include_old=false nasconde le schede vecchie, ma non le elimina. I rapporti avviati prima dell’aggiornamento mantengono la loro impostazione fino al completamento.
```

### ultra: pass

```text
Dalla versione 1.8, include_old=false nasconde le schede vecchie senza eliminarle. I rapporti avviati prima dell’aggiornamento mantengono la propria impostazione fino al completamento.
```

### off: pass

```text
Dalla versione 1.8, include_old=false nasconde le schede vecchie, ma non le elimina. I rapporti avviati prima dell’aggiornamento mantengono la propria impostazione fino al completamento.
```

## modes-it-058 · analysis

Source task:

> È corretto dire che ogni pratica è stata più veloce? In una simulazione, il tempo medio scende da 14 a 11 minuti. Non sono disponibili i tempi delle singole pratiche.

### baseline: pass

```text
No. Nella simulazione il tempo medio scende da 14 a 11 minuti, ma senza i tempi delle singole pratiche non si può affermare che ciascuna sia stata più veloce.
```

### lite: pass

```text
No. Nella simulazione, il tempo medio scende da 14 a 11 minuti, ma non sono disponibili i tempi delle singole pratiche. Non si può quindi affermare che ogni pratica sia stata più veloce.
```

### full: pass

```text
No. Nella simulazione, il tempo medio scende da 14 a 11 minuti, ma non sono disponibili i tempi delle singole pratiche. Non si può quindi affermare che ogni pratica sia stata più veloce.
```

### ultra: pass

```text
No. Nella simulazione, il tempo medio scende da 14 a 11 minuti. Senza i tempi delle singole pratiche, non si può dire che ciascuna sia stata più veloce.
```

### off: pass

```text
No. Nella simulazione, il tempo medio è sceso da 14 a 11 minuti, ma questo non significa che ogni pratica sia stata più veloce. Senza i tempi delle singole pratiche, non è possibile affermarlo.
```

## modes-it-059 · voice

Source task:

> Accorcia mantenendo la voce delicata: Il vento muoveva appena la tenda. Sul davanzale c’erano quattro limoni. Nessuno aveva aperto la finestra da ieri sera.

### baseline: flagged

```text
Il vento sfiorava la tenda. Quattro limoni sul davanzale. La finestra, mai aperta da ieri sera.
```

Review notes: Preserves meaning and tone; the final elliptical phrase is slightly less natural. / The shortened, delicate prose retains the lemons and timing but replaces slight movement with brushing.

### lite: pass

```text
Il vento muoveva appena la tenda. Sul davanzale, quattro limoni. Nessuno aveva aperto la finestra da ieri sera.
```

### full: pass

```text
Il vento muoveva appena la tenda. Quattro limoni sul davanzale. Nessuno aveva aperto la finestra da ieri sera.
```

### ultra: flagged

```text
Il vento sfiorava la tenda. Sul davanzale, quattro limoni. Nessuno aveva aperto la finestra da ieri sera.
```

Review notes: Shortens the scene while preserving its facts and gentle voice. / Preserves the delicate tone, count, location, and timing, but changes the wind’s stated effect.

### off: flagged

```text
Il vento sfiorava la tenda. Quattro limoni sul davanzale. Nessuno aveva aperto la finestra da ieri sera.
```

Review notes: Compact and faithful, with the requested delicate voice. / Clear and delicate shortening, but the curtain’s barely perceptible movement is not retained.

## modes-it-060 · exact_format

Source task:

> Restituisci solo questa riga, senza introduzione: Richiesta sospesa — pratica P-39.

### baseline: pass

```text
Richiesta sospesa — pratica P-39.
```

### lite: pass

```text
Richiesta sospesa — pratica P-39.
```

### full: pass

```text
Richiesta sospesa — pratica P-39.
```

### ultra: pass

```text
Richiesta sospesa — pratica P-39.
```

### off: pass

```text
Richiesta sospesa — pratica P-39.
```

## modes-it-061 · exact_format

Source task:

> Semplifica soltanto il valore message in italiano. Restituisci JSON valido e nient’altro, con le chiavi case, checks e message. Conserva case e checks: {"case":"IT-582","checks":2,"message":"L’immagine inviata non può essere letta; si prega di inviarla nuovamente in formato PNG."}

### baseline: pass

```text
{"case":"IT-582","checks":2,"message":"Non è possibile leggere l’immagine inviata. Inviala di nuovo in formato PNG."}
```

### lite: pass

```text
{"case":"IT-582","checks":2,"message":"L’immagine inviata non è leggibile; inviala di nuovo in formato PNG."}
```

### full: pass

```text
{"case":"IT-582","checks":2,"message":"L’immagine inviata non è leggibile. Inviala di nuovo in formato PNG."}
```

### ultra: pass

```text
{"case":"IT-582","checks":2,"message":"L’immagine inviata non è leggibile. Inviala di nuovo in formato PNG."}
```

### off: pass

```text
{"case":"IT-582","checks":2,"message":"L’immagine inviata non è leggibile. Inviala di nuovo in formato PNG."}
```

## modes-it-062 · exact_format

Source task:

> Scrivi un avviso in esattamente due frasi: La lettura della cartella /srv/bottega resta possibile. La scrittura riprende alle 18:25 UTC. Mantieni esattamente percorso e orario.

### baseline: pass

```text
La lettura della cartella /srv/bottega resta possibile. La scrittura riprende alle 18:25 UTC.
```

### lite: pass

```text
La lettura della cartella /srv/bottega resta possibile. La scrittura riprende alle 18:25 UTC.
```

### full: pass

```text
La lettura della cartella /srv/bottega resta possibile. La scrittura riprende alle 18:25 UTC.
```

### ultra: pass

```text
La lettura della cartella /srv/bottega resta possibile. La scrittura riprende alle 18:25 UTC.
```

### off: pass

```text
La lettura della cartella /srv/bottega resta possibile. La scrittura riprende alle 18:25 UTC.
```

## modes-it-063 · exact_format

Source task:

> Correggi solo « ricevvuto » e restituisci la riga senza commenti: Modulo ricevvuto: IT_08 — verifica non conclusa.

### baseline: pass

```text
Modulo ricevuto: IT_08 — verifica non conclusa.
```

### lite: pass

```text
Modulo ricevuto: IT_08 — verifica non conclusa.
```

### full: pass

```text
Modulo ricevuto: IT_08 — verifica non conclusa.
```

### ultra: pass

```text
Modulo ricevuto: IT_08 — verifica non conclusa.
```

### off: pass

```text
Modulo ricevuto: IT_08 — verifica non conclusa.
```

## modes-it-064 · exact_format

Source task:

> Scrivi un messaggio breve: {{cliente}} può modificare la consegna tramite {{delivery_link}} fino al 17 febbraio. Mantieni le variabili esattamente così e non inventarne i valori.

### baseline: pass

```text
{{cliente}} può modificare la consegna tramite {{delivery_link}} fino al 17 febbraio.
```

### lite: pass

```text
{{cliente}} può modificare la consegna tramite {{delivery_link}} fino al 17 febbraio.
```

### full: pass

```text
{{cliente}} può modificare la consegna tramite {{delivery_link}} fino al 17 febbraio.
```

### ultra: pass

```text
{{cliente}} può modificare la consegna tramite {{delivery_link}} fino al 17 febbraio.
```

### off: pass

```text
{{cliente}} può modificare la consegna tramite {{delivery_link}} fino al 17 febbraio.
```

## modes-it-065 · exact_format

Source task:

> Restituisci solo un oggetto JSON con item, complete e note. item è "CAS-14", complete è false. L’elenco è stato scritto, ma le quantità non sono ancora state controllate. note deve essere in italiano.

### baseline: pass

```text
{"item":"CAS-14","complete":false,"note":"L’elenco è stato scritto, ma le quantità non sono ancora state controllate."}
```

### lite: pass

```text
{"item":"CAS-14","complete":false,"note":"L’elenco è stato scritto, ma le quantità non sono ancora state controllate."}
```

### full: pass

```text
{"item":"CAS-14","complete":false,"note":"L’elenco è stato scritto, ma le quantità non sono ancora state controllate."}
```

### ultra: pass

```text
{"item":"CAS-14","complete":false,"note":"L’elenco è stato scritto, ma le quantità non sono ancora state controllate."}
```

### off: pass

```text
{"item":"CAS-14","complete":false,"note":"L’elenco è stato scritto, ma le quantità non sono ancora state controllate."}
```

## modes-it-066 · exact_format

Source task:

> Riproduci esattamente queste due righe, senza blocco di codice:
> Consultazione consentita: sì
> Modifica consentita: no

### baseline: pass

```text
Consultazione consentita: sì
Modifica consentita: no
```

### lite: pass

```text
Consultazione consentita: sì
Modifica consentita: no
```

### full: pass

```text
Consultazione consentita: sì
Modifica consentita: no
```

### ultra: pass

```text
Consultazione consentita: sì
Modifica consentita: no
```

### off: pass

```text
Consultazione consentita: sì
Modifica consentita: no
```

## modes-it-067 · exact_format

Source task:

> Spiega in una frase il comando stock-review --simulate. Mostra le differenze previste e non cambia il magazzino registrato. Il comando deve comparire senza modifiche.

### baseline: pass

```text
Il comando stock-review --simulate mostra le differenze previste senza modificare il magazzino registrato.
```

### lite: pass

```text
Il comando stock-review --simulate mostra le differenze previste senza cambiare il magazzino registrato.
```

### full: pass

```text
Il comando stock-review --simulate mostra le differenze previste senza modificare il magazzino registrato.
```

### ultra: pass

```text
Il comando stock-review --simulate mostra le differenze previste senza cambiare il magazzino registrato.
```

### off: pass

```text
Il comando stock-review --simulate mostra le differenze previste senza cambiare il magazzino registrato.
```

## modes-it-068 · exact_format

Source task:

> Semplifica la nota mantenendo la citazione inglese identica: Compare "upload waiting". Vuol dire che il caricamento è in attesa, non che il file sia stato perso. Il motivo dell’attesa non è ancora noto.

### baseline: flagged

```text
Compare "upload waiting": il caricamento è in attesa, ma il file non è perso; il motivo dell’attesa non è ancora noto.
```

Review notes: Turns absence of evidence of file loss into certainty that the file is not lost. / Turns a message that does not establish loss into a categorical assurance that the file is not lost.

### lite: pass

```text
Compare "upload waiting": il caricamento è in attesa, non significa che il file sia stato perso. Il motivo dell’attesa non è ancora noto.
```

### full: pass

```text
Compare "upload waiting": il caricamento è in attesa, non significa che il file sia stato perso. Il motivo dell’attesa non è ancora noto.
```

### ultra: pass

```text
Compare "upload waiting": il caricamento è in attesa, non significa che il file sia stato perso. Il motivo dell’attesa non è ancora noto.
```

### off: pass

```text
Compare "upload waiting": il caricamento è in attesa, non significa che il file sia stato perso. Il motivo dell’attesa non è ancora noto.
```

## modes-it-069 · exact_format

Source task:

> Rispondi solo con JSON contenente group, seats e notice. Conserva group="GR-62" e seats=0. notice deve dire che attualmente non ci sono posti disponibili, senza promettere quando ne arriveranno.

### baseline: pass

```text
{"group":"GR-62","seats":0,"notice":"Attualmente non ci sono posti disponibili."}
```

### lite: pass

```text
{"group":"GR-62","seats":0,"notice":"Attualmente non ci sono posti disponibili."}
```

### full: pass

```text
{"group":"GR-62","seats":0,"notice":"Attualmente non ci sono posti disponibili."}
```

### ultra: pass

```text
{"group":"GR-62","seats":0,"notice":"Attualmente non ci sono posti disponibili."}
```

### off: pass

```text
{"group":"GR-62","seats":0,"notice":"Attualmente non ci sono posti disponibili."}
```

## modes-it-070 · long_summary

Source task:

> Prepara una consegna per chi aprirà domani il piccolo laboratorio fittizio. Deve essere chiaro quali strumenti sono disponibili, quali no e quali informazioni restano provvisorie. Non presentare un’offerta di aiuto come un impegno già confermato.
> 
> Il registro contiene 62 strumenti. Cinquantasei sono stati trovati negli armadi, quattro sono in prestito con moduli firmati e due non sono stati trovati. Il rientro dei quattro prestiti è previsto per il 28 maggio. Per gli strumenti mancanti non è stato accertato un furto: potrebbero essere stati riposti altrove o registrati male. L’ultimo confronto completo tra registro e armadi risale a due mesi fa.
> 
> Sono state pulite cinque levigatrici. Soltanto L-09 ha superato anche il controllo di funzionamento e può essere prestata. Le altre quattro restano bloccate fino al controllo. Il bollino arancione indica che la pulizia è finita, non che lo strumento sia autorizzato al prestito. La L-09 è sul ripiano basso con il cavo raccolto nella sua borsa.
> 
> Il materiale abrasivo pesa 2,7 kg, comprese le buste. Questo dato non permette di calcolare il numero dei fogli utilizzabili. Sono state proposte nuove buste, ma nessun ordine è stato effettuato. Il saldo per i consumabili è stimato in 95 € e deve ancora essere verificato con tre scontrini. Non va presentato come disponibilità definitiva.
> 
> Giulia ha offerto di riscrivere le etichette martedì, ma non ha ancora confermato la presenza. L’elenco delle etichette illeggibili è nel quaderno sul tavolo. Il pavimento anteriore è stato pulito. Nel deposito la serratura è difettosa: il deposito resta chiuso finché non viene riparata e controllata. Per i nuovi prestiti si usa ancora il modulo consueto. Esiste una bozza di modulo breve, ma non è stata approvata. Il suo semplice salvataggio nella cartella comune non autorizza a sostituire quello attuale.

### baseline: pass

```text
Consegna per l’apertura di domani

Strumenti e prestiti
- Il registro contiene 62 strumenti: 56 trovati negli armadi, 4 in prestito con moduli firmati e 2 non trovati. Il rientro dei prestiti è previsto per il 28 maggio, non confermato.
- Per i due strumenti mancanti non è stato accertato un furto: potrebbero essere altrove o registrati male. L’ultimo confronto completo tra registro e armadi risale a due mesi fa.
- Delle cinque levigatrici pulite, soltanto L-09 ha superato il controllo di funzionamento ed è autorizzata al prestito. Si trova sul ripiano basso, con il cavo raccolto nella sua borsa. Le altre quattro restano bloccate fino al controllo.
- Il bollino arancione attesta soltanto la pulizia, non l’autorizzazione al prestito. La presenza negli armadi non va confusa con l’idoneità al prestito.

Materiali e saldo provvisorio
- Gli abrasivi pesano 2,7 kg comprese le buste: non è possibile ricavarne il numero di fogli utilizzabili.
- Sono state proposte nuove buste, ma non è stato effettuato alcun ordine.
- Il saldo per i consumabili è stimato in 95 € e deve essere verificato con tre scontrini: non è una disponibilità definitiva.

Locali ed etichette
- Il pavimento anteriore è stato pulito.
- Il deposito resta chiuso: la serratura difettosa deve essere riparata e controllata prima della riapertura.
- L’elenco delle etichette illeggibili è nel quaderno sul tavolo. Giulia ha offerto di riscriverle martedì, ma non ha ancora confermato la presenza: l’intervento non è un impegno confermato.

Moduli
- Per i nuovi prestiti usare il modulo consueto.
- La bozza di modulo breve non è approvata. Il salvataggio nella cartella comune non autorizza a sostituire il modulo attuale.
```

### lite: pass

```text
Consegna per l’apertura di domani

Strumenti e prestiti
Il registro contiene 62 strumenti: 56 sono stati trovati negli armadi, quattro sono in prestito con moduli firmati e due non sono stati trovati. Il rientro dei quattro prestiti è previsto per il 28 maggio. Per i due strumenti mancanti non è stato accertato un furto: potrebbero essere stati riposti altrove o registrati male. L’ultimo confronto completo tra registro e armadi risale a due mesi fa.

Sono state pulite cinque levigatrici. Solo L-09 ha superato anche il controllo di funzionamento e può essere prestata. Si trova sul ripiano basso, con il cavo raccolto nella sua borsa. Le altre quattro restano bloccate fino al controllo. Il bollino arancione indica che la pulizia è finita, non che lo strumento sia autorizzato al prestito.

Materiali e saldo provvisorio
Il materiale abrasivo pesa 2,7 kg, comprese le buste. Questo dato non permette di calcolare il numero dei fogli utilizzabili. Sono state proposte nuove buste, ma nessun ordine è stato effettuato. Il saldo per i consumabili è stimato in 95 €: deve ancora essere verificato con tre scontrini e non è una disponibilità definitiva.

Etichette e locali
Giulia ha offerto di riscrivere le etichette martedì, ma non ha ancora confermato la presenza. L’elenco delle etichette illeggibili è nel quaderno sul tavolo.

Il pavimento anteriore è stato pulito. La serratura del deposito è difettosa: il deposito resta chiuso finché la serratura non viene riparata e controllata.

Moduli
Per i nuovi prestiti si usa ancora il modulo consueto. Esiste una bozza di modulo breve, ma non è stata approvata. Il suo salvataggio nella cartella comune non autorizza a sostituire il modulo attuale.
```

### full: pass

```text
## Consegna per l’apertura di domani

### Strumenti e prestiti
- Il registro contiene 62 strumenti: 56 trovati negli armadi, quattro in prestito con moduli firmati e due non trovati. Il rientro dei quattro prestiti è previsto per il 28 maggio.
- Per i due strumenti mancanti non è stato accertato un furto: potrebbero essere stati riposti altrove o registrati male. L’ultimo confronto completo tra registro e armadi risale a due mesi fa.
- Sono state pulite cinque levigatrici. Solo L-09 ha superato anche il controllo di funzionamento e può essere prestata. Si trova sul ripiano basso, con il cavo raccolto nella sua borsa. Le altre quattro restano bloccate fino al controllo.
- Il bollino arancione indica soltanto che la pulizia è finita: non autorizza il prestito.

### Consumabili: dati provvisori
- Il materiale abrasivo pesa 2,7 kg, comprese le buste. Il peso non permette di calcolare quanti fogli siano utilizzabili.
- Sono state proposte nuove buste, ma non è stato effettuato alcun ordine.
- Il saldo per i consumabili è stimato in 95 € e deve ancora essere verificato con tre scontrini. Non è una disponibilità definitiva.

### Locali, etichette e moduli
- Il pavimento anteriore è stato pulito. La serratura del deposito è difettosa: il deposito resta chiuso finché la serratura non viene riparata e controllata.
- Giulia ha offerto di riscrivere le etichette martedì, ma non ha ancora confermato la presenza. L’elenco delle etichette illeggibili è nel quaderno sul tavolo.
- Per i nuovi prestiti si usa ancora il modulo consueto. La bozza di modulo breve non è stata approvata: il suo salvataggio nella cartella comune non autorizza a sostituire il modulo attuale.
```

### ultra: pass

```text
## Consegna per l’apertura di domani

**Strumenti e prestiti**
- Registro: 62 strumenti; 56 trovati negli armadi, 4 in prestito con moduli firmati, 2 non trovati. Il rientro dei prestiti è previsto per il 28 maggio.
- Per i 2 mancanti non è stato accertato un furto: potrebbero essere riposti altrove o registrati male. L’ultimo confronto completo tra registro e armadi risale a due mesi fa.
- Cinque levigatrici sono state pulite. Solo L-09 ha superato anche il controllo di funzionamento e può essere prestata: è sul ripiano basso, con il cavo raccolto nella sua borsa. Le altre quattro restano bloccate fino al controllo.
- Il bollino arancione indica solo che la pulizia è finita, non l’autorizzazione al prestito.

**Consumabili: dati provvisori**
- Materiale abrasivo: 2,7 kg comprese le buste; il peso non permette di calcolare quanti fogli siano utilizzabili.
- Nuove buste proposte, ma nessun ordine effettuato.
- Saldo stimato: 95 €, ancora da verificare con tre scontrini. Non è una disponibilità definitiva.

**Locali, etichette e moduli**
- Il pavimento anteriore è stato pulito. La serratura del deposito è difettosa: il deposito resta chiuso finché la serratura non viene riparata e controllata.
- Giulia ha offerto di riscrivere le etichette martedì, ma non ha confermato la presenza. L’elenco delle etichette illeggibili è nel quaderno sul tavolo.
- Per i nuovi prestiti si usa ancora il modulo consueto. La bozza di modulo breve non è approvata: il salvataggio nella cartella comune non autorizza a sostituire il modulo attuale.
```

### off: pass

```text
Consegna per l’apertura di domani

Strumenti e prestiti
Il registro contiene 62 strumenti: 56 sono stati trovati negli armadi, quattro sono in prestito con moduli firmati e due non sono stati trovati. Il rientro dei quattro prestiti è previsto per il 28 maggio. Per i due strumenti mancanti non è stato accertato un furto: potrebbero essere stati riposti altrove o registrati male. L’ultimo confronto completo tra registro e armadi risale a due mesi fa. La presenza negli armadi non va confusa con l’autorizzazione al prestito.

Levigatrici
Sono state pulite cinque levigatrici, ma soltanto L-09 ha superato anche il controllo di funzionamento e può essere prestata. Si trova sul ripiano basso, con il cavo raccolto nella sua borsa. Le altre quattro restano bloccate fino al controllo. Il bollino arancione indica soltanto che la pulizia è finita, non che lo strumento sia autorizzato al prestito.

Consumabili e dati da verificare
Il materiale abrasivo pesa 2,7 kg, comprese le buste: questo dato non permette di calcolare quanti fogli siano utilizzabili. Sono state proposte nuove buste, ma nessun ordine è stato effettuato. Il saldo per i consumabili è stimato in 95 € e deve ancora essere verificato con tre scontrini; non è una disponibilità definitiva.

Etichette e locali
Giulia ha offerto di riscrivere le etichette martedì, ma non ha ancora confermato la presenza. L’elenco delle etichette illeggibili è nel quaderno sul tavolo. Il pavimento anteriore è stato pulito. La serratura del deposito è difettosa: il deposito resta chiuso finché la serratura non viene riparata e controllata.

Moduli per i nuovi prestiti
Si usa ancora il modulo consueto. La bozza di modulo breve non è stata approvata: il semplice salvataggio nella cartella comune non autorizza a sostituire il modulo attuale.
```

## modes-it-071 · long_sampling

Source task:

> Scrivi un breve bilancio di questa consultazione fittizia per il consiglio di un centro culturale. Indica l’opzione più scelta e i limiti della rilevazione. Non aggiungere una raccomandazione sul progetto da finanziare.
> 
> Il questionario proponeva una rassegna di letture, un laboratorio di stampa e un gruppo di conversazione. È stato distribuito per due sere all’ingresso del centro e durante la pausa di un corso di stampa già avviato. Non è stato inviato a tutte le persone iscritte e non esisteva una versione online. Nessuno è stato estratto a sorte da un elenco: partecipare era una scelta volontaria.
> 
> Sono stati consegnati 180 questionari. Novanta sono rientrati con una sola risposta valida. Altri diciotto erano vuoti o avevano più scelte e sono stati esclusi dai risultati. Tra le 90 risposte valide, 45 scelgono la rassegna di letture, 27 il laboratorio di stampa e 18 il gruppo di conversazione. Le letture raccolgono quindi il 50 % delle risposte valide. Il numero complessivo degli iscritti al centro non è fornito.
> 
> Trentasei persone hanno aggiunto un commento. Dodici commenti chiedono un’attività senza prenotazione. I commenti sono stati raccolti in una scatola diversa e non possono essere associati alle scelte individuali. Non sappiamo se chi ha chiesto accesso senza prenotazione abbia preferito soprattutto le letture o un’altra attività.
> 
> Chi distribuiva i fogli ha notato molti partecipanti al corso di stampa, ma non li ha contati separatamente. Alcune persone avrebbero voluto una versione con caratteri più grandi; non era disponibile. Non sono stati raccolti costi, disponibilità dei locali o date possibili dei tre progetti. Il consiglio non ha ancora votato. Il risultato descrive le preferenze espresse da questo gruppo nelle condizioni indicate, non la preferenza accertata di tutti gli iscritti e non una scelta già approvata.

### baseline: pass

```text
La rassegna di letture è l’opzione più scelta: 45 delle 90 risposte valide (50%), contro 27 per il laboratorio di stampa e 18 per il gruppo di conversazione. Su 180 questionari consegnati, 90 sono rientrati validi e 18 sono stati esclusi perché vuoti o con più scelte.

La rilevazione era volontaria e non casuale, limitata a due sere all’ingresso e alla pausa di un corso di stampa. Non ha raggiunto tutti gli iscritti, non prevedeva una versione online né caratteri più grandi. La presenza di molti partecipanti al corso di stampa è stata osservata ma non quantificata; il totale degli iscritti non è noto. I risultati non sono quindi generalizzabili a tutti gli iscritti.

Dei 36 commenti, 12 chiedono un’attività senza prenotazione, ma non possono essere collegati alle preferenze individuali. Mancano inoltre dati su costi, locali e date. Il risultato descrive le preferenze del gruppo consultato nelle condizioni indicate: non costituisce una scelta già approvata dal consiglio.
```

### lite: pass

```text
La rassegna di letture è l’opzione più scelta: 45 delle 90 risposte valide, pari al 50 %. Il laboratorio di stampa raccoglie 27 preferenze e il gruppo di conversazione 18. Dei 180 questionari consegnati, 90 sono rientrati con una sola risposta valida; altri 18, vuoti o con più scelte, sono stati esclusi.

La rilevazione descrive soltanto le preferenze del gruppo che ha partecipato, non quelle accertate di tutti gli iscritti. La partecipazione era volontaria, senza estrazione casuale. I questionari sono stati distribuiti per due sere all’ingresso e durante la pausa di un corso di stampa già avviato, non a tutti gli iscritti. Mancavano una versione online e una versione con caratteri più grandi, richiesta da alcune persone. Il numero complessivo degli iscritti non è fornito. Chi distribuiva i fogli ha notato molti partecipanti al corso di stampa, ma non li ha contati separatamente.

Trentasei persone hanno aggiunto un commento; 12 commenti chiedono un’attività senza prenotazione. Poiché i commenti sono stati raccolti in una scatola separata, non possono essere collegati alle scelte individuali: non sappiamo quale attività preferissero queste persone.

Non sono stati raccolti costi, disponibilità dei locali o date possibili. Il consiglio non ha ancora votato: il risultato non è una scelta già approvata.
```

### full: pass

```text
La rassegna di letture è l’opzione più scelta: 45 delle 90 risposte valide (50 %), contro 27 per il laboratorio di stampa e 18 per il gruppo di conversazione. Su 180 questionari consegnati, 90 sono rientrati con una sola risposta valida; altri 18, vuoti o con più scelte, sono stati esclusi.

La rilevazione non rappresenta necessariamente tutti gli iscritti. La partecipazione era volontaria, senza estrazione casuale. I questionari sono stati distribuiti per due sere all’ingresso e durante la pausa di un corso di stampa già avviato, non a tutti gli iscritti e senza versione online. Sono stati notati molti partecipanti al corso, ma non sono stati contati separatamente. Mancava anche una versione con caratteri più grandi, richiesta da alcune persone. Il numero totale degli iscritti non è noto.

Trentasei persone hanno aggiunto un commento; 12 commenti chiedono un’attività senza prenotazione. Poiché i commenti sono stati raccolti separatamente, non possono essere collegati alle scelte individuali: non sappiamo quale attività preferissero queste persone.

Non sono stati raccolti costi, disponibilità dei locali o date possibili. Il consiglio non ha ancora votato: i risultati descrivono le preferenze espresse da questo gruppo nelle condizioni indicate, non una preferenza accertata di tutti gli iscritti né una scelta approvata.
```

### ultra: pass

```text
La rassegna di letture è l’opzione più scelta: 45 delle 90 risposte valide (50 %), contro 27 per il laboratorio di stampa e 18 per il gruppo di conversazione. Su 180 questionari consegnati, 90 sono rientrati con una sola risposta valida; altri 18, vuoti o con più scelte, sono stati esclusi.

La rilevazione descrive solo le preferenze del gruppo partecipante, non quelle accertate di tutti gli iscritti. La partecipazione era volontaria, senza estrazione casuale. I questionari sono stati distribuiti per due sere all’ingresso e durante la pausa di un corso di stampa già avviato, non a tutti gli iscritti; mancava una versione online. Il totale degli iscritti non è noto. Chi distribuiva i fogli ha notato molti partecipanti al corso di stampa, senza contarli separatamente. Mancava anche una versione a caratteri più grandi, richiesta da alcune persone.

Trentasei persone hanno commentato; 12 commenti chiedono un’attività senza prenotazione. Raccolti in una scatola separata, i commenti non sono collegabili alle scelte: non sappiamo quale attività preferissero queste persone.

Non sono stati raccolti costi, disponibilità dei locali o date possibili. Il consiglio non ha ancora votato: il risultato non è una scelta approvata.
```

### off: pass

```text
La rassegna di letture è l’opzione più scelta: 45 delle 90 risposte valide, pari al 50 %. Seguono il laboratorio di stampa con 27 preferenze e il gruppo di conversazione con 18. Sono stati consegnati 180 questionari; 90 sono rientrati con una sola risposta valida e altri 18, vuoti o con più scelte, sono stati esclusi.

La rilevazione descrive soltanto le preferenze del gruppo che ha risposto. La partecipazione era volontaria, senza estrazione casuale. Il questionario è stato distribuito per due sere all’ingresso e durante la pausa di un corso di stampa già avviato, non a tutti gli iscritti; mancavano una versione online e una versione con caratteri più grandi, richiesta da alcune persone. Sono stati notati molti partecipanti al corso di stampa, ma non sono stati contati separatamente. Il numero complessivo degli iscritti non è disponibile.

Trentasei persone hanno aggiunto un commento; dodici commenti chiedono un’attività senza prenotazione. Poiché i commenti erano raccolti in una scatola separata, non possono essere collegati alle preferenze individuali: non sappiamo quale attività abbia scelto chi chiedeva accesso senza prenotazione.

Non sono stati raccolti costi, disponibilità dei locali o date possibili. Il consiglio non ha ancora votato: il risultato non accerta la preferenza di tutti gli iscritti e non costituisce una scelta approvata.
```

## modes-it-072 · long_scope

Source task:

> Rispondi soltanto a questa domanda: « Possiamo aprire la mostra domenica alle 10 secondo la nota? » Spiega quali condizioni risultano ancora mancanti. Non serve rifare il bilancio economico.
> 
> La nota riguarda una mostra fittizia di modelli in legno. Tutti i 18 supporti sono stati montati e le schede descrittive stampate. Un volontario ha controllato che i nomi sulle schede corrispondano ai modelli. Queste attività non sostituiscono la verifica prevista dal regolamento interno: prima dell’ingresso del pubblico servono una verifica firmata dei supporti e dei passaggi, e due persone formate presenti durante l’apertura.
> 
> La persona incaricata della verifica ha detto che forse potrà passare sabato sera. Non ha confermato l’arrivo e nessuna verifica è stata firmata. Il verbale della mostra precedente riguarda un’altra sala e un altro allestimento, quindi non vale per questa apertura. Per domenica mattina è confermata una sola persona formata. La seconda ha dato disponibilità soltanto per il pomeriggio. Un’altra volontaria disponibile al mattino non ha ancora completato la formazione richiesta.
> 
> Il budget previsto è 780 €. Le spese documentate sono 610 € e manca ancora la fattura del trasporto. Il tesoriere ritiene probabile il rispetto del budget, ma non ha verificato il totale definitivo. Il rispetto del budget non elimina le condizioni per aprire. I volantini preparati riportano domenica alle 10; non sono ancora stati distribuiti.
> 
> Sabato i volontari possono entrare per sistemare le schede, senza visitatori e senza vendite. Questo accesso preparatorio non autorizza l’ingresso del pubblico. La valutazione di domenica deve basarsi su condizioni effettivamente soddisfatte. Un passaggio promesso in modo incerto, un verbale riferito altrove o una presenza nel turno sbagliato non possono essere contati come la verifica e il presidio richiesti.

### baseline: flagged

```text
Non ancora: secondo la nota, le condizioni per aprire al pubblico domenica alle 10 non risultano soddisfatte.

Mancano:
- la verifica firmata dei supporti e dei passaggi: l’arrivo dell’incaricato sabato sera è incerto e il verbale precedente riguarda un’altra sala e un altro allestimento;
- due persone formate presenti durante l’apertura: al mattino ne è confermata soltanto una. La seconda è disponibile solo nel pomeriggio e l’altra volontaria del mattino non ha completato la formazione.

Il montaggio, il controllo delle schede e l’accesso preparatorio di sabato non sostituiscono questi requisiti. L’apertura alle 10 sarà possibile solo se entrambe le condizioni saranno effettivamente soddisfatte prima dell’ingresso del pubblico.
```

Review notes: Individua correttamente verifica e presidio mancanti, ma lascia fuori ulteriori limiti richiesti dai criteri. / Individua correttamente le due condizioni mancanti, ma tralascia parte dei limiti richiesti.

### lite: flagged

```text
Non ancora: secondo la nota, le condizioni per aprire domenica alle 10 non risultano soddisfatte.

Mancano una verifica firmata dei supporti e dei passaggi e la conferma di due persone formate presenti durante l’apertura. La persona incaricata della verifica ha soltanto detto che forse passerà sabato sera; il verbale precedente riguarda un’altra sala e un altro allestimento. Domenica mattina è confermata una sola persona formata: la seconda è disponibile solo nel pomeriggio e l’altra volontaria disponibile al mattino non ha completato la formazione.

Il montaggio, il controllo delle schede, l’orario sui volantini e l’accesso preparatorio di sabato non sostituiscono questi requisiti. L’apertura alle 10 dipende dal loro effettivo completamento prima dell’ingresso del pubblico.
```

Review notes: Non inventa un’autorizzazione, ma omette il vincolo sulle vendite e l’irrilevanza autorizzativa del budget. / Conclusione e requisiti principali corretti; omette il limite sulle vendite preparatorie e la non sostitutività del budget.

### full: flagged

```text
Non ancora: secondo la nota, le condizioni per aprire domenica alle 10 non sono soddisfatte.

Mancano:
- La verifica firmata dei supporti e dei passaggi. La persona incaricata non ha confermato il passaggio di sabato sera; il verbale della mostra precedente riguarda un’altra sala e un altro allestimento e non vale per questa apertura.
- Due persone formate presenti durante l’apertura. Domenica mattina ne è confermata una sola. La seconda è disponibile solo nel pomeriggio; l’altra volontaria disponibile al mattino non ha completato la formazione.

Il montaggio dei 18 supporti, la stampa delle schede e il controllo dei nomi non sostituiscono questi requisiti. Nemmeno l’accesso preparatorio dei volontari il sabato autorizza l’ingresso del pubblico. L’apertura alle 10 sarà possibile solo se le condizioni richieste saranno effettivamente soddisfatte.
```

Review notes: Risponde correttamente sulle due condizioni mancanti, ma omette i limiti su vendite, budget e volantini. / Preserva la risposta e le condizioni essenziali, ma omette alcuni limiti esplicitamente richiesti.

### ultra: pass

```text
Non ancora: secondo la nota, le condizioni per aprire domenica alle 10 non risultano soddisfatte.

- Manca la verifica firmata dei supporti e dei passaggi. L’incaricato non ha confermato il possibile passaggio di sabato sera. Il verbale precedente riguarda un’altra sala e un altro allestimento e non vale per questa apertura.
- Devono essere presenti due persone formate durante l’apertura. Domenica mattina ne è confermata una sola; la seconda è disponibile soltanto nel pomeriggio e l’altra volontaria disponibile al mattino non ha completato la formazione.

Il montaggio dei 18 supporti, la stampa delle schede e il controllo dei nomi non sostituiscono questi requisiti. Né il rispetto del budget, né l’orario sui volantini ancora non distribuiti autorizzano l’apertura. L’accesso preparatorio di sabato, senza visitatori e senza vendite, non autorizza l’ingresso del pubblico. Si potrà aprire alle 10 solo se le condizioni richieste saranno effettivamente soddisfatte.
```

### off: flagged

```text
Non ancora: secondo la nota, l’apertura al pubblico domenica alle 10 non è autorizzata dalle condizioni attualmente soddisfatte. Mancano:

- La verifica firmata dei supporti e dei passaggi. La persona incaricata non ha confermato il passaggio di sabato sera e nessuna verifica è stata firmata. Il verbale precedente riguarda un’altra sala e un altro allestimento, quindi non vale.
- Due persone formate presenti durante l’apertura. Per domenica mattina ne è confermata soltanto una; la seconda è disponibile solo nel pomeriggio e l’altra volontaria disponibile al mattino non ha completato la formazione.

Il montaggio dei 18 supporti, la stampa delle schede e il controllo dei nomi non sostituiscono questi requisiti. Nemmeno l’accesso preparatorio dei volontari sabato o l’orario indicato sui volantini autorizzano l’ingresso del pubblico. Si potrà aprire alle 10 soltanto se entrambe le condizioni saranno effettivamente soddisfatte.
```

Review notes: Corretta sulle condizioni effettive; incompleta sui limiti dell’accesso preparatorio e del budget. / Risposta ben calibrata sui requisiti principali, ma incompleta sui limiti delle attività preparatorie e del budget.

## modes-it-073 · long_technical

Source task:

> Riscrivi questa procedura fittizia per una persona già formata. Deve essere più facile seguirla senza cambiare i comandi, il loro ordine o la portata del controllo. Non aggiungere riparazioni automatiche.
> 
> La cartella di lavoro è /opt/catalogo/batch-5. Per prima cosa occorre chiudere il programma di consultazione, perché potrebbe modificare i metadati mentre vengono copiati. Poi bisogna copiare records.xml nella sottocartella initial/. Questa copia conserva lo stato dell’indice, non tutti i documenti. Non comprende immagini o registrazioni audio e non è un backup completo dell’archivio.
> 
> Eseguire quindi verify_refs --input records.xml --output check.log. Il comando cerca riferimenti il cui file non è accessibile dall’account utilizzato. Non modifica i record e non recupera file cancellati. Un rapporto vuoto significa soltanto che in quel passaggio non sono stati trovati riferimenti inaccessibili. Non dimostra che ogni documento sia integro o corretto. Un file non accessibile a questo account potrebbe esserlo per un altro.
> 
> Se compare ACTIVE_LOCK, bisogna interrompere la procedura e conservare check.log anche se incompleto. Il blocco non deve essere rimosso manualmente. Il gruppo di supporto esaminerà il motivo prima di indicare come proseguire. Se l’errore di blocco non compare, confrontare il numero di riferimenti verificati con quello di initial/records.xml. Le differenze vanno annotate senza correggere automaticamente l’indice.
> 
> Infine registrare l’ora in UTC e il nome dell’account usato. Un account condiviso non permette di attribuire l’operazione a una persona specifica. Il programma di consultazione può essere riaperto solo dopo il salvataggio del rapporto e di questi dati. Il controllo riguarda la copia locale e non conferma lo stato della copia remota, sottoposta a una procedura distinta. Nessuna parte di questo controllo autorizza a eliminare materiale.

### baseline: pass

```text
Cartella di lavoro: `/opt/catalogo/batch-5`.

1. Chiudere il programma di consultazione, che potrebbe modificare i metadati durante la copia.
2. Copiare `records.xml` nella sottocartella `initial/`. La copia conserva lo stato dell’indice, non tutti i documenti: esclude immagini e registrazioni audio e non è un backup completo dell’archivio.
3. Eseguire:
   `verify_refs --input records.xml --output check.log`
   Il comando cerca riferimenti a file non accessibili dall’account utilizzato. Non modifica i record e non recupera file cancellati. Un rapporto vuoto indica soltanto che in questo passaggio non sono stati trovati riferimenti inaccessibili: non certifica integrità o correttezza dei documenti. Un file inaccessibile a questo account potrebbe essere accessibile a un altro.
4. Controllare se compare `ACTIVE_LOCK`:
   - Se compare, interrompere la procedura e conservare `check.log`, anche incompleto. Non rimuovere manualmente il blocco. Il gruppo di supporto ne esaminerà il motivo prima di indicare come proseguire.
   - Se non compare, confrontare il numero di riferimenti verificati con quello di `initial/records.xml`. Annotare le differenze senza correggere automaticamente l’indice.
5. Registrare l’ora in UTC e il nome dell’account utilizzato. Un account condiviso non consente di attribuire l’operazione a una persona specifica.
6. Salvare il rapporto e questi dati prima di riaprire il programma di consultazione.

Il controllo riguarda solo la copia locale. Non conferma lo stato della copia remota, che segue una procedura distinta, e non autorizza a eliminare materiale.
```

### lite: pass

```text
La cartella di lavoro è /opt/catalogo/batch-5. Per prima cosa, chiudere il programma di consultazione: potrebbe modificare i metadati durante la copia. Poi copiare records.xml nella sottocartella initial/. La copia conserva lo stato dell’indice, non tutti i documenti. Non comprende immagini o registrazioni audio e non è un backup completo dell’archivio.

Eseguire quindi verify_refs --input records.xml --output check.log. Il comando cerca riferimenti a file non accessibili dall’account utilizzato. Non modifica i record e non recupera file cancellati. Un rapporto vuoto indica soltanto che in quel passaggio non sono stati trovati riferimenti inaccessibili: non dimostra che ogni documento sia integro o corretto. Un file non accessibile a questo account potrebbe essere accessibile a un altro.

Se compare ACTIVE_LOCK, interrompere la procedura e conservare check.log, anche se incompleto. Non rimuovere manualmente il blocco. Il gruppo di supporto ne esaminerà il motivo prima di indicare come proseguire. Se ACTIVE_LOCK non compare, confrontare il numero di riferimenti verificati con quello di initial/records.xml. Annotare le differenze senza correggere automaticamente l’indice.

Infine, registrare l’ora in UTC e il nome dell’account usato. Un account condiviso non permette di attribuire l’operazione a una persona specifica. Riaprire il programma di consultazione solo dopo aver salvato il rapporto e questi dati. Il controllo riguarda la copia locale: non conferma lo stato della copia remota, che segue una procedura distinta. Nessuna parte del controllo autorizza a eliminare materiale.
```

### full: pass

```text
Cartella di lavoro: `/opt/catalogo/batch-5`.

1. Chiudere il programma di consultazione: potrebbe modificare i metadati durante la copia.
2. Copiare `records.xml` nella sottocartella `initial/`. La copia conserva lo stato dell’indice, non tutti i documenti. Non include immagini o registrazioni audio e non è un backup completo dell’archivio.
3. Eseguire:
   `verify_refs --input records.xml --output check.log`

   Il comando cerca riferimenti a file non accessibili dall’account utilizzato. Non modifica i record e non recupera file cancellati. Un rapporto vuoto indica soltanto che in quel passaggio non sono stati trovati riferimenti inaccessibili: non dimostra che ogni documento sia integro o corretto. Un file non accessibile a questo account potrebbe esserlo per un altro.
4. Se compare `ACTIVE_LOCK`, interrompere la procedura e conservare `check.log`, anche se incompleto. Non rimuovere manualmente il blocco. Il gruppo di supporto ne esaminerà il motivo prima di indicare come proseguire.
5. Se non compare l’errore di blocco, confrontare il numero di riferimenti verificati con quello di `initial/records.xml`. Annotare le differenze senza correggere automaticamente l’indice.
6. Registrare l’ora in UTC e il nome dell’account usato. Un account condiviso non consente di attribuire l’operazione a una persona specifica.
7. Riaprire il programma di consultazione solo dopo aver salvato il rapporto e questi dati.

Il controllo riguarda la copia locale. Non conferma lo stato della copia remota, che segue una procedura distinta. Nessuna parte del controllo autorizza a eliminare materiale.
```

### ultra: pass

```text
Cartella di lavoro: `/opt/catalogo/batch-5`.

1. Chiudere il programma di consultazione: potrebbe modificare i metadati durante la copia.
2. Copiare `records.xml` nella sottocartella `initial/`. La copia conserva lo stato dell’indice, non tutti i documenti: esclude immagini e registrazioni audio e non è un backup completo dell’archivio.
3. Eseguire:
   `verify_refs --input records.xml --output check.log`
   Il comando cerca riferimenti a file non accessibili dall’account usato. Non modifica i record né recupera file cancellati. Un rapporto vuoto indica solo che in quel passaggio non sono stati trovati riferimenti inaccessibili: non prova l’integrità o la correttezza di ogni documento. Un file inaccessibile a questo account potrebbe essere accessibile a un altro.
4. Se compare `ACTIVE_LOCK`, interrompere la procedura e conservare `check.log`, anche incompleto. Non rimuovere manualmente il blocco. Il gruppo di supporto ne esaminerà il motivo prima di indicare come proseguire.
5. Se non compare l’errore di blocco, confrontare il numero di riferimenti verificati con quello di `initial/records.xml`. Annotare le differenze senza correggere automaticamente l’indice.
6. Registrare l’ora in UTC e il nome dell’account usato. Un account condiviso non permette di attribuire l’operazione a una persona specifica.
7. Riaprire il programma di consultazione solo dopo aver salvato il rapporto e questi dati.

Il controllo riguarda la copia locale, non conferma lo stato della copia remota, che richiede una procedura distinta. Nessuna parte del controllo autorizza a eliminare materiale.
```

### off: pass

```text
Cartella di lavoro: /opt/catalogo/batch-5.

1. Chiudere il programma di consultazione: potrebbe modificare i metadati durante la copia.

2. Copiare records.xml nella sottocartella initial/. La copia conserva lo stato dell’indice, non tutti i documenti. Non comprende immagini o registrazioni audio e non è un backup completo dell’archivio.

3. Eseguire:

   verify_refs --input records.xml --output check.log

   Il comando cerca riferimenti il cui file non è accessibile dall’account utilizzato. Non modifica i record e non recupera file cancellati. Un rapporto vuoto indica soltanto che, in quel passaggio, non sono stati trovati riferimenti inaccessibili: non dimostra che ogni documento sia integro o corretto. Un file non accessibile all’account usato potrebbe essere accessibile a un altro account.

4. Se compare ACTIVE_LOCK, interrompere la procedura e conservare check.log, anche se incompleto. Non rimuovere manualmente il blocco. Il gruppo di supporto ne esaminerà il motivo prima di indicare come proseguire.

   Se ACTIVE_LOCK non compare, confrontare il numero di riferimenti verificati con quello di initial/records.xml. Annotare le differenze senza correggere automaticamente l’indice.

5. Registrare l’ora in UTC e il nome dell’account usato. Un account condiviso non permette di attribuire l’operazione a una persona specifica.

6. Riaprire il programma di consultazione solo dopo aver salvato il rapporto e questi dati.

Il controllo riguarda la copia locale. Non conferma lo stato della copia remota, che segue una procedura distinta. Nessuna parte del controllo autorizza a eliminare materiale.
```

## modes-it-074 · long_conflicting_notes

Source task:

> Prepara una sintesi per la riunione distinguendo accordi, contraddizioni e ipotesi non verificate. Tutto il caso è fittizio: non cercare informazioni esterne e non scegliere autonomamente quale documento prevale.
> 
> Si deve trasferire una collezione di tessuti in un deposito provvisorio. Il messaggio di lunedì indica 34 scatole. Il prospetto di martedì contiene 36 righe. Due righe sono chiamate « imballaggi ». Non è stato chiarito se siano due scatole in più oppure materiale già contenuto nelle 34 scatole. I documenti concordano sullo stesso trasportatore e su un unico viaggio.
> 
> Il messaggio prevede il ritiro il 7 settembre alle 8:45. Il prospetto indica l’8 settembre alle 8:45. Il trasportatore ha ricevuto entrambi ma non ha confermato la data. Il documento successivo, da solo, non prova che il cambio sia stato accettato. Chi apre il deposito ha tenuto libere entrambe le mattine per prudenza: non sono due ritiri concordati.
> 
> Il preventivo firmato è di 470 € IVA esclusa per un massimo di 34 scatole. Nel prospetto interno compaiono 515 € IVA esclusa, senza un nuovo preventivo. Si ipotizza che i 45 € aggiuntivi siano per gli imballaggi, ma nessuno ha verificato questa spiegazione. Il budget riservato è 600 € IVA esclusa e non stabilisce il prezzo effettivo.
> 
> Entrambi i documenti chiedono di segnare le scatole contenenti tessuti fragili prima del carico. Chiara ha completato l’elenco, ma i segni sulle scatole non sono stati applicati. Il nuovo indirizzo è confermato. Il codice del cancello non è ancora stato comunicato al trasportatore. La riunione deve chiarire quantità, data, prezzo e accesso. La sintesi deve rendere visibili questi punti senza convertirli in decisioni o attribuire a qualcuno un’attività che non risulta eseguita.

### baseline: pass

```text
**Accordi e fatti confermati**
- I documenti indicano lo stesso trasportatore e un unico viaggio.
- Il nuovo indirizzo è confermato.
- Entrambi richiedono di segnare le scatole con tessuti fragili prima del carico. Chiara ha completato l’elenco, ma i segni non sono ancora stati applicati.

**Contraddizioni e punti da chiarire**
- Quantità: il messaggio indica 34 scatole; il prospetto contiene 36 righe, di cui due denominate «imballaggi». Non è chiarito se queste rappresentino scatole aggiuntive o materiale già nelle 34 scatole.
- Data: il messaggio indica il 7 settembre alle 8:45, il prospetto l’8 settembre alla stessa ora. Il trasportatore ha ricevuto entrambi, ma non ha confermato la data. Il documento successivo non dimostra l’accettazione del cambiamento; le due mattine tenute libere non sono due ritiri concordati.
- Prezzo: il preventivo firmato prevede 470 € IVA esclusa per un massimo di 34 scatole; il prospetto interno riporta 515 € IVA esclusa senza un nuovo preventivo. Il budget di 600 € IVA esclusa non stabilisce il prezzo effettivo.
- Accesso: il codice del cancello non è ancora stato comunicato al trasportatore.

**Ipotesi non verificate**
- Le due righe «imballaggi» potrebbero indicare scatole aggiuntive oppure materiale già incluso.
- I 45 € aggiuntivi potrebbero riguardare gli imballaggi, ma questa spiegazione non è stata verificata.

La riunione deve chiarire quantità, data, prezzo e accesso, senza considerare già risolte le divergenze.
```

### lite: pass

```text
**Accordi e stato delle attività**
La collezione di tessuti deve essere trasferita in un deposito provvisorio. I documenti concordano sul trasportatore e su un unico viaggio. Il nuovo indirizzo è confermato. Entrambi chiedono di segnare le scatole con tessuti fragili prima del carico: Chiara ha completato l’elenco, ma i segni non sono stati applicati. Il codice del cancello non è ancora stato comunicato al trasportatore.

**Contraddizioni e punti da chiarire**
- Quantità: il messaggio di lunedì indica 34 scatole; il prospetto di martedì contiene 36 righe, due delle quali chiamate « imballaggi ». Non è chiaro se siano due scatole aggiuntive o materiale già contenuto nelle 34.
- Data: il messaggio indica il 7 settembre alle 8:45; il prospetto l’8 settembre alle 8:45. Il trasportatore ha ricevuto entrambi, ma non ha confermato la data. Il documento successivo non prova, da solo, che il cambio sia stato accettato.
- Prezzo: il preventivo firmato è di 470 € IVA esclusa per un massimo di 34 scatole. Il prospetto interno riporta 515 € IVA esclusa, senza un nuovo preventivo. Il budget riservato di 600 € IVA esclusa non stabilisce il prezzo effettivo.

**Ipotesi non verificate**
Non è stata verificata l’ipotesi che i 45 € aggiuntivi siano il costo degli imballaggi. Chi apre il deposito ha tenuto libere entrambe le mattine per prudenza: questo non significa che siano stati concordati due ritiri.

La riunione deve chiarire quantità, data, prezzo e accesso. Nessuno di questi punti è risolto scegliendo automaticamente quale documento prevale.
```

### full: pass

```text
La riunione deve chiarire quantità, data, prezzo e accesso al deposito provvisorio. Nessuno dei punti discordanti risulta risolto.

**Accordi e stato confermato**
- I documenti indicano lo stesso trasportatore e un unico viaggio.
- Entrambi richiedono di segnare le scatole con tessuti fragili prima del carico. Chiara ha completato l’elenco, ma i segni sulle scatole non sono stati applicati.
- Il nuovo indirizzo è confermato. Il codice del cancello non è ancora stato comunicato al trasportatore.

**Contraddizioni e ambiguità**
- **Quantità:** il messaggio di lunedì indica 34 scatole; il prospetto di martedì contiene 36 righe, di cui due chiamate « imballaggi ». Non è chiaro se rappresentino due scatole aggiuntive o materiale già incluso nelle 34.
- **Data:** il messaggio prevede il ritiro il 7 settembre alle 8:45; il prospetto indica l’8 settembre alle 8:45. Il trasportatore ha ricevuto entrambi, ma non ha confermato la data. Il documento successivo non prova da solo l’accettazione del cambio. Le due mattine tenute libere da chi apre il deposito sono una precauzione, non due ritiri concordati.
- **Prezzo:** il preventivo firmato è di 470 € IVA esclusa per un massimo di 34 scatole. Il prospetto interno riporta 515 € IVA esclusa, senza un nuovo preventivo. Il budget di 600 € IVA esclusa non stabilisce il prezzo effettivo.

**Ipotesi non verificata**
Si ipotizza che i 45 € aggiuntivi siano destinati agli imballaggi, ma questa spiegazione non è stata verificata.
```

### ultra: pass

```text
La riunione deve chiarire quantità, data, prezzo e accesso per il trasferimento della collezione di tessuti al deposito provvisorio.

**Accordi e stato confermato**
- I documenti indicano lo stesso trasportatore e un unico viaggio. Il nuovo indirizzo è confermato.
- Entrambi richiedono di segnare le scatole con tessuti fragili prima del carico. Chiara ha completato l’elenco, ma i segni non sono stati applicati.
- Il codice del cancello non è ancora stato comunicato al trasportatore.

**Contraddizioni e punti irrisolti**
- Quantità: il messaggio di lunedì indica 34 scatole; il prospetto di martedì contiene 36 righe, due chiamate «imballaggi». Non è chiaro se rappresentino due scatole aggiuntive o materiale già nelle 34.
- Data: il messaggio prevede il 7 settembre alle 8:45; il prospetto l’8 settembre alle 8:45. Il trasportatore ha ricevuto entrambi, ma non ha confermato la data. Il documento successivo non prova che il cambio sia stato accettato. Chi apre il deposito ha tenuto libere entrambe le mattine per prudenza: non sono due ritiri concordati.
- Prezzo: il preventivo firmato è di 470 € IVA esclusa, per un massimo di 34 scatole. Il prospetto interno riporta 515 € IVA esclusa, senza un nuovo preventivo. Il budget di 600 € IVA esclusa non stabilisce il prezzo effettivo.

**Ipotesi non verificata**
I 45 € aggiuntivi potrebbero riguardare gli imballaggi, ma la spiegazione non è stata verificata. Nessuna delle discrepanze è qui risolta scegliendo quale documento prevale.
```

### off: pass

```text
**Accordi e stato confermato**
- I documenti indicano lo stesso trasportatore e un unico viaggio.
- Entrambi richiedono di segnare, prima del carico, le scatole contenenti tessuti fragili. Chiara ha completato l’elenco, ma i segni sulle scatole non sono stati applicati.
- Il nuovo indirizzo è confermato. Il codice del cancello non è ancora stato comunicato al trasportatore.

**Contraddizioni e punti da chiarire**
- **Quantità:** il messaggio di lunedì indica 34 scatole; il prospetto di martedì contiene 36 righe, di cui due chiamate « imballaggi ». Non è chiarito se rappresentino due scatole aggiuntive o materiale già contenuto nelle 34.
- **Data:** il messaggio prevede il ritiro il 7 settembre alle 8:45; il prospetto indica l’8 settembre alle 8:45. Il trasportatore ha ricevuto entrambi, ma non ha confermato la data.
- **Prezzo:** il preventivo firmato è di 470 € IVA esclusa per un massimo di 34 scatole. Il prospetto interno riporta 515 € IVA esclusa, senza un nuovo preventivo. Il budget riservato di 600 € IVA esclusa non stabilisce il prezzo effettivo.

**Ipotesi non verificate**
- Non è verificato che i 45 € aggiuntivi siano destinati agli imballaggi.
- Il prospetto successivo non prova, da solo, che il cambio di data sia stato accettato.
- Chi apre il deposito ha tenuto libere entrambe le mattine per prudenza: questo non significa che siano concordati due ritiri.

La riunione deve chiarire quantità, data, prezzo e accesso, senza considerare già risolte le divergenze tra i documenti.
```

## modes-it-075 · long_policy

Source task:

> Semplifica questo regolamento fittizio per un corso di stampa. Mantieni i diritti, gli obblighi e le eccezioni. Non fornire un parere legale e non integrare usanze che il testo non prevede.
> 
> L’iscrizione comprende sei incontri. Ogni persona può chiedere di spostarne uno, avvisando almeno 24 ore prima e soltanto se c’è un posto libero in un altro gruppo dello stesso ciclo. Avvisare in tempo non garantisce il posto alternativo. Se non c’è disponibilità, l’incontro originario resta prenotato. Per cedere il posto a un’altra persona serve il consenso scritto dell’associazione.
> 
> Se l’associazione annulla un incontro, deve proporne uno sostitutivo. La persona iscritta può rifiutarlo e ricevere il rimborso dell’incontro annullato. Questo diritto non vale per un’assenza personale, salvo una deroga scritta concessa per quello specifico incontro. Una deroga non si estende automaticamente agli altri appuntamenti del corso.
> 
> Gli strumenti comuni si possono usare nel laboratorio durante gli incontri, ma non si possono portare a casa, neppure per finire un lavoro già iniziato. Prima di uscire bisogna pulirli e rimetterli nei contenitori segnati. Eventuali danni osservati devono essere segnalati anche se gli strumenti sono stati riposti. Segnalare un danno non significa, da solo, ammettere di averlo causato.
> 
> Le stampe personali vengono conservate per cinque settimane dopo l’ultimo incontro. L’associazione deve mandare un promemoria prima della scadenza. Il testo non stabilisce che cosa accada se il promemoria non viene mandato: non bisogna inventare una procedura. Le immagini dei lavori possono apparire nel bollettino solo con il consenso della persona che li ha realizzati. Il consenso a una foto non autorizza tutte le foto future. Rifiutare la pubblicazione non comporta la perdita del posto al corso.

### baseline: pass

```text
**Iscrizione e spostamenti**
- L’iscrizione comprende sei incontri.
- Puoi chiedere di spostare un solo incontro, avvisando almeno 24 ore prima. Lo spostamento è possibile solo se c’è un posto libero in un altro gruppo dello stesso ciclo.
- Avvisare in tempo non garantisce un posto alternativo. Se non c’è disponibilità, resta prenotato l’incontro originario.
- Per cedere il posto a un’altra persona serve il consenso scritto dell’associazione.

**Annullamenti e assenze**
- Se l’associazione annulla un incontro, deve proporne uno sostitutivo. Puoi rifiutarlo e ricevere il rimborso dell’incontro annullato.
- Questo diritto non vale per un’assenza personale, salvo una deroga scritta concessa per quello specifico incontro. La deroga non vale automaticamente per gli altri incontri.

**Strumenti comuni**
- Puoi usarli nel laboratorio durante gli incontri. Non puoi portarli a casa, nemmeno per finire un lavoro iniziato.
- Prima di uscire, puliscili e rimettili nei contenitori segnati.
- Segnala eventuali danni osservati, anche se gli strumenti sono già stati riposti. La segnalazione, da sola, non significa ammettere di aver causato il danno.

**Conservazione e immagini dei lavori**
- Le stampe personali sono conservate per cinque settimane dopo l’ultimo incontro. L’associazione deve inviare un promemoria prima della scadenza. Il regolamento non precisa che cosa accada se non lo invia.
- Le immagini dei lavori possono essere pubblicate nel bollettino solo con il consenso di chi li ha realizzati. Il consenso a una foto non autorizza tutte le foto future.
- Rifiutare la pubblicazione non comporta la perdita del posto al corso.
```

### lite: pass

```text
L’iscrizione comprende sei incontri. Ogni persona può chiedere di spostarne uno, avvisando almeno 24 ore prima, solo se c’è un posto libero in un altro gruppo dello stesso ciclo. Avvisare in tempo non garantisce un posto alternativo. Se non c’è disponibilità, l’incontro originario resta prenotato. Per cedere il posto a un’altra persona serve il consenso scritto dell’associazione.

Se l’associazione annulla un incontro, deve proporne uno sostitutivo. La persona iscritta può rifiutarlo e ricevere il rimborso dell’incontro annullato. Questo diritto non vale per un’assenza personale, salvo una deroga scritta concessa per quello specifico incontro. La deroga non si estende automaticamente agli altri incontri.

Gli strumenti comuni si possono usare nel laboratorio durante gli incontri, ma non si possono portare a casa, neppure per finire un lavoro già iniziato. Prima di uscire bisogna pulirli e rimetterli nei contenitori segnati. I danni osservati devono essere segnalati anche se gli strumenti sono già stati riposti. Segnalare un danno non significa, da solo, ammettere di averlo causato.

Le stampe personali vengono conservate per cinque settimane dopo l’ultimo incontro. L’associazione deve mandare un promemoria prima della scadenza. Il regolamento non stabilisce che cosa accada se il promemoria non viene mandato. Le immagini dei lavori possono apparire nel bollettino solo con il consenso della persona che li ha realizzati. Il consenso a una foto non autorizza tutte le foto future. Rifiutare la pubblicazione non comporta la perdita del posto al corso.
```

### full: pass

```text
**Iscrizione e spostamenti**
L’iscrizione comprende sei incontri. Ogni persona può chiedere di spostarne uno, avvisando almeno 24 ore prima. Lo spostamento è possibile solo se c’è un posto libero in un altro gruppo dello stesso ciclo. Il preavviso non garantisce un posto alternativo: se non c’è disponibilità, l’incontro originario resta prenotato.

Per cedere il posto a un’altra persona serve il consenso scritto dell’associazione.

**Annullamenti e assenze**
Se l’associazione annulla un incontro, deve proporne uno sostitutivo. La persona iscritta può rifiutarlo e ricevere il rimborso dell’incontro annullato.

Questo diritto non vale per un’assenza personale, salvo una deroga scritta concessa per quello specifico incontro. La deroga non si estende automaticamente agli altri incontri.

**Strumenti comuni**
Gli strumenti comuni si possono usare nel laboratorio durante gli incontri. Non si possono portare a casa, nemmeno per finire un lavoro già iniziato.

Prima di uscire bisogna pulirli e riporli nei contenitori segnati. I danni osservati devono essere segnalati anche se gli strumenti sono già stati riposti. Segnalare un danno non significa, da solo, ammettere di averlo causato.

**Conservazione e immagini dei lavori**
Le stampe personali vengono conservate per cinque settimane dopo l’ultimo incontro. L’associazione deve inviare un promemoria prima della scadenza. Il regolamento non stabilisce che cosa accada se il promemoria non viene inviato.

Le immagini dei lavori possono apparire nel bollettino solo con il consenso di chi li ha realizzati. Il consenso a una foto non autorizza tutte le foto future. Rifiutare la pubblicazione non comporta la perdita del posto al corso.
```

### ultra: pass

```text
**Iscrizione e spostamenti**
L’iscrizione comprende sei incontri. Puoi chiedere di spostarne uno, con almeno 24 ore di preavviso, solo se c’è un posto libero in un altro gruppo dello stesso ciclo. Il preavviso non garantisce il posto: senza disponibilità, resta prenotato l’incontro originario. Per cedere il posto a un’altra persona serve il consenso scritto dell’associazione.

**Annullamenti e assenze**
Se l’associazione annulla un incontro, deve proporne uno sostitutivo. Puoi rifiutarlo e ottenere il rimborso dell’incontro annullato. Questo diritto non vale per un’assenza personale, salvo una deroga scritta concessa per quello specifico incontro. La deroga non si estende automaticamente agli altri incontri.

**Strumenti comuni**
Puoi usarli nel laboratorio durante gli incontri, ma non portarli a casa, neppure per finire un lavoro iniziato. Prima di uscire devi pulirli e riporli nei contenitori segnati. Devi segnalare eventuali danni osservati anche se gli strumenti sono già stati riposti. La segnalazione, da sola, non è un’ammissione di aver causato il danno.

**Stampe e immagini**
Le stampe personali vengono conservate per cinque settimane dopo l’ultimo incontro. L’associazione deve inviare un promemoria prima della scadenza. Il regolamento non stabilisce cosa accada se non lo invia.

Le immagini dei lavori possono apparire nel bollettino solo con il consenso di chi li ha realizzati. Il consenso a una foto non autorizza tutte le foto future. Rifiutare la pubblicazione non comporta la perdita del posto al corso.
```

### off: pass

```text
**Iscrizione e spostamenti**
L’iscrizione comprende sei incontri. Ogni persona può chiedere di spostare un solo incontro, avvisando almeno 24 ore prima. Lo spostamento è possibile soltanto se c’è un posto libero in un altro gruppo dello stesso ciclo.

Avvisare in tempo non garantisce un posto alternativo. Se non c’è disponibilità, resta prenotato l’incontro originario. Per cedere il posto a un’altra persona serve il consenso scritto dell’associazione.

**Annullamenti e assenze**
Se l’associazione annulla un incontro, deve proporne uno sostitutivo. La persona iscritta può rifiutarlo e ottenere il rimborso dell’incontro annullato.

Questo diritto non vale per un’assenza personale, salvo una deroga scritta concessa per quello specifico incontro. La deroga non si estende automaticamente agli altri incontri.

**Strumenti comuni**
Gli strumenti comuni possono essere usati nel laboratorio durante gli incontri. Non possono essere portati a casa, neppure per terminare un lavoro già iniziato.

Prima di uscire, bisogna pulirli e riporli nei contenitori segnati. Eventuali danni osservati devono essere segnalati anche se gli strumenti sono già stati riposti. La segnalazione, da sola, non significa ammettere di aver causato il danno.

**Conservazione delle stampe**
Le stampe personali vengono conservate per cinque settimane dopo l’ultimo incontro. L’associazione deve inviare un promemoria prima della scadenza. Il regolamento non stabilisce che cosa accada se il promemoria non viene inviato.

**Pubblicazione delle immagini**
Le immagini dei lavori possono apparire nel bollettino soltanto con il consenso della persona che li ha realizzati. Il consenso a una foto non autorizza tutte le foto future. Rifiutare la pubblicazione non comporta la perdita del posto al corso.
```

## modes-it-076 · long_calculation

Source task:

> Rispondi alle due domande sul budget: quanto resta dopo le spese confermate e quanto resterebbe se fosse approvato l’acquisto aggiuntivo? Mostra i calcoli. Le altre informazioni spiegano il contesto e non devono diventare spese inventate.
> 
> Un gruppo prepara un laboratorio fittizio di rilegatura. Il budget per i materiali è 650 €. L’affitto della sala viene pagato da un fondo diverso e non deve essere sottratto da questo budget. Eventuali offerte ricevute durante la giornata non sono note, quindi non si possono sommare come entrate. Non è richiesto stimare il ricavo dell’attività.
> 
> Sono già stati acquistati e pagati 16 pacchi di cartoncino a 7 € ciascuno, 9 flaconi di colla a 5 € ciascuno e 6 confezioni di aghi a 13 € ciascuna. La spedizione per tutto questo ordine è costata 15 € una sola volta. I prezzi comprendono le imposte. Non ci sono sconti confermati o ulteriori costi di consegna. Il numero di aghi nelle confezioni varia, ma non modifica il prezzo totale indicato.
> 
> È stato proposto un secondo ordine di 14 rocchetti di filo a 6 € ciascuno, con 11 € di spedizione. L’ordine non è approvato e non è stato pagato. Va escluso dal saldo attuale e incluso interamente nel saldo condizionale. Il preventivo non prevede altre spese. La sintesi non deve far sembrare che i rocchetti siano già stati acquistati.
> 
> Due tavoli sono stati prestati gratuitamente e alcuni volontari porteranno forbici proprie. Si è parlato anche di un futuro taglierino, senza prezzo o richiesta formale. Nessuna di queste informazioni permette di aggiungere un costo al calcolo. Tieni separati il saldo effettivo e quello ipotetico dopo il filo. Non usare il saldo per dichiarare approvato l’acquisto e non trasformare il fondo della sala in una spesa dei materiali.

### baseline: pass

```text
Spese confermate:
- Cartoncino: 16 × 7 € = 112 €
- Colla: 9 × 5 € = 45 €
- Aghi: 6 × 13 € = 78 €
- Spedizione: 15 €
Totale: 112 + 45 + 78 + 15 = 250 €.

Saldo effettivo: 650 − 250 = 400 €.

Il secondo ordine, non approvato né pagato, costerebbe: 14 × 6 € + 11 € = 95 €.
Saldo ipotetico se fosse approvato: 400 − 95 = 305 €.

Non sono inclusi altri costi o entrate: l’affitto è pagato da un fondo diverso e le offerte non sono note.
```

### lite: pass

```text
Dopo le spese confermate restano 400 €.

- Cartoncino: 16 × 7 € = 112 €
- Colla: 9 × 5 € = 45 €
- Aghi: 6 × 13 € = 78 €
- Spedizione unica: 15 €

Totale pagato: 112 + 45 + 78 + 15 = 250 €.
Saldo effettivo: 650 − 250 = 400 €.

Se fosse approvato l’ordine aggiuntivo:
- Filo: 14 × 6 € = 84 €
- Spedizione: 11 €
- Totale aggiuntivo: 84 + 11 = 95 €

Saldo ipotetico dopo il filo: 400 − 95 = 305 €.

Il secondo ordine non è approvato né pagato. L’affitto è coperto da un altro fondo; offerte non note, prestiti gratuiti e acquisti futuri senza prezzo non entrano nel calcolo.
```

### full: pass

```text
Il saldo effettivo è 400 €. Se il secondo ordine fosse approvato, resterebbero 305 €.

Spese confermate:
- Cartoncino: 16 × 7 € = 112 €
- Colla: 9 × 5 € = 45 €
- Aghi: 6 × 13 € = 78 €
- Spedizione unica: 15 €

Totale pagato: 112 + 45 + 78 + 15 = 250 €.
Saldo effettivo: 650 − 250 = 400 €.

Secondo ordine, proposto ma non approvato né pagato:
- Filo: 14 × 6 € = 84 €
- Spedizione: 11 €

Totale proposto: 84 + 11 = 95 €.
Saldo ipotetico dopo il filo: 400 − 95 = 305 €.

L’affitto è coperto da un fondo diverso. Le offerte non note e gli altri elementi del contesto non entrano nel calcolo. Il saldo disponibile non costituisce approvazione dell’acquisto.
```

### ultra: pass

```text
Saldo effettivo:
- Cartoncino: 16 × 7 € = 112 €
- Colla: 9 × 5 € = 45 €
- Aghi: 6 × 13 € = 78 €
- Spedizione unica: 15 €

Spese confermate: 112 + 45 + 78 + 15 = 250 €.
Restano: 650 − 250 = 400 €.

Saldo ipotetico se l’ordine di filo fosse approvato:
- Filo: 14 × 6 € = 84 €
- Spedizione: 11 €

Costo aggiuntivo: 84 + 11 = 95 €.
Resterebbero: 400 − 95 = 305 €.

Il secondo ordine non è approvato né pagato. Non sono aggiunti altri costi o entrate: l’affitto è coperto da un altro fondo, le offerte sono ignote e le altre informazioni non comportano spese confermate.
```

### off: pass

```text
Dopo le spese confermate restano 400 €.

Calcolo delle spese già pagate:
- Cartoncino: 16 × 7 € = 112 €
- Colla: 9 × 5 € = 45 €
- Aghi: 6 × 13 € = 78 €
- Spedizione dell’ordine: 15 €

Totale: 112 + 45 + 78 + 15 = 250 €.
Saldo effettivo: 650 − 250 = 400 €.

Se fosse approvato l’acquisto aggiuntivo, resterebbero 305 €.
- Filo: 14 × 6 € = 84 €
- Spedizione: 11 €

Costo del secondo ordine: 84 + 11 = 95 €.
Saldo condizionale: 400 − 95 = 305 €.

Il secondo ordine non è approvato né pagato e non è incluso nel saldo effettivo. L’affitto è coperto da un altro fondo; le offerte non sono note. Tavoli e forbici non comportano costi indicati, e il futuro taglierino non ha un prezzo o una richiesta formale. Non sono quindi aggiunte altre spese o entrate.
```

## modes-it-077 · long_analysis

Source task:

> Questa valutazione fittizia basta per consigliare il nuovo modulo a tutti gli utenti? Rispondi direttamente e spiega i limiti. Non serve proporre un’indagine completa o attribuire ai dati risultati che non contengono.
> 
> Durante quattro giorni, 30 persone hanno usato un modulo abbreviato e 27 lo hanno completato senza chiedere aiuto. Nella settimana precedente, altre 30 persone hanno usato il modulo consueto e 21 lo hanno completato senza aiuto. I risultati descrivono il 90 % e il 70 % nei rispettivi gruppi. Non c’è stata un’assegnazione casuale dei partecipanti ai due moduli.
> 
> Chi ha usato il modulo breve aveva già presentato una richiesta simile l’anno prima. Il gruppo precedente era alla prima richiesta. Inoltre, il primo gruppo ha lavorato al banco con un operatore nelle vicinanze, mentre il secondo ha usato il modulo da casa. Il tipo di dispositivo usato da casa non è stato registrato. Tra le due settimane sono state anche rese più visibili le istruzioni iniziali.
> 
> Il modulo breve non contiene la sezione per chi agisce come delegato. Nessuno nel suo gruppo ne aveva bisogno. Non sappiamo quindi se il nuovo testo sia adatto a chi presenta una richiesta per conto altrui. Non sono state effettuate prove con lettori di schermo. I tempi di compilazione sarebbero stati raccolti, ma la nota non li riporta né fornisce una media: non permette di calcolare un risparmio di minuti.
> 
> La coordinatrice non ha deciso di sostituire il modulo. Vuole vedere distinti i fatti osservati, le possibili interpretazioni e le informazioni mancanti. Un risultato migliore in un gruppo non dimostra da solo che il modulo sia la causa, che ogni persona migliori o che il beneficio valga per gruppi non provati. La risposta deve conservare questi limiti senza aggiungere percentuali, motivi o impegni non presenti nella nota.

### baseline: flagged

```text
No, questa valutazione non basta per consigliare il nuovo modulo a tutti gli utenti.

Fatti osservati: hanno completato senza chiedere aiuto 27 persone su 30 con il modulo breve (90 %) e 21 su 30 con quello consueto (70 %).

Possibili interpretazioni: il modulo breve potrebbe aver facilitato la compilazione, ma non possiamo attribuirgli la differenza. Non c’è stata assegnazione casuale e i gruppi differivano per esperienza precedente e contesto d’uso: al banco con un operatore vicino oppure da casa. Inoltre, tra le settimane sono state rese più visibili le istruzioni.

Informazioni mancanti: non conosciamo i dispositivi usati da casa, l’adeguatezza per chi agisce come delegato o l’accessibilità con lettori di schermo. I tempi non sono riportati, quindi non si può calcolare un risparmio di minuti.

Il risultato non dimostra un beneficio per ogni persona o per gruppi non provati. La coordinatrice non ha deciso di sostituire il modulo.
```

Review notes: Sound overall conclusion, but materially compresses the specific delegate and accessibility testing limitations into generic unknowns. / Risposta diretta e prudente; la sintesi conserva i limiti decisionali senza risultati aggiunti.

### lite: pass

```text
No. Questa valutazione non basta per consigliare il nuovo modulo a tutti gli utenti.

Fatti osservati: nei quattro giorni di prova, 27 persone su 30 hanno completato il modulo breve senza aiuto (90 %). Nella settimana precedente, con il modulo consueto, lo hanno fatto 21 persone su 30 (70 %).

Possibili interpretazioni: il risultato migliore potrebbe dipendere dal modulo, ma i gruppi non erano assegnati casualmente e lavoravano in condizioni diverse. Chi ha usato il modulo breve aveva già presentato una richiesta simile e lavorava al banco con un operatore vicino; l’altro gruppo era alla prima richiesta e compilava da casa. Tra le due settimane erano anche state rese più visibili le istruzioni iniziali. Non si può quindi isolare l’effetto del modulo.

Informazioni mancanti: il dispositivo usato da casa non è stato registrato. Il modulo breve non contiene la sezione per i delegati e nessuno nel gruppo ne aveva bisogno, quindi la sua adeguatezza per chi presenta richieste per altri è sconosciuta. Non sono state effettuate prove con lettori di schermo. La nota non riporta i tempi di compilazione né una media: non consente di calcolare un risparmio di minuti.

Il risultato non dimostra che il modulo sia la causa del miglioramento, che ogni persona migliori o che il beneficio valga per gruppi non provati. La coordinatrice non ha deciso di sostituire il modulo.
```

### full: pass

```text
No. La valutazione mostra un risultato migliore nel gruppo che ha usato il modulo breve, ma non basta per consigliarlo a tutti gli utenti.

**Fatti osservati.** In quattro giorni, 27 persone su 30 hanno completato il modulo breve senza chiedere aiuto (90 %). Nella settimana precedente, con il modulo consueto, erano state 21 su 30 (70 %). Non c’è stata assegnazione casuale.

**Possibili interpretazioni.** Il modulo breve potrebbe aver contribuito al risultato, ma i gruppi e le condizioni erano diversi: chi lo ha usato aveva già presentato una richiesta simile l’anno prima e lavorava al banco con un operatore vicino. Il gruppo precedente era alla prima richiesta e compilava da casa. Tra le due settimane erano anche state rese più visibili le istruzioni iniziali. Non si può quindi attribuire il miglior risultato al solo modulo, né concludere che ogni persona migliori.

**Informazioni mancanti.** Il dispositivo usato da casa non è stato registrato. Il modulo breve non contiene la sezione per i delegati e nessuno nel gruppo ne aveva bisogno: la sua adeguatezza per chi presenta richieste per altri resta sconosciuta. Non sono state effettuate prove con lettori di schermo. I tempi sarebbero stati raccolti, ma la nota non li riporta né fornisce una media: non è possibile calcolare un risparmio di minuti.

Il beneficio non è dimostrato per i gruppi non provati. La coordinatrice non ha deciso di sostituire il modulo.
```

### ultra: pass

```text
No: questa valutazione non basta per consigliare il nuovo modulo a tutti gli utenti.

**Fatti osservati.** In quattro giorni, 27 persone su 30 hanno completato il modulo breve senza aiuto (90 %). Nella settimana precedente, con il modulo consueto, erano state 21 su 30 (70 %). Non c’è stata assegnazione casuale.

**Possibili interpretazioni.** Il risultato migliore potrebbe dipendere dal modulo, ma anche dalle differenze tra gruppi e condizioni: gli utenti del modulo breve avevano già presentato una richiesta simile l’anno prima e lavoravano al banco con un operatore vicino; gli altri erano alla prima richiesta e compilavano da casa. Tra le due settimane, inoltre, le istruzioni iniziali sono state rese più visibili. I dati non isolano la causa e non dimostrano un miglioramento per ogni persona.

**Informazioni mancanti.** Non è stato registrato il dispositivo usato da casa. Il modulo breve omette la sezione per i delegati, di cui nessuno nel gruppo aveva bisogno: l’idoneità per chi presenta richieste per conto altrui è quindi ignota. Non sono state fatte prove con lettori di schermo. I tempi sarebbero stati raccolti, ma la nota non li riporta né fornisce una media: non si può calcolare un risparmio di minuti.

Il beneficio non è dimostrato per gruppi non provati. La coordinatrice non ha deciso di sostituire il modulo.
```

### off: pass

```text
No. Questa valutazione fittizia non basta per consigliare il nuovo modulo a tutti gli utenti.

Fatti osservati: durante quattro giorni, 27 persone su 30 hanno completato il modulo abbreviato senza chiedere aiuto, pari al 90 %. Nella settimana precedente, 21 persone su altre 30 hanno completato quello consueto senza aiuto, pari al 70 %. Non c’è stata assegnazione casuale ai due moduli.

Possibili interpretazioni: il risultato migliore potrebbe dipendere dal modulo, ma i gruppi e le condizioni erano diversi. Chi ha usato il modulo breve aveva già presentato una richiesta simile l’anno prima e lavorava al banco con un operatore nelle vicinanze. Il gruppo precedente era alla prima richiesta e compilava da casa. Tra le due settimane sono state anche rese più visibili le istruzioni iniziali. I dati non consentono di separare questi possibili effetti né di attribuire il miglioramento al solo modulo.

Informazioni mancanti: il dispositivo usato da casa non è stato registrato. Il modulo breve non contiene la sezione per i delegati e nessuno nel gruppo ne aveva bisogno, quindi la sua adeguatezza per chi presenta richieste per altri non è nota. Non sono state effettuate prove con lettori di schermo. I tempi di compilazione sarebbero stati raccolti, ma la nota non riporta valori o una media: non si può calcolare un risparmio di minuti.

Il risultato non dimostra che ogni persona migliori o che il beneficio si estenda a gruppi non provati. La coordinatrice non ha deciso di sostituire il modulo.
```

## modes-it-078 · long_voice

Source task:

> Scrivi una versione più breve di questo racconto per il bollettino del laboratorio. Conserva la voce calma e i fatti che danno senso all’incontro. Non inventare come prosegue la storia e non aggiungere una morale esplicita.
> 
> Quando Renato entrò, il vento gli aveva rovesciato un lembo del cappotto. Portava una scatola di latta piena di vecchie cerniere. Disse che potevano essere una cinquantina, ma non le aveva contate. Alcune erano corte e altre lunghe; due avevano ancora un pezzo di stoffa cucito lungo il bordo. Nessuno provò tutte le cerniere per vedere se funzionassero.
> 
> Al banco, Amina chiese se anche la scatola fosse un dono. Renato rispose di no: era stata di sua madre e voleva tenerla. Le cerniere, invece, potevano restare per le riparazioni del laboratorio. Amina prese un vassoio e le sistemò senza fretta. Non chiese perché il dono fosse arrivato proprio quel giorno e non scrisse una spiegazione al posto di Renato.
> 
> Una ragazza trovò una cerniera gialla e domandò se potesse prenderla per la propria borsa. Renato disse di sì. Non ricordava da dove venisse quella cerniera. Nel bollettino, quindi, non possiamo attribuirla a un abito della madre. Sappiamo soltanto che era tra quelle conservate da Renato e che lui ha acconsentito a darla. La ragazza ne prese una sola.
> 
> All’uscita il vento era calato. Renato tornò a casa con la scatola vuota, mentre le altre cerniere rimasero sul vassoio come dono. Amina registrò il materiale ricevuto senza scrivere il nome della ragazza. Il racconto si ferma qui. Non sappiamo se la borsa sia stata riparata quella sera né se Renato sia tornato. La versione breve può rendere più leggero il testo, ma non riempire questi vuoti o dichiarare funzionanti tutte le cerniere senza una prova.

### baseline: pass

```text
Renato entrò con un lembo del cappotto rovesciato dal vento e una scatola di latta piena di vecchie cerniere. Disse che potevano essere una cinquantina, senza averle contate; non furono provate tutte.

Amina gli chiese se anche la scatola fosse un dono. Era stata di sua madre e Renato voleva tenerla; le cerniere, invece, potevano restare per le riparazioni. Amina le sistemò senza fretta su un vassoio, senza chiedere perché fossero arrivate proprio quel giorno.

Una ragazza chiese una cerniera gialla per la propria borsa. Renato acconsentì, ma non ricordava da dove venisse. La ragazza ne prese una sola.

Quando Renato uscì, il vento era calato. Tornò a casa con la scatola vuota; le altre cerniere rimasero sul vassoio. Amina registrò il dono senza scrivere il nome della ragazza.
```

### lite: pass

```text
Quando Renato entrò, il vento gli aveva rovesciato un lembo del cappotto. Portava una scatola di latta con vecchie cerniere: forse una cinquantina, disse, ma non le aveva contate. Alcune erano corte, altre lunghe; due conservavano un pezzo di stoffa sul bordo. Nessuno le provò tutte.

Amina chiese se anche la scatola fosse un dono. Renato disse di no: era stata di sua madre e voleva tenerla. Le cerniere potevano invece restare per le riparazioni del laboratorio. Amina le sistemò senza fretta su un vassoio, senza chiedere perché il dono fosse arrivato quel giorno né dare una spiegazione al posto suo.

Una ragazza chiese una cerniera gialla per la propria borsa. Renato acconsentì e lei ne prese una sola. Lui non ricordava da dove venisse: sappiamo soltanto che era tra quelle che aveva conservato, non che provenisse da un abito della madre.

All’uscita il vento era calato. Renato tornò a casa con la scatola vuota; le altre cerniere rimasero sul vassoio come dono. Amina registrò il materiale senza scrivere il nome della ragazza. Il racconto si ferma qui: non sappiamo se la borsa sia stata riparata quella sera né se Renato sia tornato.
```

### full: pass

```text
Renato entrò con un lembo del cappotto rovesciato dal vento e una scatola di latta piena di vecchie cerniere. Disse che potevano essere una cinquantina, ma non le aveva contate. Erano corte e lunghe; due conservavano un pezzo di stoffa cucito al bordo. Nessuno le provò tutte.

Amina chiese se anche la scatola fosse un dono. Renato voleva tenerla: era stata di sua madre. Le cerniere, invece, potevano restare per le riparazioni del laboratorio. Amina le sistemò su un vassoio, senza fretta e senza chiedere perché il dono fosse arrivato proprio quel giorno.

Una ragazza chiese di prendere una cerniera gialla per la propria borsa. Renato acconsentì e lei ne prese una sola. Lui non ricordava da dove venisse: sappiamo soltanto che l’aveva conservata, non che appartenesse a un abito della madre.

All’uscita il vento era calato. Renato tornò a casa con la scatola vuota; le altre cerniere rimasero sul vassoio come dono. Amina registrò il materiale senza scrivere il nome della ragazza né attribuire al gesto una spiegazione. Non sappiamo se la borsa sia stata riparata quella sera o se Renato sia tornato.
```

### ultra: pass

```text
Renato entrò con un lembo del cappotto rovesciato dal vento e una scatola di latta piena di vecchie cerniere. Disse che potevano essere una cinquantina, senza averle contate: corte e lunghe, due ancora con un pezzo di stoffa sul bordo. Non furono provate tutte.

Amina chiese se anche la scatola fosse un dono. Renato voleva tenerla: era stata di sua madre. Le cerniere potevano invece restare per le riparazioni del laboratorio. Amina le sistemò senza fretta su un vassoio, senza chiedere perché il dono arrivasse quel giorno né attribuirgli una spiegazione.

Una ragazza chiese una cerniera gialla per la propria borsa. Renato acconsentì e lei ne prese una sola. Lui non ne ricordava la provenienza: era tra quelle che aveva conservato, ma non sappiamo se venisse da un abito della madre.

All’uscita il vento era calato. Renato tornò a casa con la scatola vuota; le altre cerniere rimasero sul vassoio come dono. Amina registrò il materiale senza scrivere il nome della ragazza. Non sappiamo se la borsa sia stata riparata quella sera né se Renato sia tornato.
```

### off: pass

```text
Quando Renato entrò, il vento gli aveva rovesciato un lembo del cappotto. Portava una scatola di latta con vecchie cerniere: forse una cinquantina, disse, senza averle contate. Erano corte e lunghe; due conservavano un pezzo di stoffa sul bordo. Nessuno le provò tutte.

Amina chiese se anche la scatola fosse un dono. Renato voleva tenerla: era stata di sua madre. Le cerniere, invece, potevano restare per le riparazioni del laboratorio. Amina le sistemò senza fretta su un vassoio, senza chiedere perché fossero arrivate proprio quel giorno né dare una spiegazione al posto suo.

Una ragazza chiese una cerniera gialla per la propria borsa. Renato acconsentì e lei ne prese una sola. Lui non ricordava da dove venisse: era tra quelle che aveva conservato.

All’uscita il vento era calato. Renato tornò a casa con la scatola vuota; le altre cerniere rimasero sul vassoio come dono. Amina registrò il materiale ricevuto senza scrivere il nome della ragazza.
```

## modes-it-079 · long_uncertainty

Source task:

> Prepara un aggiornamento per la riunione su un sistema fittizio di misura del livello dell’acqua. Separa quello che è stato osservato dalle cause possibili. La nota non permette di stabilire se altri componenti siano stati danneggiati.
> 
> Nel registro di venerdì manca un tratto di 19 minuti, dalle 11:06 alle 11:25. Prima e dopo il tratto mancante, i valori sono tra 42 cm e 45 cm. Non ci sono misure per quei diciannove minuti e non era presente un secondo sensore nello stesso recipiente. I valori vicini non dimostrano quale fosse il livello durante la lacuna.
> 
> Sabato è stato trovato un connettore non ben fissato. Potrebbe aver interrotto la registrazione, ma il documento non mostra che abbia perso il contatto venerdì. Il connettore è stato fissato. Nei due controlli successivi, di 45 minuti ciascuno, non sono comparse lacune. Questi controlli limitati non dimostrano che il problema sia risolto per sempre.
> 
> Una lacuna nei dati non equivale necessariamente a un’interruzione della pompa. Lo stato della pompa non veniva registrato in quel periodo. La nota non descrive un’ispezione degli altri componenti. Non bisogna quindi affermare che siano stati danneggiati né garantire che non lo siano stati. L’oggetto del punto di stato è il comportamento del sistema di registrazione.
> 
> Una persona del gruppo tecnico ritiene che una registrazione continua di 48 ore potrebbe essere utile per verificare la stabilità. Questa attività è proposta, non decisa: non è iniziata, non ha una persona responsabile assegnata e non ha una data di conclusione fissata. La riunione potrà discuterne. Il testo non deve convertire la proposta in un’azione già programmata o indicare il connettore come causa certa soltanto perché è stato sistemato prima dei controlli senza lacune.

### baseline: pass

```text
**Osservazioni**
Venerdì manca una registrazione di 19 minuti, dalle 11:06 alle 11:25. Prima e dopo, i valori erano tra 42 e 45 cm; il livello durante la lacuna è sconosciuto, perché non c’erano misure né un secondo sensore nello stesso recipiente.

Sabato è stato trovato e fissato un connettore non ben fissato. Nei due controlli successivi, di 45 minuti ciascuno, non sono comparse lacune. Questo non garantisce una soluzione definitiva.

**Cause possibili e limiti**
Il connettore potrebbe aver interrotto la registrazione, ma non è documentato che abbia perso il contatto venerdì. La lacuna non dimostra un arresto della pompa, il cui stato non veniva registrato. Non è descritta un’ispezione degli altri componenti: non possiamo stabilire se siano stati danneggiati oppure no.

**Proposta da discutere**
Una persona del gruppo tecnico propone una registrazione continua di 48 ore per verificare la stabilità. L’attività non è stata decisa né avviata; non ha un responsabile assegnato o una data di conclusione fissata.
```

### lite: pass

```text
Osservazioni
Nel registro di venerdì mancano 19 minuti, dalle 11:06 alle 11:25. Prima e dopo la lacuna, i valori sono tra 42 cm e 45 cm. Non ci sono misure per quel periodo né un secondo sensore nello stesso recipiente: i valori vicini non permettono di ricostruire il livello durante la lacuna.

Sabato è stato trovato e fissato un connettore non ben fissato. Nei due controlli successivi, di 45 minuti ciascuno, non sono comparse lacune. Questi controlli limitati non dimostrano che il problema sia risolto definitivamente.

Cause possibili e limiti
Il connettore potrebbe aver interrotto la registrazione, ma non è documentato che abbia perso il contatto venerdì. Non è quindi una causa accertata.

La lacuna non equivale necessariamente a un’interruzione della pompa: il suo stato non veniva registrato. La nota non descrive un’ispezione degli altri componenti, quindi non permette né di affermare né di escludere danni. Questo aggiornamento riguarda il sistema di registrazione.

Proposta da discutere
Una persona del gruppo tecnico ritiene che una registrazione continua di 48 ore potrebbe aiutare a verificare la stabilità. L’attività è proposta, non decisa né iniziata; non ha un responsabile assegnato o una data di conclusione fissata. La riunione potrà discuterne.
```

### full: pass

```text
**Stato della registrazione.** Venerdì manca un tratto di 19 minuti, dalle 11:06 alle 11:25. Il livello dell’acqua durante la lacuna è sconosciuto; la causa dell’interruzione della registrazione non è accertata.

**Osservazioni.** Prima e dopo la lacuna, i valori sono tra 42 cm e 45 cm. Non c’erano misure per quei 19 minuti né un secondo sensore nello stesso recipiente: i valori vicini non permettono di ricostruire il livello mancante. Sabato è stato trovato e fissato un connettore non ben fissato. Nei due controlli successivi, di 45 minuti ciascuno, non sono comparse lacune. Questi controlli limitati non dimostrano una risoluzione definitiva.

**Causa possibile e limiti.** Il connettore potrebbe aver interrotto la registrazione, ma non è documentato che abbia perso il contatto venerdì. La lacuna non implica necessariamente un’interruzione della pompa, il cui stato non veniva registrato. La nota non descrive un’ispezione degli altri componenti: non permette né di affermare che siano danneggiati né di garantire che siano integri.

**Proposta da discutere.** Una persona del gruppo tecnico ritiene che una registrazione continua di 48 ore potrebbe aiutare a verificare la stabilità. È una proposta, non un’attività decisa o iniziata; non ha un responsabile assegnato né una data di conclusione. La riunione potrà discuterne.
```

### ultra: pass

```text
**Osservazioni.** Nel registro di venerdì mancano 19 minuti, dalle 11:06 alle 11:25. Prima e dopo, i valori sono tra 42 e 45 cm; nella lacuna non ci sono misure né era presente un secondo sensore nello stesso recipiente. Il livello in quei minuti resta ignoto.

Sabato è stato trovato e fissato un connettore non ben fissato. Nei due controlli successivi, di 45 minuti ciascuno, non sono comparse lacune. Questi controlli limitati non dimostrano una risoluzione definitiva.

**Causa possibile e limiti.** Il connettore potrebbe aver interrotto la registrazione, ma non è documentata una perdita di contatto venerdì. Una lacuna non implica necessariamente un’interruzione della pompa, il cui stato non veniva registrato. La nota non descrive ispezioni degli altri componenti: non consente di affermare né escludere danni. L’aggiornamento riguarda il sistema di registrazione.

**Proposta da discutere.** Una persona del gruppo tecnico ritiene utile una registrazione continua di 48 ore per verificare la stabilità. È una proposta, non una decisione: non è iniziata, non ha un responsabile assegnato né una data di conclusione fissata.
```

### off: pass

```text
**Osservazioni**
Nel registro di venerdì manca un tratto di 19 minuti, dalle 11:06 alle 11:25. Prima e dopo la lacuna, i valori sono tra 42 cm e 45 cm. Non ci sono misure per quei minuti né un secondo sensore nello stesso recipiente: il livello durante la lacuna non è quindi noto.

Sabato è stato trovato un connettore non ben fissato, che è stato fissato. Nei due controlli successivi, di 45 minuti ciascuno, non sono comparse lacune. Questi controlli limitati non dimostrano che il problema sia risolto definitivamente.

**Cause possibili e limiti**
Il connettore potrebbe aver interrotto la registrazione, ma il documento non dimostra che abbia perso il contatto venerdì. Non è quindi una causa accertata.

La lacuna nei dati non equivale necessariamente a un’interruzione della pompa: in quel periodo il suo stato non veniva registrato. La nota non descrive un’ispezione degli altri componenti, quindi non permette né di affermare che siano danneggiati né di garantire che non lo siano. Questo aggiornamento riguarda il comportamento del sistema di registrazione.

**Proposta da discutere**
Una persona del gruppo tecnico ritiene che una registrazione continua di 48 ore potrebbe essere utile per verificare la stabilità. L’attività è soltanto proposta: non è stata decisa o iniziata, non ha una persona responsabile assegnata né una data di conclusione fissata. La riunione potrà discuterne.
```

## modes-it-080 · scope

Source task:

> Rispondi a queste domande: è obbligatorio portare una tazza personale e come funziona il prestito? In questo incontro fittizio si possono portare tazze proprie, ma non è obbligatorio. Le tazze del gruppo sono gratuite e vanno riconsegnate lavate prima di uscire.

### baseline: pass

```text
No, portare una tazza personale è facoltativo. Le tazze del gruppo si possono prendere in prestito gratuitamente e vanno riconsegnate lavate prima di uscire.
```

### lite: pass

```text
No, portare una tazza personale è facoltativo. Le tazze del gruppo sono disponibili in prestito gratuito e vanno riconsegnate lavate prima di uscire.
```

### full: pass

```text
No, portare una tazza personale è facoltativo. Puoi prendere in prestito gratuitamente una tazza del gruppo e devi riconsegnarla lavata prima di uscire.
```

### ultra: pass

```text
No, portare una tazza personale è facoltativo. Puoi prendere in prestito gratuitamente una tazza del gruppo e devi riconsegnarla lavata prima di uscire.
```

### off: pass

```text
No, portare una tazza personale è facoltativo. Puoi prendere gratuitamente in prestito una tazza del gruppo, da riconsegnare lavata prima di uscire.
```

## modes-it-081 · translation_permissions

Source task:

> Translate this fictional craft-club notice into Italian: You may borrow a cutting mat during the session. You must leave it on the marked shelf before going home. Borrowing a mat is optional and does not include taking it away.

### baseline: pass

```text
Puoi prendere in prestito un tappetino da taglio durante la sessione. Devi lasciarlo sullo scaffale contrassegnato prima di tornare a casa. Prendere in prestito un tappetino è facoltativo e non comprende la possibilità di portarlo via.
```

### lite: pass

```text
Puoi prendere in prestito un tappetino da taglio durante la sessione. Devi lasciarlo sullo scaffale contrassegnato prima di andare a casa. Prendere in prestito un tappetino è facoltativo e non permette di portarlo via.
```

### full: pass

```text
Puoi prendere in prestito un tappetino da taglio durante la sessione. Devi lasciarlo sullo scaffale contrassegnato prima di tornare a casa. Prendere in prestito un tappetino è facoltativo e non consente di portarlo via.
```

### ultra: pass

```text
Puoi prendere in prestito un tappetino da taglio durante la sessione. Devi lasciarlo sullo scaffale contrassegnato prima di andare a casa. Prenderlo in prestito è facoltativo e non consente di portarlo via.
```

### off: pass

```text
Puoi prendere in prestito un tappetino da taglio durante la sessione. Devi lasciarlo sul ripiano contrassegnato prima di andare a casa. Prendere in prestito un tappetino è facoltativo e non comprende la possibilità di portarlo via.
```

## modes-it-082 · translation_negation

Source task:

> Translate into Italian: Do not close the request because the photograph is missing. It may have been sent in a separate message. We have not yet checked yesterday’s messages.

### baseline: pass

```text
Non chiudere la richiesta perché manca la fotografia. Potrebbe essere stata inviata in un messaggio separato. Non abbiamo ancora controllato i messaggi di ieri.
```

### lite: pass

```text
Non chiudere la richiesta perché manca la fotografia. Potrebbe essere stata inviata in un messaggio separato. Non abbiamo ancora controllato i messaggi di ieri.
```

### full: pass

```text
Non chiudere la richiesta perché manca la fotografia. Potrebbe essere stata inviata in un messaggio separato. Non abbiamo ancora controllato i messaggi di ieri.
```

### ultra: pass

```text
Non chiudere la richiesta perché manca la fotografia. Potrebbe essere stata inviata in un messaggio separato. Non abbiamo ancora controllato i messaggi di ieri.
```

### off: pass

```text
Non chiudere la richiesta perché manca la fotografia. Potrebbe essere stata inviata in un messaggio separato. Non abbiamo ancora controllato i messaggi di ieri.
```

## modes-it-083 · translation_actor

Source task:

> Translate into Italian: Rosa listed the missing screws on Tuesday. The case was refilled on Wednesday, but the record does not name who did it. On Thursday, Bruno collected the refilled case.

### baseline: pass

```text
Rosa ha elencato le viti mancanti martedì. La cassetta è stata rifornita mercoledì, ma il registro non indica chi lo abbia fatto. Giovedì Bruno ha ritirato la cassetta rifornita.
```

### lite: pass

```text
Rosa ha elencato le viti mancanti martedì. La cassetta è stata rifornita mercoledì, ma il registro non indica chi l'ha fatto. Giovedì, Bruno ha ritirato la cassetta rifornita.
```

### full: pass

```text
Martedì Rosa ha elencato le viti mancanti. Mercoledì la custodia è stata riempita di nuovo, ma il registro non indica chi lo abbia fatto. Giovedì Bruno ha ritirato la custodia riempita.
```

### ultra: pass

```text
Rosa ha elencato le viti mancanti martedì. Il contenitore è stato riempito di nuovo mercoledì, ma il registro non indica chi l’abbia fatto. Giovedì Bruno ha ritirato il contenitore riempito.
```

### off: pass

```text
Rosa ha elencato le viti mancanti martedì. La custodia è stata rifornita mercoledì, ma il registro non indica chi lo abbia fatto. Giovedì Bruno ha ritirato la custodia rifornita.
```

## modes-it-084 · translation_uncertainty

Source task:

> Translate into Italian: The loose belt might explain the delay, but no comparison test has confirmed that. Only the short cycle was observed. The long cycle has not been tested.

### baseline: pass

```text
La cinghia allentata potrebbe spiegare il ritardo, ma nessuna prova comparativa lo ha confermato. È stato osservato soltanto il ciclo breve. Il ciclo lungo non è stato testato.
```

### lite: pass

```text
La cinghia allentata potrebbe spiegare il ritardo, ma nessun test comparativo lo ha confermato. È stato osservato solo il ciclo breve. Il ciclo lungo non è stato testato.
```

### full: pass

```text
La cinghia allentata potrebbe spiegare il ritardo, ma nessun test comparativo lo ha confermato. È stato osservato solo il ciclo breve. Il ciclo lungo non è stato testato.
```

### ultra: pass

```text
La cinghia allentata potrebbe spiegare il ritardo, ma nessuna prova comparativa lo ha confermato. È stato osservato solo il ciclo breve. Il ciclo lungo non è stato testato.
```

### off: pass

```text
La cinghia allentata potrebbe spiegare il ritardo, ma nessun test comparativo lo ha confermato. È stato osservato solo il ciclo breve. Il ciclo lungo non è stato testato.
```

## modes-it-085 · translation_json

Source task:

> Translate the notice value into Italian. Return only valid JSON, preserving keys, reference, and number: {"reference":"IT-M47","number":5,"notice":"Five covers are missing. Keep the trays inside until replacement covers arrive."}

### baseline: pass

```text
{"reference":"IT-M47","number":5,"notice":"Mancano cinque coperchi. Tenere i vassoi all'interno fino all'arrivo dei coperchi sostitutivi."}
```

### lite: pass

```text
{"reference":"IT-M47","number":5,"notice":"Mancano cinque coperchi. Tieni i vassoi all'interno finché non arrivano i coperchi di ricambio."}
```

### full: pass

```text
{"reference":"IT-M47","number":5,"notice":"Mancano cinque coperchi. Tieni i vassoi all'interno finché non arrivano i coperchi di ricambio."}
```

### ultra: pass

```text
{"reference":"IT-M47","number":5,"notice":"Mancano cinque coperchi. Tieni i vassoi all’interno finché non arrivano i coperchi sostitutivi."}
```

### off: pass

```text
{"reference":"IT-M47","number":5,"notice":"Mancano cinque coperchi. Tieni i vassoi all'interno finché non arrivano i coperchi sostitutivi."}
```

## modes-it-086 · translation_format

Source task:

> Translate into Italian, keeping two bullets and the literal placeholders:
> - Hello, {{member}}. Your fitting is confirmed for 24 October.
> - You may use {{fitting_link}} to change the time, but the fitting location remains the same.

### baseline: pass

```text
- Ciao, {{member}}. La tua prova è confermata per il 24 ottobre.
- Puoi usare {{fitting_link}} per cambiare l'orario, ma il luogo della prova rimane lo stesso.
```

### lite: pass

```text
- Ciao, {{member}}. La tua prova è confermata per il 24 ottobre.
- Puoi usare {{fitting_link}} per cambiare l'orario, ma il luogo della prova rimane lo stesso.
```

### full: pass

```text
- Ciao, {{member}}. La tua prova è confermata per il 24 ottobre.
- Puoi usare {{fitting_link}} per cambiare l'orario, ma il luogo della prova rimane lo stesso.
```

### ultra: pass

```text
- Ciao, {{member}}. La tua prova è confermata per il 24 ottobre.
- Puoi usare {{fitting_link}} per cambiare l’orario, ma il luogo della prova resta lo stesso.
```

### off: pass

```text
- Ciao, {{member}}. Il tuo appuntamento per la prova è confermato per il 24 ottobre.
- Puoi usare {{fitting_link}} per cambiare l'orario, ma il luogo della prova rimane lo stesso.
```

## modes-it-087 · translation_conditions

Source task:

> Translate this fictional workshop rule into Italian: The display cabinet may be opened only after the key is logged and the coordinator gives consent. Logging the key alone does not authorize opening.

### baseline: pass

```text
La vetrina può essere aperta solo dopo che la chiave è stata registrata e il coordinatore ha dato il proprio consenso. La sola registrazione della chiave non autorizza l'apertura.
```

### lite: pass

```text
La vetrina può essere aperta solo dopo che la chiave è stata registrata e il coordinatore ha dato il consenso. La sola registrazione della chiave non autorizza l'apertura.
```

### full: pass

```text
La vetrina può essere aperta solo dopo che la chiave è stata registrata e il coordinatore ha dato il consenso. La sola registrazione della chiave non autorizza l'apertura.
```

### ultra: pass

```text
La vetrina può essere aperta solo dopo che la chiave è stata registrata e il coordinatore ha dato il consenso. La sola registrazione della chiave non autorizza l’apertura.
```

### off: pass

```text
La vetrina può essere aperta solo dopo che la chiave è stata registrata e il coordinatore ha dato il consenso. La sola registrazione della chiave non autorizza l'apertura.
```

## modes-it-088 · translation_estimates

Source task:

> Translate into Italian: We estimate about 5 to 7 hours for binding if the pages are already in order. The estimate does not include replacing torn pages. We cannot guarantee a completion time.

### baseline: pass

```text
Stimiamo circa 5–7 ore per la rilegatura se le pagine sono già in ordine. La stima non include la sostituzione delle pagine strappate. Non possiamo garantire un orario di completamento.
```

### lite: pass

```text
Stimiamo circa 5–7 ore per la rilegatura se le pagine sono già in ordine. La stima non include la sostituzione delle pagine strappate. Non possiamo garantire un orario di completamento.
```

### full: pass

```text
Stimiamo circa 5–7 ore per la rilegatura, se le pagine sono già in ordine. La stima non comprende la sostituzione delle pagine strappate. Non possiamo garantire un orario di completamento.
```

### ultra: pass

```text
Stimiamo circa 5–7 ore per la rilegatura se le pagine sono già in ordine. La stima non include la sostituzione delle pagine strappate. Non possiamo garantire un orario di completamento.
```

### off: pass

```text
Stimiamo circa 5–7 ore per la rilegatura se le pagine sono già in ordine. La stima non comprende la sostituzione delle pagine strappate. Non possiamo garantire un orario di completamento.
```

## modes-it-089 · translation_units

Source task:

> Translate into Italian without converting currency or units: Each pack contains 1.5 kg of clay and costs CAD 12 before tax. Collection is free. Courier delivery costs CAD 18 per order.

### baseline: pass

```text
Ogni confezione contiene 1,5 kg di argilla e costa CAD 12, tasse escluse. Il ritiro è gratuito. La consegna tramite corriere costa CAD 18 per ordine.
```

### lite: pass

```text
Ogni confezione contiene 1,5 kg di argilla e costa CAD 12, tasse escluse. Il ritiro è gratuito. La consegna tramite corriere costa CAD 18 per ordine.
```

### full: pass

```text
Ogni confezione contiene 1,5 kg di argilla e costa CAD 12, tasse escluse. Il ritiro è gratuito. La consegna tramite corriere costa CAD 18 per ordine.
```

### ultra: pass

```text
Ogni confezione contiene 1,5 kg di argilla e costa CAD 12, tasse escluse. Il ritiro è gratuito. La consegna tramite corriere costa CAD 18 per ordine.
```

### off: pass

```text
Ogni confezione contiene 1,5 kg di argilla e costa CAD 12, tasse escluse. Il ritiro è gratuito. La consegna tramite corriere costa CAD 18 per ordine.
```

## modes-it-090 · translation_sampling

Source task:

> Translate into Italian: Thirty-four people volunteered to answer after a pottery lesson. Nobody was randomly selected. Their preferences cannot be treated as those of all adults in the town.

### baseline: pass

```text
Trentaquattro persone si sono offerte volontariamente di rispondere dopo una lezione di ceramica. Nessuno è stato selezionato casualmente. Le loro preferenze non possono essere considerate rappresentative di quelle di tutti gli adulti della cittadina.
```

### lite: pass

```text
Trentaquattro persone si sono offerte volontariamente di rispondere dopo una lezione di ceramica. Nessuno è stato selezionato casualmente. Le loro preferenze non possono essere considerate rappresentative di quelle di tutti gli adulti della cittadina.
```

### full: pass

```text
Trentaquattro persone si sono offerte volontariamente di rispondere dopo una lezione di ceramica. Nessuno è stato selezionato casualmente. Le loro preferenze non possono essere considerate rappresentative di quelle di tutti gli adulti della cittadina.
```

### ultra: pass

```text
Trentaquattro persone si sono offerte volontariamente di rispondere dopo una lezione di ceramica. Nessuno è stato selezionato casualmente. Le loro preferenze non possono essere considerate rappresentative di quelle di tutti gli adulti della cittadina.
```

### off: pass

```text
Trentaquattro persone si sono offerte volontariamente di rispondere dopo una lezione di ceramica. Nessuno è stato selezionato casualmente. Le loro preferenze non possono essere considerate quelle di tutti gli adulti della città.
```

## modes-it-091 · translation_percentage_points

Source task:

> Translate into Italian: In the fictional table, the share increased from 36% to 45%, a rise of 9 percentage points. That is not the same as a 9% relative increase.

### baseline: pass

```text
Nella tabella fittizia, la quota è aumentata dal 36% al 45%, con un incremento di 9 punti percentuali. Non è la stessa cosa di un aumento relativo del 9%.
```

### lite: pass

```text
Nella tabella fittizia, la quota è aumentata dal 36% al 45%, con un aumento di 9 punti percentuali. Non è la stessa cosa di un aumento relativo del 9%.
```

### full: pass

```text
Nella tabella fittizia, la quota è aumentata dal 36% al 45%, con un incremento di 9 punti percentuali. Non è la stessa cosa di un aumento relativo del 9%.
```

### ultra: pass

```text
Nella tabella fittizia, la quota è aumentata dal 36% al 45%, un aumento di 9 punti percentuali. Non equivale a un aumento relativo del 9%.
```

### off: pass

```text
Nella tabella fittizia, la quota è aumentata dal 36% al 45%, con un incremento di 9 punti percentuali. Non è la stessa cosa di un aumento relativo del 9%.
```

## modes-it-092 · translation_exceptions

Source task:

> Translate this fictional lesson policy into Italian: Once a lesson has taken place, its fee is not refundable. If the studio cancels in advance, learners may request a refund instead of accepting another lesson. They are not obliged to accept the alternative.

### baseline: pass

```text
Una volta che una lezione si è svolta, il relativo costo non è rimborsabile. Se lo studio annulla la lezione in anticipo, gli allievi possono richiedere un rimborso anziché accettare un'altra lezione. Non sono obbligati ad accettare l'alternativa.
```

### lite: pass

```text
Una volta svolta una lezione, il relativo costo non è rimborsabile. Se lo studio annulla la lezione in anticipo, gli allievi possono richiedere un rimborso invece di accettare un'altra lezione. Non sono obbligati ad accettare l'alternativa.
```

### full: pass

```text
Una volta svolta la lezione, il relativo costo non è rimborsabile. Se lo studio annulla la lezione in anticipo, gli allievi possono chiedere un rimborso anziché accettare un'altra lezione. Non sono obbligati ad accettare l'alternativa.
```

### ultra: pass

```text
Una volta svolta la lezione, il relativo costo non è rimborsabile. Se lo studio annulla la lezione in anticipo, gli allievi possono richiedere un rimborso anziché accettare un’altra lezione. Non sono obbligati ad accettare l’alternativa.
```

### off: pass

```text
Una volta svolta la lezione, il relativo costo non è rimborsabile. Se lo studio annulla la lezione in anticipo, gli allievi possono richiedere un rimborso anziché accettare un'altra lezione. Non sono obbligati ad accettare l'alternativa.
```

## modes-it-093 · translation_ambiguity

Source task:

> Translate into Italian without interpreting the date: The invitation says 09/10. The source does not tell us which date convention was used. Confirm the day and month before reserving the room.

### baseline: pass

```text
L'invito riporta 09/10. La fonte non ci dice quale convenzione sia stata usata per la data. Conferma il giorno e il mese prima di prenotare la sala.
```

### lite: pass

```text
L'invito riporta 09/10. La fonte non indica quale convenzione sia stata usata per la data. Conferma il giorno e il mese prima di prenotare la sala.
```

### full: pass

```text
L'invito riporta 09/10. La fonte non indica quale convenzione sia stata usata per la data. Conferma il giorno e il mese prima di prenotare la sala.
```

### ultra: pass

```text
L’invito riporta 09/10. La fonte non indica quale convenzione sia stata usata per la data. Conferma il giorno e il mese prima di prenotare la sala.
```

### off: pass

```text
L'invito riporta 09/10. La fonte non ci dice quale convenzione sia stata usata per la data. Conferma il giorno e il mese prima di prenotare la sala.
```

## modes-it-094 · translation_technical

Source task:

> Translate into Italian, preserving technical strings: Run batch-inspect --report-only before changing batch.tsv. The command lists mismatched codes; it does not correct them. Keep batch.audit even if the list is empty.

### baseline: pass

```text
Esegui batch-inspect --report-only prima di modificare batch.tsv. Il comando elenca i codici non corrispondenti; non li corregge. Conserva batch.audit anche se l'elenco è vuoto.
```

### lite: pass

```text
Esegui batch-inspect --report-only prima di modificare batch.tsv. Il comando elenca i codici non corrispondenti; non li corregge. Conserva batch.audit anche se l'elenco è vuoto.
```

### full: pass

```text
Esegui batch-inspect --report-only prima di modificare batch.tsv. Il comando elenca i codici non corrispondenti; non li corregge. Conserva batch.audit anche se l'elenco è vuoto.
```

### ultra: pass

```text
Esegui batch-inspect --report-only prima di modificare batch.tsv. Il comando elenca i codici non corrispondenti; non li corregge. Conserva batch.audit anche se l’elenco è vuoto.
```

### off: pass

```text
Esegui batch-inspect --report-only prima di modificare batch.tsv. Il comando elenca i codici non corrispondenti; non li corregge. Conserva batch.audit anche se l'elenco è vuoto.
```

## modes-it-095 · translation_voice

Source task:

> Translate into Italian in a gentle narrative voice: One candle still burned. Four folded maps lay beside the door. I waited for footsteps, but no one returned before sunrise.

### baseline: pass

```text
Una candela ardeva ancora. Quattro mappe ripiegate giacevano accanto alla porta. Rimasi in attesa di un rumore di passi, ma nessuno tornò prima dell'alba.
```

### lite: pass

```text
Una candela ardeva ancora. Quattro mappe ripiegate erano posate accanto alla porta. Rimasi in attesa di passi, ma nessuno tornò prima dell'alba.
```

### full: pass

```text
Una candela ardeva ancora. Quattro mappe ripiegate erano posate accanto alla porta. Rimasi in attesa di passi, ma nessuno tornò prima dell'alba.
```

### ultra: pass

```text
Una candela ardeva ancora. Quattro mappe piegate giacevano accanto alla porta. Attendevo il suono di passi, ma nessuno tornò prima dell’alba.
```

### off: pass

```text
Una candela ardeva ancora. Quattro mappe ripiegate giacevano accanto alla porta. Attesi il rumore dei passi, ma nessuno tornò prima dell'alba.
```

## modes-it-096 · translation_quotation

Source task:

> Translate the explanation into Italian and leave the quoted message unchanged: The log says "transfer held". The transfer is on hold; the message does not confirm that the parcel was returned.

### baseline: pass

```text
Il registro riporta "transfer held". Il trasferimento è sospeso; il messaggio non conferma che il pacco sia stato restituito.
```

### lite: pass

```text
Il registro riporta "transfer held". Il trasferimento è in sospeso; il messaggio non conferma che il pacco sia stato restituito.
```

### full: pass

```text
Il registro riporta "transfer held". Il trasferimento è in sospeso; il messaggio non conferma che il pacco sia stato restituito.
```

### ultra: pass

```text
Il registro riporta "transfer held". Il trasferimento è sospeso; il messaggio non conferma che il pacco sia stato restituito.
```

### off: pass

```text
Il registro riporta "transfer held". Il trasferimento è sospeso; il messaggio non conferma che il pacco sia stato restituito.
```

## modes-it-097 · translation_scope

Source task:

> Translate into Italian: The new schedule applies only to the loan desk. The reading room still opens at 10:00. Loans begin at 11:00, including requests reserved before the schedule changed.

### baseline: pass

```text
Il nuovo orario si applica solo al banco prestiti. La sala di lettura continua ad aprire alle 10:00. I prestiti iniziano alle 11:00, comprese le richieste prenotate prima della modifica dell'orario.
```

### lite: pass

```text
Il nuovo orario si applica solo al banco prestiti. La sala di lettura continua ad aprire alle 10:00. I prestiti iniziano alle 11:00, anche per le richieste prenotate prima del cambio di orario.
```

### full: pass

```text
Il nuovo orario si applica solo al banco prestiti. La sala di lettura continua ad aprire alle 10:00. I prestiti iniziano alle 11:00, comprese le richieste prenotate prima del cambio di orario.
```

### ultra: pass

```text
Il nuovo orario si applica solo al banco prestiti. La sala lettura continua ad aprire alle 10:00. I prestiti iniziano alle 11:00, anche per le richieste prenotate prima del cambio di orario.
```

### off: pass

```text
Il nuovo orario si applica solo al banco prestiti. La sala di lettura continua ad aprire alle 10:00. I prestiti iniziano alle 11:00, comprese le richieste prenotate prima della modifica dell'orario.
```

## modes-it-098 · translation_sequence

Source task:

> Translate into Italian: Record the count first, then ask someone else to compare it with the label. Release the box only after the comparison. Recording the count is not permission to release it.

### baseline: pass

```text
Registra prima il conteggio, poi chiedi a un'altra persona di confrontarlo con l'etichetta. Rilascia la scatola solo dopo il confronto. La registrazione del conteggio non autorizza il rilascio della scatola.
```

### lite: pass

```text
Registra prima il conteggio, poi chiedi a un'altra persona di confrontarlo con l'etichetta. Rilascia la scatola solo dopo il confronto. Registrare il conteggio non autorizza il rilascio.
```

### full: pass

```text
Registra prima il conteggio, poi chiedi a un'altra persona di confrontarlo con l'etichetta. Rilascia la scatola solo dopo il confronto. Registrare il conteggio non autorizza a rilasciarla.
```

### ultra: pass

```text
Registra prima il conteggio, poi chiedi a un’altra persona di confrontarlo con l’etichetta. Rilascia la scatola solo dopo il confronto. Registrare il conteggio non autorizza il rilascio.
```

### off: pass

```text
Registra prima il conteggio, poi chiedi a un'altra persona di confrontarlo con l'etichetta. Rilascia la scatola solo dopo il confronto. Registrare il conteggio non autorizza a rilasciarla.
```

## modes-it-099 · translation_conflict

Source task:

> Translate into Italian: The label lists 56 buttons, but the manual count found 55. No independent count has been made. The actual quantity is not yet confirmed.

### baseline: pass

```text
L'etichetta indica 56 bottoni, ma il conteggio manuale ne ha rilevati 55. Non è stato effettuato alcun conteggio indipendente. La quantità effettiva non è ancora confermata.
```

### lite: pass

```text
L'etichetta indica 56 bottoni, ma il conteggio manuale ne ha rilevati 55. Non è stato effettuato alcun conteggio indipendente. La quantità effettiva non è ancora confermata.
```

### full: pass

```text
L'etichetta indica 56 bottoni, ma il conteggio manuale ne ha rilevati 55. Non è stato effettuato alcun conteggio indipendente. La quantità effettiva non è ancora confermata.
```

### ultra: pass

```text
L’etichetta indica 56 bottoni, ma il conteggio manuale ne ha rilevati 55. Non è stato effettuato alcun conteggio indipendente. La quantità effettiva non è ancora confermata.
```

### off: pass

```text
L'etichetta indica 56 bottoni, ma il conteggio manuale ne ha rilevati 55. Non è stato effettuato alcun conteggio indipendente. La quantità effettiva non è ancora confermata.
```

## modes-it-100 · translation_denominators

Source task:

> Translate into Italian: Of 132 applications reviewed, 33 lacked a photograph. Nine of those 33 arrived through the mobile form. The total number received through that form is unknown.

### baseline: pass

```text
Delle 132 domande esaminate, 33 erano prive di fotografia. Nove di queste 33 sono pervenute tramite il modulo per dispositivi mobili. Il numero totale di domande ricevute tramite quel modulo è sconosciuto.
```

### lite: pass

```text
Delle 132 domande esaminate, 33 erano prive di fotografia. Nove di queste 33 sono arrivate tramite il modulo per dispositivi mobili. Il numero totale di domande ricevute tramite quel modulo è sconosciuto.
```

### full: pass

```text
Delle 132 domande esaminate, 33 erano prive di fotografia. Nove di queste 33 sono arrivate tramite il modulo per dispositivi mobili. Il numero totale di domande ricevute tramite quel modulo non è noto.
```

### ultra: pass

```text
Delle 132 domande esaminate, 33 erano prive di fotografia. Nove di queste 33 sono arrivate tramite il modulo mobile. Il numero totale di domande ricevute tramite quel modulo è sconosciuto.
```

### off: pass

```text
Delle 132 domande esaminate, 33 erano prive di fotografia. Nove di quelle 33 sono arrivate tramite il modulo per dispositivi mobili. Il numero totale di domande ricevute tramite quel modulo non è noto.
```

