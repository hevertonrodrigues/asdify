# de: all source tasks and answers

Labels below are unblinded after review. Pass requires both meaning reviews and exact checks. A flagged answer is retained unchanged.

## modes-de-001 · already_clear

Source task:

> Prüfe diesen Satz. Wenn er klar ist, gib ihn unverändert und ohne Kommentar zurück: „Bitte stellen Sie die Stühle nach dem Kurs an die Wand.“

### baseline: pass

```text
Bitte stellen Sie die Stühle nach dem Kurs an die Wand.
```

### lite: pass

```text
Bitte stellen Sie die Stühle nach dem Kurs an die Wand.
```

### full: pass

```text
Bitte stellen Sie die Stühle nach dem Kurs an die Wand.
```

### ultra: pass

```text
Bitte stellen Sie die Stühle nach dem Kurs an die Wand.
```

### off: pass

```text
Bitte stellen Sie die Stühle nach dem Kurs an die Wand.
```

## modes-de-002 · permissions

Source task:

> Formuliere einfacher: Mitglieder dürfen eigene Handschuhe mitbringen. Sie müssen das bereitgestellte Werkzeug nach Gebrauch reinigen. Eigene Handschuhe sind keine Voraussetzung für die Teilnahme.

### baseline: pass

```text
Mitglieder können eigene Handschuhe mitbringen, müssen aber nicht. Nach Gebrauch müssen sie das bereitgestellte Werkzeug reinigen.
```

### lite: pass

```text
Mitglieder dürfen eigene Handschuhe mitbringen, müssen aber nicht. Sie müssen das bereitgestellte Werkzeug nach Gebrauch reinigen.
```

### full: pass

```text
Mitglieder dürfen eigene Handschuhe mitbringen, müssen aber nicht. Sie müssen das bereitgestellte Werkzeug nach Gebrauch reinigen.
```

### ultra: pass

```text
Mitglieder dürfen eigene Handschuhe mitbringen, müssen aber nicht. Sie müssen das bereitgestellte Werkzeug nach Gebrauch reinigen.
```

### off: pass

```text
Mitglieder können eigene Handschuhe mitbringen, müssen es aber nicht. Das bereitgestellte Werkzeug müssen sie nach Gebrauch reinigen.
```

## modes-de-003 · conditions

Source task:

> Schreibe diese fiktive Hausregel klarer: Der Dachraum darf nur benutzt werden, wenn die Beleuchtung geprüft und der Zugang freigegeben wurde. Eine Prüfung allein ersetzt die Freigabe nicht.

### baseline: pass

```text
Der Dachraum darf erst benutzt werden, wenn die Beleuchtung geprüft und der Zugang freigegeben wurde. Die Prüfung allein reicht nicht aus.
```

### lite: pass

```text
Der Dachraum darf nur benutzt werden, wenn die Beleuchtung geprüft wurde und der Zugang freigegeben ist. Die Prüfung allein reicht nicht aus.
```

### full: pass

```text
Der Dachraum darf nur benutzt werden, wenn die Beleuchtung geprüft wurde und der Zugang freigegeben ist. Die Prüfung allein reicht nicht aus.
```

### ultra: pass

```text
Der Dachraum darf nur benutzt werden, wenn die Beleuchtung geprüft und der Zugang freigegeben wurde. Die Prüfung allein reicht nicht.
```

### off: pass

```text
Der Dachraum darf erst benutzt werden, wenn die Beleuchtung geprüft und der Zugang freigegeben wurde. Die Prüfung allein reicht nicht aus.
```

## modes-de-004 · negation

Source task:

> Kürze diese Nachricht: Die fehlende Unterschrift bedeutet nicht, dass der Antrag abgelehnt wurde. Er bleibt in Bearbeitung. Bitte reichen Sie nur die unterschriebene letzte Seite nach, nicht den ganzen Antrag.

### baseline: pass

```text
Ihr Antrag bleibt trotz fehlender Unterschrift in Bearbeitung und ist nicht abgelehnt. Bitte reichen Sie nur die unterschriebene letzte Seite nach, nicht den ganzen Antrag.
```

### lite: pass

```text
Trotz fehlender Unterschrift bleibt der Antrag in Bearbeitung; er wurde nicht abgelehnt. Bitte reichen Sie nur die unterschriebene letzte Seite nach, nicht den ganzen Antrag.
```

### full: pass

```text
Der Antrag ist trotz fehlender Unterschrift nicht abgelehnt und bleibt in Bearbeitung. Bitte reichen Sie nur die unterschriebene letzte Seite nach, nicht den ganzen Antrag.
```

### ultra: pass

```text
Der Antrag ist trotz fehlender Unterschrift nicht abgelehnt, sondern weiter in Bearbeitung. Bitte reichen Sie nur die unterschriebene letzte Seite nach, nicht den ganzen Antrag.
```

### off: pass

```text
Der Antrag ist trotz fehlender Unterschrift nicht abgelehnt, sondern weiter in Bearbeitung. Bitte reichen Sie nur die unterschriebene letzte Seite nach, nicht den ganzen Antrag.
```

## modes-de-005 · exceptions

Source task:

> Überarbeite: Für die Leihgeräte ist eine Kaution nötig. Ausgenommen sind Geräte, die ausschließlich im Kursraum benutzt werden. Wer ein solches Gerät mitnimmt, fällt nicht mehr unter die Ausnahme.

### baseline: pass

```text
Für Leihgeräte ist eine Kaution nötig. Nur Geräte, die ausschließlich im Kursraum benutzt werden, sind davon ausgenommen. Wer ein Gerät mitnimmt, muss dafür eine Kaution hinterlegen.
```

### lite: pass

```text
Für Leihgeräte ist eine Kaution nötig. Die Ausnahme gilt nur für Geräte, die ausschließlich im Kursraum benutzt werden. Wer ein solches Gerät mitnimmt, muss eine Kaution hinterlegen.
```

### full: pass

```text
Für Leihgeräte ist eine Kaution nötig, außer wenn sie ausschließlich im Kursraum benutzt werden. Wer ein solches Gerät mitnimmt, muss eine Kaution hinterlegen.
```

### ultra: pass

```text
Für Leihgeräte ist eine Kaution nötig, außer sie werden ausschließlich im Kursraum benutzt. Wer ein solches Gerät mitnimmt, muss eine Kaution hinterlegen.
```

### off: pass

```text
Für Leihgeräte ist eine Kaution erforderlich. Nur Geräte, die ausschließlich im Kursraum benutzt werden, sind davon ausgenommen. Wer ein solches Gerät mitnimmt, muss eine Kaution hinterlegen.
```

## modes-de-006 · unknown_actor

Source task:

> Mache die Notiz verständlicher, ohne jemanden zu erfinden: Jonas meldete den beschädigten Griff am Dienstag. Am Mittwoch wurde der Griff ersetzt. Wer ihn ersetzt hat, ist im Protokoll nicht vermerkt.

### baseline: pass

```text
Jonas meldete am Dienstag, dass der Griff beschädigt war. Am Mittwoch wurde der Griff ersetzt. Das Protokoll nennt nicht, wer ihn ersetzt hat.
```

### lite: pass

```text
Jonas meldete den beschädigten Griff am Dienstag. Am Mittwoch wurde der Griff ersetzt. Im Protokoll steht nicht, wer ihn ersetzt hat.
```

### full: pass

```text
Jonas meldete den beschädigten Griff am Dienstag. Am Mittwoch wurde der Griff ersetzt. Das Protokoll nennt nicht, wer ihn ersetzt hat.
```

### ultra: pass

```text
Jonas meldete am Dienstag den beschädigten Griff. Am Mittwoch wurde er ersetzt. Wer den Griff ersetzt hat, steht nicht im Protokoll.
```

### off: pass

```text
Jonas meldete am Dienstag, dass der Griff beschädigt war. Am Mittwoch wurde der Griff ersetzt. Im Protokoll steht nicht, wer ihn ersetzt hat.
```

## modes-de-007 · sequence

Source task:

> Schreibe eine kurze Anleitung in drei Schritten: Zuerst den Entwurf lokal speichern, danach die Vorschau prüfen und erst nach der Prüfung auf „Veröffentlichen“ klicken.

### baseline: pass

```text
1. Speichere den Entwurf lokal.
2. Prüfe die Vorschau.
3. Klicke erst nach der Prüfung auf „Veröffentlichen“.
```

### lite: pass

```text
1. Den Entwurf lokal speichern.
2. Danach die Vorschau prüfen.
3. Erst nach der Prüfung auf „Veröffentlichen“ klicken.
```

### full: pass

```text
1. Den Entwurf lokal speichern.
2. Danach die Vorschau prüfen.
3. Erst nach der Prüfung auf „Veröffentlichen“ klicken.
```

### ultra: pass

```text
1. Den Entwurf lokal speichern.
2. Die Vorschau prüfen.
3. Erst nach der Prüfung auf „Veröffentlichen“ klicken.
```

### off: pass

```text
1. Den Entwurf lokal speichern.
2. Danach die Vorschau prüfen.
3. Erst nach der Prüfung auf „Veröffentlichen“ klicken.
```

## modes-de-008 · uncertainty

Source task:

> Formuliere präziser: Der erhöhte Stromverbrauch könnte mit dem neuen Lüfter zusammenhängen. Bisher gibt es nur Messwerte für zwei Abende. Der Verbrauch ohne Lüfter wurde nicht unter denselben Bedingungen gemessen.

### baseline: pass

```text
Der neue Lüfter könnte zum erhöhten Stromverbrauch beitragen. Ein Zusammenhang ist jedoch nicht belegt: Es liegen nur Messwerte für zwei Abende vor, und der Verbrauch ohne Lüfter wurde nicht unter denselben Bedingungen gemessen.
```

### lite: pass

```text
Der erhöhte Stromverbrauch könnte mit dem neuen Lüfter zusammenhängen. Bisher liegen nur Messwerte für zwei Abende vor. Der Verbrauch ohne Lüfter wurde nicht unter denselben Bedingungen gemessen.
```

### full: pass

```text
Der erhöhte Stromverbrauch könnte mit dem neuen Lüfter zusammenhängen. Bisher liegen nur Messwerte für zwei Abende vor. Vergleichswerte ohne Lüfter unter denselben Bedingungen fehlen.
```

### ultra: flagged

```text
Der erhöhte Stromverbrauch könnte mit dem neuen Lüfter zusammenhängen. Messwerte liegen bisher nur für zwei Abende vor. Der Verbrauch ohne Lüfter wurde unter anderen Bedingungen gemessen.
```

Review notes: Die verneinte gleichartige Messung wird zu einer positiven Aussage über andersartige Messungen verstärkt. / Bewahrt die drei Kernaussagen, verstärkt aber die Aussage zur Existenz einer Messung ohne Lüfter.

### off: flagged

```text
Der erhöhte Stromverbrauch könnte mit dem neuen Lüfter zusammenhängen. Bisher liegen jedoch nur Messwerte für zwei Abende vor. Der Verbrauch ohne Lüfter wurde nicht unter denselben Bedingungen gemessen; ein direkter Vergleich ist daher nicht möglich.
```

Review notes: Alle Einschränkungen erhalten; der fehlende direkte Vergleich folgt aus den unterschiedlichen Messbedingungen. / Alle Ausgangsangaben bleiben erhalten, doch die zusätzliche Schlussfolgerung ist zu absolut.

## modes-de-009 · estimates

Source task:

> Kürze den Hinweis: Wir rechnen mit ungefähr 90 bis 120 Minuten für das Sortieren, sofern die Etiketten lesbar sind. Für beschädigte Etiketten ist keine zusätzliche Zeit geschätzt worden. Die Dauer ist nicht zugesichert.

### baseline: pass

```text
Geschätzte Sortierdauer bei lesbaren Etiketten: ca. 90–120 Minuten, ohne Zusicherung. Zusätzliche Zeit für beschädigte Etiketten wurde nicht geschätzt.
```

### lite: pass

```text
Für das Sortieren rechnen wir mit etwa 90 bis 120 Minuten, sofern die Etiketten lesbar sind. Zusätzliche Zeit für beschädigte Etiketten wurde nicht geschätzt. Die Dauer ist nicht zugesichert.
```

### full: pass

```text
Das Sortieren dauert voraussichtlich etwa 90 bis 120 Minuten, sofern die Etiketten lesbar sind. Zusätzliche Zeit für beschädigte Etiketten wurde nicht geschätzt. Die Dauer ist nicht zugesichert.
```

### ultra: pass

```text
Für das Sortieren rechnen wir mit etwa 90 bis 120 Minuten, sofern die Etiketten lesbar sind. Zusätzliche Zeit für beschädigte Etiketten wurde nicht geschätzt. Die Dauer ist nicht zugesichert.
```

### off: pass

```text
Für das Sortieren rechnen wir mit etwa 90 bis 120 Minuten, sofern die Etiketten lesbar sind. Zusätzliche Zeit für beschädigte Etiketten wurde nicht geschätzt. Die Dauer ist nicht zugesichert.
```

## modes-de-010 · numbers_units

Source task:

> Schreibe das Angebot klarer: Die Miete beträgt 36 € je Kalenderwoche und Kiste. Die erste angefangene Kalenderwoche zählt vollständig. Der Preis enthält die Reinigung, aber nicht den Transport.

### baseline: pass

```text
Die Miete beträgt 36 € pro Kiste und Kalenderwoche. Die erste angefangene Kalenderwoche wird vollständig berechnet. Die Reinigung ist im Preis enthalten, der Transport nicht.
```

### lite: pass

```text
Die Miete beträgt 36 € pro Kiste und Kalenderwoche. Die erste angefangene Kalenderwoche wird vollständig berechnet. Die Reinigung ist im Preis enthalten, der Transport nicht.
```

### full: pass

```text
Die Miete beträgt 36 € pro Kiste und Kalenderwoche. Die erste angefangene Kalenderwoche wird voll berechnet. Die Reinigung ist im Preis enthalten, der Transport nicht.
```

### ultra: pass

```text
Die Miete beträgt 36 € pro Kiste und Kalenderwoche. Die erste angefangene Kalenderwoche wird voll berechnet. Reinigung ist enthalten, Transport nicht.
```

### off: pass

```text
Die Miete beträgt 36 € pro Kiste und Kalenderwoche. Die erste angefangene Kalenderwoche wird vollständig berechnet. Die Reinigung ist im Preis enthalten, der Transport nicht.
```

## modes-de-011 · denominators

Source task:

> Fasse korrekt zusammen: Von 96 bearbeiteten Anfragen wurden 24 am Wochenende beantwortet. Von diesen 24 betrafen 8 die Anmeldung. Wir kennen die Gesamtzahl der Anmeldeanfragen nicht.

### baseline: pass

```text
Von 96 bearbeiteten Anfragen wurden 24 (25 %) am Wochenende beantwortet. Davon betrafen 8 die Anmeldung, also ein Drittel der am Wochenende beantworteten Anfragen. Die Gesamtzahl der Anmeldeanfragen ist unbekannt.
```

### lite: pass

```text
Von 96 bearbeiteten Anfragen wurden 24 am Wochenende beantwortet. Davon betrafen 8 die Anmeldung. Die Gesamtzahl der Anmeldeanfragen ist unbekannt.
```

### full: pass

```text
Von 96 bearbeiteten Anfragen wurden 24 am Wochenende beantwortet. Davon betrafen 8 die Anmeldung. Die Gesamtzahl der Anmeldeanfragen ist unbekannt.
```

### ultra: pass

```text
Von 96 bearbeiteten Anfragen wurden 24 am Wochenende beantwortet; davon betrafen 8 die Anmeldung. Die Gesamtzahl der Anmeldeanfragen ist unbekannt.
```

### off: pass

```text
Von 96 bearbeiteten Anfragen wurden 24 am Wochenende beantwortet. Darunter waren 8 Anmeldeanfragen. Wie viele Anmeldeanfragen es insgesamt gab, ist nicht bekannt.
```

## modes-de-012 · sampling

Source task:

> Formuliere die Grenzen dieser fiktiven Befragung: 31 Besucher eines Tauschmarkts haben freiwillig geantwortet. Befragt wurden nur Personen am Ausgang zwischen 11 und 12 Uhr. Eine Zufallsauswahl fand nicht statt.

### baseline: pass

```text
Die Befragung umfasst nur 31 freiwillig antwortende Besucher, die zwischen 11 und 12 Uhr am Ausgang erreicht wurden. Durch die freiwillige Teilnahme und die zeitlich sowie örtlich begrenzte Auswahl können Verzerrungen entstehen. Da keine Zufallsauswahl stattfand, sind die Ergebnisse nicht ohne Weiteres auf alle Besucher des Tauschmarkts übertragbar.
```

### lite: pass

```text
Die fiktive Befragung umfasst 31 Besucher eines Tauschmarkts, die freiwillig geantwortet haben. Befragt wurden nur Personen am Ausgang zwischen 11 und 12 Uhr; eine Zufallsauswahl fand nicht statt. Die Ergebnisse sind daher nicht ohne Weiteres auf alle Besucher übertragbar.
```

### full: pass

```text
Die fiktive Befragung erfasst nur 31 Besucher, die zwischen 11 und 12 Uhr am Ausgang des Tauschmarkts freiwillig geantwortet haben. Es gab keine Zufallsauswahl. Durch die freiwillige Teilnahme sowie die Beschränkung auf einen Ort und ein Zeitfenster können die Ergebnisse verzerrt sein. Sie lassen sich nicht ohne Weiteres auf alle Besucher übertragen.
```

### ultra: pass

```text
Die fiktive Befragung umfasst 31 freiwillig antwortende Besucher eines Tauschmarkts. Befragt wurden nur Personen am Ausgang zwischen 11 und 12 Uhr, ohne Zufallsauswahl. Die Ergebnisse sind daher nicht ohne Weiteres auf alle Besucher übertragbar.
```

### off: pass

```text
Die fiktive Befragung umfasst 31 Besucher eines Tauschmarkts, die freiwillig geantwortet haben. Befragt wurden ausschließlich Personen am Ausgang zwischen 11 und 12 Uhr; eine Zufallsauswahl fand nicht statt. Durch die freiwillige Teilnahme und die Beschränkung auf diesen Ort und Zeitraum können bestimmte Besuchergruppen über- oder unterrepräsentiert sein. Die Ergebnisse lassen sich daher nicht ohne Weiteres auf alle Besucher des Tauschmarkts übertragen.
```

## modes-de-013 · calculation

Source task:

> Ein Verein kauft 9 Ordner für jeweils 4,50 € und bezahlt einmalig 6 € Versand. Wie hoch ist der Gesamtbetrag? Zeige die Rechnung.

### baseline: pass

```text
9 × 4,50 € + 6,00 € = 40,50 € + 6,00 € = 46,50 €.
Der Gesamtbetrag beträgt 46,50 €.
```

### lite: pass

```text
9 × 4,50 € = 40,50 €
40,50 € + 6 € Versand = 46,50 €

Der Gesamtbetrag beträgt 46,50 €.
```

### full: pass

```text
9 × 4,50 € + 6 € Versand = 40,50 € + 6 € = 46,50 €.
Der Gesamtbetrag beträgt 46,50 €.
```

### ultra: pass

```text
9 × 4,50 € + 6 € einmaliger Versand = 40,50 € + 6 € = 46,50 € Gesamtbetrag.
```

### off: pass

```text
9 × 4,50 € = 40,50 €
40,50 € + 6,00 € Versand = 46,50 €

Der Gesamtbetrag beträgt 46,50 €.
```

## modes-de-014 · percentage_points

Source task:

> In einer fiktiven Tabelle steigt der Anteil von 41 % auf 47 %. Nenne den Anstieg in Prozentpunkten und vermeide eine relative Prozentangabe.

### baseline: pass

```text
Der Anteil steigt von 41 % auf 47 %, also um 6 Prozentpunkte.
```

### lite: pass

```text
Der Anteil steigt von 41 % auf 47 %, also um 6 Prozentpunkte.
```

### full: pass

```text
Der Anteil steigt von 41 % auf 47 %, also um 6 Prozentpunkte.
```

### ultra: pass

```text
Der Anteil steigt von 41 % auf 47 %, also um 6 Prozentpunkte.
```

### off: pass

```text
Der Anteil steigt um 6 Prozentpunkte: 47 % − 41 % = 6 Prozentpunkte.
```

## modes-de-015 · conflicting_notes

Source task:

> Schreibe eine Statusnotiz: Auf dem Aufkleber steht Fach 7, im Übergabeformular steht Fach 9. Beide Angaben wurden am selben Tag eingetragen. Der tatsächliche Lagerort wurde noch nicht geprüft.

### baseline: pass

```text
Status: Die Lagerortangaben widersprechen sich. Auf dem Aufkleber steht Fach 7, im Übergabeformular Fach 9. Beide Angaben wurden am selben Tag eingetragen. Der tatsächliche Lagerort wurde noch nicht geprüft und ist daher ungeklärt.
```

### lite: pass

```text
Auf dem Aufkleber steht Fach 7, im Übergabeformular Fach 9. Beide Angaben wurden am selben Tag eingetragen. Die Angaben widersprechen sich; der tatsächliche Lagerort wurde noch nicht geprüft.
```

### full: pass

```text
Die Lagerortangaben widersprechen sich: Auf dem Aufkleber steht Fach 7, im Übergabeformular Fach 9. Beide Angaben wurden am selben Tag eingetragen. Der tatsächliche Lagerort wurde noch nicht geprüft.
```

### ultra: pass

```text
Die Angaben widersprechen sich: Aufkleber „Fach 7“, Übergabeformular „Fach 9“. Beide wurden am selben Tag eingetragen. Der tatsächliche Lagerort wurde noch nicht geprüft.
```

### off: pass

```text
Status: Die Lagerortangaben widersprechen sich. Auf dem Aufkleber steht Fach 7, im Übergabeformular Fach 9. Beide Angaben wurden am selben Tag eingetragen. Der tatsächliche Lagerort wurde noch nicht geprüft.
```

## modes-de-016 · technical

Source task:

> Überarbeite den Hilfetext: Bei HTTP 408 darf der Client die GET-Anfrage einmal wiederholen. Das gilt nicht für POST. Wenn der zweite Versuch scheitert, soll eine Fehlermeldung angezeigt werden.

### baseline: flagged

```text
Bei HTTP 408 darf der Client eine GET-Anfrage einmal wiederholen. POST-Anfragen dürfen nicht wiederholt werden. Scheitert auch der zweite Versuch, wird eine Fehlermeldung angezeigt.
```

Review notes: Broadens the POST restriction and changes prescribed error handling into asserted behavior. / Erweitert die POST-Ausnahme und macht aus einer Vorgabe eine Verhaltenszusage.

### lite: pass

```text
Bei HTTP 408 darf der Client die GET-Anfrage einmal wiederholen. Für POST gilt das nicht. Scheitert der zweite Versuch, soll eine Fehlermeldung angezeigt werden.
```

### full: pass

```text
Bei HTTP 408 darf der Client eine GET-Anfrage einmal wiederholen. Für POST gilt das nicht. Scheitert der zweite Versuch, soll eine Fehlermeldung angezeigt werden.
```

### ultra: pass

```text
Bei HTTP 408 darf der Client eine GET-Anfrage einmal wiederholen, eine POST-Anfrage nicht. Scheitert auch der zweite Versuch, soll eine Fehlermeldung angezeigt werden.
```

### off: flagged

```text
Bei HTTP 408 darf der Client eine GET-Anfrage einmal wiederholen. POST-Anfragen dürfen nicht wiederholt werden. Scheitert auch der zweite Versuch, soll eine Fehlermeldung angezeigt werden.
```

Review notes: Turns a condition-specific exclusion into a blanket POST prohibition. / Die POST-Ausnahme wird zu einem unbeschränkten Verbot erweitert.

## modes-de-017 · technical

Source task:

> Erkläre diese Einstellung: retention_days=14 betrifft nur automatisch erstellte Vorschaubilder. Originaldateien werden dadurch nicht gelöscht. Die Änderung gilt für neu erzeugte Vorschaubilder, nicht rückwirkend.

### baseline: pass

```text
retention_days=14 legt eine Aufbewahrungsdauer von 14 Tagen für automatisch erstellte Vorschaubilder fest. Originaldateien werden dadurch nicht gelöscht. Die Änderung gilt nur für neu erzeugte Vorschaubilder, nicht rückwirkend.
```

### lite: pass

```text
retention_days=14 legt eine Aufbewahrungsdauer von 14 Tagen nur für automatisch erstellte Vorschaubilder fest. Originaldateien werden dadurch nicht gelöscht. Die Änderung gilt nur für neu erzeugte Vorschaubilder, nicht rückwirkend.
```

### full: pass

```text
retention_days=14 legt die Aufbewahrungsdauer für automatisch erstellte Vorschaubilder auf 14 Tage fest. Originaldateien werden dadurch nicht gelöscht. Die Änderung gilt nur für neu erzeugte Vorschaubilder, nicht rückwirkend.
```

### ultra: pass

```text
retention_days=14 legt eine Aufbewahrungsdauer von 14 Tagen nur für automatisch erstellte Vorschaubilder fest. Originaldateien werden dadurch nicht gelöscht. Die Änderung gilt nur für neu erzeugte Vorschaubilder, nicht rückwirkend.
```

### off: pass

```text
Die Einstellung `retention_days=14` legt eine Aufbewahrungsdauer von 14 Tagen für automatisch erstellte Vorschaubilder fest. Originaldateien werden dadurch nicht gelöscht. Die Änderung gilt nur für neu erzeugte Vorschaubilder, nicht für bereits vorhandene.
```

## modes-de-018 · summary

Source task:

> Fasse für die Kursteilnehmenden zusammen: Der Kurs beginnt am Montag wie geplant um 18 Uhr. Wegen der defekten Spüle wird nicht gekocht. Stattdessen findet die Einführung in die Zutatenkunde statt. Der praktische Kochtermin wird später mitgeteilt.

### baseline: pass

```text
Der Kurs beginnt wie geplant am Montag um 18 Uhr. Wegen der defekten Spüle wird nicht gekocht; stattdessen findet die Einführung in die Zutatenkunde statt. Der praktische Kochtermin wird später mitgeteilt.
```

### lite: pass

```text
Der Kurs beginnt am Montag wie geplant um 18 Uhr. Wegen der defekten Spüle wird nicht gekocht. Stattdessen findet die Einführung in die Zutatenkunde statt. Der praktische Kochtermin wird später mitgeteilt.
```

### full: pass

```text
Der Kurs beginnt wie geplant am Montag um 18 Uhr. Wegen der defekten Spüle wird nicht gekocht. Stattdessen gibt es eine Einführung in die Zutatenkunde. Der praktische Kochtermin wird später mitgeteilt.
```

### ultra: pass

```text
Der Kurs beginnt wie geplant am Montag um 18 Uhr. Wegen der defekten Spüle gibt es statt Kochen eine Einführung in die Zutatenkunde. Der praktische Kochtermin wird später mitgeteilt.
```

### off: pass

```text
Der Kurs beginnt wie geplant am Montag um 18 Uhr. Da die Spüle defekt ist, wird nicht gekocht. Stattdessen findet die Einführung in die Zutatenkunde statt. Der praktische Kochtermin wird später mitgeteilt.
```

## modes-de-019 · scope

Source task:

> Beantworte kurz: Kann ich am Sonntag eine geliehene Kamera zurückgeben, und wann und wo ist das möglich? Angaben: Die Ausgabe ist sonntags geschlossen. Rückgaben sind über das bewachte Empfangsfenster von 10 bis 13 Uhr möglich. Akkus dürfen nicht separat eingeworfen werden.

### baseline: pass

```text
Ja, sonntags sind Rückgaben von 10 bis 13 Uhr über das bewachte Empfangsfenster möglich, obwohl die Ausgabe geschlossen ist. Akkus dürfen nicht separat eingeworfen werden.
```

### lite: pass

```text
Ja, sonntags kannst du die Kamera von 10 bis 13 Uhr über das bewachte Empfangsfenster zurückgeben. Die Ausgabe ist geschlossen. Akkus dürfen nicht separat eingeworfen werden.
```

### full: pass

```text
Ja, sonntags von 10 bis 13 Uhr über das bewachte Empfangsfenster. Die Ausgabe ist geschlossen. Akkus dürfen nicht separat eingeworfen werden.
```

### ultra: pass

```text
Ja, sonntags von 10 bis 13 Uhr am bewachten Empfangsfenster. Die Ausgabe ist geschlossen. Akkus dürfen nicht separat eingeworfen werden.
```

### off: pass

```text
Ja, du kannst die Kamera am Sonntag von 10 bis 13 Uhr über das bewachte Empfangsfenster zurückgeben. Die Ausgabe ist sonntags geschlossen. Akkus dürfen nicht separat eingeworfen werden.
```

## modes-de-020 · analysis

Source task:

> Beweist diese Beobachtung den Erfolg der neuen Beschilderung? In einem fiktiven Laden sinken Nachfragen nach dem Ausgang von 22 auf 10 pro Tag. Gleichzeitig wurde der Ausgang geöffnet, der vorher gesperrt war.

### baseline: pass

```text
Nein. Die Nachfragen sind zwar von 22 auf 10 pro Tag gesunken, gleichzeitig wurde aber der zuvor gesperrte Ausgang geöffnet. Daher lässt sich der Rückgang nicht eindeutig der neuen Beschilderung zuschreiben.
```

