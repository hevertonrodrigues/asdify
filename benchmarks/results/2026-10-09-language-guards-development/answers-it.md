# it: all source tasks and answers

Labels below are unblinded after review. Pass requires both meaning reviews and exact checks. A flagged answer is retained unchanged.

## modes-it-018 · summary

Source task:

> Riassumi per gli iscritti: L’incontro di giovedì inizia alle 17 come previsto. La visita al cortile non si farà perché il passaggio è occupato. Si terrà invece la presentazione in aula. La nuova data della visita non è ancora fissata.

### baseline: pass

```text
L’incontro di giovedì è confermato alle 17, con la presentazione in aula. La visita al cortile è rinviata perché il passaggio è occupato; la nuova data non è ancora fissata.
```

### lite: pass

```text
L’incontro di giovedì inizia alle 17, come previsto, con la presentazione in aula. La visita al cortile non si farà perché il passaggio è occupato. La nuova data della visita non è ancora fissata.
```

### full: pass

```text
L’incontro di giovedì inizierà alle 17, come previsto, con la presentazione in aula. La visita al cortile non si farà perché il passaggio è occupato. La nuova data della visita non è ancora fissata.
```

### ultra: pass

```text
L’incontro di giovedì resta alle 17, con la presentazione in aula. La visita al cortile salta perché il passaggio è occupato; la nuova data non è ancora fissata.
```

### off: pass

```text
L’incontro di giovedì inizierà alle 17, come previsto, con la presentazione in aula. La visita al cortile non si farà perché il passaggio è occupato; la nuova data non è ancora fissata.
```

## modes-it-028 · numbers_units

Source task:

> Riformula: Il recipiente ha una capacità di 900 mL. La linea a 700 mL indica il riempimento consigliato, non la capacità massima. Questi valori valgono soltanto per il campione mostrato.

### baseline: pass

```text
Il recipiente può contenere fino a 900 mL; la linea a 700 mL segnala il riempimento consigliato, non quello massimo. Questi valori si riferiscono solo al campione mostrato.
```

### lite: pass

```text
Il recipiente ha una capacità di 900 mL. La linea a 700 mL indica il riempimento consigliato, non la capacità massima. Questi valori valgono solo per il campione mostrato.
```

### full: pass

```text
Il recipiente ha una capacità di 900 mL. La linea a 700 mL indica il riempimento consigliato, non la capacità massima. Entrambi i valori valgono solo per il campione mostrato.
```

### ultra: pass

```text
Il recipiente contiene al massimo 900 mL; la linea a 700 mL indica il riempimento consigliato. I valori valgono solo per il campione mostrato.
```

### off: pass

```text
Il recipiente può contenere 900 mL. La linea a 700 mL indica il livello di riempimento consigliato, non la capacità massima. Questi valori si riferiscono soltanto al campione mostrato.
```

## modes-it-031 · summary

Source task:

> Scrivi una breve consegna: Elisa ha etichettato le scatole dei colori, ma non quelle dei tessuti. L’elenco delle etichette mancanti è nel cassetto alto. La stampante è stata riavviata; non sappiamo da chi.

### baseline: flagged

```text
Elisa ha etichettato le scatole dei colori; restano da etichettare quelle dei tessuti. L’elenco delle etichette mancanti è nel cassetto alto. La stampante è stata riavviata, ma non sappiamo da chi.
```

Review notes: Clear handover retaining the unfinished labeling work, list location, and unknown restart actor. / Turns an actor-specific negative into an unqualified statement about remaining work.

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

## modes-it-034 · voice

Source task:

> Accorcia conservando l’ironia gentile: Oggi la macchina del caffè ha scelto il silenzio. Fino al controllo del tecnico, usate pure il bollitore in cucina. Non sappiamo ancora quando tornerà a fare rumore.

### baseline: flagged

```text
La macchina del caffè oggi fa voto di silenzio. In attesa del controllo tecnico, usate il bollitore in cucina: non sappiamo ancora quando tornerà a farsi sentire.
```

Review notes: Retains gentle irony and the temporary kettle suggestion; the imperative does not assert an obligation. / Effective compression and irony, but changes permission into an instruction.

### lite: pass

```text
Oggi la macchina del caffè ha scelto il silenzio. Fino al controllo del tecnico, usate pure il bollitore in cucina. Non sappiamo quando tornerà a fare rumore.
```

### full: pass

```text
Oggi la macchina del caffè ha scelto il silenzio. Fino al controllo del tecnico, usate pure il bollitore in cucina. Non sappiamo quando tornerà a farsi sentire.
```