### lite: pass

```text
Nein. Die Nachfragen nach dem Ausgang sinken zwar von 22 auf 10 pro Tag. Gleichzeitig wurde aber der zuvor gesperrte Ausgang geöffnet. Daher lässt sich der Rückgang nicht eindeutig auf die neue Beschilderung zurückführen.
```

### full: pass

```text
Nein. Im fiktiven Laden sinken die Nachfragen nach dem Ausgang zwar von 22 auf 10 pro Tag. Gleichzeitig wurde aber der zuvor gesperrte Ausgang geöffnet. Deshalb lässt sich aus der Beobachtung nicht bestimmen, welchen Anteil die neue Beschilderung am Rückgang hat.
```

### ultra: pass

```text
Nein. Im fiktiven Laden sanken die Nachfragen nach dem Ausgang von 22 auf 10 pro Tag. Gleichzeitig wurde der zuvor gesperrte Ausgang geöffnet. Daher lässt sich nicht feststellen, welchen Anteil die neue Beschilderung am Rückgang hatte.
```

### off: pass

```text
Nein. Die Nachfragen nach dem Ausgang sind zwar von 22 auf 10 pro Tag gesunken, gleichzeitig wurde aber der zuvor gesperrte Ausgang geöffnet. Deshalb lässt sich aus dieser Beobachtung nicht bestimmen, ob die neue Beschilderung, die Öffnung des Ausgangs oder beides den Rückgang verursacht hat.
```

## modes-de-021 · voice

Source task:

> Kürze diese persönliche Nachricht, behalte das Du und den freundlichen Ton: Danke für deine Hilfe beim Einräumen. Die letzte Kiste lasse ich bis Mittwoch ungeöffnet, weil du prüfen wolltest, ob deine Notizbücher darin liegen.

### baseline: flagged

```text
Danke fürs Einräumen! Die letzte Kiste bleibt bis Mittwoch zu, damit du prüfen kannst, ob deine Notizbücher drin sind.
```

Review notes: Loses the explicit planned-check rationale and weakens unopened to closed. / The recipient’s previously expressed intention is replaced by an opportunity to check.

### lite: pass

```text
Danke fürs Einräumen! Die letzte Kiste bleibt bis Mittwoch ungeöffnet, weil du prüfen wolltest, ob deine Notizbücher darin liegen.
```

### full: pass

```text
Danke fürs Helfen beim Einräumen! Die letzte Kiste bleibt bis Mittwoch ungeöffnet, weil du prüfen wolltest, ob deine Notizbücher darin liegen.
```

### ultra: pass

```text
Danke fürs Einräumen! Die letzte Kiste bleibt bis Mittwoch ungeöffnet, weil du prüfen wolltest, ob deine Notizbücher darin sind.
```

### off: pass

```text
Danke fürs Helfen beim Einräumen! Die letzte Kiste bleibt bis Mittwoch ungeöffnet, weil du nachsehen wolltest, ob deine Notizbücher darin sind.
```

## modes-de-022 · ambiguity

Source task:

> Zeige die Mehrdeutigkeit, ohne sie aufzulösen: „Mara sprach mit Deniz über ihren Entwurf.“ Es ist nicht klar, wem der Entwurf gehört. Gib zwei mögliche Lesarten an.

### baseline: pass

```text
1. Mara sprach mit Deniz über Maras Entwurf.
2. Mara sprach mit Deniz über Deniz’ Entwurf.
```

### lite: pass

```text
1. Mara sprach mit Deniz über Maras Entwurf.
2. Mara sprach mit Deniz über Deniz’ Entwurf.
```

### full: pass

```text
1. Mara sprach mit Deniz über Maras Entwurf.
2. Mara sprach mit Deniz über Deniz’ Entwurf.
```

### ultra: pass

```text
1. Mara sprach mit Deniz über Maras Entwurf.
2. Mara sprach mit Deniz über Deniz’ Entwurf.
```

### off: pass

```text
1. Mara sprach mit Deniz über Maras Entwurf.
2. Mara sprach mit Deniz über Deniz’ Entwurf.
```

## modes-de-023 · permissions

Source task:

> Formuliere diese fiktive Vereinsregel einfacher: Gäste dürfen an der offenen Probe teilnehmen. Sie müssen nicht sofort Mitglied werden. Für die anschließende geschlossene Sitzung sind jedoch nur Mitglieder zugelassen.

### baseline: pass

```text
Gäste dürfen bei der offenen Probe mitmachen, ohne sofort Mitglied zu werden. An der geschlossenen Sitzung danach dürfen nur Mitglieder teilnehmen.
```

### lite: pass

```text
Gäste dürfen an der offenen Probe teilnehmen und müssen nicht sofort Mitglied werden. An der anschließenden geschlossenen Sitzung dürfen jedoch nur Mitglieder teilnehmen.
```

### full: pass

```text
Gäste dürfen an der offenen Probe teilnehmen und müssen nicht sofort Mitglied werden. An der anschließenden geschlossenen Sitzung dürfen nur Mitglieder teilnehmen.
```

### ultra: pass

```text
Gäste dürfen an der offenen Probe teilnehmen, ohne sofort Mitglied zu werden. An der anschließenden geschlossenen Sitzung dürfen nur Mitglieder teilnehmen.
```

### off: pass

```text
Gäste dürfen bei der offenen Probe mitmachen und müssen nicht sofort Mitglied werden. An der anschließenden geschlossenen Sitzung dürfen nur Mitglieder teilnehmen.
```

## modes-de-024 · conditions

Source task:

> Überarbeite: Ein Rabatt von 15 % gilt nur bei Buchung von mindestens drei Terminen im selben Monat. Bereits bezahlte Einzeltermine werden dafür nicht rückwirkend zusammengerechnet.

### baseline: flagged

```text
Du erhältst 15 % Rabatt, wenn du mindestens drei Termine im selben Monat buchst. Bereits bezahlte Einzeltermine zählen dafür nicht nachträglich mit.
```

Review notes: States when the discount is received but no longer explicitly makes that condition necessary. / Dropping “only” changes the logical force of the eligibility condition.

### lite: pass

```text
Der Rabatt von 15 % gilt nur, wenn mindestens drei Termine im selben Monat gebucht werden. Bereits bezahlte Einzeltermine werden dafür nicht rückwirkend zusammengerechnet.
```

### full: pass

```text
15 % Rabatt gibt es nur, wenn mindestens drei Termine im selben Monat gebucht werden. Bereits bezahlte Einzeltermine werden dafür nicht rückwirkend zusammengerechnet.
```

### ultra: pass

```text
15 % Rabatt gibt es nur bei Buchung von mindestens drei Terminen im selben Monat. Bereits bezahlte Einzeltermine zählen nicht rückwirkend dazu.
```

### off: pass

```text
Der Rabatt von 15 % gilt nur, wenn mindestens drei Termine im selben Monat gebucht werden. Bereits bezahlte Einzeltermine werden dafür nicht nachträglich zusammengerechnet.
```

## modes-de-025 · negation

Source task:

> Schreibe klarer: „Noch nicht geprüft“ heißt weder „sicher“ noch „unsicher“. Das Etikett beschreibt ausschließlich den fehlenden Prüfstatus. Bis zur Prüfung darf das Gerät nicht ausgeliehen werden.

### baseline: pass

```text
„Noch nicht geprüft“ bedeutet nur, dass das Gerät bisher nicht geprüft wurde. Es sagt nichts darüber aus, ob das Gerät sicher oder unsicher ist. Bis zur Prüfung darf es nicht ausgeliehen werden.
```

### lite: pass

```text
„Noch nicht geprüft“ bedeutet weder „sicher“ noch „unsicher“. Das Etikett sagt nur aus, dass die Prüfung fehlt. Bis zur Prüfung darf das Gerät nicht ausgeliehen werden.
```

### full: pass

```text
„Noch nicht geprüft“ bedeutet weder „sicher“ noch „unsicher“. Das Etikett sagt nur, dass die Prüfung fehlt. Bis zur Prüfung darf das Gerät nicht ausgeliehen werden.
```

### ultra: pass

```text
„Noch nicht geprüft“ beschreibt nur den fehlenden Prüfstatus, nicht, ob das Gerät sicher oder unsicher ist. Bis zur Prüfung darf es nicht ausgeliehen werden.
```

### off: pass

```text
„Noch nicht geprüft“ bedeutet nur, dass das Gerät bisher nicht geprüft wurde. Das Etikett sagt nicht aus, ob es sicher oder unsicher ist. Bis zur Prüfung darf das Gerät nicht ausgeliehen werden.
```

## modes-de-026 · unknown_actor

Source task:

> Überarbeite die Chronologie: Um 15 Uhr gab Fatma den Schlüssel zurück. Um 15:20 Uhr wurde der Schrank geöffnet. Um 16 Uhr überprüfte Paul den Inhalt. Wer den Schrank geöffnet hat, wurde nicht dokumentiert.

### baseline: pass

```text
Um 15 Uhr gab Fatma den Schlüssel zurück. Um 15:20 Uhr wurde der Schrank geöffnet; wer ihn öffnete, wurde nicht dokumentiert. Um 16 Uhr überprüfte Paul den Inhalt.
```

### lite: pass

```text
Um 15 Uhr gab Fatma den Schlüssel zurück. Um 15:20 Uhr wurde der Schrank geöffnet. Wer ihn öffnete, wurde nicht dokumentiert. Um 16 Uhr überprüfte Paul den Inhalt.
```

### full: pass

```text
Um 15 Uhr gab Fatma den Schlüssel zurück. Um 15:20 Uhr wurde der Schrank geöffnet; wer ihn öffnete, wurde nicht dokumentiert. Um 16 Uhr überprüfte Paul den Inhalt.
```

### ultra: pass

```text
Um 15 Uhr gab Fatma den Schlüssel zurück. Um 15:20 Uhr wurde der Schrank geöffnet; von wem, wurde nicht dokumentiert. Um 16 Uhr überprüfte Paul den Inhalt.
```

### off: pass

```text
Um 15:00 Uhr gab Fatma den Schlüssel zurück. Um 15:20 Uhr wurde der Schrank geöffnet; wer ihn öffnete, wurde nicht dokumentiert. Um 16:00 Uhr überprüfte Paul den Inhalt.
```

## modes-de-027 · uncertainty

Source task:

> Fasse zusammen: Drei von zehn geprüften Akkus hielten weniger als zwei Stunden. Die übrigen 25 Akkus wurden noch nicht geprüft. Aus diesem Ergebnis kann kein Ausfallanteil für den gesamten Bestand angegeben werden.

### baseline: pass

```text
Drei der zehn geprüften Akkus hielten weniger als zwei Stunden. Die übrigen 25 Akkus sind noch ungeprüft; ein Ausfallanteil für den gesamten Bestand lässt sich daher nicht angeben.
```

### lite: pass

```text
Drei von zehn geprüften Akkus hielten weniger als zwei Stunden. Die übrigen 25 Akkus sind noch ungeprüft. Daraus lässt sich kein Ausfallanteil für den gesamten Bestand ableiten.
```

### full: pass

```text
Drei von zehn geprüften Akkus hielten weniger als zwei Stunden. Die übrigen 25 Akkus sind noch ungeprüft. Daraus lässt sich kein Ausfallanteil für den gesamten Bestand angeben.
```

### ultra: pass

```text
Drei von zehn geprüften Akkus hielten weniger als zwei Stunden. Die übrigen 25 sind ungeprüft. Daraus lässt sich kein Ausfallanteil für den gesamten Bestand ableiten.
```

### off: pass

```text
Drei der zehn geprüften Akkus hielten weniger als zwei Stunden. Die übrigen 25 Akkus sind noch ungeprüft. Ein Ausfallanteil für den gesamten Bestand lässt sich daraus nicht ableiten.
```

## modes-de-028 · numbers_units

Source task:

> Formuliere direkt: Der Vorratsbehälter fasst 1,2 Liter. Die Markierung bei 1 Liter bezeichnet die empfohlene Füllmenge, nicht das Gesamtvolumen. Diese Angabe gehört zum Musterbehälter.

### baseline: pass

```text
Der Musterbehälter fasst insgesamt 1,2 Liter. Die 1-Liter-Markierung zeigt die empfohlene Füllmenge, nicht das Gesamtvolumen.
```

### lite: pass

```text
Der Vorratsbehälter fasst 1,2 Liter. Die 1-Liter-Markierung zeigt die empfohlene Füllmenge, nicht das Gesamtvolumen. Diese Angabe gilt für den Musterbehälter.
```

### full: pass

```text
Der Musterbehälter fasst 1,2 Liter. Die Markierung bei 1 Liter zeigt die empfohlene Füllmenge, nicht das Gesamtvolumen.
```

### ultra: pass

```text
Der Musterbehälter fasst 1,2 Liter. Die 1-Liter-Markierung zeigt die empfohlene Füllmenge, nicht das Gesamtvolumen.
```

### off: pass

```text
Der Musterbehälter fasst insgesamt 1,2 Liter. Die Markierung bei 1 Liter zeigt die empfohlene Füllmenge an, nicht das Gesamtvolumen.
```

## modes-de-029 · calculation

Source task:

> Eine Werkstatt öffnet von 8:35 bis 12:10 und von 13:00 bis 16:25. Wie lange ist sie insgesamt geöffnet? Die Mittagspause zählt nicht.

### baseline: pass

```text
Die Werkstatt ist insgesamt 7 Stunden geöffnet: vormittags 3 Stunden 35 Minuten und nachmittags 3 Stunden 25 Minuten.
```

### lite: pass

```text
Die Werkstatt ist insgesamt 7 Stunden geöffnet: vormittags 3 Stunden 35 Minuten und nachmittags 3 Stunden 25 Minuten. Die Mittagspause ist nicht mitgerechnet.
```

### full: pass

```text
Die Werkstatt ist insgesamt 7 Stunden geöffnet: vormittags 3 Stunden 35 Minuten und nachmittags 3 Stunden 25 Minuten. Die Mittagspause zählt nicht mit.
```

### ultra: pass

```text
Die Werkstatt ist insgesamt 7 Stunden geöffnet: vormittags 3 Stunden 35 Minuten, nachmittags 3 Stunden 25 Minuten. Die Mittagspause ist nicht mitgerechnet.
```

### off: pass

```text
Die Werkstatt ist insgesamt 7 Stunden geöffnet: vormittags 3 Stunden und 35 Minuten, nachmittags 3 Stunden und 25 Minuten. Die Mittagspause ist nicht mitgerechnet.
```

## modes-de-030 · sampling

Source task:

> Überarbeite die Schlussfolgerung: Die 16 befragten Personen empfehlen einen Onlinekurs. Alle wurden aus einer Liste früherer Onlinekursteilnehmender ausgewählt. Menschen ohne Onlinekurserfahrung wurden nicht befragt.

### baseline: pass

```text
Die 16 Befragten empfehlen einen Onlinekurs. Da alle aus einer Liste früherer Onlinekursteilnehmender ausgewählt wurden, lässt sich das Ergebnis nicht auf Menschen ohne Onlinekurserfahrung übertragen. Diese wurden nicht befragt.
```

### lite: pass

```text
Die 16 befragten Personen empfehlen einen Onlinekurs. Alle wurden aus einer Liste früherer Onlinekursteilnehmender ausgewählt. Menschen ohne Onlinekurserfahrung wurden nicht befragt.
```

### full: pass

```text
Die 16 befragten Personen empfehlen einen Onlinekurs. Alle wurden aus einer Liste früherer Onlinekursteilnehmender ausgewählt. Menschen ohne Onlinekurserfahrung wurden nicht befragt; über ihre Empfehlung lässt sich daher keine Aussage treffen.
```

### ultra: pass

```text
Alle 16 Befragten empfehlen einen Onlinekurs. Sie wurden ausschließlich aus einer Liste früherer Onlinekursteilnehmender ausgewählt. Menschen ohne Onlinekurserfahrung wurden nicht befragt.
```

### off: pass

```text
Die 16 befragten Personen empfehlen einen Onlinekurs. Sie wurden jedoch alle aus einer Liste früherer Onlinekursteilnehmender ausgewählt. Menschen ohne Onlinekurserfahrung wurden nicht befragt; über deren Empfehlung lässt sich daher keine Aussage treffen.
```

## modes-de-031 · summary

Source task:

> Schreibe eine kurze Übergabe: Lotte hat die Regale beschriftet, die Schubladen aber noch nicht. Die Liste der fehlenden Schilder liegt im roten Ordner. Die Druckdatei wurde gespeichert; wer sie gespeichert hat, ist unbekannt.

### baseline: flagged

```text
Lotte hat die Regale beschriftet; die Schubladen fehlen noch. Die Liste der fehlenden Schilder liegt im roten Ordner. Die Druckdatei ist gespeichert, aber von wem, ist unbekannt.
```

Review notes: The drawer wording introduces material ambiguity about what remains unfinished. / Die ausstehende Schubladenbeschriftung wird materiell mehrdeutig beschrieben.

### lite: pass

```text
Lotte hat die Regale beschriftet, die Schubladen noch nicht. Die Liste der fehlenden Schilder liegt im roten Ordner. Die Druckdatei wurde gespeichert; von wem, ist unbekannt.
```

### full: pass

```text
Lotte hat die Regale beschriftet, die Schubladen noch nicht. Die Liste der fehlenden Schilder liegt im roten Ordner. Die Druckdatei wurde gespeichert; von wem, ist unbekannt.
```

### ultra: flagged

```text
Lotte hat die Regale beschriftet; die Schubladen fehlen noch. Die Liste der fehlenden Schilder liegt im roten Ordner. Die Druckdatei ist gespeichert; von wem, ist unbekannt.
```

Review notes: The drawer wording could incorrectly communicate missing drawers. / Die ausstehende Schubladenbeschriftung wird materiell mehrdeutig beschrieben.

### off: pass

```text
Lotte hat die Regale beschriftet; die Schubladen sind noch nicht beschriftet. Die Liste der fehlenden Schilder liegt im roten Ordner. Die Druckdatei wurde gespeichert, aber es ist unbekannt, von wem.
```

## modes-de-032 · analysis

Source task:

> Welche Kombination ist für genau 48 Becher günstiger? Paket X enthält 16 Becher und kostet 12 €; Paket Y enthält 24 und kostet 19 €. Einzelbecher sind nicht erhältlich. Rechne beide Möglichkeiten aus.

### baseline: pass

```text
3 Pakete X: 3 × 16 = 48 Becher für 3 × 12 € = 36 €.
2 Pakete Y: 2 × 24 = 48 Becher für 2 × 19 € = 38 €.
Damit sind 3 Pakete X um 2 € günstiger.
```

### lite: pass

```text
Paket X ist für genau 48 Becher günstiger:
- 3 × Paket X: 3 × 16 = 48 Becher für 3 × 12 € = 36 €.
- 2 × Paket Y: 2 × 24 = 48 Becher für 2 × 19 € = 38 €.
Mit Paket X spart ihr 2 €.
```

### full: pass

```text
Für genau 48 Becher ist Paket X günstiger:
- 3 × Paket X: 3 × 16 = 48 Becher; 3 × 12 € = 36 €.
- 2 × Paket Y: 2 × 24 = 48 Becher; 2 × 19 € = 38 €.

Paket X spart 2 €. Eine Mischung beider Pakete ergibt nicht genau 48 Becher; Einzelbecher sind nicht erhältlich.
```

### ultra: pass

```text
Für genau 48 Becher ist Paket X günstiger:
- 3 × Paket X: 48 Becher für 36 €.
- 2 × Paket Y: 48 Becher für 38 €.

Paket X spart 2 €. Eine Mischung ergibt nicht genau 48 Becher; Einzelbecher sind nicht erhältlich.
```

### off: pass

```text
3 Pakete X: 3 × 16 = 48 Becher für 3 × 12 € = 36 €.
2 Pakete Y: 2 × 24 = 48 Becher für 2 × 19 € = 38 €.
Damit sind 3 Pakete X um 2 € günstiger. Eine Mischung aus X und Y ergibt nicht genau 48 Becher.
```

## modes-de-033 · conflicting_notes

Source task:

> Fasse für die Organisation zusammen: Die Einladung nennt Raum Blau, der Kalender nennt Raum Grün. Beide nennen den 6. Februar um 14 Uhr. Die Raumverwaltung hat bisher keinen der Räume bestätigt.

### baseline: flagged

```text
Termin: 6. Februar, 14 Uhr. Der Raum ist ungeklärt: Die Einladung nennt Raum Blau, der Kalender Raum Grün. Die Raumverwaltung hat bisher keinen der beiden Räume bestätigt.
```

Review notes: Preserves the common appointment and unresolved room conflict in summary form. / Datum und Uhrzeit stimmen, aber ihre Übereinstimmung in beiden Quellen fehlt.

### lite: pass

```text
Der Termin ist in Einladung und Kalender mit dem 6. Februar um 14 Uhr angegeben. Beim Raum gibt es einen Widerspruch: Die Einladung nennt Raum Blau, der Kalender Raum Grün. Die Raumverwaltung hat bisher keinen der Räume bestätigt.
```

### full: pass

```text
Der Termin ist in Einladung und Kalender mit dem 6. Februar um 14 Uhr angegeben. Der Raum ist unklar: Die Einladung nennt Raum Blau, der Kalender Raum Grün. Die Raumverwaltung hat bisher keinen der Räume bestätigt.
```

### ultra: flagged

```text
Termin: 6. Februar, 14 Uhr. Der Raum ist ungeklärt: Die Einladung nennt Raum Blau, der Kalender Raum Grün. Die Raumverwaltung hat bisher keinen bestätigt.
```

Review notes: Compact summary accurately distinguishes the shared appointment from the unresolved room. / Datum und Uhrzeit stimmen, aber ihre Übereinstimmung in beiden Quellen fehlt.

### off: pass

```text
Der Termin ist in Einladung und Kalender für den 6. Februar um 14 Uhr angegeben. Beim Raum gibt es einen Widerspruch: Die Einladung nennt Raum Blau, der Kalender Raum Grün. Die Raumverwaltung hat bisher keinen der beiden Räume bestätigt.
```

## modes-de-034 · voice

Source task:

> Mach den Text kürzer, aber behalte den leichten Humor: Unser Kopierer hat heute beschlossen, nur halbe Seiten zu liefern. Bis er wieder ganze Geschichten mag, nutzt bitte den Drucker im Nebenraum. Eine Reparaturzeit kennen wir noch nicht.

### baseline: pass

```text
Der Kopierer erzählt heute nur halbe Geschichten. Bitte nutzt den Drucker im Nebenraum. Wann er wieder ganze Seiten liefert, ist noch unklar.
```

### lite: pass

```text
Unser Kopierer liefert heute nur halbe Seiten. Bis er wieder ganze Geschichten mag, nutzt bitte den Drucker im Nebenraum. Eine Reparaturzeit kennen wir noch nicht.
```

### full: pass

```text
Unser Kopierer liefert heute nur halbe Geschichten. Nutzt bitte den Drucker im Nebenraum, bis er wieder ganze Seiten mag. Die Reparaturzeit ist noch unbekannt.
```

### ultra: pass

```text
Unser Kopierer liefert heute nur halbe Geschichten. Nutzt bitte den Drucker im Nebenraum, bis er wieder ganze Seiten mag. Die Reparaturzeit ist noch unbekannt.
```

### off: pass

```text
Unser Kopierer liefert heute nur halbe Geschichten. Nutzt bitte den Drucker im Nebenraum, bis er wieder ganze Seiten mag. Eine Reparaturzeit kennen wir noch nicht.
```

## modes-de-035 · scope

Source task:

> Welche Unterlage fehlt? Antworte in einem Satz. Im Paket liegen ein unterschriebenes Formular und die Rechnung. Erforderlich sind außerdem ein Foto des Gegenstands und, nur bei Versand ins Ausland, eine Zollerklärung. Das Paket wird im Inland verschickt.

### baseline: pass

```text
Es fehlt ein Foto des Gegenstands; eine Zollerklärung ist beim Inlandsversand nicht erforderlich.
```

### lite: pass

```text
Es fehlt ein Foto des Gegenstands; eine Zollerklärung ist beim Versand im Inland nicht erforderlich.
```

### full: pass

```text
Es fehlt ein Foto des Gegenstands; eine Zollerklärung ist beim Versand im Inland nicht erforderlich.
```

### ultra: pass

```text
Es fehlt ein Foto des Gegenstands; eine Zollerklärung ist beim Inlandsversand nicht erforderlich.
```

### off: pass

```text
Es fehlt ein Foto des Gegenstands; eine Zollerklärung ist beim Versand im Inland nicht erforderlich.
```

## modes-de-036 · ambiguity

Source task:

> Überarbeite diese Notiz, ohne die Uhrzeit umzudeuten: „Treffen um 7; morgens oder abends ist noch nicht geklärt.“ Erhalte die Unklarheit und fordere ihre Klärung statt eine Zeit festzulegen.

### baseline: pass

```text
Das Treffen ist um 7 Uhr. Bitte klären, ob morgens oder abends gemeint ist.
```

### lite: pass

```text
Treffen um 7 Uhr. Ob morgens oder abends, ist noch unklar. Bitte klären.
```

### full: pass

```text
Treffen um 7 Uhr. Ob morgens oder abends, ist noch offen. Bitte klären.
```

### ultra: pass

```text
Treffen um 7. Bitte klären, ob morgens oder abends gemeint ist.
```

### off: pass

```text
Treffen um 7 Uhr. Ob morgens oder abends, ist noch offen. Bitte klären, welche Tageszeit gemeint ist.
```

## modes-de-037 · technical

Source task:

> Erkläre den Ablauf kurz: Vor export_notes --format csv muss notes.db kopiert werden. Die Exportdatei enthält nur freigegebene Notizen. Ein leerer Export bedeutet nicht, dass die Datenbank leer ist.

### baseline: pass

```text
Kopiere zuerst notes.db und führe danach export_notes --format csv aus. Die Exportdatei enthält nur freigegebene Notizen. Ein leerer Export bedeutet daher nicht, dass die Datenbank leer ist.
```

### lite: pass

```text
Vor dem Aufruf von export_notes --format csv muss notes.db kopiert werden. Die Exportdatei enthält nur freigegebene Notizen. Ein leerer Export bedeutet nicht, dass die Datenbank leer ist.
```

### full: pass

```text
Kopiere zuerst notes.db. Führe danach export_notes --format csv aus. Die Exportdatei enthält nur freigegebene Notizen. Ein leerer Export bedeutet daher nicht, dass die Datenbank leer ist.
```

### ultra: pass

```text
Zuerst notes.db kopieren, dann export_notes --format csv ausführen. Der Export enthält nur freigegebene Notizen. Ein leerer Export bedeutet nicht, dass die Datenbank leer ist.
```

### off: pass

```text
Kopiere zuerst notes.db und führe danach export_notes --format csv aus. Die Exportdatei enthält nur freigegebene Notizen. Ein leerer Export bedeutet daher nicht, dass die Datenbank leer ist.
```

## modes-de-038 · technical

Source task:

> Schreibe verständlicher: flag=preview zeigt die geplanten Änderungen an. Sie werden erst mit apply=true gespeichert. Ein Aufruf mit flag=preview allein ändert den Bestand nicht.

### baseline: pass

```text
flag=preview zeigt die geplanten Änderungen nur an und verändert den Bestand nicht. Erst mit apply=true werden die Änderungen gespeichert.
```

### lite: pass

```text
flag=preview zeigt die geplanten Änderungen an. Erst mit apply=true werden sie gespeichert. Ein Aufruf nur mit flag=preview ändert den Bestand nicht.
```

### full: pass

```text
flag=preview zeigt die geplanten Änderungen an, ohne den Bestand zu ändern. Die Änderungen werden erst mit apply=true gespeichert.
```

### ultra: pass

```text
flag=preview zeigt geplante Änderungen nur an und ändert den Bestand nicht. Erst mit apply=true werden die Änderungen gespeichert.
```

### off: pass

```text
flag=preview zeigt die geplanten Änderungen an, speichert sie aber nicht. Erst mit apply=true werden die Änderungen gespeichert. Ein Aufruf nur mit flag=preview lässt den Bestand unverändert.
```

## modes-de-039 · exceptions

Source task:

> Mache diese Regel klarer: Pro Stand sind zwei Personen zugelassen. Eine dritte Person darf nur beim Aufbau helfen und muss vor Beginn des Verkaufs gehen. Die Ausnahme gilt nicht für die Verkaufszeit.

### baseline: pass

```text
Pro Stand sind höchstens zwei Personen zugelassen. Eine dritte Person darf ausschließlich beim Aufbau helfen und muss vor Verkaufsbeginn gehen. Während der Verkaufszeit gilt diese Ausnahme nicht.
```

### lite: pass

```text
Pro Stand sind zwei Personen zugelassen. Eine dritte Person darf nur beim Aufbau helfen und muss vor Verkaufsbeginn gehen. Während der Verkaufszeit gilt diese Ausnahme nicht.
```

### full: pass

```text
Pro Stand sind zwei Personen zugelassen. Eine dritte Person darf nur beim Aufbau helfen und muss vor Verkaufsbeginn gehen. Während des Verkaufs gilt diese Ausnahme nicht.
```

### ultra: pass

```text
Pro Stand sind zwei Personen zugelassen. Eine dritte Person darf nur beim Aufbau helfen und muss vor Verkaufsbeginn gehen. Während des Verkaufs gilt diese Ausnahme nicht.
```

### off: pass

```text
Pro Stand sind zwei Personen zugelassen. Nur beim Aufbau darf eine dritte Person helfen. Sie muss vor Beginn des Verkaufs gehen; während der Verkaufszeit gilt diese Ausnahme nicht.
```

## modes-de-040 · conditions

Source task:

> Formuliere eine kurze Anweisung: Die Abdeckung darf erst nach dem Ausschalten und Abkühlen geöffnet werden. Ausschalten allein reicht nicht aus. Die Abkühlung ist abzuwarten, auch wenn nur nachgesehen werden soll.

### baseline: pass

```text
Schalte das Gerät aus und warte, bis es abgekühlt ist. Öffne erst dann die Abdeckung – auch wenn du nur nachsehen möchtest. Ausschalten allein reicht nicht aus.
```

### lite: pass

```text
Öffnen Sie die Abdeckung erst nach dem Ausschalten und Abkühlen. Ausschalten allein reicht nicht: Warten Sie die Abkühlung auch dann ab, wenn Sie nur nachsehen möchten.
```

### full: pass

```text
Schalte das Gerät aus und warte, bis es abgekühlt ist. Öffne erst dann die Abdeckung – auch wenn du nur nachsehen möchtest. Ausschalten allein reicht nicht aus.
```

### ultra: pass

```text
Vor dem Öffnen der Abdeckung ausschalten und die Abkühlung abwarten. Ausschalten allein reicht nicht – auch dann nicht, wenn Sie nur nachsehen möchten.
```

### off: pass

```text
Schalte das Gerät aus und warte, bis es abgekühlt ist. Öffne erst dann die Abdeckung. Ausschalten allein reicht nicht aus – auch wenn du nur nachsehen möchtest, musst du die Abkühlung abwarten.
```

## modes-de-041 · denominators

Source task:

> Korrigiere die Aussage „Jeder zweite Kunde wollte die lange Öffnungszeit“. Tatsächlich wählten 15 von 30 Personen, die den freiwilligen Fragebogen zurückgaben, diese Option. 200 Fragebögen wurden ausgegeben.

### baseline: pass

```text
15 von 30 Personen, die den freiwilligen Fragebogen zurückgaben, wählten die lange Öffnungszeit. Das ist die Hälfte der Antwortenden, nicht aller Kunden. Insgesamt wurden 200 Fragebögen ausgegeben.
```

### lite: pass

```text
15 von 30 Personen, die den freiwilligen Fragebogen zurückgaben, wählten die lange Öffnungszeit. Insgesamt wurden 200 Fragebögen ausgegeben. Daraus lässt sich nicht ableiten, dass jeder zweite Kunde die lange Öffnungszeit wollte.
```

### full: pass

```text
15 von 30 Personen, die den freiwilligen Fragebogen zurückgaben, wählten die lange Öffnungszeit. Insgesamt wurden 200 Fragebögen ausgegeben. Daraus lässt sich nicht ableiten, dass jeder zweite Kunde die lange Öffnungszeit wollte.
```

### ultra: pass

```text
15 von 30 Personen, die den freiwilligen Fragebogen zurückgaben, wählten die lange Öffnungszeit. Ausgegeben wurden 200 Fragebögen. Das belegt nicht, dass jeder zweite Kunde sie wollte.
```

### off: pass

```text
15 von 30 Personen, die den freiwilligen Fragebogen zurückgaben, wählten die lange Öffnungszeit. Insgesamt wurden 200 Fragebögen ausgegeben. Daraus lässt sich nicht ableiten, dass jeder zweite Kunde die lange Öffnungszeit wollte.
```

## modes-de-042 · estimates

Source task:

> Kürze: Die Montage könnte 420 € kosten, wenn die vorhandenen Halterungen wiederverwendet werden können. Bestätigt sind nur 85 € für die Begutachtung. Ob neue Halterungen gebraucht werden, steht noch nicht fest.

### baseline: pass

```text
Bestätigt sind 85 € für die Begutachtung. Die Montage könnte 420 € kosten, falls die vorhandenen Halterungen wiederverwendbar sind. Ob neue nötig sind, ist offen.
```

### lite: pass

```text
Die Montage könnte 420 € kosten, wenn die vorhandenen Halterungen wiederverwendbar sind. Bestätigt sind nur 85 € für die Begutachtung. Ob neue Halterungen nötig sind, ist offen.
```

### full: pass

```text
Bestätigt sind nur 85 € für die Begutachtung. Die Montage könnte 420 € kosten, wenn die vorhandenen Halterungen wiederverwendbar sind. Ob neue nötig sind, ist noch offen.
```

### ultra: pass

```text
Die Montage könnte 420 € kosten, sofern die vorhandenen Halterungen wiederverwendbar sind. Bestätigt sind nur 85 € für die Begutachtung. Ob neue Halterungen nötig sind, ist offen.
```

### off: pass

```text
Die Montage könnte 420 € kosten, sofern die vorhandenen Halterungen wiederverwendbar sind. Bestätigt sind nur 85 € für die Begutachtung. Ob neue Halterungen nötig sind, ist offen.
```

## modes-de-043 · percentage_points

Source task:

> Ein fiktiver Anteil sinkt von 18 % auf 11 %. Wie viele Prozentpunkte sind das? Gib keine relative Veränderung an.

### baseline: pass

```text
Der Anteil sinkt um 7 Prozentpunkte.
```

### lite: pass

```text
Der Anteil sinkt um 7 Prozentpunkte.
```

### full: pass

```text
Der Anteil sinkt um 7 Prozentpunkte.
```

### ultra: pass

```text
Der Anteil sinkt um 7 Prozentpunkte.
```

### off: pass

```text
Der Anteil sinkt um 7 Prozentpunkte.
```

## modes-de-044 · calculation

Source task:

> Für 5 Dekorationen benötigt eine Gruppe 350 cm Band. Wie viel Band braucht sie für 8 Dekorationen bei gleichem Verbrauch? Rechne in Zentimetern.

### baseline: pass

```text
350 cm ÷ 5 × 8 = 560 cm Band.
```

### lite: pass

```text
350 cm ÷ 5 × 8 = 560 cm. Die Gruppe braucht 560 cm Band.
```

### full: pass

```text
350 cm ÷ 5 × 8 = 560 cm Band.
```

### ultra: pass

```text
350 cm ÷ 5 × 8 = 560 cm Band.
```

### off: pass

```text
350 cm ÷ 5 × 8 = 560 cm Band.
```

## modes-de-045 · summary

Source task:

> Fasse die Änderung zusammen: Ab 15. Juli werden Reparaturaufträge am Seiteneingang angenommen. Die Abholung bleibt an der Haupttheke. Bereits vereinbarte Abgabetermine ab dem 15. Juli nutzen ebenfalls den Seiteneingang.

### baseline: pass

```text
Ab 15. Juli werden Reparaturaufträge am Seiteneingang angenommen, auch bei bereits vereinbarten Abgabeterminen ab diesem Datum. Die Abholung bleibt an der Haupttheke.
```

### lite: pass

```text
Ab 15. Juli werden Reparaturaufträge am Seiteneingang angenommen. Das gilt auch für bereits vereinbarte Abgabetermine ab diesem Datum. Die Abholung bleibt an der Haupttheke.
```

### full: pass

```text
Ab 15. Juli werden Reparaturaufträge am Seiteneingang angenommen, auch bei bereits vereinbarten Abgabeterminen ab diesem Datum. Die Abholung bleibt an der Haupttheke.
```

### ultra: pass

```text
Ab 15. Juli werden Reparaturaufträge am Seiteneingang angenommen, auch bei bereits vereinbarten Abgabeterminen ab diesem Datum. Die Abholung bleibt an der Haupttheke.
```

### off: pass

```text
Ab 15. Juli werden Reparaturaufträge am Seiteneingang angenommen, auch bei bereits vereinbarten Abgabeterminen ab diesem Datum. Die Abholung bleibt an der Haupttheke.
```

## modes-de-046 · permissions

Source task:

> Vereinfache diese fiktive Vertragsklausel ohne Rechtsberatung: Die nutzende Person darf die Leihe jederzeit beenden. Sie muss den Gegenstand binnen drei Tagen zurückgeben. Eine frühere Rückgabe begründet keinen Anspruch auf Erstattung bereits bezahlter Nutzungstage.

### baseline: pass

```text
Sie können die Leihe jederzeit beenden. Danach müssen Sie den Gegenstand innerhalb von drei Tagen zurückgeben. Wenn Sie ihn früher zurückgeben, haben Sie keinen Anspruch auf eine Erstattung für bereits bezahlte Nutzungstage.
```

### lite: pass

```text
Die nutzende Person darf die Leihe jederzeit beenden. Sie muss den Gegenstand innerhalb von drei Tagen zurückgeben. Bei einer früheren Rückgabe besteht kein Anspruch auf Erstattung bereits bezahlter Nutzungstage.
```

### full: pass

```text
Die nutzende Person darf die Leihe jederzeit beenden. Sie muss den Gegenstand innerhalb von drei Tagen zurückgeben. Bei einer früheren Rückgabe besteht kein Anspruch auf Erstattung bereits bezahlter Nutzungstage.
```

### ultra: pass

```text
Die nutzende Person darf die Leihe jederzeit beenden. Sie muss den Gegenstand innerhalb von drei Tagen zurückgeben. Bei früherer Rückgabe besteht kein Anspruch auf Erstattung bereits bezahlter Nutzungstage.
```

### off: pass

```text
Die nutzende Person darf die Leihe jederzeit beenden. Danach muss sie den Gegenstand innerhalb von drei Tagen zurückgeben. Gibt sie ihn früher zurück, hat sie keinen Anspruch auf Erstattung bereits bezahlter Nutzungstage.
```

## modes-de-047 · unknown_actor

Source task:

> Schreibe verständlicher: Die Freigabe wurde erteilt, bevor Sven die Prüfung übernahm. Sven dokumentierte später nur den aktuellen Zustand. Die freigebende Person wird nicht genannt.

### baseline: pass

```text
Die Freigabe erfolgte, bevor Sven die Prüfung übernahm. Später hielt Sven nur den aktuellen Zustand fest. Wer die Freigabe erteilt hat, wird nicht genannt.
```

### lite: pass

```text
Die Freigabe wurde erteilt, bevor Sven die Prüfung übernahm. Später dokumentierte Sven nur den aktuellen Zustand. Wer die Freigabe erteilt hat, wird nicht genannt.
```

### full: pass

```text
Die Freigabe wurde erteilt, bevor Sven die Prüfung übernahm. Wer die Freigabe erteilte, wird nicht genannt. Sven dokumentierte später nur den aktuellen Zustand.
```

### ultra: pass

```text
Die Freigabe erfolgte, bevor Sven die Prüfung übernahm. Später dokumentierte Sven nur den aktuellen Zustand. Wer die Freigabe erteilte, wird nicht genannt.
```

### off: pass

```text
Die Freigabe wurde erteilt, bevor Sven die Prüfung übernahm. Später dokumentierte Sven lediglich den aktuellen Zustand. Wer die Freigabe erteilt hat, wird nicht genannt.
```

## modes-de-048 · analysis

Source task:

> Warum ist „kein Fehler in den gespeicherten Protokollen“ präziser als „kein Fehler im gesamten Betrieb“? In diesem fiktiven Fall wurden Protokolle nur an Werktagen gespeichert.

### baseline: pass

```text
„Kein Fehler in den gespeicherten Protokollen“ beschränkt die Aussage auf die vorhandenen Aufzeichnungen. Da nur an Werktagen Protokolle gespeichert wurden, lässt sich daraus nicht schließen, dass es im gesamten Betrieb keine Fehler gab.
```

### lite: pass

```text
„Kein Fehler in den gespeicherten Protokollen“ beschränkt die Aussage auf die vorhandenen Aufzeichnungen. Da nur an Werktagen Protokolle gespeichert wurden, lässt sich daraus nicht schließen, dass es auch an anderen Tagen keine Fehler gab. „Kein Fehler im gesamten Betrieb“ geht daher über die belegte Aussage hinaus.
```

### full: pass

```text
„Kein Fehler in den gespeicherten Protokollen“ beschränkt die Aussage auf die vorhandenen Aufzeichnungen. Da nur an Werktagen Protokolle gespeichert wurden, lässt sich daraus nicht schließen, dass es im gesamten Betrieb keine Fehler gab. Für die übrigen Tage fehlen Protokolle.
```

### ultra: pass

```text
„Kein Fehler in den gespeicherten Protokollen“ beschränkt die Aussage auf die vorhandenen Aufzeichnungen. Da nur an Werktagen Protokolle gespeichert wurden, lässt sich daraus nicht schließen, dass im gesamten Betrieb kein Fehler auftrat.
```

### off: pass

```text
„Kein Fehler in den gespeicherten Protokollen“ beschränkt die Aussage auf die vorhandenen Aufzeichnungen. Da nur an Werktagen Protokolle gespeichert wurden, lässt sich daraus nicht schließen, dass auch an den übrigen Tagen keine Fehler auftraten. „Kein Fehler im gesamten Betrieb“ geht daher über das hinaus, was die Protokolle belegen können.
```

## modes-de-049 · negation

Source task:

> Überarbeite: Sie sollen nicht alle Anhänge erneut senden. Es fehlt nur die Rückseite des Ausweises. Die bereits eingegangenen Dateien müssen nicht ersetzt werden.

### baseline: pass

```text
Bitte senden Sie nur noch die Rückseite des Ausweises. Die anderen Dateien sind bereits eingegangen und müssen nicht erneut gesendet oder ersetzt werden.
```

### lite: pass

```text
Sie sollen nicht alle Anhänge erneut senden. Es fehlt nur die Rückseite des Ausweises. Die bereits eingegangenen Dateien müssen nicht ersetzt werden.
```

### full: pass

```text
Bitte senden Sie nur die fehlende Rückseite des Ausweises. Sie müssen nicht alle Anhänge erneut senden oder die bereits eingegangenen Dateien ersetzen.
```

### ultra: pass

```text
Bitte senden Sie nur die fehlende Rückseite des Ausweises nach. Bereits eingegangene Dateien müssen Sie nicht ersetzen.
```

### off: pass

```text
Bitte senden Sie nur die fehlende Rückseite des Ausweises nach, nicht alle Anhänge erneut. Die bereits eingegangenen Dateien müssen Sie nicht ersetzen.
```

## modes-de-050 · voice

Source task:

> Schreibe eine höfliche kurze Absage an eine Einladung. Verwende nur diese Fakten: Ich kann am Samstag nicht kommen; ich möchte keine Begründung nennen; ich wünsche der Gruppe einen schönen Abend. Erfinde keinen Ersatztermin.

### baseline: pass

```text
Leider kann ich am Samstag nicht kommen. Ich wünsche euch einen schönen Abend!
```

### lite: pass

```text
Leider kann ich am Samstag nicht kommen. Ich wünsche euch einen schönen Abend!
```

### full: pass

```text
Vielen Dank für die Einladung. Leider kann ich am Samstag nicht kommen. Ich wünsche euch einen schönen Abend!
```

### ultra: pass

```text
Leider kann ich am Samstag nicht kommen. Ich wünsche euch einen schönen Abend!
```

### off: pass

```text
Leider kann ich am Samstag nicht kommen. Ich wünsche euch einen schönen Abend!
```

## modes-de-051 · ambiguity

Source task:

> Erkläre den Unterschied zwischen „Die Datei darf gelöscht werden“ und „Die Datei muss gelöscht werden“. Beschreibe nur die sprachliche Bedeutung und leite keine Handlung für eine reale Datei ab.

### baseline: pass

```text
„Die Datei darf gelöscht werden“ drückt eine Erlaubnis aus, keine Verpflichtung. „Die Datei muss gelöscht werden“ drückt dagegen eine Verpflichtung oder Notwendigkeit aus.
```

### lite: pass

```text
„Die Datei darf gelöscht werden“ drückt eine Erlaubnis aus, keine Pflicht. „Die Datei muss gelöscht werden“ drückt eine Pflicht aus.
```

### full: pass

```text
„Die Datei darf gelöscht werden“ bedeutet, dass das Löschen erlaubt ist, aber nicht verlangt wird. „Die Datei muss gelöscht werden“ bedeutet, dass das Löschen verpflichtend ist.
```

### ultra: pass

```text
„Die Datei darf gelöscht werden“ drückt eine Erlaubnis aus, keine Pflicht. „Die Datei muss gelöscht werden“ drückt eine Pflicht aus.
```

### off: pass

```text
„Die Datei darf gelöscht werden“ drückt eine Erlaubnis aus: Das Löschen ist erlaubt, aber nicht vorgeschrieben. „Die Datei muss gelöscht werden“ drückt eine Verpflichtung aus: Das Löschen ist vorgeschrieben.
```

## modes-de-052 · conditions

Source task:

> Formuliere klarer: Eine neue Zugangskarte kann beantragt werden, wenn die alte verloren ging oder nicht mehr lesbar ist. Beide Gründe müssen nicht gleichzeitig vorliegen. Ein Antrag ist noch keine Bewilligung.

### baseline: pass

```text
Eine neue Zugangskarte kann beantragt werden, wenn die alte Karte verloren gegangen oder nicht mehr lesbar ist. Einer dieser Gründe genügt. Die Antragstellung bedeutet noch keine Bewilligung.
```

### lite: pass

```text
Eine neue Zugangskarte kann beantragt werden, wenn die alte verloren ging oder nicht mehr lesbar ist. Einer der beiden Gründe genügt. Ein Antrag ist noch keine Bewilligung.
```

### full: pass

```text
Eine neue Zugangskarte kann beantragt werden, wenn die alte verloren ging oder nicht mehr lesbar ist. Einer der beiden Gründe genügt. Ein Antrag bedeutet noch keine Bewilligung.
```

### ultra: pass

```text
Eine neue Zugangskarte kann beantragt werden, wenn die alte verloren ging oder nicht mehr lesbar ist. Einer der beiden Gründe genügt. Ein Antrag bedeutet noch keine Bewilligung.
```

### off: pass

```text
Eine neue Zugangskarte kann beantragt werden, wenn die alte Karte verloren gegangen oder nicht mehr lesbar ist. Einer dieser Gründe genügt; beide müssen nicht gleichzeitig vorliegen. Der Antrag bedeutet noch keine Bewilligung.
```

## modes-de-053 · scope

Source task:

> Antworte nur auf „Darf der Hund in den Leseraum?“ Hinweis: Hunde dürfen in den Hof. Im Leseraum sind keine Tiere erlaubt. Für diese fiktive Regel ist keine weitere Ausnahme beschrieben.

### baseline: pass

```text
Nein, im Leseraum sind keine Tiere erlaubt.
```

### lite: pass

```text
Nein. Im Leseraum sind keine Tiere erlaubt.
```

### full: pass

```text
Nein. Im Leseraum sind keine Tiere erlaubt.
```

### ultra: pass

```text
Nein. Im Leseraum sind keine Tiere erlaubt.
```

### off: pass

```text
Nein, im Leseraum sind keine Tiere erlaubt.
```

## modes-de-054 · sampling

Source task:

> Schreibe eine sachliche Einschränkung: Acht geübte Teilnehmende montierten das Modell in weniger als zwölf Minuten. Alle kannten das Modell aus dem Vorjahr. Neulinge waren nicht dabei.

### baseline: pass

```text
Die Montagezeit von weniger als zwölf Minuten wurde bei acht geübten Teilnehmenden beobachtet, die das Modell bereits aus dem Vorjahr kannten. Da keine Neulinge teilnahmen, lässt sich daraus keine Aussage über deren Montagezeit ableiten.
```

### lite: pass

```text
Acht geübte Teilnehmende montierten das Modell in weniger als zwölf Minuten. Alle kannten es aus dem Vorjahr; Neulinge waren nicht dabei. Das Ergebnis lässt daher keine Aussage über die Montagezeit von Neulingen zu.
```

### full: pass

```text
Die Montagezeit von weniger als zwölf Minuten wurde bei acht geübten Teilnehmenden beobachtet. Alle kannten das Modell aus dem Vorjahr. Neulinge waren nicht dabei; über deren Montagezeit lässt sich daraus keine Aussage ableiten.
```

### ultra: pass

```text
Die Montagezeit von weniger als zwölf Minuten wurde bei acht geübten Teilnehmenden beobachtet, die das Modell alle aus dem Vorjahr kannten. Neulinge waren nicht dabei; für sie lässt sich daraus keine Montagezeit ableiten.
```

### off: pass

```text
Die Montagezeit von weniger als zwölf Minuten wurde bei acht geübten Teilnehmenden beobachtet, die das Modell alle aus dem Vorjahr kannten. Da keine Neulinge teilnahmen, lässt sich daraus keine Aussage über deren Montagezeit ableiten.
```

## modes-de-055 · conflicting_notes

Source task:

> Formuliere für das Lagerbuch: Der Lieferschein nennt 65 Schrauben. In der geöffneten Tüte wurden 64 gezählt. Die Waage wurde nicht verwendet und eine zweite Zählung steht aus.

### baseline: pass

```text
Laut Lieferschein: 65 Schrauben. Bei der ersten Zählung in der geöffneten Tüte: 64 Schrauben, somit eine Schraube weniger als angegeben. Die Waage wurde nicht verwendet. Eine zweite Zählung steht noch aus.
```

### lite: pass

```text
Der Lieferschein nennt 65 Schrauben. In der geöffneten Tüte wurden 64 Schrauben gezählt. Die Waage wurde nicht verwendet. Eine zweite Zählung steht noch aus.
```

### full: pass

```text
Laut Lieferschein: 65 Schrauben. In der geöffneten Tüte gezählt: 64 Schrauben. Die Waage wurde nicht verwendet. Eine zweite Zählung steht aus.
```

### ultra: pass

```text
Lieferschein: 65 Schrauben. In der geöffneten Tüte gezählt: 64 Schrauben. Die Waage wurde nicht verwendet; eine zweite Zählung steht aus.
```

### off: pass

```text
Laut Lieferschein: 65 Schrauben. In der geöffneten Tüte gezählt: 64 Schrauben. Die Waage wurde nicht verwendet. Eine zweite Zählung steht aus.
```

## modes-de-056 · numbers_units

Source task:

> Schreibe klarer: Die Höchstmenge beträgt 800 g je Beutel einschließlich Verpackung. Pro Bestellung sind höchstens fünf Beutel erlaubt. Die Grenze ist nicht 800 g für die ganze Bestellung.

### baseline: pass

```text
Pro Beutel sind höchstens 800 g einschließlich Verpackung erlaubt. Pro Bestellung dürfen es maximal fünf Beutel sein. Die 800-g-Grenze gilt für jeden einzelnen Beutel, nicht für die gesamte Bestellung.
```

### lite: pass

```text
Jeder Beutel darf einschließlich Verpackung höchstens 800 g wiegen. Pro Bestellung sind höchstens fünf Beutel erlaubt. Die Grenze von 800 g gilt je Beutel, nicht für die gesamte Bestellung.
```

### full: pass

```text
Je Beutel sind höchstens 800 g einschließlich Verpackung erlaubt. Pro Bestellung sind höchstens fünf Beutel erlaubt. Die 800-g-Grenze gilt je Beutel, nicht für die gesamte Bestellung.
```

### ultra: pass

```text
Je Beutel sind höchstens 800 g einschließlich Verpackung erlaubt, je Bestellung höchstens fünf Beutel. Die 800-g-Grenze gilt nicht für die gesamte Bestellung.
```

### off: pass

```text
Jeder Beutel darf einschließlich Verpackung höchstens 800 g wiegen. Pro Bestellung sind höchstens fünf Beutel erlaubt. Die Grenze von 800 g gilt pro Beutel, nicht für die gesamte Bestellung.
```

## modes-de-057 · technical

Source task:

> Überarbeite: Seit Version 3.1 blendet show_hidden=false versteckte Einträge aus. Die Einträge bleiben gespeichert. Vor der Aktualisierung begonnene Berichte verwenden ihre bisherige Einstellung bis zum Abschluss.

### baseline: pass

```text
Seit Version 3.1 werden versteckte Einträge bei show_hidden=false ausgeblendet, bleiben aber gespeichert. Berichte, die vor der Aktualisierung begonnen wurden, behalten bis zu ihrem Abschluss die bisherige Einstellung bei.
```

### lite: pass

```text
Seit Version 3.1 blendet show_hidden=false versteckte Einträge aus. Die Einträge bleiben gespeichert. Berichte, die vor der Aktualisierung begonnen wurden, verwenden bis zum Abschluss ihre bisherige Einstellung.
```

### full: pass

```text
Seit Version 3.1 blendet show_hidden=false versteckte Einträge aus, ohne sie zu löschen. Berichte, die vor der Aktualisierung begonnen wurden, behalten ihre bisherige Einstellung bis zum Abschluss.
```

### ultra: pass

```text
Seit Version 3.1 blendet show_hidden=false versteckte Einträge aus, ohne sie zu löschen. Vor der Aktualisierung begonnene Berichte behalten ihre bisherige Einstellung bis zum Abschluss.
```

### off: pass

```text
Seit Version 3.1 werden versteckte Einträge mit show_hidden=false ausgeblendet, bleiben aber gespeichert. Berichte, die vor der Aktualisierung begonnen wurden, behalten ihre bisherige Einstellung bis zum Abschluss.
```

## modes-de-058 · analysis

Source task:

> Kann man sagen, dass jede Person mehr gelesen hat? Der Durchschnitt in einer fiktiven Gruppe steigt von 3 auf 4 Bücher pro Monat. Angaben zu einzelnen Personen liegen nicht vor.

### baseline: pass

```text
Nein. Der Durchschnitt steigt zwar von 3 auf 4 Bücher pro Monat, doch daraus folgt nicht, dass jede Person mehr gelesen hat. Ohne Angaben zu einzelnen Personen lässt sich das nicht sagen.
```

### lite: pass

```text
Nein. Der Durchschnitt in der fiktiven Gruppe steigt von 3 auf 4 Bücher pro Monat. Ohne Angaben zu einzelnen Personen lässt sich nicht sagen, dass jede Person mehr gelesen hat.
```

### full: pass

```text
Nein. In der fiktiven Gruppe steigt der Durchschnitt von 3 auf 4 Bücher pro Monat. Ohne Angaben zu einzelnen Personen lässt sich nicht sagen, ob jede Person mehr gelesen hat.
```

### ultra: pass

```text
Nein. Der Durchschnitt der fiktiven Gruppe steigt von 3 auf 4 Bücher pro Monat. Ohne Angaben zu einzelnen Personen lässt sich nicht sagen, dass jede Person mehr gelesen hat.
```

### off: pass

```text
Nein. Der Durchschnitt steigt von 3 auf 4 Bücher pro Monat. Daraus folgt nicht, dass jede Person mehr gelesen hat. Ohne Angaben zu einzelnen Personen lässt sich das nicht feststellen.
```

## modes-de-059 · voice

Source task:

> Verdichte den Text, behalte seine ruhige Erzählstimme: Im Treppenhaus roch es nach frischem Holz. Auf der dritten Stufe lag ein roter Handschuh. Seit dem Mittag war niemand die Treppe hinaufgegangen.

### baseline: pass

```text
Im Treppenhaus roch es nach frischem Holz. Ein roter Handschuh lag auf der dritten Stufe. Seit Mittag war niemand hinaufgegangen.
```

### lite: pass

```text
Im Treppenhaus roch es nach frischem Holz. Auf der dritten Stufe lag ein roter Handschuh. Seit Mittag war niemand hinaufgegangen.
```

### full: pass

```text
Im Treppenhaus roch es nach frischem Holz. Auf der dritten Stufe lag ein roter Handschuh. Seit Mittag war niemand hinaufgegangen.
```

### ultra: pass

```text
Im Treppenhaus roch es nach frischem Holz. Auf der dritten Stufe lag ein roter Handschuh. Seit Mittag war niemand hinaufgegangen.
```

### off: pass

```text
Im Treppenhaus roch es nach frischem Holz. Ein roter Handschuh lag auf der dritten Stufe. Seit Mittag war niemand hinaufgegangen.
```

## modes-de-060 · exact_format

Source task:

> Gib nur diese Zeile zurück, ohne Einleitung: Freigabe ausstehend — Vorgang V-72.

### baseline: pass

```text
Freigabe ausstehend — Vorgang V-72.
```

### lite: pass

```text
Freigabe ausstehend — Vorgang V-72.
```

### full: pass

```text
Freigabe ausstehend — Vorgang V-72.
```

### ultra: pass

```text
Freigabe ausstehend — Vorgang V-72.
```

### off: pass

```text
Freigabe ausstehend — Vorgang V-72.
```

## modes-de-061 · exact_format

Source task:

> Vereinfache den deutschen message-Wert. Antworte ausschließlich mit JSON und den Schlüsseln request, retries, message. request und retries bleiben gleich: {"request":"N-407","retries":1,"message":"Ihre Datei konnte nicht verarbeitet werden; bitte laden Sie sie als TXT-Datei erneut hoch."}

### baseline: flagged

```text
{"request":"N-407","retries":1,"message":"Wir konnten Ihre Datei nicht verarbeiten. Bitte laden Sie sie erneut als TXT-Datei hoch."}
```

Review notes: Preserves the error and retry instruction in simpler German and valid JSON. / Preserves the failure and retry instruction but introduces an actor absent from the source.

### lite: pass