### ultra: pass

```text
Oggi la macchina del caffè ha scelto il silenzio. Fino al controllo del tecnico, usate pure il bollitore in cucina. Non sappiamo quando tornerà a farsi sentire.
```

### off: pass

```text
Oggi la macchina del caffè ha scelto il silenzio. Fino al controllo del tecnico, usate pure il bollitore in cucina. Il ritorno al rumore resta un mistero.
```

## modes-it-037 · technical

Source task:

> Riscrivi per il collega: Prima di eseguire export_tags --type json, copia tags.db nella cartella copy/. L’esportazione contiene solo le etichette attive; un risultato vuoto non dimostra che il database sia vuoto.

### baseline: pass

```text
Prima di eseguire `export_tags --type json`, copia `tags.db` nella cartella `copy/`. L’esportazione include solo le etichette attive: un risultato vuoto non significa necessariamente che il database sia vuoto.
```

### lite: pass

```text
Prima di eseguire export_tags --type json, copia tags.db nella cartella copy/. L’esportazione contiene solo le etichette attive: un risultato vuoto non dimostra che il database sia vuoto.
```

### full: pass

```text
Prima di eseguire `export_tags --type json`, copia `tags.db` nella cartella `copy/`. L’esportazione include solo le etichette attive: un risultato vuoto non dimostra che il database sia vuoto.
```

### ultra: pass

```text
Prima di eseguire `export_tags --type json`, copia `tags.db` nella cartella `copy/`. L’esportazione include solo le etichette attive: un risultato vuoto non dimostra che il database sia vuoto.
```

### off: pass

```text
Prima di eseguire `export_tags --type json`, copia `tags.db` nella cartella `copy/`. L’esportazione include soltanto le etichette attive: un risultato vuoto non significa che il database sia vuoto.
```

## modes-it-043 · percentage_points

Source task:

> In una tabella fittizia, la percentuale scende dal 63 % al 54 %. Di quanti punti percentuali diminuisce? Non calcolare la variazione relativa.

### baseline: pass

```text
Diminuisce di 9 punti percentuali.
```

### lite: pass

```text
Diminuisce di 9 punti percentuali.
```

### full: pass

```text
Diminuisce di 9 punti percentuali.
```

### ultra: pass

```text
Diminuisce di 9 punti percentuali.
```

### off: pass

```text
Diminuisce di 9 punti percentuali.
```

## modes-it-046 · permissions

Source task:

> Riscrivi questa clausola fittizia senza parere legale: Chi utilizza l’attrezzatura può terminare il prestito in qualsiasi momento. Deve riconsegnarla entro due giorni. La restituzione anticipata non dà diritto al rimborso dei giorni già pagati.

### baseline: pass

```text
Chi utilizza l’attrezzatura può interrompere il prestito in qualsiasi momento e deve restituirla entro due giorni. La restituzione anticipata non comporta il rimborso dei giorni già pagati.
```

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
Chi utilizza l’attrezzatura può terminare il prestito in qualsiasi momento e deve riconsegnarla entro due giorni. La restituzione anticipata non dà diritto al rimborso dei giorni già pagati.
```

## modes-it-068 · exact_format

Source task:

> Semplifica la nota mantenendo la citazione inglese identica: Compare "upload waiting". Vuol dire che il caricamento è in attesa, non che il file sia stato perso. Il motivo dell’attesa non è ancora noto.

### baseline: pass

```text
Compare "upload waiting": il caricamento è in attesa, non significa che il file sia perso. Il motivo dell’attesa non è ancora noto.
```

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
"upload waiting" indica che il caricamento è in attesa, non che il file sia stato perso. Il motivo dell’attesa non è ancora noto.
```

### off: pass