```text
{"request":"N-407","retries":1,"message":"Ihre Datei konnte nicht verarbeitet werden. Bitte laden Sie sie erneut als TXT-Datei hoch."}
```

### full: pass

```text
{"request":"N-407","retries":1,"message":"Ihre Datei konnte nicht verarbeitet werden. Bitte laden Sie sie erneut als TXT-Datei hoch."}
```

### ultra: pass

```text
{"request":"N-407","retries":1,"message":"Ihre Datei konnte nicht verarbeitet werden. Bitte laden Sie sie erneut als TXT-Datei hoch."}
```

### off: pass

```text
{"request":"N-407","retries":1,"message":"Ihre Datei konnte nicht verarbeitet werden. Bitte laden Sie sie erneut als TXT-Datei hoch."}
```

## modes-de-062 · exact_format

Source task:

> Schreibe einen Hinweis in genau zwei Sätzen: Lesender Zugriff auf /srv/werkraum bleibt möglich. Schreibender Zugriff ist erst wieder ab 06:40 UTC erlaubt. Pfad und Uhrzeit müssen unverändert vorkommen.

### baseline: pass

```text
Lesender Zugriff auf /srv/werkraum bleibt möglich. Schreibender Zugriff ist erst wieder ab 06:40 UTC erlaubt.
```

### lite: pass

```text
Lesender Zugriff auf /srv/werkraum bleibt möglich. Schreibender Zugriff ist erst wieder ab 06:40 UTC erlaubt.
```

### full: pass

```text
Lesender Zugriff auf /srv/werkraum bleibt möglich. Schreibender Zugriff ist erst wieder ab 06:40 UTC erlaubt.
```

### ultra: pass

```text
Lesender Zugriff auf /srv/werkraum bleibt möglich. Schreibender Zugriff ist erst wieder ab 06:40 UTC erlaubt.
```

### off: pass

```text
Lesender Zugriff auf /srv/werkraum bleibt möglich. Schreibender Zugriff ist erst wieder ab 06:40 UTC erlaubt.
```

## modes-de-063 · exact_format

Source task:

> Korrigiere nur „erhaltn“ und gib die Zeile allein zurück: Formular erhaltn: DE_17 — Antwort noch offen.

### baseline: pass

```text
Formular erhalten: DE_17 — Antwort noch offen.
```

### lite: pass

```text
Formular erhalten: DE_17 — Antwort noch offen.
```

### full: pass

```text
Formular erhalten: DE_17 — Antwort noch offen.
```

### ultra: pass

```text
Formular erhalten: DE_17 — Antwort noch offen.
```

### off: pass

```text
Formular erhalten: DE_17 — Antwort noch offen.
```

## modes-de-064 · exact_format

Source task:

> Schreibe eine kurze Erinnerungsnachricht: {{name}} darf die Reservierung unter {{booking_url}} bis zum 9. September ändern. Behalte die Variablen genau so und erfinde keine Werte.

### baseline: pass

```text
Erinnerung: {{name}} darf die Reservierung unter {{booking_url}} bis zum 9. September ändern.
```

### lite: pass

```text
Zur Erinnerung: {{name}} darf die Reservierung unter {{booking_url}} bis zum 9. September ändern.
```

### full: pass

```text
Zur Erinnerung: {{name}} darf die Reservierung unter {{booking_url}} bis zum 9. September ändern.
```

### ultra: pass

```text
Zur Erinnerung: {{name}} darf die Reservierung unter {{booking_url}} bis zum 9. September ändern.
```

### off: pass

```text
Erinnerung: {{name}} darf die Reservierung unter {{booking_url}} bis zum 9. September ändern.
```

## modes-de-065 · exact_format

Source task:

> Gib nur JSON mit den Schlüsseln object, verified, note aus. object ist "REG-23", verified ist false. Die Beschriftung wurde geprüft; der Inhalt wurde noch nicht gezählt. Die note soll deutsch sein.

### baseline: pass

```text
{"object":"REG-23","verified":false,"note":"Die Beschriftung wurde geprüft; der Inhalt wurde noch nicht gezählt."}
```

### lite: pass

```text
{"object":"REG-23","verified":false,"note":"Die Beschriftung wurde geprüft; der Inhalt wurde noch nicht gezählt."}
```

### full: pass

```text
{"object":"REG-23","verified":false,"note":"Die Beschriftung wurde geprüft; der Inhalt wurde noch nicht gezählt."}
```

### ultra: pass

```text
{"object":"REG-23","verified":false,"note":"Die Beschriftung wurde geprüft; der Inhalt wurde noch nicht gezählt."}
```

### off: pass

```text
{"object":"REG-23","verified":false,"note":"Die Beschriftung wurde geprüft; der Inhalt wurde noch nicht gezählt."}
```

## modes-de-066 · exact_format

Source task:

> Gib genau diese beiden Zeilen ohne Codeblock zurück:
> Entwurf sichtbar: ja
> Veröffentlichung erlaubt: nein

### baseline: pass

```text
Entwurf sichtbar: ja
Veröffentlichung erlaubt: nein
```

### lite: pass

```text
Entwurf sichtbar: ja
Veröffentlichung erlaubt: nein
```

### full: pass

```text
Entwurf sichtbar: ja
Veröffentlichung erlaubt: nein
```

### ultra: pass

```text
Entwurf sichtbar: ja
Veröffentlichung erlaubt: nein
```

### off: pass

```text
Entwurf sichtbar: ja
Veröffentlichung erlaubt: nein
```

## modes-de-067 · exact_format

Source task:

> Erkläre in einem Satz, was archive-check --list-only tut. Der Befehl listet Probleme auf und behebt sie nicht. Der Befehl muss unverändert in der Antwort stehen.

### baseline: pass

```text
archive-check --list-only listet Probleme auf, behebt sie aber nicht.
```

### lite: pass

```text
archive-check --list-only listet Probleme auf, behebt sie aber nicht.
```

### full: pass

```text
archive-check --list-only listet Probleme auf, behebt sie aber nicht.
```

### ultra: pass

```text
archive-check --list-only listet Probleme auf, behebt sie aber nicht.
```

### off: pass

```text
archive-check --list-only listet Probleme auf, behebt sie aber nicht.
```

## modes-de-068 · exact_format

Source task:

> Vereinfache die Notiz, lasse das englische Zitat unverändert: Die Anzeige lautet "queue paused". Das zeigt eine angehaltene Warteschlange, aber keinen bestätigten Verlust von Aufträgen. Der Grund ist noch unbekannt.

### baseline: pass

```text
Die Anzeige lautet "queue paused". Die Warteschlange ist angehalten. Ein Verlust von Aufträgen ist nicht bestätigt. Der Grund ist noch unbekannt.
```

### lite: pass

```text
Die Anzeige lautet "queue paused". Die Warteschlange ist angehalten, ein Verlust von Aufträgen ist aber nicht bestätigt. Der Grund ist noch unbekannt.
```

### full: pass

```text
Die Anzeige "queue paused" bedeutet, dass die Warteschlange angehalten ist. Ein Verlust von Aufträgen ist damit nicht bestätigt. Der Grund ist noch unbekannt.
```

### ultra: flagged

```text
Die Anzeige „queue paused“ bedeutet: Die Warteschlange ist angehalten. Ein Verlust von Aufträgen ist nicht bestätigt. Der Grund ist noch unbekannt.
```

Review notes: Meaning is intact, but the protected quoted token is not reproduced exactly. / Preserves substantive meaning but changes the explicitly protected quoted token.

### off: pass

```text
Die Anzeige "queue paused" bedeutet, dass die Warteschlange angehalten ist. Ein Verlust von Aufträgen ist damit nicht bestätigt. Der Grund ist noch unbekannt.
```

## modes-de-069 · exact_format

Source task:

> Antworte nur mit einem JSON-Objekt mit code, available und notice. code bleibt "BK-56", available bleibt 0. Die notice soll sagen, dass derzeit kein Exemplar ausgeliehen werden kann, ohne eine künftige Verfügbarkeit zu versprechen.

### baseline: pass

```text
{"code":"BK-56","available":0,"notice":"Derzeit kann kein Exemplar ausgeliehen werden."}
```

### lite: pass

```text
{"code":"BK-56","available":0,"notice":"Derzeit kann kein Exemplar ausgeliehen werden."}
```

### full: pass

```text
{"code":"BK-56","available":0,"notice":"Derzeit kann kein Exemplar ausgeliehen werden."}
```

### ultra: pass

```text
{"code":"BK-56","available":0,"notice":"Derzeit kann kein Exemplar ausgeliehen werden."}
```

### off: pass

```text
{"code":"BK-56","available":0,"notice":"Derzeit kann kein Exemplar ausgeliehen werden."}
```

## modes-de-070 · long_summary

Source task:

> Schreibe eine Übergabe für die nächste Schicht im fiktiven Leihladen. Der Text soll zeigen, was ausgeliehen werden darf und welche Angaben noch geprüft werden müssen. Vorschläge dürfen nicht als erledigte Maßnahmen erscheinen.
> 
> Im Bestand stehen 54 Geräte. 49 wurden heute im Laden gesehen, drei sind mit unterschriebenem Leihschein unterwegs und zwei wurden nicht gefunden. Die drei ausgeliehenen Geräte sollen am 22. Oktober zurückkommen. Bei den fehlenden Geräten ist offen, ob sie falsch einsortiert oder nicht korrekt verbucht wurden. Ein Diebstahl wurde nicht festgestellt. Der letzte vollständige Abgleich liegt sechs Wochen zurück.
> 
> Vier Nähmaschinen wurden gereinigt. Nur Maschine N-12 hat zusätzlich die Funktionsprüfung bestanden und darf ausgeliehen werden. Die anderen drei bleiben bis zu ihrer Funktionsprüfung gesperrt. Ein weißes Etikett bedeutet lediglich „gereinigt“. Es ersetzt keine Freigabe. N-12 steht am Fenster; ihr Zubehör liegt in einer beschrifteten Tasche unter dem Tisch.
> 
> Es sind 3,6 kg Stoffreste vorhanden. Das Gewicht schließt die Aufbewahrungsbeutel ein und gibt keine verlässliche Stofffläche an. Neue Beutel wurden vorgeschlagen, aber noch nicht bestellt. Für Verbrauchsmaterial sind vermutlich 140 € übrig; zwei Kartenzahlungen wurden noch nicht mit den Belegen abgeglichen. Der Betrag ist daher vorläufig.
> 
> Tobias hat angeboten, am Freitag die Schilder zu erneuern. Seine Teilnahme ist noch nicht bestätigt. Die Liste der beschädigten Schilder liegt neben dem Kassenbuch. Der vordere Boden wurde gewischt. Im hinteren Raum ist die Beleuchtung defekt; dieser Raum bleibt geschlossen, bis der Fehler behoben und die Beleuchtung geprüft ist. Für neue Ausleihen gilt weiterhin das bisherige Formular. Eine kürzere Formularfassung liegt als Entwurf vor und wurde noch nicht freigegeben.

### baseline: pass

```text
Übergabe an die nächste Schicht

Ausleihfreigabe und Zugang
- Vier Nähmaschinen wurden gereinigt. Nur N-12 hat zusätzlich die Funktionsprüfung bestanden und darf ausgeliehen werden. Sie steht am Fenster; ihr Zubehör liegt in einer beschrifteten Tasche unter dem Tisch.
- Die anderen drei Nähmaschinen bleiben bis zu ihrer Funktionsprüfung gesperrt. Ein weißes Etikett bedeutet nur „gereinigt“, nicht „freigegeben“.
- Für neue Ausleihen gilt weiterhin das bisherige Formular. Die kürzere Fassung ist nur ein Entwurf und noch nicht freigegeben.
- Der hintere Raum bleibt wegen defekter Beleuchtung geschlossen, bis der Fehler behoben und die Beleuchtung geprüft ist. Der vordere Boden wurde gewischt.

Bestand und offene Prüfung
- Im Bestand stehen 54 Geräte: 49 wurden heute im Laden gesehen, drei sind mit unterschriebenem Leihschein ausgeliehen, zwei wurden nicht gefunden. Für die drei ausgeliehenen Geräte ist die Rückgabe am 22. Oktober vorgesehen.
- Bei den zwei fehlenden Geräten muss geklärt werden, ob sie falsch einsortiert oder nicht korrekt verbucht wurden. Ein Diebstahl wurde nicht festgestellt. Der letzte vollständige Abgleich liegt sechs Wochen zurück.

Material und Budget
- Vorhanden sind 3,6 kg Stoffreste einschließlich Aufbewahrungsbeuteln. Daraus lässt sich keine verlässliche Stofffläche ableiten.
- Neue Beutel wurden vorgeschlagen, aber noch nicht bestellt.
- Für Verbrauchsmaterial sind vermutlich 140 € übrig. Der Betrag ist vorläufig: Zwei Kartenzahlungen müssen noch mit den Belegen abgeglichen werden.

Schilder
- Tobias hat angeboten, am Freitag die Schilder zu erneuern; seine Teilnahme ist noch nicht bestätigt.
- Die Liste der beschädigten Schilder liegt neben dem Kassenbuch.
```

### lite: pass

```text
Übergabe an die nächste Schicht

Bestand
Im Bestand stehen 54 Geräte: 49 wurden heute im Laden gesehen, drei sind mit unterschriebenem Leihschein ausgeliehen und zwei wurden nicht gefunden. Die drei ausgeliehenen Geräte sollen am 22. Oktober zurückkommen. Bei den fehlenden Geräten muss noch geklärt werden, ob sie falsch einsortiert oder nicht korrekt verbucht wurden. Ein Diebstahl wurde nicht festgestellt. Der letzte vollständige Abgleich liegt sechs Wochen zurück.

Nähmaschinen und Freigabe
Vier Nähmaschinen wurden gereinigt. Nur N-12 hat zusätzlich die Funktionsprüfung bestanden und darf ausgeliehen werden. Die anderen drei bleiben bis zu ihrer Funktionsprüfung gesperrt. Ein weißes Etikett bedeutet nur „gereinigt“ und ersetzt keine Freigabe. N-12 steht am Fenster; ihr Zubehör liegt in einer beschrifteten Tasche unter dem Tisch.

Material und Budget
Es sind 3,6 kg Stoffreste vorhanden. Das Gewicht enthält die Aufbewahrungsbeutel und gibt keine verlässliche Stofffläche an. Neue Beutel wurden vorgeschlagen, aber noch nicht bestellt. Für Verbrauchsmaterial sind vermutlich 140 € übrig. Zwei Kartenzahlungen müssen noch mit den Belegen abgeglichen werden; der Betrag ist daher vorläufig.

Schilder und Räume
Tobias hat angeboten, am Freitag die Schilder zu erneuern. Seine Teilnahme ist noch nicht bestätigt. Die Liste der beschädigten Schilder liegt neben dem Kassenbuch. Der vordere Boden wurde gewischt. Im hinteren Raum ist die Beleuchtung defekt. Dieser Raum bleibt geschlossen, bis der Fehler behoben und die Beleuchtung geprüft ist.

Formulare
Für neue Ausleihen gilt weiterhin das bisherige Formular. Eine kürzere Fassung liegt als Entwurf vor und wurde noch nicht freigegeben.
```

### full: pass

```text
## Übergabe an die nächste Schicht

### Ausleihen und Freigaben
- Vier Nähmaschinen wurden gereinigt. Nur N-12 hat zusätzlich die Funktionsprüfung bestanden und darf ausgeliehen werden. Sie steht am Fenster; ihr Zubehör liegt in einer beschrifteten Tasche unter dem Tisch.
- Die anderen drei Nähmaschinen bleiben bis zu ihrer Funktionsprüfung gesperrt. Ein weißes Etikett bedeutet nur „gereinigt“, nicht „freigegeben“.
- Für neue Ausleihen gilt weiterhin das bisherige Formular. Die kürzere Fassung ist ein Entwurf und noch nicht freigegeben.

### Bestand: Angaben noch prüfen
- Im Bestand stehen 54 Geräte: 49 wurden heute im Laden gesehen, drei sind mit unterschriebenem Leihschein ausgeliehen, zwei wurden nicht gefunden.
- Die drei ausgeliehenen Geräte sollen am 22. Oktober zurückkommen.
- Bei den zwei fehlenden Geräten ist offen, ob sie falsch einsortiert oder nicht korrekt verbucht wurden. Ein Diebstahl wurde nicht festgestellt. Der letzte vollständige Abgleich liegt sechs Wochen zurück.

### Material und Budget
- Vorhanden sind 3,6 kg Stoffreste einschließlich Aufbewahrungsbeuteln. Daraus lässt sich keine verlässliche Stofffläche ableiten.
- Neue Beutel wurden vorgeschlagen, aber noch nicht bestellt.
- Für Verbrauchsmaterial sind vermutlich 140 € übrig. Zwei Kartenzahlungen wurden noch nicht mit den Belegen abgeglichen; der Betrag ist vorläufig.

### Schilder und Räume
- Tobias hat angeboten, am Freitag die Schilder zu erneuern. Seine Teilnahme ist noch nicht bestätigt. Die Liste der beschädigten Schilder liegt neben dem Kassenbuch.
- Der vordere Boden wurde gewischt.
- Im hinteren Raum ist die Beleuchtung defekt. Der Raum bleibt geschlossen, bis der Fehler behoben und die Beleuchtung geprüft ist.
```

### ultra: pass

```text
## Ausleihe und Zugang
- Vier Nähmaschinen sind gereinigt. Nur N-12 hat auch die Funktionsprüfung bestanden und darf ausgeliehen werden. Sie steht am Fenster; ihr Zubehör liegt in einer beschrifteten Tasche unter dem Tisch. Die anderen drei bleiben bis zu ihrer Funktionsprüfung gesperrt. Weißes Etikett = „gereinigt“, keine Freigabe.
- Der hintere Raum bleibt wegen defekter Beleuchtung geschlossen, bis der Fehler behoben und die Beleuchtung geprüft ist. Der vordere Boden wurde gewischt.
- Für neue Ausleihen gilt das bisherige Formular. Die kürzere Fassung ist ein nicht freigegebener Entwurf.

## Bestand und offene Prüfungen
- Bestand: 54 Geräte. Heute wurden 49 im Laden gesehen; drei sind mit unterschriebenem Leihschein ausgeliehen und sollen am 22. Oktober zurückkommen. Zwei wurden nicht gefunden. Ob sie falsch einsortiert oder nicht korrekt verbucht wurden, ist offen. Ein Diebstahl wurde nicht festgestellt. Letzter vollständiger Abgleich: vor sechs Wochen.
- Stoffreste: 3,6 kg einschließlich Aufbewahrungsbeuteln; daraus lässt sich keine verlässliche Stofffläche ableiten. Neue Beutel wurden vorgeschlagen, aber noch nicht bestellt.
- Verbrauchsmaterial: vermutlich 140 € übrig. Der Betrag ist vorläufig, da zwei Kartenzahlungen noch mit den Belegen abgeglichen werden müssen.
- Tobias hat angeboten, am Freitag die Schilder zu erneuern; seine Teilnahme ist noch nicht bestätigt. Die Liste beschädigter Schilder liegt neben dem Kassenbuch.
```

### off: pass

```text
## Übergabe an die nächste Schicht

### Ausleihe und Freigaben
Vier Nähmaschinen wurden gereinigt. Nur N-12 hat zusätzlich die Funktionsprüfung bestanden und darf ausgeliehen werden. Die anderen drei bleiben bis zu ihrer Funktionsprüfung gesperrt. Ein weißes Etikett bedeutet nur „gereinigt“ und ersetzt keine Freigabe.

N-12 steht am Fenster. Ihr Zubehör liegt in einer beschrifteten Tasche unter dem Tisch.

Für neue Ausleihen gilt weiterhin das bisherige Formular. Die kürzere Formularfassung ist ein Entwurf und noch nicht freigegeben.

### Bestand und offene Prüfungen
Im Bestand stehen 54 Geräte: 49 wurden heute im Laden gesehen, drei sind mit unterschriebenem Leihschein ausgeliehen und zwei wurden nicht gefunden. Die drei ausgeliehenen Geräte sollen am 22. Oktober zurückkommen.

Bei den zwei fehlenden Geräten muss noch geklärt werden, ob sie falsch einsortiert oder nicht korrekt verbucht wurden. Ein Diebstahl wurde nicht festgestellt. Der letzte vollständige Bestandsabgleich liegt sechs Wochen zurück.

### Material und Budget
Es sind 3,6 kg Stoffreste vorhanden. Das Gewicht enthält die Aufbewahrungsbeutel und lässt keine verlässliche Aussage zur Stofffläche zu. Neue Beutel wurden vorgeschlagen, aber noch nicht bestellt.

Für Verbrauchsmaterial sind vermutlich 140 € übrig. Zwei Kartenzahlungen müssen noch mit den Belegen abgeglichen werden; der Betrag ist daher vorläufig.

### Räume und Schilder
Der vordere Boden wurde gewischt. Im hinteren Raum ist die Beleuchtung defekt. Der Raum bleibt geschlossen, bis der Fehler behoben und die Beleuchtung geprüft ist.

Tobias hat angeboten, am Freitag die Schilder zu erneuern. Seine Teilnahme ist noch nicht bestätigt. Die Liste der beschädigten Schilder liegt neben dem Kassenbuch.
```

## modes-de-071 · long_sampling

Source task:

> Schreibe einen sachlichen Ergebnistext über diese fiktive Befragung. Er soll für den Vorstand eines Kulturvereins verständlich sein. Nenne das führende Angebot und die wichtigsten Grenzen der Aussage, ohne selbst eine Entscheidung zu treffen.
> 
> Zur Wahl standen ein Filmabend, eine offene Musikprobe und ein Brettspieltreff. Der Fragebogen lag an zwei Samstagen im Vereinscafé und einmal beim Ende eines bestehenden Musikworkshops aus. Eine Zufallsauswahl aus der Mitgliederliste fand nicht statt. Personen, die diese Orte nicht besuchten, wurden nicht gezielt angeschrieben. Eine Onlinefassung gab es nicht.
> 
> Von 150 ausgegebenen Bögen kamen 75 mit genau einer gültigen Auswahl zurück. Weitere 15 zurückgegebene Bögen waren unleserlich oder enthielten mehrere Kreuze. Sie wurden nicht in die Auswertung aufgenommen. Von den 75 gültigen Antworten wählten 39 den Filmabend, 24 die offene Musikprobe und 12 den Brettspieltreff. Der Filmabend erreicht damit 52 % der gültigen Antworten. Die Zahl aller Vereinsmitglieder wird in dieser Notiz nicht genannt.
> 
> Dreißig Personen schrieben zusätzlich einen Kommentar. Elf Kommentare wünschen eine Veranstaltung ohne Anmeldung. Die Kommentare wurden getrennt gesammelt, sodass sie keinem angekreuzten Angebot zugeordnet werden können. Es ist deshalb nicht bekannt, ob die elf Kommentare überwiegend von Personen stammen, die den Filmabend gewählt haben.
> 
> Die Helfenden bemerkten viele Stammgäste des Cafés, führten jedoch keine gesonderte Zählung durch. Eine Person fragte nach einem Fragebogen in leichter lesbarer Schrift; eine solche Fassung lag nicht vor. Kosten, Raumverfügbarkeit und mögliche Termine der drei Angebote wurden nicht erhoben. Die Befragung beschreibt freiwillig geäußerte Präferenzen in diesem begrenzten Verfahren. Sie ist weder ein Beschluss noch der Nachweis, dass die Mehrheit aller Mitglieder ein bestimmtes Angebot bevorzugt.

### baseline: pass

```text
Unter den 75 gültigen Antworten liegt der Filmabend mit 39 Stimmen (52 %) vorn. Die offene Musikprobe erhielt 24 Stimmen (32 %), der Brettspieltreff 12 Stimmen (16 %). Von 150 ausgegebenen Fragebögen wurden außerdem 15 zurückgegeben, die wegen Unleserlichkeit oder mehrerer Kreuze nicht ausgewertet wurden.

Die Ergebnisse beschreiben die freiwillig geäußerten Präferenzen der erreichten Personen, nicht die Meinung aller Vereinsmitglieder. Die Fragebögen lagen an zwei Samstagen im Vereinscafé und einmal am Ende eines bestehenden Musikworkshops aus. Es gab weder eine Zufallsauswahl noch eine gezielte Ansprache der Personen, die diese Orte nicht besuchten, noch eine Onlinefassung. Die Gesamtzahl der Mitglieder ist nicht angegeben. Die Helfenden beobachteten viele Café-Stammgäste, zählten diese aber nicht gesondert. Eine angefragte Fassung in leichter lesbarer Schrift war nicht verfügbar.

Von 30 zusätzlichen Kommentaren wünschen elf eine Veranstaltung ohne Anmeldung. Da die Kommentare getrennt gesammelt wurden, lassen sie sich keinem gewählten Angebot zuordnen. Insbesondere ist nicht bekannt, ob dieser Wunsch überwiegend von Personen stammt, die den Filmabend gewählt haben.

Kosten, Raumverfügbarkeit und mögliche Termine wurden nicht erhoben. Die Befragung ist daher weder ein Beschluss noch ein Nachweis dafür, dass die Mehrheit aller Mitglieder den Filmabend bevorzugt.
```

### lite: pass

```text
Der Filmabend liegt unter den gültigen Antworten vorn: 39 von 75 Personen wählten ihn, das entspricht 52 %. Die offene Musikprobe erhielt 24 Stimmen, der Brettspieltreff 12.

Von 150 ausgegebenen Fragebögen kamen 75 mit genau einer gültigen Auswahl zurück. Weitere 15 zurückgegebene Bögen waren unleserlich oder enthielten mehrere Kreuze und wurden nicht ausgewertet. Die Gesamtzahl der Vereinsmitglieder ist in der Notiz nicht angegeben. Aus dem Ergebnis lässt sich daher nicht ableiten, dass die Mehrheit aller Mitglieder den Filmabend bevorzugt.

Die Teilnahme war freiwillig. Die Fragebögen lagen an zwei Samstagen im Vereinscafé und einmal am Ende eines bestehenden Musikworkshops aus. Es gab weder eine Zufallsauswahl aus der Mitgliederliste noch eine Onlinefassung. Personen, die diese Orte nicht besuchten, wurden nicht gezielt angeschrieben. Die Helfenden bemerkten viele Stammgäste des Cafés, zählten sie aber nicht gesondert. Eine Person fragte nach einer Fassung in leichter lesbarer Schrift; diese war nicht verfügbar.

30 Personen hinterließen zusätzlich einen Kommentar. Elf Kommentare wünschen eine Veranstaltung ohne Anmeldung. Da die Kommentare getrennt gesammelt wurden, lassen sie sich keinem gewählten Angebot zuordnen. Es ist deshalb unbekannt, ob diese elf Kommentare überwiegend von Personen stammen, die den Filmabend gewählt haben.

Kosten, Raumverfügbarkeit und mögliche Termine wurden nicht erhoben. Die Befragung zeigt freiwillig geäußerte Präferenzen innerhalb dieses begrenzten Verfahrens. Sie ist weder ein Beschluss noch ein Nachweis für die Präferenz der Mehrheit aller Mitglieder.
```

### full: pass

```text
Der Filmabend führt mit 39 von 75 gültigen Antworten (52 %). Die offene Musikprobe erhielt 24 Stimmen, der Brettspieltreff 12. Das Ergebnis beschreibt freiwillig geäußerte Präferenzen innerhalb eines begrenzten Befragungsverfahrens. Es belegt nicht, dass die Mehrheit aller Vereinsmitglieder den Filmabend bevorzugt, und ist kein Beschluss.

Von 150 ausgegebenen Fragebögen kamen 75 mit genau einer gültigen Auswahl zurück. Weitere 15 zurückgegebene Bögen waren unleserlich oder enthielten mehrere Kreuze und wurden ausgeschlossen. Die Gesamtzahl der Vereinsmitglieder ist in der Notiz nicht angegeben.

Die Fragebögen lagen an zwei Samstagen im Vereinscafé und einmal am Ende eines bestehenden Musikworkshops aus. Es gab weder eine Zufallsauswahl aus der Mitgliederliste noch eine Onlinefassung. Personen, die diese Orte nicht besuchten, wurden nicht gezielt angeschrieben. Die Helfenden bemerkten viele Stammgäste des Cafés, zählten sie aber nicht gesondert. Eine Person fragte nach leichter lesbarer Schrift; eine entsprechende Fassung war nicht verfügbar. Diese Bedingungen begrenzen die Aussagekraft für den gesamten Verein.

30 Personen ergänzten einen Kommentar. Elf Kommentare wünschen eine Veranstaltung ohne Anmeldung. Da die Kommentare getrennt gesammelt wurden, lassen sie sich keinem gewählten Angebot zuordnen. Ob diese elf Kommentare überwiegend von Personen stammen, die den Filmabend gewählt haben, ist daher unbekannt.

Kosten, Raumverfügbarkeit und mögliche Termine der drei Angebote wurden nicht erhoben.
```

### ultra: pass

```text
Der Filmabend liegt mit 39 von 75 gültigen Antworten (52 %) vorn. Die offene Musikprobe erhielt 24 Stimmen, der Brettspieltreff 12.

Von 150 ausgegebenen Fragebögen kamen 75 mit genau einer gültigen Auswahl zurück. Weitere 15 zurückgegebene Bögen waren unleserlich oder mehrfach angekreuzt und wurden ausgeschlossen.

Die Befragung erfasst freiwillig geäußerte Präferenzen in einem begrenzten Verfahren: Die Bögen lagen an zwei Samstagen im Vereinscafé und einmal am Ende eines bestehenden Musikworkshops aus. Es gab weder eine Zufallsauswahl aus der Mitgliederliste noch eine Onlinefassung. Personen, die diese Orte nicht besuchten, wurden nicht gezielt angeschrieben. Helfende bemerkten viele Café-Stammgäste, zählten sie aber nicht gesondert. Eine gewünschte Fassung in leichter lesbarer Schrift war nicht vorhanden. Die Gesamtzahl der Vereinsmitglieder ist nicht angegeben. Die 52 % beziehen sich deshalb ausschließlich auf die gültigen Antworten, nicht auf alle Mitglieder.

30 Personen ergänzten einen Kommentar; elf wünschten eine Veranstaltung ohne Anmeldung. Da die Kommentare getrennt gesammelt wurden, lassen sie sich keinem gewählten Angebot zuordnen. Ob die elf Wünsche überwiegend von Personen stammen, die den Filmabend gewählt haben, ist unbekannt.

Kosten, Räume und mögliche Termine wurden nicht erhoben. Das Ergebnis ist weder ein Beschluss noch ein Nachweis, dass die Mehrheit aller Mitglieder ein bestimmtes Angebot bevorzugt.
```

### off: pass

```text
Bei der fiktiven Befragung liegt der Filmabend vorn: Von 75 gültigen Antworten entfielen 39 auf den Filmabend (52 %), 24 auf die offene Musikprobe und 12 auf den Brettspieltreff.

Von 150 ausgegebenen Fragebögen kamen 75 mit genau einer gültigen Auswahl zurück. Weitere 15 zurückgegebene Bögen waren unleserlich oder enthielten mehrere Kreuze und wurden ausgeschlossen. Die Gesamtzahl der Vereinsmitglieder ist nicht angegeben. Die 52 % beziehen sich daher ausschließlich auf die gültigen Antworten, nicht auf alle Mitglieder.

Die Teilnahme war freiwillig. Die Fragebögen lagen an zwei Samstagen im Vereinscafé und einmal am Ende eines bestehenden Musikworkshops aus. Es gab weder eine Zufallsauswahl aus der Mitgliederliste noch eine gezielte Ansprache der Personen, die diese Orte nicht besuchten. Eine Onlinefassung fehlte. Die Helfenden bemerkten viele Stammgäste des Cafés, zählten diese aber nicht gesondert. Eine gewünschte Fassung in leichter lesbarer Schrift war nicht verfügbar. Diese Bedingungen begrenzen die Aussagekraft für die gesamte Mitgliedschaft.

Dreißig Personen ergänzten einen Kommentar; elf Kommentare wünschen eine Veranstaltung ohne Anmeldung. Da die Kommentare getrennt gesammelt wurden, lassen sie sich keinem gewählten Angebot zuordnen. Ob dieser Wunsch überwiegend von Personen stammt, die den Filmabend gewählt haben, ist unbekannt.

Kosten, Raumverfügbarkeit und mögliche Termine wurden nicht erhoben. Die Befragung beschreibt freiwillig geäußerte Präferenzen innerhalb dieses begrenzten Verfahrens. Sie ist weder ein Beschluss noch ein Nachweis dafür, dass die Mehrheit aller Mitglieder ein bestimmtes Angebot bevorzugt.
```

## modes-de-072 · long_scope

Source task:

> Beantworte nur die Frage: „Darf der Verkaufsraum am Dienstag um 9 Uhr öffnen?“ Begründe die Antwort anhand der folgenden fiktiven Notiz. Eine neue Kostenplanung wird nicht verlangt.
> 
> Die neuen Regale sind aufgebaut. Alle 30 Preisetiketten wurden gedruckt und kontrolliert. Ein Helfer hat die Kabel ordentlich zusammengelegt. Diese Arbeiten ersetzen nicht die im internen Plan vorgeschriebene Prüfung der Beleuchtung und der freien Wege. Vor einer Öffnung für Kundschaft muss eine unterschriebene Prüfung für diesen Raum vorliegen. Außerdem müssen während der gesamten Öffnungszeit zwei eingewiesene Personen anwesend sein.
> 
> Eine Prüferin hat gesagt, sie könne möglicherweise am Montag vorbeikommen. Es gibt noch keine bestätigte Uhrzeit und keine unterschriebene Prüfung. Ein Bericht aus dem alten Laden bezieht sich auf andere Regale und kann hier nicht verwendet werden. Für Dienstagvormittag ist eine eingewiesene Person sicher eingeplant. Eine zweite Person hat nur für Dienstagnachmittag zugesagt. Eine Helferin ohne Einweisung könnte morgens kommen; sie erfüllt die Vorgabe nach dem aktuellen Plan nicht.
> 
> Die bisher bezahlten Einrichtungskosten betragen 730 €. Ein Budget von 900 € steht zur Verfügung, eine Rechnung für Transport fehlt noch. Der Kassenwart erwartet, dass die Kosten im Rahmen bleiben, hat dies aber noch nicht abschließend geprüft. Die finanzielle Lage hebt weder die Prüfung noch die Besetzungsvorgabe auf. Auf den vorbereiteten Karten steht als Eröffnung Dienstag, 9 Uhr. Die Karten sind noch nicht verteilt.
> 
> Montag dürfen Helfende den Raum für das Einräumen betreten. Kundenbesuche und Verkäufe sind dabei nicht erlaubt. Die Erlaubnis zum Einräumen ist keine Erlaubnis zur Öffnung. Entscheidend ist, ob die erforderliche Prüfung unterschrieben vorliegt und zwei eingewiesene Personen tatsächlich für den Vormittag zugesagt haben. Erwartete Besuche und Zusagen für einen anderen Zeitraum dürfen nicht als erfüllt gerechnet werden.

### baseline: flagged

```text
Nach dem derzeitigen Stand darf der Verkaufsraum am Dienstag um 9 Uhr nicht öffnen. Die vorgeschriebene unterschriebene Prüfung der Beleuchtung und der freien Wege liegt noch nicht vor. Der mögliche Besuch der Prüferin am Montag ist nicht bestätigt; der Bericht aus dem alten Laden ist für diesen Raum nicht verwendbar.

Außerdem ist für Dienstagvormittag nur eine eingewiesene Person sicher eingeplant. Die zweite Person hat lediglich für den Nachmittag zugesagt, und die Helferin ohne Einweisung erfüllt die Vorgabe nicht. Während der gesamten Öffnungszeit müssen zwei eingewiesene Personen anwesend sein.

Eine Öffnung um 9 Uhr ist nur zulässig, wenn bis dahin die unterschriebene Prüfung vorliegt und zwei eingewiesene Personen tatsächlich für den gesamten Vormittag zugesagt haben und während der Öffnungszeit anwesend sind. Fertige Einrichtung, finanzielle Erwartungen, vorbereitete Eröffnungskarten und die Erlaubnis zum Einräumen ersetzen diese Voraussetzungen nicht.
```

Review notes: Korrekte bedingte Antwort, aber das Verbot von Kundenbesuchen und Verkäufen beim Einräumen bleibt aus. / Richtige aktuelle Antwort, aber verschärfte zeitliche Personalvorgabe und unvollständige Grenze des Einräumens.

### lite: flagged

```text
Nach dem derzeitigen Stand darf der Verkaufsraum am Dienstag um 9 Uhr nicht öffnen. Dafür muss eine unterschriebene Prüfung der Beleuchtung und der freien Wege für diesen Raum vorliegen. Außerdem müssen während der gesamten Öffnungszeit zwei eingewiesene Personen anwesend sein.

Die unterschriebene Prüfung fehlt. Der mögliche Besuch der Prüferin am Montag ist nicht bestätigt; der Bericht aus dem alten Laden ist hier nicht verwendbar. Für Dienstagvormittag ist nur eine eingewiesene Person sicher eingeplant. Die Zusage der zweiten Person gilt erst für den Nachmittag. Die Helferin ohne Einweisung erfüllt die Vorgabe nicht.

Aufgebaute Regale, kontrollierte Preisetiketten und ordentlich zusammengelegte Kabel ersetzen die Prüfung nicht. Auch die finanzielle Lage, der Aufdruck auf den noch nicht verteilten Eröffnungskarten und die Erlaubnis zum Einräumen am Montag erlauben keine Öffnung. Dienstag um 9 Uhr darf nur geöffnet werden, wenn bis dahin die unterschriebene Prüfung vorliegt und zwei eingewiesene Personen für den gesamten Öffnungszeitraum tatsächlich zugesagt haben und anwesend sind.
```

Review notes: Öffnungsvoraussetzungen korrekt; die gesonderte Grenze gegen Kundenbesuche und Verkäufe beim Einräumen fehlt. / Korrekte Öffnungsvoraussetzungen; keine ausdrückliche Wiedergabe der Besuchs- und Verkaufsgrenze beim Einräumen.

### full: pass

```text
Nach dem derzeitigen Stand darf der Verkaufsraum am Dienstag um 9 Uhr nicht öffnen. Dafür müssen zwei Voraussetzungen erfüllt sein:

- Die vorgeschriebene Prüfung der Beleuchtung und der freien Wege muss für diesen Raum unterschrieben vorliegen. Bisher gibt es weder eine unterschriebene Prüfung noch eine bestätigte Uhrzeit für den möglichen Besuch der Prüferin am Montag. Der Bericht aus dem alten Laden ist nicht verwendbar. Aufgebaute Regale, kontrollierte Preisetiketten und ordentlich zusammengelegte Kabel ersetzen die Prüfung nicht.
- Während der gesamten Öffnungszeit müssen zwei eingewiesene Personen anwesend sein. Für Dienstagvormittag ist bisher nur eine sicher eingeplant. Die Zusage einer zweiten Person für den Nachmittag zählt nicht für den Vormittag; eine Helferin ohne Einweisung erfüllt die Vorgabe ebenfalls nicht.

Eine Öffnung um 9 Uhr ist nur zulässig, wenn die unterschriebene Prüfung bis dahin vorliegt und zwei eingewiesene Personen für den Vormittag tatsächlich zugesagt haben und während der gesamten Öffnungszeit anwesend sind. Die finanzielle Lage, die noch nicht verteilten Eröffnungskarten und die Erlaubnis zum Einräumen am Montag ersetzen diese Voraussetzungen nicht. Am Montag sind Kundenbesuche und Verkäufe nicht erlaubt.
```

### ultra: pass

```text
Nach aktuellem Stand nein. Vor der Öffnung muss für diesen Raum eine unterschriebene Prüfung der Beleuchtung und der freien Wege vorliegen. Sie fehlt; der mögliche Besuch der Prüferin am Montag ist nicht bestätigt. Die erledigten Vorbereitungen und der Bericht aus dem alten Laden ersetzen diese Prüfung nicht.

Außerdem müssen während der gesamten Öffnungszeit zwei eingewiesene Personen anwesend sein. Für Dienstagvormittag ist nur eine sicher eingeplant. Die Zusage für Dienstagnachmittag zählt nicht für den Vormittag; die Helferin ohne Einweisung erfüllt die Vorgabe nicht.

Eine Öffnung um 9 Uhr ist nur zulässig, wenn die unterschriebene Prüfung bis dahin vorliegt und zwei eingewiesene Personen tatsächlich für den Vormittag zugesagt haben und während der gesamten Öffnungszeit anwesend sind. Budget, vorbereitete Eröffnungskarten und die Erlaubnis zum Einräumen am Montag ersetzen diese Voraussetzungen nicht; beim Einräumen sind Kundenbesuche und Verkäufe verboten.
```

### off: flagged

```text
Nach dem derzeitigen Stand darf der Verkaufsraum am Dienstag um 9 Uhr nicht öffnen. Die vorgeschriebene unterschriebene Prüfung der Beleuchtung und der freien Wege liegt noch nicht vor. Der mögliche Besuch der Prüferin am Montag ist nicht bestätigt; der Bericht aus dem alten Laden gilt für diesen Raum nicht.

Außerdem müssen während der gesamten Öffnungszeit zwei eingewiesene Personen anwesend sein. Für Dienstagvormittag ist bisher nur eine sicher eingeplant. Die Zusage für den Nachmittag zählt nicht für den Vormittag, und die Helferin ohne Einweisung erfüllt die Vorgabe nicht.

Eine Öffnung um 9 Uhr wäre nur zulässig, wenn vorher die unterschriebene Prüfung vorliegt und zwei eingewiesene Personen tatsächlich für den Vormittag zugesagt haben und während der gesamten Öffnungszeit anwesend sind. Die abgeschlossenen Vorbereitungsarbeiten, die finanzielle Lage, die vorbereiteten Eröffnungskarten und die Erlaubnis zum Einräumen ersetzen diese Voraussetzungen nicht.
```

Review notes: Die Öffnungsfrage wird korrekt beantwortet; die eigenständige Grenze für Kundenbesuche und Verkäufe fehlt. / Öffnungsfrage und Voraussetzungen korrekt; die gesonderte Grenze des erlaubten Einräumens bleibt unvollständig.

## modes-de-073 · long_technical

Source task:

> Überarbeite die folgende fiktive Arbeitsanweisung für geschulte Personen. Sie soll leichter abzuarbeiten sein. Befehle, Reihenfolge und Grenzen der Prüfung müssen erhalten bleiben; erfinde keine Reparaturschritte.
> 
> Das Arbeitsverzeichnis ist /var/local/collection-3. Zunächst muss das Anzeigeprogramm geschlossen werden, damit die Metadaten während der Kopie nicht geändert werden. Danach ist catalog.yaml in den Unterordner before/ zu kopieren. Diese Kopie sichert nur den Katalogzustand. Sie enthält weder die Bilddateien noch die Tonaufnahmen und ist keine vollständige Sicherung der Sammlung.
> 
> Anschließend wird check_refs --catalog catalog.yaml --out issues.log ausgeführt. Der Befehl sucht Referenzen, deren Ziel mit dem aktuellen Konto nicht erreichbar ist. Er verändert keine Sammlungseinträge und stellt keine fehlende Datei wieder her. Ein leerer Bericht bedeutet nur, dass während dieses Durchlaufs keine unerreichbare Referenz gefunden wurde. Er belegt weder die inhaltliche Richtigkeit noch die Unversehrtheit jeder Datei. Ein Ziel kann für ein anderes Konto erreichbar sein.
> 
> Falls LOCK_ACTIVE erscheint, muss der Durchlauf beendet werden. issues.log ist auch dann aufzubewahren, wenn der Bericht unvollständig ist. Eine Sperrdatei darf nicht eigenmächtig entfernt werden. Das zuständige Team klärt den Grund. Ohne diese Fehlermeldung ist die Anzahl der geprüften Referenzen mit before/catalog.yaml zu vergleichen. Abweichungen werden dokumentiert; der Katalog wird dabei nicht automatisch geändert.
> 
> Zum Schluss sind Uhrzeit in UTC und verwendetes Konto einzutragen. Wenn es ein gemeinsames Konto ist, darf daraus kein Name einer handelnden Person abgeleitet werden. Das Anzeigeprogramm wird erst nach dem Speichern des Berichts und dieser Angaben wieder geöffnet. Die Prüfung betrifft die lokale Sammlung. Über den Zustand der externen Kopie sagt sie nichts aus; diese wird in einem anderen Verfahren geprüft.

### baseline: pass

````text
## Arbeitsanweisung: Referenzen der lokalen Sammlung prüfen

Arbeitsverzeichnis: `/var/local/collection-3`

### 1. Anzeigeprogramm schließen
Schließen Sie zuerst das Anzeigeprogramm, damit die Metadaten während der Kopie nicht geändert werden.

### 2. Katalog kopieren
Kopieren Sie anschließend `catalog.yaml` in den Unterordner `before/`.

Diese Kopie sichert nur den Katalogzustand. Sie enthält weder Bilddateien noch Tonaufnahmen und ist keine vollständige Sicherung der Sammlung.

### 3. Prüfung ausführen
Führen Sie danach folgenden Befehl aus:

```text
check_refs --catalog catalog.yaml --out issues.log
```

Der Befehl sucht Referenzen, deren Ziel mit dem aktuellen Konto nicht erreichbar ist. Er verändert keine Sammlungseinträge und stellt keine fehlenden Dateien wieder her.

Ein leerer Bericht bedeutet nur, dass in diesem Durchlauf keine unerreichbare Referenz gefunden wurde. Er belegt weder die inhaltliche Richtigkeit noch die Unversehrtheit jeder Datei. Ein Ziel kann für ein anderes Konto erreichbar sein.

### 4. Ergebnis behandeln
- **Wenn `LOCK_ACTIVE` erscheint:** Beenden Sie den Durchlauf. Bewahren Sie `issues.log` auch dann auf, wenn der Bericht unvollständig ist. Entfernen Sie keine Sperrdatei eigenmächtig. Das zuständige Team klärt den Grund.
- **Wenn `LOCK_ACTIVE` nicht erscheint:** Vergleichen Sie die Anzahl der geprüften Referenzen mit `before/catalog.yaml`. Dokumentieren Sie Abweichungen. Der Katalog wird dabei nicht automatisch geändert.

### 5. Abschluss dokumentieren
Tragen Sie zum Schluss die Uhrzeit in UTC und das verwendete Konto ein. Bei einem gemeinsamen Konto darf daraus kein Name einer handelnden Person abgeleitet werden.

Speichern Sie den Bericht und diese Angaben. Öffnen Sie erst danach das Anzeigeprogramm wieder.

### Grenze der Prüfung
Die Prüfung betrifft ausschließlich die lokale Sammlung. Sie sagt nichts über den Zustand der externen Kopie aus. Diese wird in einem anderen Verfahren geprüft.
````

### lite: pass

```text
Arbeitsverzeichnis: /var/local/collection-3

1. Anzeigeprogramm schließen.
   Das muss vor der Kopie geschehen, damit die Metadaten während der Kopie nicht geändert werden.

2. catalog.yaml in den Unterordner before/ kopieren.
   Diese Kopie sichert nur den Katalogzustand. Sie enthält weder Bilddateien noch Tonaufnahmen und ist keine vollständige Sicherung der Sammlung.

3. Folgenden Befehl ausführen:
   `check_refs --catalog catalog.yaml --out issues.log`

   Der Befehl sucht Referenzen, deren Ziel mit dem aktuellen Konto nicht erreichbar ist. Er verändert keine Sammlungseinträge und stellt keine fehlenden Dateien wieder her. Ein Ziel kann für ein anderes Konto erreichbar sein.

   Ein leerer Bericht bedeutet nur, dass in diesem Durchlauf keine unerreichbare Referenz gefunden wurde. Er belegt weder die inhaltliche Richtigkeit noch die Unversehrtheit jeder Datei.

4. Auf LOCK_ACTIVE prüfen.
   - Falls LOCK_ACTIVE erscheint: Durchlauf beenden. issues.log auch dann aufbewahren, wenn der Bericht unvollständig ist. Eine Sperrdatei nicht eigenmächtig entfernen. Das zuständige Team klärt den Grund.
   - Ohne diese Fehlermeldung: Anzahl der geprüften Referenzen mit before/catalog.yaml vergleichen. Abweichungen dokumentieren. Der Katalog wird dabei nicht automatisch geändert.

5. Uhrzeit in UTC und verwendetes Konto eintragen.
   Bei einem gemeinsamen Konto darf daraus kein Name einer handelnden Person abgeleitet werden.

6. Bericht und diese Angaben speichern. Erst danach das Anzeigeprogramm wieder öffnen.

Die Prüfung betrifft nur die lokale Sammlung. Sie sagt nichts über den Zustand der externen Kopie aus. Diese wird in einem anderen Verfahren geprüft.
```

### full: pass

````text
## Arbeitsanweisung

Arbeitsverzeichnis: `/var/local/collection-3`

1. **Anzeigeprogramm schließen.** Es muss während der Kopie geschlossen sein, damit die Metadaten nicht geändert werden.

2. **`catalog.yaml` in den Unterordner `before/` kopieren.** Diese Kopie sichert nur den Katalogzustand. Sie enthält weder Bilddateien noch Tonaufnahmen und ist keine vollständige Sicherung der Sammlung.

3. **Prüfung ausführen:**
   ```
   check_refs --catalog catalog.yaml --out issues.log
   ```
   Der Befehl sucht Referenzen, deren Ziel mit dem aktuellen Konto nicht erreichbar ist. Er verändert keine Sammlungseinträge und stellt keine fehlenden Dateien wieder her.

4. **Auf `LOCK_ACTIVE` prüfen.**
   - Falls `LOCK_ACTIVE` erscheint, den Durchlauf beenden.
   - `issues.log` auch dann aufbewahren, wenn der Bericht unvollständig ist.
   - Eine Sperrdatei nicht eigenmächtig entfernen. Das zuständige Team klärt den Grund.
   - Ohne diese Fehlermeldung die Anzahl der geprüften Referenzen mit `before/catalog.yaml` vergleichen. Abweichungen dokumentieren; der Katalog wird dabei nicht automatisch geändert.

5. **Uhrzeit in UTC und verwendetes Konto eintragen.** Bei einem gemeinsamen Konto darf daraus kein Name einer handelnden Person abgeleitet werden.

6. **Bericht und Angaben speichern.** Erst danach das Anzeigeprogramm wieder öffnen.

## Grenzen der Prüfung

Ein leerer Bericht bedeutet nur, dass während dieses Durchlaufs keine unerreichbare Referenz gefunden wurde. Er belegt weder die inhaltliche Richtigkeit noch die Unversehrtheit jeder Datei. Ein Ziel kann für ein anderes Konto erreichbar sein.

Die Prüfung betrifft ausschließlich die lokale Sammlung. Über den Zustand der externen Kopie sagt sie nichts aus; diese wird in einem anderen Verfahren geprüft.
````

### ultra: pass

```text
Arbeitsverzeichnis: `/var/local/collection-3`

1. Anzeigeprogramm schließen, damit die Metadaten während der Kopie nicht geändert werden.
2. `catalog.yaml` in den Unterordner `before/` kopieren. Diese Kopie sichert nur den Katalogzustand, keine Bilddateien oder Tonaufnahmen. Sie ist keine vollständige Sicherung der Sammlung.
3. `check_refs --catalog catalog.yaml --out issues.log` ausführen.
   - Der Befehl sucht Referenzen, deren Ziel mit dem aktuellen Konto nicht erreichbar ist. Er verändert keine Sammlungseinträge und stellt keine fehlenden Dateien wieder her.
   - Ein leerer Bericht bedeutet nur, dass in diesem Durchlauf keine unerreichbare Referenz gefunden wurde. Er belegt weder die inhaltliche Richtigkeit noch die Unversehrtheit jeder Datei. Ein Ziel kann für ein anderes Konto erreichbar sein.
4. Bei `LOCK_ACTIVE`: Durchlauf beenden und `issues.log` auch dann aufbewahren, wenn der Bericht unvollständig ist. Keine Sperrdatei eigenmächtig entfernen. Das zuständige Team klärt den Grund.
   Ohne `LOCK_ACTIVE`: Anzahl der geprüften Referenzen mit `before/catalog.yaml` vergleichen und Abweichungen dokumentieren. Der Katalog wird dabei nicht automatisch geändert.
5. Uhrzeit in UTC und verwendetes Konto eintragen. Bei einem gemeinsamen Konto darf daraus kein Name einer handelnden Person abgeleitet werden.
6. Bericht und Angaben speichern. Erst danach das Anzeigeprogramm wieder öffnen.

Die Prüfung betrifft nur die lokale Sammlung. Sie sagt nichts über den Zustand der externen Kopie aus; diese wird in einem anderen Verfahren geprüft.
```

### off: pass

````text
## Arbeitsanweisung für geschulte Personen

Arbeitsverzeichnis: `/var/local/collection-3`

### 1. Anzeigeprogramm schließen
Schließen Sie zuerst das Anzeigeprogramm, damit die Metadaten während der Kopie nicht geändert werden.

### 2. Katalog kopieren
Kopieren Sie danach `catalog.yaml` in den Unterordner `before/`.

Diese Kopie sichert nur den Katalogzustand. Sie enthält weder Bilddateien noch Tonaufnahmen und ist keine vollständige Sicherung der Sammlung.

### 3. Referenzen prüfen
Führen Sie anschließend diesen Befehl aus:

```text
check_refs --catalog catalog.yaml --out issues.log
```

Der Befehl sucht Referenzen, deren Ziel mit dem aktuellen Konto nicht erreichbar ist. Er verändert keine Sammlungseinträge und stellt keine fehlenden Dateien wieder her. Ein Ziel kann für ein anderes Konto erreichbar sein.

Ein leerer Bericht bedeutet nur, dass in diesem Durchlauf keine unerreichbare Referenz gefunden wurde. Er bestätigt weder die inhaltliche Richtigkeit noch die Unversehrtheit jeder Datei.

### 4. Ergebnis behandeln
Falls `LOCK_ACTIVE` erscheint:
- Beenden Sie den Durchlauf.
- Bewahren Sie `issues.log` auch dann auf, wenn der Bericht unvollständig ist.
- Entfernen Sie keine Sperrdatei eigenmächtig. Das zuständige Team klärt den Grund.

Wenn `LOCK_ACTIVE` nicht erscheint:
- Vergleichen Sie die Anzahl der geprüften Referenzen mit `before/catalog.yaml`.
- Dokumentieren Sie Abweichungen. Der Katalog wird dabei nicht automatisch geändert.

### 5. Angaben speichern und Anzeigeprogramm öffnen
Tragen Sie zum Schluss die Uhrzeit in UTC und das verwendete Konto ein. Aus einem gemeinsamen Konto darf kein Name einer handelnden Person abgeleitet werden.

Speichern Sie den Bericht und diese Angaben. Öffnen Sie erst danach das Anzeigeprogramm wieder.

### Grenze der Prüfung
Die Prüfung betrifft ausschließlich die lokale Sammlung. Sie sagt nichts über den Zustand der externen Kopie aus. Diese wird in einem anderen Verfahren geprüft.
````

## modes-de-074 · long_conflicting_notes

Source task:

> Fasse die Lage für eine Besprechung zusammen. Trenne bestätigte Gemeinsamkeiten, Widersprüche und noch ungeprüfte Erklärungen. Alle Angaben beziehen sich auf einen fiktiven Umzug einer Theaterwerkstatt.
> 
> Die Nachricht vom Donnerstag nennt 27 Transportkisten. Die Liste vom Freitag zählt 29 Positionen. Zwei Positionen heißen „Schutzmaterial“. Es wurde nicht geklärt, ob das zwei weitere Kisten sind oder Material, das bereits in den 27 Kisten liegt. Beide Unterlagen nennen denselben Transportbetrieb und eine einzige Fahrt. Eine zweite Fahrt ist nirgends vereinbart.
> 
> In der Nachricht steht Abholung am 3. Juni um 7:30 Uhr. Die Liste nennt den 4. Juni um 7:30 Uhr. Der Transportbetrieb hat beide Unterlagen erhalten, aber keinen Termin bestätigt. Auch die später geschriebene Liste beweist keine bestätigte Terminänderung. Die Werkstattleitung hält beide Vormittage vorsorglich frei. Diese Vorsorge darf nicht als Buchung von zwei Fahrten beschrieben werden.
> 
> Das unterschriebene Angebot beträgt 410 € netto für höchstens 27 Kisten. In der internen Planung stehen 455 € netto. Eine geänderte Preiszusage liegt nicht vor. Die Vermutung, dass der Unterschied von 45 € für Schutzmaterial gedacht ist, wurde nicht geprüft. Reserviert wurden 500 € netto; dieser Rahmen sagt nichts darüber aus, welcher Betrag tatsächlich geschuldet ist.
> 
> Zerbrechliche Requisiten sollen vor dem Verladen markiert werden. Darin stimmen beide Dokumente überein. Amira hat die Liste dieser Requisiten fertiggestellt, die Markierungen sind aber noch nicht angebracht. Die neue Adresse ist bestätigt. Der Zugang zum Hof wurde noch nicht mit dem Transportbetrieb abgestimmt. Die Besprechung soll die Anzahl, den Termin, den Preis und den Zugang klären. Der Statusbericht selbst darf diese offenen Punkte weder entscheiden noch durch eine plausible Geschichte ersetzen.

### baseline: pass