```text
Il messaggio "upload waiting" indica che il caricamento è in attesa, non che il file sia stato perso. Il motivo dell’attesa non è ancora noto.
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
## Consegna per l’apertura di domani

### Strumenti: presenza e disponibilità
- Il registro contiene 62 strumenti: 56 trovati negli armadi, 4 in prestito con moduli firmati e 2 non trovati. La presenza negli armadi non equivale, da sola, all’autorizzazione al prestito.
- Il rientro dei 4 prestiti è previsto per il 28 maggio, non confermato come già avvenuto.
- Non è stato accertato un furto dei 2 strumenti mancanti: potrebbero essere stati riposti altrove o registrati male. L’ultimo confronto completo tra registro e armadi risale a due mesi fa.
- Sono state pulite 5 levigatrici. Solo L-09 ha superato anche il controllo di funzionamento ed è autorizzata al prestito: si trova sul ripiano basso, con il cavo raccolto nella sua borsa.
- Le altre 4 levigatrici restano bloccate fino al controllo. Il bollino arancione attesta soltanto la pulizia, non l’autorizzazione al prestito.

### Consumabili e dati provvisori
- Il materiale abrasivo pesa 2,7 kg, buste comprese: non è possibile ricavarne il numero di fogli utilizzabili.
- Le nuove buste sono state proposte, ma non ordinate.
- Il saldo per i consumabili è stimato in 95 €: va ancora verificato con 3 scontrini e non costituisce una disponibilità definitiva.

### Locali, etichette e procedure
- Il pavimento anteriore è stato pulito.
- Il deposito resta chiuso finché la serratura difettosa non viene riparata e controllata.
- Giulia ha offerto di riscrivere le etichette martedì, ma non ha confermato la presenza. L’elenco delle etichette illeggibili è nel quaderno sul tavolo.
- Per i nuovi prestiti usare ancora il modulo consueto. La bozza del modulo breve non è approvata: il salvataggio nella cartella comune non autorizza a sostituire quello attuale.
```

### lite: pass

```text
## Consegna per l’apertura di domani

### Strumenti presenti e disponibilità
Il registro contiene 62 strumenti: 56 sono stati trovati negli armadi, quattro sono in prestito con moduli firmati e due non sono stati trovati. Il rientro dei quattro prestiti è previsto per il 28 maggio. Per i due mancanti non è stato accertato un furto: potrebbero essere stati riposti altrove o registrati male. L’ultimo confronto completo tra registro e armadi risale a due mesi fa.

Sono state pulite cinque levigatrici. Solo L-09 ha superato anche il controllo di funzionamento e può essere prestata. Si trova sul ripiano basso, con il cavo raccolto nella sua borsa. Le altre quattro restano bloccate fino al controllo. Il bollino arancione indica soltanto che la pulizia è finita, non che il prestito sia autorizzato.

### Consumabili: dati provvisori
Il materiale abrasivo pesa 2,7 kg, comprese le buste. Questo peso non permette di calcolare il numero dei fogli utilizzabili. Sono state proposte nuove buste, ma non è stato effettuato alcun ordine.

Il saldo per i consumabili è stimato in 95 € e deve ancora essere verificato con tre scontrini: non è una disponibilità definitiva.

### Etichette, locali e moduli
Giulia ha offerto di riscrivere le etichette martedì, ma non ha ancora confermato la presenza. L’elenco delle etichette illeggibili è nel quaderno sul tavolo.

Il pavimento anteriore è stato pulito. La serratura del deposito è difettosa: il deposito resta chiuso finché la serratura non viene riparata e controllata.

Per i nuovi prestiti si usa ancora il modulo consueto. La bozza di modulo breve non è stata approvata: il suo salvataggio nella cartella comune non autorizza a sostituire il modulo attuale.
```

### full: pass

```text
## Consegna per l’apertura di domani

### Strumenti: presenti, assenti e prestabili
Il registro contiene 62 strumenti: 56 sono stati trovati negli armadi, quattro sono in prestito con moduli firmati e due non sono stati trovati. Il rientro dei quattro prestiti è previsto per il 28 maggio.

Per i due strumenti mancanti non è stato accertato un furto: potrebbero essere stati riposti altrove o registrati male. L’ultimo confronto completo tra registro e armadi risale a due mesi fa.

Delle cinque levigatrici pulite, soltanto L-09 ha superato anche il controllo di funzionamento e può essere prestata. Si trova sul ripiano basso, con il cavo raccolto nella sua borsa. Le altre quattro restano bloccate fino al controllo. Il bollino arancione indica solo che la pulizia è finita: non autorizza il prestito.

### Consumabili: dati e acquisti non confermati
Il materiale abrasivo pesa 2,7 kg, comprese le buste. Il peso non permette di calcolare quanti fogli siano utilizzabili.

Sono state proposte nuove buste, ma non è stato effettuato alcun ordine. Il saldo per i consumabili è stimato in 95 €: deve ancora essere verificato con tre scontrini e non è una disponibilità definitiva.

### Locali, etichette e moduli
Il pavimento anteriore è stato pulito. La serratura del deposito è difettosa: il deposito resta chiuso finché la serratura non viene riparata e controllata.

Giulia ha offerto di riscrivere le etichette martedì, ma non ha ancora confermato la presenza. L’elenco delle etichette illeggibili è nel quaderno sul tavolo.

Per i nuovi prestiti si usa ancora il modulo consueto. La bozza di modulo breve non è stata approvata: il suo salvataggio nella cartella comune non autorizza a sostituire il modulo attuale.
```

### ultra: pass

```text
## Consegna per l’apertura di domani

### Strumenti e accesso
- Il registro contiene 62 strumenti: 56 trovati negli armadi, quattro in prestito con moduli firmati e due non trovati. Il rientro dei prestiti è previsto per il 28 maggio.
- Per i due strumenti mancanti non è stato accertato un furto: potrebbero essere altrove o registrati male. L’ultimo confronto completo tra registro e armadi risale a due mesi fa.
- Cinque levigatrici sono state pulite. Solo L-09 ha superato anche il controllo di funzionamento ed è prestabile: si trova sul ripiano basso, con il cavo raccolto nella sua borsa. Le altre quattro restano bloccate fino al controllo. Il bollino arancione indica soltanto la pulizia completata, non l’autorizzazione al prestito.
- Il pavimento anteriore è stato pulito. Il deposito resta chiuso finché la serratura difettosa non viene riparata e controllata.

### Materiali e dati provvisori
- Il materiale abrasivo pesa 2,7 kg, buste comprese: il peso non permette di calcolare quanti fogli siano utilizzabili.
- Sono state proposte nuove buste, ma non è stato effettuato alcun ordine.
- Il saldo per i consumabili è stimato in 95 €: deve ancora essere verificato con tre scontrini e non è una disponibilità definitiva.
- Giulia ha offerto di riscrivere le etichette martedì, ma non ha confermato la presenza. L’elenco delle etichette illeggibili è nel quaderno sul tavolo.

### Modulo per i prestiti
Per i nuovi prestiti si usa ancora il modulo consueto. La bozza di modulo breve non è approvata: il salvataggio nella cartella comune non autorizza a sostituire il modulo attuale.
```

### off: pass

```text
## Consegna per l’apertura di domani

### Strumenti: presenza e disponibilità
Il registro contiene 62 strumenti: 56 sono stati trovati negli armadi, quattro sono in prestito con moduli firmati e due non sono stati trovati. Il rientro dei quattro prestiti è previsto per il 28 maggio.

Per i due strumenti mancanti non è stato accertato un furto: potrebbero essere stati riposti altrove o registrati male. L’ultimo confronto completo tra registro e armadi risale a due mesi fa. La presenza negli armadi non va confusa con l’autorizzazione al prestito.

Sono state pulite cinque levigatrici:
- **L-09:** ha superato anche il controllo di funzionamento e può essere prestata. Si trova sul ripiano basso, con il cavo raccolto nella sua borsa.
- **Le altre quattro:** restano bloccate fino al controllo di funzionamento.

Il bollino arancione indica soltanto che la pulizia è finita, non che lo strumento sia autorizzato al prestito.

### Consumabili e informazioni provvisorie
Il materiale abrasivo pesa 2,7 kg, comprese le buste. Il peso non permette di calcolare quanti fogli siano utilizzabili.

Sono state proposte nuove buste, ma non è stato effettuato alcun ordine. Il saldo per i consumabili è stimato in 95 €: deve ancora essere verificato con tre scontrini e non rappresenta una disponibilità definitiva.

### Etichette e locali
Giulia ha offerto di riscrivere le etichette martedì, ma non ha ancora confermato la presenza. Il suo intervento non è quindi confermato. L’elenco delle etichette illeggibili è nel quaderno sul tavolo.

Il pavimento anteriore è stato pulito. La serratura del deposito è difettosa: il deposito resta chiuso finché la serratura non viene riparata e controllata.

### Moduli per i prestiti
Per i nuovi prestiti si usa ancora il modulo consueto. La bozza di modulo breve non è stata approvata: il fatto che sia salvata nella cartella comune non autorizza a sostituire il modulo attuale.
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
## Aggiornamento per la riunione

### Osservazioni
- Nel registro di venerdì mancano 19 minuti di dati, dalle 11:06 alle 11:25. Prima e dopo, i valori sono compresi tra 42 e 45 cm.
- Durante la lacuna non ci sono misure e non era presente un secondo sensore nello stesso recipiente. I valori vicini non permettono di stabilire il livello dell’acqua in quei 19 minuti.
- Sabato è stato trovato e fissato un connettore non ben fissato. Nei due controlli successivi, di 45 minuti ciascuno, non sono comparse lacune. La durata limitata dei controlli non dimostra una risoluzione definitiva.

### Cause possibili e limiti delle informazioni
- Il connettore potrebbe aver interrotto la registrazione, ma non è documentato che abbia perso il contatto venerdì. Il fatto che sia stato fissato prima dei controlli senza lacune non dimostra che fosse la causa.
- La lacuna non prova un’interruzione della pompa: il suo stato non veniva registrato.
- La nota non descrive un’ispezione degli altri componenti: non consente né di affermare che siano stati danneggiati né di escluderlo. Questo aggiornamento riguarda il comportamento del sistema di registrazione.

### Proposta da discutere
Una persona del gruppo tecnico ha proposto una registrazione continua di 48 ore per verificare la stabilità. L’attività non è stata decisa né iniziata; non ha un responsabile assegnato o una data di conclusione fissata. La riunione potrà discuterne.
```