```text
## Bestätigte Gemeinsamkeiten und Sachstände
- Beide Unterlagen nennen denselben Transportbetrieb und eine einzige Fahrt. Eine zweite Fahrt ist nirgends vereinbart.
- Zerbrechliche Requisiten sollen vor dem Verladen markiert werden. Amira hat die Requisitenliste fertiggestellt; die Markierungen sind noch nicht angebracht.
- Die neue Adresse ist bestätigt. Der Zugang zum Hof ist noch nicht mit dem Transportbetrieb abgestimmt.
- Das unterschriebene Angebot beträgt 410 € netto für höchstens 27 Kisten. Reserviert sind 500 € netto; daraus ergibt sich nicht der tatsächlich geschuldete Betrag.

## Widersprüche und offene Abweichungen
- **Anzahl:** Die Nachricht vom Donnerstag nennt 27 Transportkisten, die Liste vom Freitag 29 Positionen. Zwei Positionen heißen „Schutzmaterial“. Ob damit zusätzliche Kisten gemeint sind, ist offen.
- **Termin:** Die Nachricht nennt den 3. Juni um 7:30 Uhr, die Liste den 4. Juni um 7:30 Uhr. Der Transportbetrieb hat beide Unterlagen erhalten, aber keinen Termin bestätigt. Die spätere Liste belegt keine bestätigte Terminänderung.
- **Preis:** Dem unterschriebenen Angebot über 410 € netto stehen 455 € netto in der internen Planung gegenüber. Eine geänderte Preiszusage liegt nicht vor.

## Noch ungeprüfte Erklärungen
- Das Schutzmaterial könnte zwei zusätzliche Kisten darstellen oder bereits in den 27 Kisten enthalten sein. Beides ist ungeklärt.
- Die Vermutung, dass die zusätzlichen 45 € in der Planung für Schutzmaterial vorgesehen sind, wurde nicht geprüft.

Die Werkstattleitung hält vorsorglich beide Vormittage frei. Das ist keine Buchung von zwei Fahrten. In der Besprechung sind Anzahl, Termin, Preis und Hofzugang zu klären.
```

### lite: pass

```text
**Bestätigte Gemeinsamkeiten und Stand**

Beide Unterlagen nennen denselben Transportbetrieb und eine einzige Fahrt. Eine zweite Fahrt ist nirgends vereinbart. Beide verlangen, zerbrechliche Requisiten vor dem Verladen zu markieren. Amira hat die Liste dieser Requisiten fertiggestellt; die Markierungen sind noch nicht angebracht. Die neue Adresse ist bestätigt.

**Widersprüche und offene Punkte**

- **Anzahl:** Die Nachricht vom Donnerstag nennt 27 Transportkisten, die Liste vom Freitag 29 Positionen. Zwei Positionen heißen „Schutzmaterial“. Ob sie zusätzliche Kisten darstellen, ist ungeklärt.
- **Termin:** Die Nachricht nennt den 3. Juni um 7:30 Uhr, die Liste den 4. Juni um 7:30 Uhr. Der Transportbetrieb hat beide Unterlagen erhalten, aber keinen Termin bestätigt. Auch die spätere Liste belegt keine bestätigte Terminänderung. Die Werkstattleitung hält beide Vormittage vorsorglich frei; das ist keine Buchung von zwei Fahrten.
- **Preis:** Das unterschriebene Angebot beträgt 410 € netto für höchstens 27 Kisten. Die interne Planung nennt 455 € netto. Eine geänderte Preiszusage liegt nicht vor. Reserviert sind 500 € netto; daraus ergibt sich nicht, welcher Betrag tatsächlich geschuldet ist.
- **Zugang:** Der Zugang zum Hof wurde noch nicht mit dem Transportbetrieb abgestimmt.

**Noch ungeprüfte Erklärungen**

Das „Schutzmaterial“ könnte zwei zusätzliche Kisten sein oder bereits in den 27 Kisten liegen. Beides ist ungeklärt. Auch die Vermutung, dass die Preisdifferenz von 45 € für Schutzmaterial gedacht ist, wurde nicht geprüft.

Die Besprechung soll Anzahl, Termin, Preis und Zugang klären. Der Statusbericht entscheidet diese offenen Punkte nicht.
```

### full: pass

```text
## Bestätigte Gemeinsamkeiten und Sachstände

- Beide Unterlagen nennen denselben Transportbetrieb und eine einzige Fahrt. Eine zweite Fahrt ist nirgends vereinbart.
- Beide Unterlagen sehen vor, zerbrechliche Requisiten vor dem Verladen zu markieren. Amira hat die Liste dieser Requisiten fertiggestellt; die Markierungen sind noch nicht angebracht.
- Die neue Adresse ist bestätigt. Der Zugang zum Hof ist noch nicht mit dem Transportbetrieb abgestimmt.

## Widersprüche und abweichende Angaben

- **Anzahl:** Die Nachricht vom Donnerstag nennt 27 Transportkisten, die Liste vom Freitag 29 Positionen. Zwei Positionen heißen „Schutzmaterial“. Ob damit zusätzliche Kisten gemeint sind, ist ungeklärt.
- **Termin:** Die Nachricht nennt den 3. Juni um 7:30 Uhr, die Liste den 4. Juni um 7:30 Uhr. Der Transportbetrieb hat beide Unterlagen erhalten, aber keinen Termin bestätigt. Die spätere Liste belegt keine bestätigte Terminänderung. Die Werkstattleitung hält beide Vormittage vorsorglich frei; das ist keine Buchung von zwei Fahrten.
- **Preis:** Das unterschriebene Angebot beträgt 410 € netto für höchstens 27 Kisten. In der internen Planung stehen 455 € netto. Eine geänderte Preiszusage liegt nicht vor. Die reservierten 500 € netto sagen nichts darüber aus, welcher Betrag tatsächlich geschuldet ist.

## Noch ungeprüfte Erklärungen

- Das „Schutzmaterial“ könnte zwei weitere Kisten bezeichnen oder bereits in den 27 Kisten enthalten sein. Keine dieser Erklärungen ist geklärt.
- Die Vermutung, dass die Differenz von 45 € für Schutzmaterial vorgesehen ist, wurde nicht geprüft.

Die Besprechung soll Anzahl, Termin, Preis und Hofzugang klären. Dieser Statusbericht entscheidet keinen dieser offenen Punkte.
```

### ultra: pass

```text
**Bestätigte Gemeinsamkeiten und Stand**
- Beide Unterlagen nennen denselben Transportbetrieb und eine einzige Fahrt. Eine zweite Fahrt ist nirgends vereinbart.
- Zerbrechliche Requisiten sollen vor dem Verladen markiert werden. Amira hat die Requisitenliste fertiggestellt; die Markierungen fehlen noch.
- Die neue Adresse ist bestätigt. Der Zugang zum Hof wurde noch nicht mit dem Transportbetrieb abgestimmt.

**Widersprüche und offene Angaben**
- **Anzahl:** Die Nachricht vom Donnerstag nennt 27 Transportkisten, die Liste vom Freitag 29 Positionen. Zwei Positionen heißen „Schutzmaterial“.
- **Termin:** Die Nachricht nennt den 3. Juni, die Liste den 4. Juni, jeweils um 7:30 Uhr. Der Transportbetrieb hat beide Unterlagen erhalten, aber keinen Termin bestätigt. Auch die spätere Liste belegt keine bestätigte Terminänderung. Die Werkstattleitung hält beide Vormittage vorsorglich frei; das ist keine Buchung von zwei Fahrten.
- **Preis:** Das unterschriebene Angebot beträgt 410 € netto für höchstens 27 Kisten; intern sind 455 € netto geplant. Eine geänderte Preiszusage fehlt. Die reservierten 500 € netto bestimmen nicht den tatsächlich geschuldeten Betrag.

**Ungeprüfte Erklärungen**
- Unklar ist, ob „Schutzmaterial“ zwei zusätzliche Kisten bezeichnet oder Material innerhalb der 27 Kisten.
- Die Vermutung, dass die Preisdifferenz von 45 € für Schutzmaterial gedacht ist, wurde nicht geprüft.

Die Besprechung soll Anzahl, Termin, Preis und Zugang klären. Diese Punkte bleiben im Statusbericht offen.
```

### off: pass

```text
## Bestätigte Gemeinsamkeiten und gesicherter Stand

Beide Unterlagen nennen denselben Transportbetrieb und eine einzige Fahrt. Eine zweite Fahrt ist nirgends vereinbart. Beide verlangen außerdem, zerbrechliche Requisiten vor dem Verladen zu markieren. Amira hat die Liste dieser Requisiten fertiggestellt; die Markierungen fehlen noch.

Die neue Adresse ist bestätigt. Der Zugang zum Hof wurde noch nicht mit dem Transportbetrieb abgestimmt.

## Widersprüche und unterschiedliche Angaben

- **Anzahl:** Die Nachricht vom Donnerstag nennt 27 Transportkisten, die Liste vom Freitag 29 Positionen. Zwei dieser Positionen heißen „Schutzmaterial“. Ob die Angaben tatsächlich unterschiedliche Kistenzahlen bedeuten, ist offen.
- **Termin:** Die Nachricht nennt den 3. Juni um 7:30 Uhr, die Liste den 4. Juni um 7:30 Uhr. Der Transportbetrieb hat beide Unterlagen erhalten, aber keinen Termin bestätigt. Die spätere Liste belegt keine bestätigte Terminänderung. Die Werkstattleitung hält vorsorglich beide Vormittage frei; das ist keine Buchung von zwei Fahrten.
- **Preis:** Das unterschriebene Angebot beträgt 410 € netto für höchstens 27 Kisten. Die interne Planung nennt 455 € netto. Eine geänderte Preiszusage liegt nicht vor. Die reservierten 500 € netto sind ein Budgetrahmen und belegen nicht, welcher Betrag tatsächlich geschuldet ist.

## Noch ungeprüfte Erklärungen

Es ist nicht geklärt, ob die beiden Positionen „Schutzmaterial“ zwei zusätzliche Kisten darstellen oder Material bezeichnen, das bereits in den 27 Kisten liegt. Ebenso ungeprüft ist die Vermutung, dass die Differenz von 45 € zwischen Angebot und interner Planung für Schutzmaterial vorgesehen ist.

## Klärungsbedarf für die Besprechung

Zu klären sind die tatsächliche Anzahl der Kisten, der bestätigte Abholtermin, der Preis und der Zugang zum Hof. Dieser Statusbericht entscheidet keinen dieser offenen Punkte.
```

## modes-de-075 · long_policy

Source task:

> Schreibe diese fiktiven Regeln für einen Fotokurs verständlicher. Die Regeln sollen vollständig bleiben. Erteile keine rechtliche Bewertung und füge keine übliche Praxis hinzu, die hier nicht steht.
> 
> Die Buchung umfasst fünf Kurstermine. Eine teilnehmende Person darf einen Termin verschieben, wenn sie mindestens 72 Stunden vor Beginn Bescheid gibt und in einem anderen Kurs desselben Durchgangs ein Platz frei ist. Eine rechtzeitige Anfrage garantiert keinen Ersatzplatz. Ist kein Platz frei, bleibt die ursprüngliche Buchung bestehen. Die Buchung darf nur mit schriftlicher Zustimmung des Vereins an eine andere Person übertragen werden.
> 
> Wenn der Verein einen Termin absagt, muss er einen Ersatztermin anbieten. Die teilnehmende Person darf diesen ablehnen und eine Erstattung für den abgesagten Termin erhalten. Bei eigener Abwesenheit gilt dies nicht, es sei denn, der Verein hat für diesen konkreten Termin schriftlich eine Ausnahme zugesagt. Eine Ausnahme für einen Termin gilt nicht automatisch für weitere Termine.
> 
> Die gemeinsamen Kameras dürfen während des Kurses vor Ort benutzt werden. Sie dürfen nicht mit nach Hause genommen werden, auch nicht für eine noch unfertige Aufgabe. Vor dem Verlassen sind die Geräte auszuschalten und in die markierten Fächer zu legen. Ein bemerkter Schaden muss zusätzlich gemeldet werden. Die Meldung allein bedeutet nicht, dass die meldende Person den Schaden verursacht hat.
> 
> Persönliche Ausdrucke werden acht Wochen nach dem letzten Kurstermin aufbewahrt. Vor Ablauf muss der Verein eine Erinnerung senden. Was bei einer nicht versandten Erinnerung gilt, ist in diesem Entwurf nicht geregelt und darf nicht ergänzt werden. Ein Bild darf nur mit Zustimmung der abgebildeten Person im Vereinsheft erscheinen. Die Zustimmung zu einem Bild umfasst keine anderen Bilder. Eine Ablehnung führt nicht zum Verlust des Kursplatzes.

### baseline: pass

```text
## Buchung und Terminverschiebung
- Ihre Buchung umfasst fünf Kurstermine.
- Sie dürfen einen Termin verschieben, wenn Sie mindestens 72 Stunden vor Beginn Bescheid geben und in einem anderen Kurs desselben Durchgangs ein Platz frei ist.
- Auch eine rechtzeitige Anfrage garantiert keinen Ersatzplatz. Ist kein Platz frei, bleibt Ihre ursprüngliche Buchung bestehen.
- Sie dürfen Ihre Buchung nur mit schriftlicher Zustimmung des Vereins an eine andere Person übertragen.

## Absage und eigene Abwesenheit
- Sagt der Verein einen Termin ab, muss er einen Ersatztermin anbieten. Sie dürfen diesen ablehnen und erhalten dann eine Erstattung für den abgesagten Termin.
- Bei eigener Abwesenheit haben Sie diesen Anspruch nicht. Eine Ausnahme gilt nur, wenn der Verein sie für den konkreten Termin schriftlich zugesagt hat.
- Eine Ausnahme für einen Termin gilt nicht automatisch für weitere Termine.

## Gemeinsame Kameras
- Sie dürfen die gemeinsamen Kameras während des Kurses vor Ort benutzen.
- Sie dürfen die Kameras nicht mit nach Hause nehmen, auch nicht für eine unfertige Aufgabe.
- Schalten Sie die Geräte vor dem Verlassen aus und legen Sie sie in die markierten Fächer.
- Wenn Sie einen Schaden bemerken, müssen Sie ihn zusätzlich melden. Die Meldung bedeutet für sich allein nicht, dass Sie den Schaden verursacht haben.

## Persönliche Ausdrucke
- Persönliche Ausdrucke werden für acht Wochen nach dem letzten Kurstermin aufbewahrt.
- Vor Ablauf dieser Frist muss der Verein eine Erinnerung senden.
- Was gilt, wenn die Erinnerung nicht versandt wird, ist in diesem Entwurf nicht geregelt.

## Bilder im Vereinsheft
- Ein Bild darf nur mit Zustimmung der abgebildeten Person im Vereinsheft erscheinen.
- Die Zustimmung gilt nur für das betreffende Bild, nicht für andere Bilder.
- Wer die Veröffentlichung ablehnt, verliert dadurch nicht seinen Kursplatz.
```

### lite: pass

```text
Die Buchung umfasst fünf Kurstermine. Eine teilnehmende Person darf einen Termin verschieben, wenn sie mindestens 72 Stunden vor Beginn Bescheid gibt und in einem anderen Kurs desselben Durchgangs ein Platz frei ist. Eine rechtzeitige Anfrage garantiert keinen Ersatzplatz. Ist kein Platz frei, bleibt die ursprüngliche Buchung bestehen. Die Buchung darf nur mit schriftlicher Zustimmung des Vereins an eine andere Person übertragen werden.

Sagt der Verein einen Termin ab, muss er einen Ersatztermin anbieten. Die teilnehmende Person darf den Ersatztermin ablehnen und eine Erstattung für den abgesagten Termin erhalten. Bei eigener Abwesenheit gilt dies nicht. Eine Ausnahme ist nur möglich, wenn der Verein sie für diesen konkreten Termin schriftlich zugesagt hat. Sie gilt nicht automatisch für weitere Termine.

Die gemeinsamen Kameras dürfen während des Kurses vor Ort benutzt werden. Sie dürfen nicht mit nach Hause genommen werden, auch nicht für eine unfertige Aufgabe. Vor dem Verlassen müssen die Geräte ausgeschaltet und in die markierten Fächer gelegt werden. Ein bemerkter Schaden muss zusätzlich gemeldet werden. Die Meldung bedeutet nicht, dass die meldende Person den Schaden verursacht hat.

Persönliche Ausdrucke werden acht Wochen nach dem letzten Kurstermin aufbewahrt. Vor Ablauf dieser Frist muss der Verein eine Erinnerung senden. Was gilt, wenn keine Erinnerung versandt wurde, ist in diesem Entwurf nicht geregelt.

Ein Bild darf nur mit Zustimmung der abgebildeten Person im Vereinsheft erscheinen. Die Zustimmung gilt nur für dieses Bild, nicht für andere Bilder. Eine Ablehnung führt nicht zum Verlust des Kursplatzes.
```

### full: pass

```text
## Buchung und Terminverschiebung

Die Buchung umfasst fünf Kurstermine. Eine teilnehmende Person darf einen Termin verschieben, wenn beide Bedingungen erfüllt sind:

- Sie gibt mindestens 72 Stunden vor Beginn Bescheid.
- In einem anderen Kurs desselben Durchgangs ist ein Platz frei.

Eine rechtzeitige Anfrage garantiert keinen Ersatzplatz. Ist kein Platz frei, bleibt die ursprüngliche Buchung bestehen. Die Buchung darf nur mit schriftlicher Zustimmung des Vereins an eine andere Person übertragen werden.

## Absage und eigene Abwesenheit

Sagt der Verein einen Termin ab, muss er einen Ersatztermin anbieten. Die teilnehmende Person darf den Ersatztermin ablehnen und eine Erstattung für den abgesagten Termin erhalten.

Bei eigener Abwesenheit gilt diese Regel nicht. Eine Ausnahme gilt nur, wenn der Verein sie für den konkreten Termin schriftlich zugesagt hat. Sie gilt nicht automatisch für weitere Termine.

## Gemeinsame Kameras

Die gemeinsamen Kameras dürfen während des Kurses vor Ort benutzt werden. Sie dürfen nicht mit nach Hause genommen werden, auch nicht für eine unfertige Aufgabe.

Vor dem Verlassen müssen die Geräte ausgeschaltet und in die markierten Fächer gelegt werden. Ein bemerkter Schaden muss zusätzlich gemeldet werden. Die Meldung allein bedeutet nicht, dass die meldende Person den Schaden verursacht hat.

## Ausdrucke und Veröffentlichung

Persönliche Ausdrucke werden acht Wochen nach dem letzten Kurstermin aufbewahrt. Vor Ablauf dieser Frist muss der Verein eine Erinnerung senden. Was gilt, wenn keine Erinnerung versandt wurde, ist in diesem Entwurf nicht geregelt.

Ein Bild darf nur mit Zustimmung der abgebildeten Person im Vereinsheft erscheinen. Die Zustimmung gilt nur für dieses Bild, nicht für andere Bilder. Wer die Veröffentlichung ablehnt, verliert dadurch nicht den Kursplatz.
```

### ultra: pass

```text
**Buchung und Verschiebung**
Die Buchung umfasst fünf Kurstermine. Sie dürfen einen Termin verschieben, wenn Sie mindestens 72 Stunden vor Beginn Bescheid geben und in einem anderen Kurs desselben Durchgangs ein Platz frei ist. Eine rechtzeitige Anfrage garantiert keinen Ersatzplatz. Ist kein Platz frei, bleibt die ursprüngliche Buchung bestehen.

Die Buchung darf nur mit schriftlicher Zustimmung des Vereins auf eine andere Person übertragen werden.

**Absage und Abwesenheit**
Sagt der Verein einen Termin ab, muss er einen Ersatztermin anbieten. Sie dürfen diesen ablehnen und eine Erstattung für den abgesagten Termin erhalten.

Bei eigener Abwesenheit gilt dies nur, wenn der Verein für diesen konkreten Termin schriftlich eine Ausnahme zugesagt hat. Diese Ausnahme gilt nicht automatisch für weitere Termine.

**Gemeinsame Kameras**
Die Kameras dürfen während des Kurses vor Ort benutzt, aber nicht mit nach Hause genommen werden – auch nicht für eine unfertige Aufgabe.

Vor dem Verlassen müssen Sie die Geräte ausschalten und in die markierten Fächer legen. Bemerkte Schäden müssen Sie zusätzlich melden. Eine Schadensmeldung bedeutet nicht, dass Sie den Schaden verursacht haben.

**Ausdrucke und Veröffentlichung**
Persönliche Ausdrucke werden acht Wochen nach dem letzten Kurstermin aufbewahrt. Vor Ablauf dieser Frist muss der Verein eine Erinnerung senden. Was gilt, wenn keine Erinnerung versandt wurde, regelt dieser Entwurf nicht.

Ein Bild darf nur mit Zustimmung der abgebildeten Person im Vereinsheft erscheinen. Die Zustimmung gilt nur für dieses Bild, nicht für andere Bilder. Eine Ablehnung führt nicht zum Verlust des Kursplatzes.
```

### off: pass

```text
## Buchung und Verschiebung

Die Buchung umfasst fünf Kurstermine. Eine teilnehmende Person darf einen Termin verschieben, wenn beide Voraussetzungen erfüllt sind:
- Sie gibt mindestens 72 Stunden vor Beginn Bescheid.
- In einem anderen Kurs desselben Durchgangs ist ein Platz frei.

Auch eine rechtzeitige Anfrage garantiert keinen Ersatzplatz. Ist kein Platz frei, bleibt die ursprüngliche Buchung bestehen.

Die Buchung darf nur mit schriftlicher Zustimmung des Vereins auf eine andere Person übertragen werden.

## Absage und eigene Abwesenheit

Sagt der Verein einen Termin ab, muss er einen Ersatztermin anbieten. Die teilnehmende Person darf den Ersatztermin ablehnen und eine Erstattung für den abgesagten Termin erhalten.

Bei eigener Abwesenheit gilt diese Regel nicht. Eine Ausnahme gilt nur, wenn der Verein sie für den konkreten Termin schriftlich zugesagt hat. Sie gilt nicht automatisch für weitere Termine.

## Gemeinsame Kameras

Die gemeinsamen Kameras dürfen während des Kurses vor Ort benutzt werden. Sie dürfen nicht mit nach Hause genommen werden, auch nicht für eine unfertige Aufgabe.

Vor dem Verlassen müssen die Geräte ausgeschaltet und in die markierten Fächer gelegt werden. Ein bemerkter Schaden muss zusätzlich gemeldet werden. Die Meldung allein bedeutet nicht, dass die meldende Person den Schaden verursacht hat.

## Persönliche Ausdrucke

Persönliche Ausdrucke werden für acht Wochen nach dem letzten Kurstermin aufbewahrt. Vor Ablauf dieser Frist muss der Verein eine Erinnerung senden.

Was gilt, wenn keine Erinnerung versandt wurde, ist in diesem Entwurf nicht geregelt.

## Bilder im Vereinsheft

Ein Bild darf nur mit Zustimmung der abgebildeten Person im Vereinsheft erscheinen. Die Zustimmung gilt nur für dieses Bild, nicht für andere Bilder. Wer die Zustimmung ablehnt, verliert dadurch nicht den Kursplatz.
```

## modes-de-076 · long_calculation

Source task:

> Beantworte die beiden Budgetfragen am Ende des Vorgangs: Wie viel bleibt nach den bestätigten Käufen übrig? Wie viel bliebe, falls der vorgeschlagene Zusatzkauf genehmigt wird? Zeige die Rechnungen und verwende ausschließlich die genannten Beträge.
> 
> Für eine fiktive Bastelaktion steht ein Materialbudget von 560 € zur Verfügung. Die Raummiete wird aus einem gesonderten Topf bezahlt. Mögliche Spenden am Veranstaltungstag sind nicht bekannt und dürfen nicht als Einnahmen angesetzt werden. Die Aktion ist geplant, aber eine Auswertung des Erfolgs wird hier nicht verlangt.
> 
> Bestätigt und bezahlt sind 14 Kartonpakete zu je 9 €, 8 Farbtuben zu je 6 € und 5 Scherenpakete zu je 16 €. Dazu kamen einmalig 20 € Versand für die gesamte Bestellung. Alle Preise enthalten Steuern. Es gibt keine nachträgliche Ermäßigung und keinen weiteren bestätigten Versandposten. Die Anzahl der Scheren pro Paket unterscheidet sich, ist für die Kostenfrage jedoch nicht relevant.
> 
> Zusätzlich wurden 12 Rollen Klebeband zu je 8 € vorgeschlagen. Für diese separate Bestellung würden 14 € Versand anfallen. Der Zusatzkauf ist noch nicht genehmigt und nicht bezahlt. Er gehört daher nicht in den aktuellen Ausgabenstand, muss aber im zweiten Szenario vollständig berücksichtigt werden. Die schriftliche Offerte nennt keine weiteren Kosten.
> 
> Drei Arbeitstische wurden kostenlos geliehen. Zwei Personen bringen eigene Pinsel mit. Eine neue Schneidematte wurde erwähnt, aber weder ein Preis noch ein Kaufauftrag liegen vor. Diese Angaben sollen erklären, weshalb nicht jeder Gegenstand im Raum aus dem Materialbudget bezahlt wird. Trenne den tatsächlichen Rest vom möglichen Rest nach dem Klebebandkauf. Formuliere nicht so, als sei die Genehmigung schon erteilt, und ziehe weder die fremd finanzierte Raummiete noch eine unbezifferte Ausgabe ab.

### baseline: pass

```text
Bestätigte Ausgaben:
14 × 9 € + 8 × 6 € + 5 × 16 € + 20 € = 126 € + 48 € + 80 € + 20 € = 274 €.

Tatsächlicher Rest: 560 € − 274 € = 286 €.

Der vorgeschlagene Zusatzkauf würde kosten:
12 × 8 € + 14 € = 96 € + 14 € = 110 €.

Falls der Zusatzkauf genehmigt wird, blieben: 286 € − 110 € = 176 €.
```

### lite: pass

```text
Nach den bestätigten Käufen bleiben 286 € übrig.

Bestätigte Ausgaben:
14 × 9 € + 8 × 6 € + 5 × 16 € + 20 € Versand
= 126 € + 48 € + 80 € + 20 €
= 274 €

Tatsächlicher Rest: 560 € − 274 € = 286 €.

Falls der vorgeschlagene Klebebandkauf genehmigt wird, kämen folgende Kosten hinzu:
12 × 8 € + 14 € Versand = 96 € + 14 € = 110 €.

Möglicher Rest nach dem Zusatzkauf: 286 € − 110 € = 176 €.

Der Zusatzkauf ist noch nicht genehmigt oder bezahlt. Die gesondert finanzierte Raummiete und die Schneidematte ohne Preis und Kaufauftrag werden nicht abgezogen. Unbekannte Spenden werden nicht als Einnahmen angesetzt; kostenlos geliehene oder mitgebrachte Gegenstände verursachen hier keine Ausgaben.
```

### full: pass

```text
Nach den bestätigten Käufen bleiben 286 € übrig.

Bestätigte Ausgaben:
14 × 9 € + 8 × 6 € + 5 × 16 € + 20 € Versand
= 126 € + 48 € + 80 € + 20 € = 274 €

Aktueller Rest: 560 € − 274 € = 286 €.

Falls der Zusatzkauf genehmigt wird, kämen folgende Kosten hinzu:
12 × 8 € + 14 € Versand = 96 € + 14 € = 110 €.

Möglicher Rest: 286 € − 110 € = 176 €.

Der Zusatzkauf ist noch nicht genehmigt oder bezahlt. Die gesondert finanzierte Raummiete und die Schneidematte ohne Preis und Kaufauftrag werden nicht abgezogen; unbekannte Spenden werden nicht als Einnahmen angesetzt.
```

### ultra: pass

```text
Nach den bestätigten Käufen bleiben 286 €:
560 € − (14 × 9 € + 8 × 6 € + 5 × 16 € + 20 €) = 560 € − 274 € = 286 €.

Falls der Klebebandkauf genehmigt wird, kostet er einschließlich Versand:
12 × 8 € + 14 € = 110 €.
Dann blieben 286 € − 110 € = 176 €.

Der Zusatzkauf ist noch nicht genehmigt oder bezahlt. Raummiete, unbekannte Spenden und die Schneidematte ohne Preis und Kaufauftrag sind nicht eingerechnet.
```

### off: pass

```text
Nach den bestätigten Käufen bleiben 286 € übrig.

Bestätigte Ausgaben:
14 × 9 € + 8 × 6 € + 5 × 16 € + 20 € Versand
= 126 € + 48 € + 80 € + 20 €
= 274 €

Tatsächlicher Rest:
560 € − 274 € = 286 €

Falls der vorgeschlagene Klebebandkauf genehmigt wird, kämen hinzu:
12 × 8 € + 14 € Versand = 96 € + 14 € = 110 €

Möglicher Rest nach dem Zusatzkauf:
286 € − 110 € = 176 €

Der Zusatzkauf ist noch nicht genehmigt oder bezahlt und gehört deshalb nicht zum aktuellen Ausgabenstand. Die gesondert finanzierte Raummiete, unbekannte Spenden und die Schneidematte ohne Preis und Kaufauftrag sind nicht eingerechnet.
```

## modes-de-077 · long_analysis

Source task:

> Reicht diese fiktive Auswertung aus, um die neue Anleitung für sämtliche Nutzenden zu empfehlen? Antworte direkt und erläutere die Grenzen. Es wird kein ausführlicher Plan für eine weitere Untersuchung verlangt.
> 
> In einem dreitägigen Versuch arbeiteten 25 Personen mit einer gekürzten Anleitung. 23 erledigten die Aufgabe ohne Nachfrage. In der Vorwoche arbeiteten 25 andere Personen mit der bisherigen Anleitung; 19 erledigten sie ohne Nachfrage. Daraus ergeben sich 92 % und 76 % für diese beiden Gruppen. Die Personen wurden nicht zufällig auf die Anleitungen verteilt.
> 
> Die Gruppe mit der kurzen Anleitung hatte das Gerät bereits in einem Einführungskurs gesehen. Die frühere Gruppe sah es zum ersten Mal. Außerdem fand der neue Versuch an ruhigen Vormittagen statt, während die frühere Gruppe am Nachmittag in einem stark genutzten Raum arbeitete. Die Zahl anderer Anwesender wurde nicht erfasst. Zwischen den Wochen wurden auch die Symbole am Gerät vergrößert, unabhängig vom Anleitungstext.
> 
> Die kurze Anleitung enthält keinen Abschnitt für die Bedienung mit einer Hand. Niemand in dieser Gruppe benötigte diese Variante. Es ist nicht bekannt, wie sie für solche Personen funktioniert. Ein Test mit vorgelesenem Text fand ebenfalls nicht statt. Zeitangaben wurden angeblich gesammelt, sind in der Auswertung aber nicht aufgeführt; ein durchschnittlicher Zeitgewinn lässt sich damit nicht berechnen.
> 
> Die Leitung hat noch keinen Austausch beschlossen. Sie möchte Beobachtung und Deutung getrennt sehen. Ein höherer Anteil erfolgreicher Aufgaben in einer Gruppe zeigt nicht automatisch, dass die Anleitung selbst die Ursache war. Ebenso lässt sich daraus nicht ableiten, dass jede einzelne Person oder eine nicht getestete Nutzergruppe profitieren wird. Die fehlenden Angaben sollen sichtbar bleiben, ohne im Antworttext eine nicht verlangte Forschungsplanung oder zusätzliche Zahlen einzuführen.

### baseline: pass

```text
Nein, die Auswertung reicht nicht für eine Empfehlung für sämtliche Nutzenden.

Beobachtet wurde: Mit der kurzen Anleitung erledigten 23 von 25 Personen die Aufgabe ohne Nachfrage (92 %), mit der bisherigen Anleitung 19 von 25 (76 %).

Dieser Unterschied belegt keine Ursache: Die Gruppen wurden nicht zufällig zugeteilt und unterschieden sich bei Vorerfahrung und Arbeitsbedingungen. Zudem wurden die Gerätesymbole vergrößert; die Zahl anderer Anwesender wurde nicht erfasst. Der höhere Erfolgsanteil lässt sich deshalb nicht eindeutig der Anleitung zuschreiben.

Zur einhändigen Bedienung und zur Nutzung mit vorgelesenem Text fehlen Tests. Ohne aufgeführte Zeitdaten lässt sich auch kein durchschnittlicher Zeitgewinn berechnen. Ein Vorteil für jede einzelne Person oder für nicht getestete Nutzergruppen ist damit nicht belegt.
```

### lite: pass

```text
Nein. Die Auswertung reicht nicht aus, um die neue Anleitung für sämtliche Nutzenden zu empfehlen.

Beobachtung: Im dreitägigen Versuch erledigten 23 von 25 Personen mit der gekürzten Anleitung die Aufgabe ohne Nachfrage (92 %). In der Vorwoche waren es mit der bisherigen Anleitung 19 von 25 anderen Personen (76 %).

Grenzen der Deutung: Die Personen wurden nicht zufällig verteilt. Die neue Gruppe kannte das Gerät bereits aus einem Einführungskurs und arbeitete an ruhigen Vormittagen. Die frühere Gruppe sah es erstmals und arbeitete nachmittags in einem stark genutzten Raum. Die Zahl anderer Anwesender wurde nicht erfasst. Außerdem wurden zwischen den Wochen die Gerätesymbole vergrößert. Der höhere Erfolgsanteil lässt sich deshalb nicht eindeutig auf die Anleitung zurückführen.

Die kurze Anleitung enthält keinen Abschnitt zur einhändigen Bedienung; niemand in der neuen Gruppe benötigte diese Variante. Wie sie für solche Personen funktioniert, ist unbekannt. Vorgelesener Text wurde ebenfalls nicht getestet. Zeitangaben wurden angeblich gesammelt, fehlen aber in der Auswertung. Ein durchschnittlicher Zeitgewinn lässt sich daher nicht berechnen.

Die Ergebnisse belegen weder einen Nutzen für jede einzelne Person noch für nicht getestete Nutzergruppen. Ein Austausch der Anleitung ist noch nicht beschlossen.
```

### full: pass

```text
Nein. Die Auswertung reicht nicht aus, um die kurze Anleitung für sämtliche Nutzenden zu empfehlen.

**Beobachtung:** Im dreitägigen Versuch erledigten 23 von 25 Personen die Aufgabe ohne Nachfrage (92 %). In der Vorwoche waren es mit der bisherigen Anleitung 19 von 25 anderen Personen (76 %).

**Grenzen der Deutung:** Die Personen wurden nicht zufällig verteilt. Die neue Gruppe kannte das Gerät aus einem Einführungskurs und arbeitete an ruhigen Vormittagen. Die frühere Gruppe sah es erstmals und arbeitete nachmittags in einem stark genutzten Raum. Die Zahl anderer Anwesender wurde nicht erfasst. Außerdem wurden zwischen den Wochen die Gerätesymbole unabhängig vom Anleitungstext vergrößert. Der höhere Erfolgsanteil lässt sich deshalb nicht eindeutig auf die kurze Anleitung zurückführen.

Die kurze Anleitung enthält keinen Abschnitt zur einhändigen Bedienung; niemand in der neuen Gruppe benötigte diese Variante. Ihre Eignung dafür ist unbekannt. Auch vorgelesener Text wurde nicht getestet. Die angeblich erhobenen Zeitangaben fehlen, sodass kein durchschnittlicher Zeitgewinn berechnet werden kann.

Die Ergebnisse belegen weder einen Nutzen für jede einzelne Person noch für ungetestete Nutzergruppen. Die Leitung hat noch keinen Austausch beschlossen.
```

### ultra: pass

```text
Nein. Die Auswertung reicht nicht aus, um die neue Anleitung sämtlichen Nutzenden zu empfehlen.

Beobachtung: Im dreitägigen Versuch erledigten 23 von 25 Personen mit der kurzen Anleitung die Aufgabe ohne Nachfrage (92 %). In der Vorwoche waren es mit der bisherigen Anleitung 19 von 25 anderen Personen (76 %).

Deutung und Grenzen: Die Gruppen wurden nicht zufällig zugeteilt. Nur die neue Gruppe kannte das Gerät aus einem Einführungskurs. Sie arbeitete an ruhigen Vormittagen, die frühere Gruppe nachmittags in einem stark genutzten Raum; die Zahl anderer Anwesender fehlt. Zudem wurden zwischen den Wochen die Gerätesymbole unabhängig vom Anleitungstext vergrößert. Der höhere Erfolgsanteil lässt sich daher nicht eindeutig der Anleitung zuschreiben.

Die kurze Anleitung enthält keinen Abschnitt zur einhändigen Bedienung; niemand in der neuen Gruppe benötigte sie. Ihre Eignung dafür ist unbekannt. Vorgelesener Text wurde nicht getestet. Angeblich gesammelte Zeitangaben fehlen, sodass kein durchschnittlicher Zeitgewinn berechnet werden kann. Ein Nutzen für jede einzelne Person oder ungetestete Nutzergruppen ist nicht belegt. Die Leitung hat noch keinen Austausch beschlossen.
```

### off: pass

```text
Nein. Die Auswertung reicht nicht aus, um die neue Anleitung für sämtliche Nutzenden zu empfehlen.

Beobachtung: Im dreitägigen Versuch erledigten mit der gekürzten Anleitung 23 von 25 Personen die Aufgabe ohne Nachfrage (92 %). In der Vorwoche waren es mit der bisherigen Anleitung 19 von 25 anderen Personen (76 %).

Deutung und Grenzen: Die Personen wurden nicht zufällig verteilt. Die Gruppe mit der kurzen Anleitung kannte das Gerät bereits aus einem Einführungskurs und arbeitete an ruhigen Vormittagen. Die frühere Gruppe sah es erstmals und arbeitete nachmittags in einem stark genutzten Raum. Die Zahl anderer Anwesender wurde nicht erfasst. Zudem wurden zwischen den Wochen die Gerätesymbole vergrößert. Der höhere Erfolgsanteil lässt sich daher nicht eindeutig auf die Anleitung zurückführen.

Die kurze Anleitung enthält keinen Abschnitt zur einhändigen Bedienung; niemand in der Gruppe benötigte diese Variante. Ihre Eignung dafür ist unbekannt. Vorgelesener Text wurde ebenfalls nicht getestet. Die angeblich gesammelten Zeitangaben fehlen in der Auswertung, sodass kein durchschnittlicher Zeitgewinn berechnet werden kann.

Die Ergebnisse zeigen einen höheren Erfolgsanteil in der getesteten Gruppe, aber keinen nachgewiesenen Nutzen für jede einzelne Person oder für nicht getestete Nutzergruppen. Ein Austausch wurde noch nicht beschlossen.
```

## modes-de-078 · long_voice

Source task:

> Kürze die folgende Geschichte für das Vereinsblatt. Bewahre den ruhigen, freundlichen Ton und die Tatsachen, die die Begegnung tragen. Erfinde keine spätere Entwicklung und keine ausdrücklich formulierte Lebensweisheit.
> 
> Als Hannes in den Tauschraum kam, tropfte Wasser von seinem Schirm. Er trug eine Blechdose, in der er alte Garnrollen gesammelt hatte. Es seien ungefähr vierzig, sagte er, gezählt habe er sie nicht. Manche Rollen waren fast voll, andere hatten nur noch wenige Windungen. Er stellte die Dose neben die Waage, ohne dass jemand die Rollen wog.
> 
> Mina fragte, ob die Dose auch abgegeben werden sollte. Hannes verneinte das. Sie gehörte früher seinem Bruder, und er wollte sie wieder mitnehmen. Das Garn durfte im Raum bleiben. Mina stellte eine Schale bereit und legte die Rollen vorsichtig hinein. Sie fragte nicht nach dem Grund für die späte Abgabe und schrieb keine Geschichte über den Bruder dazu.
> 
> Ein junger Besucher entdeckte eine grüne Rolle und fragte, ob er sie für seinen Stoffbeutel nehmen dürfe. Hannes stimmte zu. Er wusste nicht mehr, woher genau diese Rolle gekommen war. Im Vereinsblatt darf sie daher nicht als Garn des Bruders beschrieben werden. Bekannt ist nur, dass Hannes sie aufbewahrt hatte und jetzt weitergab. Der Besucher nahm eine Rolle, nicht die ganze Schale.
> 
> Beim Abschied war der Regen schwächer geworden. Hannes ging mit der leeren Dose nach Hause. Die übrigen Rollen blieben als Spende für Reparaturen im Tauschraum. Mina vermerkte die Spende im Buch, ohne den jungen Besucher namentlich zu erfassen. Hier endet die beobachtete Szene. Ob der Stoffbeutel schon am selben Abend repariert wurde oder ob Hannes später erneut kam, ist nicht bekannt. Die kürzere Fassung soll diese offenen Enden nicht ausfüllen und den kleinen Moment trotzdem als Erzählung erhalten.

### baseline: pass

```text
Als Hannes in den Tauschraum kam, tropfte sein Schirm. In einer Blechdose brachte er ungefähr vierzig alte Garnrollen mit, manche fast voll, andere mit wenigen Windungen. Gezählt hatte er sie nicht.

Mina fragte, ob auch die Dose bleiben sollte. Doch sie hatte früher seinem Bruder gehört, und Hannes wollte sie wieder mitnehmen. Mina legte die Rollen vorsichtig in eine Schale.

Ein junger Besucher entdeckte eine grüne Rolle und fragte, ob er sie für seinen Stoffbeutel nehmen dürfe. Hannes stimmte zu. Woher diese Rolle stammte, wusste er nicht mehr.

Beim Abschied hatte der Regen nachgelassen. Hannes ging mit der leeren Dose nach Hause. Die übrigen Rollen blieben als Spende für Reparaturen im Tauschraum; Mina trug die Spende ins Buch ein.
```

### lite: pass

```text
Als Hannes in den Tauschraum kam, tropfte Wasser von seinem Schirm. In einer Blechdose brachte er alte Garnrollen mit, ungefähr vierzig, wie er sagte. Gezählt hatte er sie nicht. Manche waren fast voll, andere trugen nur wenige Windungen. Er stellte die Dose neben die Waage; gewogen wurden die Rollen nicht.

Mina fragte, ob auch die Dose bleiben sollte. Hannes verneinte: Sie hatte seinem Bruder gehört, und er wollte sie wieder mitnehmen. Das Garn durfte bleiben. Mina legte die Rollen vorsichtig in eine Schale, ohne nach dem Grund für die späte Abgabe zu fragen oder eine Geschichte über den Bruder hinzuzufügen.

Ein junger Besucher entdeckte eine grüne Rolle und fragte, ob er sie für seinen Stoffbeutel nehmen dürfe. Hannes stimmte zu. Woher diese Rolle stammte, wusste er nicht mehr; er hatte sie aufbewahrt und gab sie nun weiter. Der Besucher nahm nur diese eine Rolle.

Beim Abschied hatte der Regen nachgelassen. Hannes ging mit der leeren Dose nach Hause. Die übrigen Rollen blieben als Spende für Reparaturen im Tauschraum. Mina vermerkte die Spende im Buch, ohne den jungen Besucher namentlich zu erfassen.
```

### full: flagged

```text
Als Hannes in den Tauschraum kam, tropfte sein Schirm. In einer Blechdose brachte er alte Garnrollen mit: ungefähr vierzig, sagte er, gezählt hatte er sie nicht. Manche waren fast voll, andere trugen nur noch wenige Windungen. Er stellte die Dose neben die Waage; gewogen wurden die Rollen nicht.

Mina fragte, ob auch die Dose bleiben sollte. Hannes schüttelte den Kopf. Sie hatte früher seinem Bruder gehört, und er wollte sie wieder mitnehmen. Das Garn durfte bleiben. Mina legte die Rollen vorsichtig in eine Schale, ohne nach dem Grund für die späte Abgabe zu fragen.

Ein junger Besucher entdeckte eine grüne Rolle und fragte, ob er sie für seinen Stoffbeutel nehmen dürfe. Hannes stimmte zu. Woher diese Rolle stammte, wusste er nicht mehr. Der Besucher nahm sie aus der Schale.

Beim Abschied hatte der Regen nachgelassen. Hannes ging mit der leeren Dose nach Hause. Die übrigen Rollen blieben als Spende für Reparaturen im Tauschraum. Mina trug die Spende ins Buch ein, ohne den Besucher namentlich zu erfassen.
```

Review notes: Alle tragenden Tatsachen bleiben erhalten. Die ergänzte Geste ist unbelegt, aber keine materielle Veränderung der Begegnung. / Central facts and quiet narrative are intact; only a minor refusal gesture is embellished.

### ultra: pass

```text
Als Hannes den Tauschraum betrat, tropfte sein Schirm. In einer Blechdose brachte er alte Garnrollen mit: ungefähr vierzig, sagte er, gezählt hatte er sie nicht. Manche waren fast voll, andere trugen nur wenige Windungen. Er stellte die Dose neben die Waage; gewogen wurde nichts.

Mina fragte, ob auch die Dose bleiben sollte. Hannes wollte sie wieder mitnehmen: Sie hatte früher seinem Bruder gehört. Nur das Garn gab er ab. Mina legte die Rollen vorsichtig in eine Schale, ohne nach dem Grund für die späte Abgabe zu fragen oder eine Geschichte über den Bruder hinzuzufügen.

Ein junger Besucher bat um eine grüne Rolle für seinen Stoffbeutel. Hannes stimmte zu. Woher diese Rolle stammte, wusste er nicht mehr; er hatte sie aufbewahrt und gab sie nun weiter. Der Besucher nahm die eine Rolle.

Beim Abschied hatte der Regen nachgelassen. Hannes ging mit der leeren Dose nach Hause. Die übrigen Rollen blieben als Spende für Reparaturen im Tauschraum. Mina vermerkte die Spende im Buch, ohne den Besucher namentlich zu erfassen.
```

### off: flagged

```text
Als Hannes den Tauschraum betrat, tropfte Wasser von seinem Schirm. In einer Blechdose brachte er alte Garnrollen mit: ungefähr vierzig, wie er sagte, gezählt hatte er sie nicht. Manche waren fast voll, andere trugen nur noch wenige Windungen.

Mina fragte, ob auch die Dose bleiben sollte. Hannes schüttelte den Kopf. Sie hatte früher seinem Bruder gehört, und er wollte sie wieder mitnehmen. Das Garn durfte bleiben. Mina legte die Rollen vorsichtig in eine Schale, ohne nach dem Grund für die späte Abgabe zu fragen.

Ein junger Besucher entdeckte eine grüne Rolle und fragte, ob er sie für seinen Stoffbeutel nehmen dürfe. Hannes stimmte zu. Woher diese Rolle ursprünglich gekommen war, wusste er nicht mehr. Der Besucher nahm die eine Rolle mit.

Beim Abschied hatte der Regen nachgelassen. Hannes ging mit der leeren Dose nach Hause. Die übrigen Rollen blieben als Spende für Reparaturen im Tauschraum. Mina vermerkte die Spende im Buch, ohne den jungen Besucher namentlich zu erfassen.
```

Review notes: Die Kürzung bewahrt sämtliche tragenden Tatsachen; lediglich die konkrete Geste der Verneinung ist unbelegt. / Preserves the central facts and gentle tone; the added refusal gesture is minor and does not alter the encounter.

## modes-de-079 · long_uncertainty

Source task:

> Schreibe einen Statusbericht für die nächste Besprechung. Es geht um einen fiktiven Feuchtesensor in einem Lager. Beschreibe Beobachtungen und Vermutungen getrennt. Die Notiz erlaubt keine Aussage darüber, ob die gelagerten Gegenstände beschädigt wurden.
> 
> Im gespeicherten Verlauf fehlt am Mittwoch ein Abschnitt von 23 Minuten, zwischen 09:12 und 09:35. Vor und nach der Lücke liegen die angezeigten Werte zwischen 44 % und 47 % relativer Luftfeuchte. Für die Lücke selbst gibt es keine Werte. Ein weiterer Sensor im selben Raum war nicht vorhanden. Die Werte daneben belegen nicht, dass die Feuchte während der Lücke konstant geblieben ist.
> 
> Am Donnerstag fand die Werkstatt einen locker sitzenden Stecker. Dies könnte eine Unterbrechung der Aufzeichnung erklären. Es ist jedoch nicht dokumentiert, dass der Stecker am Mittwoch tatsächlich den Kontakt verlor. Nach dem Befestigen wurden drei Tests von jeweils zwanzig Minuten durchgeführt. In diesen Tests trat keine Lücke auf. Die kurzen Tests zeigen nicht, dass eine Unterbrechung künftig ausgeschlossen ist.
> 
> Eine Aufzeichnungslücke ist nicht automatisch ein Stromausfall des gesamten Lagers. Der Betriebszustand der Lüftung wurde zu dieser Zeit nicht gespeichert. Es gibt in dieser Notiz auch keine Untersuchung der gelagerten Gegenstände. Weder ein Schaden noch die Unversehrtheit dieser Gegenstände darf deshalb als nachgewiesen beschrieben werden. Gegenstand des Berichts ist zunächst die Datenerfassung.
> 
> Die Werkstatt hält einen ununterbrochenen Beobachtungslauf über 36 Stunden für möglicherweise hilfreich. Dieser Lauf ist lediglich vorgeschlagen. Er wurde noch nicht gestartet, niemand ist für die Betreuung eingeteilt und ein Endtermin ist nicht festgelegt. Die Besprechung soll über den Vorschlag reden. Der Bericht darf daraus keinen beschlossenen Ablauf machen oder den Stecker allein aufgrund des zeitlichen Zusammenhangs als sichere Ursache benennen.

### baseline: pass

```text
Statusbericht zur Datenerfassung

Beobachtungen:
Am Mittwoch fehlt im gespeicherten Verlauf zwischen 09:12 und 09:35 ein Abschnitt von 23 Minuten. Vor und nach der Lücke lagen die angezeigten Werte zwischen 44 % und 47 % relativer Luftfeuchte. Für die Lücke fehlen Messwerte; ein weiterer Sensor war nicht vorhanden.

Am Donnerstag fand die Werkstatt einen lockeren Stecker. Nach dessen Befestigung verliefen drei Tests von jeweils zwanzig Minuten ohne Aufzeichnungslücke.

Vermutungen und Grenzen:
Der lockere Stecker könnte die Unterbrechung erklären. Ein tatsächlicher Kontaktverlust am Mittwoch ist jedoch nicht dokumentiert. Die Tests schließen künftige Unterbrechungen nicht aus. Auch eine konstante Feuchte während der Lücke ist nicht belegt.

Die Aufzeichnungslücke weist keinen Stromausfall des gesamten Lagers nach. Der Lüftungszustand wurde nicht gespeichert. Die gelagerten Gegenstände wurden laut Notiz nicht untersucht; weder Schäden noch ihre Unversehrtheit sind nachgewiesen.

Vorschlag für die Besprechung:
Die Werkstatt hält einen ununterbrochenen Beobachtungslauf über 36 Stunden für möglicherweise hilfreich. Er ist lediglich vorgeschlagen, noch nicht gestartet und ohne eingeteilte Betreuung oder festgelegten Endtermin.
```

### lite: pass

```text
Statusbericht: Datenerfassung des Feuchtesensors

Beobachtungen
Im gespeicherten Verlauf fehlt am Mittwoch zwischen 09:12 und 09:35 ein Abschnitt von 23 Minuten. Vor und nach der Lücke liegen die angezeigten Werte zwischen 44 % und 47 % relativer Luftfeuchte. Für die Lücke selbst gibt es keine Werte; ein weiterer Sensor war nicht vorhanden. Eine konstante Feuchte während dieser Zeit ist damit nicht belegt.

Am Donnerstag fand die Werkstatt einen locker sitzenden Stecker. Nach dem Befestigen wurden drei Tests von jeweils zwanzig Minuten durchgeführt. Dabei trat keine Aufzeichnungslücke auf. Die kurzen Tests schließen künftige Unterbrechungen nicht aus.

Vermutungen und offene Fragen
Der lockere Stecker könnte die Aufzeichnungslücke erklären. Es ist jedoch nicht dokumentiert, dass er am Mittwoch tatsächlich den Kontakt verlor. Er ist daher keine nachgewiesene Ursache.

Die Aufzeichnungslücke belegt keinen Stromausfall des gesamten Lagers. Der Betriebszustand der Lüftung wurde zu dieser Zeit nicht gespeichert. Die gelagerten Gegenstände wurden laut dieser Notiz nicht untersucht; weder ein Schaden noch ihre Unversehrtheit ist nachgewiesen.

Vorschlag für die Besprechung
Die Werkstatt hält einen ununterbrochenen Beobachtungslauf über 36 Stunden für möglicherweise hilfreich. Der Lauf ist nur vorgeschlagen und noch nicht gestartet. Niemand ist für die Betreuung eingeteilt, ein Endtermin ist nicht festgelegt. Die Besprechung soll den Vorschlag erörtern; ein Ablauf ist noch nicht beschlossen.
```

### full: pass

```text
## Status der Datenerfassung

Am Mittwoch fehlt im gespeicherten Verlauf ein Abschnitt von 23 Minuten, von 09:12 bis 09:35. Die Ursache ist nicht bestätigt.

### Beobachtungen
Vor und nach der Lücke lagen die angezeigten Werte zwischen 44 % und 47 % relativer Luftfeuchte. Während der Lücke liegen keine Werte vor; ein zweiter Sensor war nicht vorhanden. Eine konstante Feuchte in diesem Zeitraum ist daher nicht belegt.

Am Donnerstag fand die Werkstatt einen locker sitzenden Stecker. Nach dessen Befestigung wurden drei Tests von jeweils zwanzig Minuten durchgeführt. Dabei trat keine Aufzeichnungslücke auf. Künftige Unterbrechungen sind dadurch nicht ausgeschlossen.

### Vermutung und offene Fragen
Der lockere Stecker könnte die Aufzeichnungslücke erklären. Ein tatsächlicher Kontaktverlust am Mittwoch ist jedoch nicht dokumentiert; der Stecker ist keine gesicherte Ursache.

Die Aufzeichnungslücke belegt keinen Stromausfall des gesamten Lagers. Der damalige Betriebszustand der Lüftung wurde nicht gespeichert. Die gelagerten Gegenstände wurden laut Notiz nicht untersucht. Weder Schäden noch ihre Unversehrtheit sind nachgewiesen.

### Vorschlag für die Besprechung
Die Werkstatt hält einen ununterbrochenen Beobachtungslauf über 36 Stunden für möglicherweise hilfreich. Er ist nur vorgeschlagen und noch nicht gestartet. Eine Betreuung ist nicht eingeteilt, ein Endtermin nicht festgelegt. Die Besprechung soll den Vorschlag erörtern.
```

### ultra: pass

```text
Status: Die Datenerfassung weist eine ungeklärte Lücke auf.

Beobachtungen: Am Mittwoch fehlen zwischen 09:12 und 09:35 insgesamt 23 Minuten im gespeicherten Verlauf. Davor und danach lagen die angezeigten Werte bei 44–47 % relativer Luftfeuchte. Für die Lücke fehlen Werte; ein zweiter Sensor war nicht vorhanden. Eine konstante Feuchte während der Lücke ist damit nicht belegt.

Am Donnerstag fand die Werkstatt einen lockeren Stecker. Nach dessen Befestigung verliefen drei Tests von jeweils zwanzig Minuten ohne Aufzeichnungslücke. Das schließt künftige Unterbrechungen nicht aus.

Vermutung und Grenzen: Der Stecker könnte die Lücke erklären. Ein tatsächlicher Kontaktverlust am Mittwoch ist jedoch nicht dokumentiert; die Ursache bleibt ungeklärt. Die Aufzeichnungslücke belegt keinen Stromausfall des gesamten Lagers. Der damalige Lüftungsbetrieb wurde nicht gespeichert. Die gelagerten Gegenstände wurden laut Notiz nicht untersucht: Weder Schaden noch Unversehrtheit sind nachgewiesen.

Zur Besprechung: Die Werkstatt schlägt einen ununterbrochenen Beobachtungslauf über 36 Stunden als möglicherweise hilfreich vor. Er ist nicht beschlossen oder gestartet; Betreuung und Endtermin sind nicht festgelegt.
```

### off: pass

```text
Statusbericht: Datenerfassung des Feuchtesensors im Lager

Beobachtungen
Am Mittwoch fehlt im gespeicherten Verlauf zwischen 09:12 und 09:35 ein Abschnitt von 23 Minuten. Vor und nach der Lücke lagen die angezeigten Werte zwischen 44 % und 47 % relativer Luftfeuchte. Für die Lücke selbst fehlen Messwerte; ein weiterer Sensor im Raum war nicht vorhanden. Die benachbarten Werte belegen keine konstante Feuchte während der Unterbrechung.

Am Donnerstag fand die Werkstatt einen locker sitzenden Stecker. Nach dessen Befestigung wurden drei Tests von jeweils zwanzig Minuten durchgeführt. Dabei trat keine Aufzeichnungslücke auf. Diese kurzen Tests schließen künftige Unterbrechungen nicht aus.

Vermutung und offene Fragen
Der lockere Stecker könnte die Aufzeichnungslücke erklären. Ein tatsächlicher Kontaktverlust am Mittwoch ist jedoch nicht dokumentiert; der Stecker ist daher keine nachgewiesene Ursache.

Die Aufzeichnungslücke belegt keinen Stromausfall des gesamten Lagers. Der Betriebszustand der Lüftung wurde für diesen Zeitraum nicht gespeichert. Die gelagerten Gegenstände wurden laut Notiz nicht untersucht. Weder Schäden noch ihre Unversehrtheit sind damit nachgewiesen.

Vorschlag für die Besprechung
Die Werkstatt hält einen ununterbrochenen Beobachtungslauf über 36 Stunden für möglicherweise hilfreich. Der Lauf ist lediglich vorgeschlagen und noch nicht gestartet. Es sind weder eine Betreuung noch ein Endtermin festgelegt. Die Besprechung soll den Vorschlag erörtern; ein Ablauf ist noch nicht beschlossen.
```

## modes-de-080 · scope

Source task:

> Beantworte kurz: Müssen Teilnehmende eigene Notebooks mitbringen? Was erfordert und kostet die Leihoption? Für den fiktiven Kurs stehen Leihgeräte bereit. Eigene Geräte sind erlaubt, aber freiwillig. Ein Leihgerät muss vorab reserviert werden; seine Nutzung kostet nichts.

### baseline: pass

```text
Nein, eigene Notebooks sind freiwillig. Ein Leihgerät muss vorab reserviert werden; die Nutzung ist kostenlos.
```

### lite: pass

```text
Nein. Eigene Notebooks sind erlaubt, aber freiwillig. Für ein Leihgerät ist eine Reservierung vorab erforderlich; die Nutzung ist kostenlos.
```

### full: pass

```text
Nein. Eigene Notebooks sind erlaubt, aber freiwillig. Ein Leihgerät muss vorab reserviert werden; die Nutzung ist kostenlos.
```

### ultra: pass

```text
Nein. Eigene Notebooks sind erlaubt, aber freiwillig. Leihgeräte stehen bereit, müssen vorab reserviert werden und sind kostenlos nutzbar.
```

### off: pass

```text
Nein. Eigene Notebooks sind erlaubt, aber freiwillig. Ein Leihgerät muss vorab reserviert werden; die Nutzung ist kostenlos.
```

## modes-de-081 · translation_permissions

Source task:

> Translate this fictional library notice into German: You may borrow a reading lamp for one evening. You must return it by 11:00 the next day. Borrowing a lamp does not extend your room booking.

### baseline: pass

```text
Sie dürfen eine Leselampe für einen Abend ausleihen. Sie müssen sie am nächsten Tag bis 11:00 Uhr zurückgeben. Das Ausleihen einer Lampe verlängert Ihre Raumbuchung nicht.
```

### lite: pass

```text
Sie dürfen eine Leselampe für einen Abend ausleihen. Sie müssen sie am nächsten Tag bis 11:00 Uhr zurückgeben. Das Ausleihen einer Lampe verlängert Ihre Zimmerbuchung nicht.
```

### full: pass

```text
Sie dürfen eine Leselampe für einen Abend ausleihen. Sie müssen sie am nächsten Tag bis 11:00 Uhr zurückgeben. Das Ausleihen einer Lampe verlängert Ihre Zimmerbuchung nicht.
```

### ultra: pass

```text
Sie dürfen eine Leselampe für einen Abend ausleihen. Sie müssen sie am nächsten Tag bis 11:00 Uhr zurückgeben. Das Ausleihen einer Lampe verlängert Ihre Raumbuchung nicht.
```

### off: pass

```text
Sie dürfen eine Leselampe für einen Abend ausleihen. Sie müssen sie am nächsten Tag bis 11:00 Uhr zurückgeben. Das Ausleihen einer Lampe verlängert Ihre Raumbuchung nicht.
```

## modes-de-082 · translation_negation

Source task:

> Translate into German: Do not delete the draft when a receipt is missing. The receipt may arrive separately. We have not yet checked the second envelope.

### baseline: pass

```text
Löschen Sie den Entwurf nicht, wenn ein Beleg fehlt. Der Beleg kann separat eintreffen. Wir haben den zweiten Umschlag noch nicht überprüft.
```

### lite: pass

```text
Löschen Sie den Entwurf nicht, wenn ein Beleg fehlt. Der Beleg kann separat eintreffen. Wir haben den zweiten Umschlag noch nicht geprüft.
```

### full: pass

```text
Löschen Sie den Entwurf nicht, wenn ein Beleg fehlt. Der Beleg kann separat eintreffen. Wir haben den zweiten Umschlag noch nicht geprüft.
```

### ultra: pass

```text
Löschen Sie den Entwurf nicht, wenn ein Beleg fehlt. Der Beleg kann separat eintreffen. Wir haben den zweiten Umschlag noch nicht geprüft.
```

### off: pass

```text
Löschen Sie den Entwurf nicht, wenn ein Beleg fehlt. Der Beleg kann separat eintreffen. Wir haben den zweiten Umschlag noch nicht geprüft.
```

## modes-de-083 · translation_actor

Source task:

> Translate into German: Elena recorded the damaged latch on Friday. It was repaired on Saturday, but the log does not identify the repairer. On Sunday, Omar tested the repaired latch.

### baseline: pass

```text
Elena dokumentierte den beschädigten Riegel am Freitag. Er wurde am Samstag repariert, aber aus dem Protokoll geht nicht hervor, wer die Reparatur durchgeführt hat. Am Sonntag testete Omar den reparierten Riegel.
```

### lite: pass

```text
Elena dokumentierte den beschädigten Riegel am Freitag. Er wurde am Samstag repariert, aber aus dem Protokoll geht nicht hervor, wer ihn repariert hat. Am Sonntag testete Omar den reparierten Riegel.
```

### full: pass

```text
Elena dokumentierte den beschädigten Riegel am Freitag. Er wurde am Samstag repariert, aber aus dem Protokoll geht nicht hervor, wer ihn repariert hat. Am Sonntag testete Omar den reparierten Riegel.
```

### ultra: pass

```text
Elena dokumentierte am Freitag den beschädigten Riegel. Er wurde am Samstag repariert, aber aus dem Protokoll geht nicht hervor, wer ihn repariert hat. Am Sonntag testete Omar den reparierten Riegel.
```

### off: pass

```text
Elena dokumentierte am Freitag den beschädigten Riegel. Er wurde am Samstag repariert, aber im Protokoll ist nicht angegeben, wer die Reparatur durchgeführt hat. Am Sonntag testete Omar den reparierten Riegel.
```

## modes-de-084 · translation_uncertainty

Source task:

> Translate into German: The noise may come from the upper wheel. This has not been confirmed. Only the empty trolley was tested; no loaded test has been completed.

### baseline: pass

```text
Das Geräusch könnte vom oberen Rad kommen. Dies wurde nicht bestätigt. Nur der leere Wagen wurde getestet; ein Test mit beladenem Wagen wurde noch nicht abgeschlossen.
```

### lite: pass

```text
Das Geräusch könnte vom oberen Rad kommen. Dies wurde nicht bestätigt. Nur der leere Wagen wurde getestet; ein Test mit beladenem Wagen wurde noch nicht abgeschlossen.
```

### full: pass

```text
Das Geräusch könnte vom oberen Rad kommen. Das ist noch nicht bestätigt. Nur der leere Wagen wurde getestet; ein Test mit beladenem Wagen wurde noch nicht abgeschlossen.
```

### ultra: pass

```text
Das Geräusch könnte vom oberen Rad kommen. Das wurde nicht bestätigt. Nur der leere Wagen wurde getestet; ein Test mit beladenem Wagen wurde noch nicht abgeschlossen.
```

### off: pass

```text
Das Geräusch könnte vom oberen Rad kommen. Dies wurde nicht bestätigt. Es wurde nur der leere Transportwagen getestet; ein Test mit beladenem Transportwagen wurde noch nicht abgeschlossen.
```

## modes-de-085 · translation_json

Source task:

> Translate the note value into German. Return only valid JSON with the original keys, code, and quantity: {"code":"DE-K31","quantity":4,"note":"Four seals are missing. Do not open the containers until replacement seals are ready."}

### baseline: pass

```text
{"code":"DE-K31","quantity":4,"note":"Vier Siegel fehlen. Öffnen Sie die Behälter nicht, bevor Ersatzsiegel bereitliegen."}
```

### lite: pass

```text
{"code":"DE-K31","quantity":4,"note":"Vier Dichtungen fehlen. Öffnen Sie die Behälter erst, wenn Ersatzdichtungen bereitstehen."}
```

### full: pass

```text
{"code":"DE-K31","quantity":4,"note":"Vier Siegel fehlen. Öffnen Sie die Behälter erst, wenn Ersatzsiegel bereitliegen."}
```

### ultra: pass

```text
{"code":"DE-K31","quantity":4,"note":"Vier Dichtungen fehlen. Öffnen Sie die Behälter erst, wenn Ersatzdichtungen bereitliegen."}
```

### off: pass

```text
{"code":"DE-K31","quantity":4,"note":"Vier Dichtungen fehlen. Öffnen Sie die Behälter nicht, bevor Ersatzdichtungen bereitliegen."}
```

## modes-de-086 · translation_format

Source task:

> Translate into German, keeping the two bullets and placeholders:
> - Dear {{reader}}, your collection is booked for 21 August.
> - Use {{collection_url}} to change the time; changing the time does not change the address.

### baseline: pass

```text
- Guten Tag {{reader}}, Ihre Abholung ist für den 21. August gebucht.
- Nutzen Sie {{collection_url}}, um die Uhrzeit zu ändern; eine Änderung der Uhrzeit ändert nicht die Adresse.
```

### lite: pass

```text
- Liebe/r {{reader}}, Ihre Abholung ist für den 21. August gebucht.
- Nutzen Sie {{collection_url}}, um die Uhrzeit zu ändern; eine Änderung der Uhrzeit ändert nicht die Adresse.
```

### full: pass

```text
- Guten Tag {{reader}}, Ihre Abholung ist für den 21. August gebucht.
- Nutzen Sie {{collection_url}}, um die Uhrzeit zu ändern; die Adresse bleibt dabei unverändert.
```

### ultra: pass

```text
- Guten Tag {{reader}}, Ihre Abholung ist für den 21. August gebucht.
- Über {{collection_url}} können Sie die Uhrzeit ändern; die Adresse bleibt dabei unverändert.
```

### off: pass

```text
- Guten Tag {{reader}}, Ihre Abholung ist für den 21. August gebucht.
- Verwenden Sie {{collection_url}}, um die Uhrzeit zu ändern; eine Änderung der Uhrzeit ändert nicht die Adresse.
```

## modes-de-087 · translation_conditions

Source task:

> Translate this fictional room rule into German: The rehearsal room may be used only after the floor has dried and the caretaker has unlocked the door. An unlocked door alone is not permission to enter.

### baseline: pass

```text
Der Proberaum darf erst genutzt werden, nachdem der Boden getrocknet ist und der Hausmeister die Tür aufgeschlossen hat. Eine aufgeschlossene Tür allein ist keine Erlaubnis zum Betreten.
```

### lite: pass

```text
Der Proberaum darf erst genutzt werden, nachdem der Boden getrocknet ist und die für die Betreuung zuständige Person die Tür aufgeschlossen hat. Eine aufgeschlossene Tür allein ist keine Erlaubnis zum Betreten.
```

### full: flagged

```text
Der Proberaum darf erst genutzt werden, nachdem der Boden getrocknet ist und die Hausverwaltung die Tür aufgeschlossen hat. Eine aufgeschlossene Tür allein ist keine Erlaubnis, den Raum zu betreten.
```

Review notes: Changes the actor whose unlocking is required for permission. / Changes the actor whose unlocking is required, despite preserving the other restrictions.

### ultra: pass

```text
Der Proberaum darf erst genutzt werden, wenn der Boden getrocknet ist und die zuständige Betreuungsperson die Tür aufgeschlossen hat. Eine aufgeschlossene Tür allein erlaubt noch keinen Zutritt.
```

### off: pass

```text
Der Proberaum darf erst benutzt werden, nachdem der Boden getrocknet ist und der Hausmeister die Tür aufgeschlossen hat. Eine aufgeschlossene Tür allein ist keine Erlaubnis zum Betreten.
```

## modes-de-088 · translation_estimates

Source task:

> Translate into German: Sorting is expected to take roughly 7 to 9 working hours if the printed list matches the boxes. The estimate excludes relabelling. No finishing time is guaranteed.

### baseline: pass

```text
Das Sortieren wird voraussichtlich etwa 7 bis 9 Arbeitsstunden dauern, sofern die gedruckte Liste mit den Kartons übereinstimmt. Die Schätzung umfasst keine Neuetikettierung. Ein Fertigstellungszeitpunkt wird nicht garantiert.
```

### lite: pass

```text
Das Sortieren dauert voraussichtlich etwa 7 bis 9 Arbeitsstunden, sofern die gedruckte Liste mit den Kartons übereinstimmt. Die Schätzung umfasst keine Neuetikettierung. Ein Fertigstellungszeitpunkt wird nicht garantiert.
```

### full: pass

```text
Das Sortieren dauert voraussichtlich etwa 7 bis 9 Arbeitsstunden, sofern die gedruckte Liste mit den Kisten übereinstimmt. Die Schätzung schließt eine erneute Etikettierung nicht ein. Ein Fertigstellungszeitpunkt wird nicht garantiert.
```

### ultra: pass

```text
Das Sortieren dauert voraussichtlich etwa 7 bis 9 Arbeitsstunden, sofern die gedruckte Liste mit den Kartons übereinstimmt. Die Schätzung schließt eine erneute Beschriftung aus. Ein Fertigstellungszeitpunkt wird nicht garantiert.
```

### off: pass

```text
Das Sortieren wird voraussichtlich etwa 7 bis 9 Arbeitsstunden dauern, sofern die gedruckte Liste mit den Kartons übereinstimmt. Die Schätzung umfasst nicht das erneute Beschriften. Ein Fertigstellungszeitpunkt wird nicht garantiert.
```

## modes-de-089 · translation_units

Source task:

> Translate into German without currency or unit conversion: Each panel covers 2.5 m² and costs USD 38 before tax. Fitting costs USD 16 per panel. Delivery is included in the panel price.

### baseline: pass

```text
Jedes Paneel deckt 2,5 m² ab und kostet USD 38 vor Steuern. Die Montage kostet USD 16 pro Paneel. Die Lieferung ist im Paneelpreis enthalten.
```

### lite: pass

```text
Jedes Paneel deckt 2,5 m² ab und kostet USD 38 vor Steuern. Die Montage kostet USD 16 pro Paneel. Die Lieferung ist im Paneelpreis enthalten.
```

### full: pass

```text
Jede Platte deckt 2,5 m² ab und kostet USD 38 vor Steuern. Die Montage kostet USD 16 pro Platte. Die Lieferung ist im Plattenpreis enthalten.
```

### ultra: pass

```text
Jede Platte deckt 2,5 m² ab und kostet USD 38 vor Steuern. Die Montage kostet USD 16 pro Platte. Die Lieferung ist im Plattenpreis enthalten.
```

### off: pass

```text
Jedes Paneel deckt 2,5 m² ab und kostet USD 38 vor Steuern. Die Montage kostet USD 16 pro Paneel. Die Lieferung ist im Paneelpreis enthalten.
```

## modes-de-090 · translation_sampling

Source task:

> Translate into German: The 27 respondents volunteered after a gardening class. They were not selected from a random sample of residents. The results describe this group, not the whole neighbourhood.

### baseline: pass

```text
Die 27 Befragten meldeten sich nach einem Gartenkurs freiwillig. Sie wurden nicht aus einer Zufallsstichprobe der Bewohner ausgewählt. Die Ergebnisse beschreiben diese Gruppe, nicht die gesamte Nachbarschaft.
```

### lite: pass

```text
Die 27 Befragten meldeten sich nach einem Gartenkurs freiwillig. Sie wurden nicht aus einer Zufallsstichprobe der Wohnbevölkerung ausgewählt. Die Ergebnisse beschreiben diese Gruppe, nicht die gesamte Nachbarschaft.
```

### full: pass

```text
Die 27 Befragten meldeten sich nach einem Gartenkurs freiwillig. Sie wurden nicht aus einer Zufallsstichprobe der Bewohner ausgewählt. Die Ergebnisse beschreiben diese Gruppe, nicht die gesamte Nachbarschaft.
```

### ultra: pass

```text
Die 27 Befragten meldeten sich nach einem Gartenkurs freiwillig zur Teilnahme. Sie wurden nicht aus einer Zufallsstichprobe der Nachbarschaftsbevölkerung ausgewählt. Die Ergebnisse beschreiben diese Gruppe, nicht die gesamte Nachbarschaft.
```

### off: pass

```text
Die 27 Befragten meldeten sich nach einem Gartenkurs freiwillig. Sie wurden nicht aus einer Zufallsstichprobe der Bewohner ausgewählt. Die Ergebnisse beschreiben diese Gruppe, nicht die gesamte Nachbarschaft.
```

## modes-de-091 · translation_percentage_points

Source task:

> Translate into German: In the fictional example, the rate fell from 52% to 46%, a decrease of 6 percentage points. This should not be described as a 6% relative decrease.

### baseline: pass

```text
Im fiktiven Beispiel sank die Rate von 52 % auf 46 %, ein Rückgang um 6 Prozentpunkte. Dies sollte nicht als relativer Rückgang um 6 % beschrieben werden.
```

### lite: pass

```text
Im fiktiven Beispiel sank die Rate von 52 % auf 46 %, ein Rückgang um 6 Prozentpunkte. Dies sollte nicht als relativer Rückgang um 6 % bezeichnet werden.
```

### full: pass

```text
Im fiktiven Beispiel sank die Rate von 52 % auf 46 %, also um 6 Prozentpunkte. Dies sollte nicht als relativer Rückgang um 6 % bezeichnet werden.
```

### ultra: pass

```text
Im fiktiven Beispiel sank die Rate von 52% auf 46%, also um 6 Prozentpunkte. Dies sollte nicht als relativer Rückgang um 6% bezeichnet werden.
```

### off: pass

```text
In dem fiktiven Beispiel sank die Quote von 52% auf 46%, ein Rückgang um 6 Prozentpunkte. Dies sollte nicht als relativer Rückgang um 6% bezeichnet werden.
```

## modes-de-092 · translation_exceptions

Source task:

> Translate this fictional booking rule into German: A completed lesson is not refundable. If the teacher cancels beforehand, the student may choose a refund or a replacement lesson. A replacement must not be imposed.

### baseline: pass

```text
Eine bereits abgehaltene Unterrichtsstunde ist nicht erstattungsfähig. Wenn die Lehrkraft vorher absagt, kann der Schüler zwischen einer Rückerstattung und einer Ersatzstunde wählen. Eine Ersatzstunde darf nicht aufgezwungen werden.
```

### lite: pass

```text
Für eine abgeschlossene Unterrichtsstunde ist keine Rückerstattung möglich. Wenn die Lehrkraft vorher absagt, darf die lernende Person zwischen einer Rückerstattung und einer Ersatzstunde wählen. Eine Ersatzstunde darf nicht aufgezwungen werden.
```

### full: pass

```text
Für eine bereits abgeschlossene Unterrichtsstunde gibt es keine Rückerstattung. Sagt die Lehrkraft vorher ab, darf die unterrichtete Person zwischen einer Rückerstattung und einer Ersatzstunde wählen. Eine Ersatzstunde darf nicht aufgezwungen werden.
```

### ultra: pass

```text
Eine bereits durchgeführte Unterrichtsstunde ist nicht erstattungsfähig. Sagt die Lehrkraft vorher ab, darf die lernende Person zwischen einer Erstattung und einer Ersatzstunde wählen. Eine Ersatzstunde darf nicht aufgezwungen werden.
```

### off: pass

```text
Für eine bereits abgehaltene Unterrichtsstunde ist keine Rückerstattung möglich. Wenn die Lehrkraft vorher absagt, darf die lernende Person zwischen einer Rückerstattung und einer Ersatzstunde wählen. Eine Ersatzstunde darf nicht aufgezwungen werden.
```

## modes-de-093 · translation_ambiguity

Source task:

> Translate into German without choosing a date interpretation: The note gives 11/12. We do not know whether the day or month was written first. Confirm the intended date before ordering the vehicle.

### baseline: pass

```text
In der Notiz steht 11/12. Wir wissen nicht, ob zuerst der Tag oder der Monat angegeben wurde. Bestätigen Sie das gemeinte Datum, bevor Sie das Fahrzeug bestellen.
```

### lite: pass

```text
In der Notiz steht 11/12. Wir wissen nicht, ob der Tag oder der Monat zuerst geschrieben wurde. Bestätigen Sie das gemeinte Datum, bevor Sie das Fahrzeug bestellen.
```

### full: pass

```text
In der Notiz steht 11/12. Wir wissen nicht, ob der Tag oder der Monat zuerst angegeben wurde. Bestätigen Sie das gemeinte Datum, bevor Sie das Fahrzeug bestellen.
```

### ultra: pass

```text
In der Notiz steht 11/12. Wir wissen nicht, ob der Tag oder der Monat zuerst angegeben wurde. Bestätigen Sie das gemeinte Datum, bevor Sie das Fahrzeug bestellen.
```

### off: pass

```text
Die Notiz enthält die Angabe 11/12. Wir wissen nicht, ob der Tag oder der Monat zuerst geschrieben wurde. Bestätigen Sie das gemeinte Datum, bevor Sie das Fahrzeug bestellen.
```

## modes-de-094 · translation_technical

Source task:

> Translate into German and keep technical tokens exact: Run label-check --no-write before editing labels.csv. The command reports repeated identifiers and does not edit the file. Keep labels.report even when it is empty.

### baseline: pass

```text
Führen Sie label-check --no-write aus, bevor Sie labels.csv bearbeiten. Der Befehl meldet mehrfach vorkommende Kennungen und verändert die Datei nicht. Behalten Sie labels.report auch dann bei, wenn die Datei leer ist.
```

### lite: pass

```text
Führen Sie label-check --no-write aus, bevor Sie labels.csv bearbeiten. Der Befehl meldet mehrfach vorkommende Kennungen und verändert die Datei nicht. Behalten Sie labels.report auch dann, wenn die Datei leer ist.
```

### full: pass

```text
Führen Sie label-check --no-write aus, bevor Sie labels.csv bearbeiten. Der Befehl meldet wiederholte Kennungen und verändert die Datei nicht. Bewahren Sie labels.report auf, auch wenn die Datei leer ist.
```

### ultra: pass

```text
Führen Sie label-check --no-write aus, bevor Sie labels.csv bearbeiten. Der Befehl meldet wiederholte Kennungen und verändert die Datei nicht. Behalten Sie labels.report auch dann, wenn die Datei leer ist.
```

### off: pass

```text
Führen Sie label-check --no-write aus, bevor Sie labels.csv bearbeiten. Der Befehl meldet mehrfach vorkommende Kennungen und verändert die Datei nicht. Behalten Sie labels.report auch dann, wenn die Datei leer ist.
```

## modes-de-095 · translation_voice

Source task:

> Translate into German with a restrained storybook voice: The blue door remained open. Three paper boats rested on the sill. We listened for the rain, but the street stayed quiet until morning.

### baseline: pass

```text
Die blaue Tür blieb offen. Drei Papierboote ruhten auf der Fensterbank. Wir lauschten auf den Regen, doch die Straße blieb still bis zum Morgen.
```

### lite: pass

```text
Die blaue Tür blieb offen. Drei Papierboote ruhten auf der Fensterbank. Wir lauschten auf den Regen, doch die Straße blieb bis zum Morgen still.
```

### full: pass

```text
Die blaue Tür blieb offen. Drei Papierboote lagen auf der Fensterbank. Wir lauschten auf den Regen, doch die Straße blieb bis zum Morgen still.
```

### ultra: pass

```text
Die blaue Tür blieb offen. Drei Papierboote ruhten auf der Türschwelle. Wir lauschten auf den Regen, doch die Straße blieb still bis zum Morgen.
```

### off: pass

```text
Die blaue Tür blieb offen. Drei Papierboote ruhten auf der Fensterbank. Wir lauschten auf den Regen, doch die Straße blieb bis zum Morgen still.
```

## modes-de-096 · translation_quotation

Source task:

> Translate the surrounding text into German, preserving the quoted English message: The display reads "scan incomplete". It means the scan has not finished; it does not prove that the archive is damaged.

### baseline: pass

```text
Auf dem Display steht "scan incomplete". Das bedeutet, dass der Scan noch nicht abgeschlossen ist; es beweist nicht, dass das Archiv beschädigt ist.
```

### lite: pass

```text
Auf dem Display steht "scan incomplete". Das bedeutet, dass der Scan noch nicht abgeschlossen ist; es beweist nicht, dass das Archiv beschädigt ist.
```

### full: flagged

```text
Auf dem Display steht „scan incomplete“. Das bedeutet, dass der Scan noch nicht abgeschlossen ist; es beweist nicht, dass das Archiv beschädigt ist.
```

Review notes: Meaning is preserved, but the explicitly protected quotation is not reproduced exactly. / Meaning preserved, but exact protected quotation formatting changed.

### ultra: pass

```text
Auf dem Display steht "scan incomplete". Das bedeutet, dass der Scan noch nicht abgeschlossen ist; es beweist nicht, dass das Archiv beschädigt ist.
```

### off: pass

```text
Auf dem Display steht "scan incomplete". Das bedeutet, dass der Scan noch nicht abgeschlossen ist; es beweist nicht, dass das Archiv beschädigt ist.
```

## modes-de-097 · translation_scope

Source task:

> Translate into German: The change concerns parcel collection only. The information desk still opens at 08:30. Parcels can be collected from 09:15, including parcels that arrived before the change.

### baseline: pass

```text
Die Änderung betrifft nur die Paketabholung. Die Information öffnet weiterhin um 08:30 Uhr. Pakete können ab 09:15 Uhr abgeholt werden, auch solche, die vor der Änderung eingetroffen sind.
```

### lite: pass

```text
Die Änderung betrifft nur die Paketabholung. Die Information öffnet weiterhin um 08:30 Uhr. Pakete können ab 09:15 Uhr abgeholt werden, auch solche, die vor der Änderung eingetroffen sind.
```

### full: pass

```text
Die Änderung betrifft nur die Paketabholung. Die Information öffnet weiterhin um 08:30 Uhr. Pakete können ab 09:15 Uhr abgeholt werden, auch solche, die vor der Änderung eingetroffen sind.
```

### ultra: pass

```text
Die Änderung betrifft nur die Paketabholung. Die Information öffnet weiterhin um 08:30 Uhr. Pakete können ab 09:15 Uhr abgeholt werden, auch wenn sie vor der Änderung eingetroffen sind.
```

### off: pass

```text
Die Änderung betrifft nur die Paketabholung. Der Informationsschalter öffnet weiterhin um 08:30 Uhr. Pakete können ab 09:15 Uhr abgeholt werden, einschließlich der Pakete, die vor der Änderung eingetroffen sind.
```

## modes-de-098 · translation_sequence

Source task:

> Translate into German: Save the inventory first. Then have a second person check the missing items. Approve the order only after that check. A saved inventory is not an approved order.

### baseline: pass

```text
Speichern Sie zuerst den Bestand. Lassen Sie anschließend eine zweite Person die fehlenden Artikel überprüfen. Geben Sie die Bestellung erst nach dieser Überprüfung frei. Ein gespeicherter Bestand ist keine freigegebene Bestellung.
```

### lite: pass

```text
Speichern Sie zuerst die Bestandsliste. Lassen Sie dann eine zweite Person die fehlenden Artikel überprüfen. Genehmigen Sie die Bestellung erst nach dieser Prüfung. Eine gespeicherte Bestandsliste ist keine genehmigte Bestellung.
```

### full: pass

```text
Speichern Sie zuerst den Bestand. Lassen Sie dann eine zweite Person die fehlenden Artikel prüfen. Geben Sie die Bestellung erst nach dieser Prüfung frei. Ein gespeicherter Bestand ist keine freigegebene Bestellung.
```

### ultra: pass

```text
Speichern Sie zuerst den Bestand. Lassen Sie dann eine zweite Person die fehlenden Artikel prüfen. Geben Sie die Bestellung erst nach dieser Prüfung frei. Ein gespeicherter Bestand ist keine freigegebene Bestellung.
```

### off: pass

```text
Speichern Sie zuerst den Bestand. Lassen Sie dann eine zweite Person die fehlenden Artikel überprüfen. Genehmigen Sie die Bestellung erst nach dieser Überprüfung. Ein gespeicherter Bestand ist keine genehmigte Bestellung.
```

## modes-de-099 · translation_conflict

Source task:

> Translate into German: The packing list states 32 clips, but the hand count found 31. Nobody has repeated the count. The confirmed quantity is still unknown.

### baseline: pass

```text
Die Packliste gibt 32 Clips an, bei der manuellen Zählung wurden jedoch 31 festgestellt. Niemand hat die Zählung wiederholt. Die bestätigte Menge ist weiterhin unbekannt.
```

### lite: pass

```text
Die Packliste gibt 32 Clips an, aber bei der manuellen Zählung wurden 31 festgestellt. Niemand hat die Zählung wiederholt. Die bestätigte Menge ist weiterhin unbekannt.
```

### full: pass

```text
Die Packliste gibt 32 Clips an, bei der manuellen Zählung wurden jedoch 31 festgestellt. Niemand hat die Zählung wiederholt. Die bestätigte Menge ist weiterhin unbekannt.
```

### ultra: pass

```text
Die Packliste nennt 32 Clips, bei der manuellen Zählung wurden jedoch 31 festgestellt. Niemand hat die Zählung wiederholt. Die bestätigte Menge ist weiterhin unbekannt.
```

### off: pass

```text
Die Packliste gibt 32 Clips an, aber bei der manuellen Zählung wurden 31 festgestellt. Niemand hat die Zählung wiederholt. Die bestätigte Menge ist weiterhin unbekannt.
```

## modes-de-100 · translation_denominators

Source task:

> Translate into German: Of 110 messages checked, 22 requested a receipt. Seven of those 22 came from the website form. The total number of website-form messages is not recorded.

### baseline: pass

```text
Von 110 überprüften Nachrichten wurde in 22 um eine Empfangsbestätigung gebeten. Sieben dieser 22 Nachrichten gingen über das Website-Formular ein. Die Gesamtzahl der über das Website-Formular eingegangenen Nachrichten ist nicht erfasst.
```

### lite: pass

```text
Von 110 überprüften Nachrichten wurde in 22 um eine Empfangsbestätigung gebeten. Sieben dieser 22 Nachrichten kamen über das Website-Formular. Die Gesamtzahl der Nachrichten über das Website-Formular wurde nicht erfasst.
```

### full: pass

```text
In 22 von 110 geprüften Nachrichten wurde um eine Empfangsbestätigung gebeten. Sieben dieser 22 Nachrichten kamen über das Website-Formular. Die Gesamtzahl der Nachrichten über das Website-Formular ist nicht erfasst.
```

### ultra: pass

```text
Von 110 geprüften Nachrichten wurde in 22 um eine Empfangsbestätigung gebeten. Sieben dieser 22 Nachrichten kamen über das Website-Formular. Die Gesamtzahl der Nachrichten über das Website-Formular ist nicht erfasst.
```

### off: pass

```text
Von 110 überprüften Nachrichten wurde in 22 um eine Empfangsbestätigung gebeten. Sieben dieser 22 Nachrichten kamen über das Formular auf der Website. Die Gesamtzahl der Nachrichten, die über das Formular auf der Website eingingen, ist nicht erfasst.
```