### lite: pass

```text
## Aggiornamento sul sistema di registrazione

### Osservazioni
Nel registro di venerdì manca un tratto di 19 minuti, dalle 11:06 alle 11:25. Prima e dopo la lacuna, i valori sono tra 42 cm e 45 cm. Per quei 19 minuti non ci sono misure e non era presente un secondo sensore nello stesso recipiente. I valori vicini non dimostrano quale fosse il livello durante la lacuna.

Sabato è stato trovato un connettore non ben fissato ed è stato fissato. Nei due controlli successivi, di 45 minuti ciascuno, non sono comparse lacune. Questi controlli limitati non dimostrano che il problema sia risolto per sempre.

### Causa possibile e limiti delle informazioni
Il connettore potrebbe aver interrotto la registrazione, ma il documento non mostra che abbia perso il contatto venerdì. Il fatto che sia stato fissato prima dei controlli senza lacune non lo identifica come causa certa.

Una lacuna nei dati non equivale necessariamente a un’interruzione della pompa. In quel periodo lo stato della pompa non veniva registrato.

La nota non descrive un’ispezione degli altri componenti: non permette di affermare che siano stati danneggiati né di garantire che non lo siano stati. Questo aggiornamento riguarda il comportamento del sistema di registrazione.

### Proposta da discutere
Una persona del gruppo tecnico ritiene che una registrazione continua di 48 ore potrebbe essere utile per verificare la stabilità. È una proposta, non una decisione: l’attività non è iniziata, non ha una persona responsabile assegnata e non ha una data di conclusione fissata. La riunione potrà discuterne.
```

### full: pass

```text
## Aggiornamento sul sistema di registrazione

### Osservazioni
Nel registro di venerdì mancano 19 minuti di dati, dalle 11:06 alle 11:25. Prima e dopo la lacuna, i valori sono tra 42 cm e 45 cm. Per quei 19 minuti non ci sono misure e non era presente un secondo sensore nello stesso recipiente. I valori vicini non dimostrano quale fosse il livello durante la lacuna.

Sabato è stato trovato e fissato un connettore non ben fissato. Nei due controlli successivi, di 45 minuti ciascuno, non sono comparse lacune. Questi controlli limitati non dimostrano che il problema sia risolto per sempre.

### Cause possibili e limiti
Il connettore potrebbe aver interrotto la registrazione, ma il documento non dimostra che abbia perso il contatto venerdì. Il fatto che sia stato fissato prima dei controlli senza lacune non basta a identificarlo come causa certa.

Una lacuna nei dati non equivale necessariamente a un’interruzione della pompa. In quel periodo lo stato della pompa non veniva registrato.

La nota non descrive un’ispezione degli altri componenti: non permette di affermare che siano stati danneggiati né di garantire che non lo siano stati. Questo aggiornamento riguarda il comportamento del sistema di registrazione.

### Proposta da discutere
Una persona del gruppo tecnico ritiene che una registrazione continua di 48 ore potrebbe essere utile per verificare la stabilità. È una proposta, non un’attività decisa o programmata: non è iniziata, non ha una persona responsabile assegnata né una data di conclusione fissata. La riunione potrà discuterne.
```

### ultra: pass

```text
## Aggiornamento sul sistema di registrazione

### Osservazioni
- Nel registro di venerdì mancano 19 minuti, dalle 11:06 alle 11:25. Prima e dopo, i valori sono tra 42 cm e 45 cm. Durante la lacuna non ci sono misure e non era presente un secondo sensore nello stesso recipiente: i valori vicini non dimostrano quale fosse il livello in quei minuti.
- Sabato è stato trovato e fissato un connettore non ben fissato. Nei due controlli successivi, di 45 minuti ciascuno, non sono comparse lacune. Questi controlli limitati non dimostrano che il problema sia risolto per sempre.

### Cause possibili e limiti
Il connettore potrebbe aver interrotto la registrazione, ma il documento non dimostra che abbia perso il contatto venerdì. Il fatto che sia stato fissato prima dei controlli senza lacune non lo rende una causa certa.

Una lacuna nei dati non equivale necessariamente a un’interruzione della pompa: il suo stato non veniva registrato. La nota non descrive un’ispezione degli altri componenti; non permette quindi di affermare né di escludere che siano stati danneggiati. Questo aggiornamento riguarda il comportamento del sistema di registrazione.

### Proposta da discutere
Una persona del gruppo tecnico ritiene che una registrazione continua di 48 ore potrebbe essere utile per verificare la stabilità. È una proposta, non una decisione: l’attività non è iniziata, non ha una persona responsabile assegnata né una data di conclusione fissata. La riunione potrà discuterne.
```

### off: pass

```text
## Aggiornamento sul sistema di registrazione del livello dell’acqua

### Osservazioni
Nel registro di venerdì manca un tratto di 19 minuti, dalle 11:06 alle 11:25. Prima e dopo la lacuna, i valori sono tra 42 cm e 45 cm. Per quei diciannove minuti non ci sono misure e non era presente un secondo sensore nello stesso recipiente. I valori vicini non dimostrano quale fosse il livello durante la lacuna.

Sabato è stato trovato un connettore non ben fissato ed è stato fissato. Nei due controlli successivi, di 45 minuti ciascuno, non sono comparse lacune. Questi controlli limitati non dimostrano che il problema sia risolto per sempre.

### Cause possibili e limiti delle informazioni
Il connettore potrebbe aver interrotto la registrazione, ma il documento non dimostra che abbia perso il contatto venerdì. Il fatto che sia stato sistemato prima dei controlli senza lacune non basta a identificarlo come causa certa.

Una lacuna nei dati non equivale necessariamente a un’interruzione della pompa: in quel periodo lo stato della pompa non veniva registrato.

La nota non descrive un’ispezione degli altri componenti. Non è quindi possibile stabilire se siano stati danneggiati, né garantire che non lo siano stati. Questo aggiornamento riguarda il comportamento del sistema di registrazione.

### Proposta da discutere
Una persona del gruppo tecnico ritiene che una registrazione continua di 48 ore potrebbe essere utile per verificare la stabilità. La riunione potrà discuterne.

L’attività è soltanto proposta: non è stata decisa né iniziata, non ha una persona responsabile assegnata e non ha una data di conclusione fissata.
```

## modes-it-092 · translation_exceptions

Source task:

> Translate this fictional lesson policy into Italian: Once a lesson has taken place, its fee is not refundable. If the studio cancels in advance, learners may request a refund instead of accepting another lesson. They are not obliged to accept the alternative.

### baseline: pass

```text
Una volta svolta la lezione, il relativo costo non è rimborsabile. Se lo studio annulla la lezione in anticipo, gli allievi possono richiedere un rimborso anziché accettare un’altra lezione. Non sono obbligati ad accettare l’alternativa.
```

### lite: pass

```text
Una volta che una lezione si è svolta, il relativo costo non è rimborsabile. Se lo studio annulla la lezione in anticipo, gli allievi possono richiedere un rimborso invece di accettare un'altra lezione. Non sono obbligati ad accettare l'alternativa.
```

### full: pass

```text
Una volta svolta la lezione, la relativa quota non è rimborsabile. Se lo studio annulla la lezione in anticipo, gli allievi possono chiedere un rimborso anziché accettare un’altra lezione. Non sono obbligati ad accettare l’alternativa.
```

### ultra: pass

```text
Una volta svolta la lezione, la relativa quota non è rimborsabile. Se lo studio annulla la lezione in anticipo, gli allievi possono richiedere un rimborso anziché accettare un’altra lezione. Non sono obbligati ad accettare l’alternativa.
```

### off: pass

```text
Una volta che una lezione si è svolta, la relativa quota non è rimborsabile. Se lo studio annulla la lezione in anticipo, gli allievi possono richiedere un rimborso anziché accettare un'altra lezione. Non sono obbligati ad accettare l'alternativa.
```

