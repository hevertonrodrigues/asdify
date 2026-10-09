# de: all source tasks and answers

Labels below are unblinded after review. Pass requires both meaning reviews and exact checks. A flagged answer is retained unchanged.

## modes-de-016 · technical

Source task:

> Überarbeite den Hilfetext: Bei HTTP 408 darf der Client die GET-Anfrage einmal wiederholen. Das gilt nicht für POST. Wenn der zweite Versuch scheitert, soll eine Fehlermeldung angezeigt werden.

### baseline: pass

```text
Bei HTTP 408 darf der Client eine GET-Anfrage einmal wiederholen. Für POST-Anfragen gilt dies nicht. Scheitert auch der zweite Versuch, soll eine Fehlermeldung angezeigt werden.
```

### lite: pass

```text
Bei HTTP 408 darf der Client die GET-Anfrage einmal wiederholen. Das gilt nicht für POST. Scheitert der zweite Versuch, soll eine Fehlermeldung angezeigt werden.
```

### full: pass

```text
Bei HTTP 408 darf der Client eine GET-Anfrage einmal wiederholen. Für POST gilt das nicht. Scheitert auch der zweite Versuch, soll eine Fehlermeldung angezeigt werden.
```

### ultra: pass

```text
Bei HTTP 408 darf der Client eine GET-Anfrage einmal wiederholen, eine POST-Anfrage nicht. Scheitert auch der zweite Versuch, soll eine Fehlermeldung angezeigt werden.
```

### off: flagged

```text
Bei HTTP 408 darf der Client eine GET-Anfrage einmal wiederholen. POST-Anfragen dürfen nicht wiederholt werden. Scheitert auch der zweite Versuch, soll eine Fehlermeldung angezeigt werden.
```

Review notes: Die fehlende Wiederholungserlaubnis bei HTTP 408 wird zu einem allgemeinen POST-Verbot. / Das POST-Verbot reicht über die HTTP-408-Regel hinaus.

## modes-de-018 · summary

Source task:

> Fasse für die Kursteilnehmenden zusammen: Der Kurs beginnt am Montag wie geplant um 18 Uhr. Wegen der defekten Spüle wird nicht gekocht. Stattdessen findet die Einführung in die Zutatenkunde statt. Der praktische Kochtermin wird später mitgeteilt.

### baseline: pass

```text
Der Kurs beginnt wie geplant am Montag um 18 Uhr. Wegen der defekten Spüle kochen wir nicht, sondern starten mit der Einführung in die Zutatenkunde. Der praktische Kochtermin wird später bekannt gegeben.
```

### lite: pass

```text
Der Kurs beginnt wie geplant am Montag um 18 Uhr. Wegen der defekten Spüle wird nicht gekocht; stattdessen gibt es eine Einführung in die Zutatenkunde. Der praktische Kochtermin wird später mitgeteilt.
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
Der Kurs beginnt wie geplant am Montag um 18 Uhr. Wegen der defekten Spüle wird nicht gekocht; stattdessen findet die Einführung in die Zutatenkunde statt. Der praktische Kochtermin wird später mitgeteilt.
```

## modes-de-024 · conditions

Source task:

> Überarbeite: Ein Rabatt von 15 % gilt nur bei Buchung von mindestens drei Terminen im selben Monat. Bereits bezahlte Einzeltermine werden dafür nicht rückwirkend zusammengerechnet.

### baseline: pass

```text
15 % Rabatt gibt es nur bei Buchung von mindestens drei Terminen im selben Monat. Bereits bezahlte Einzeltermine werden dafür nicht rückwirkend zusammengerechnet.
```

### lite: pass

```text
15 % Rabatt gelten nur bei Buchung von mindestens drei Terminen im selben Monat. Bereits bezahlte Einzeltermine werden dafür nicht rückwirkend zusammengerechnet.
```

### full: pass

```text
15 % Rabatt gelten nur bei Buchung von mindestens drei Terminen im selben Monat. Bereits bezahlte Einzeltermine werden dafür nicht rückwirkend zusammengerechnet.
```

### ultra: pass

```text
15 % Rabatt gelten nur bei Buchung von mindestens drei Terminen im selben Monat. Bereits bezahlte Einzeltermine zählen nicht rückwirkend dazu.
```

### off: pass

```text
Der Rabatt von 15 % gilt nur, wenn mindestens drei Termine im selben Monat gebucht werden. Bereits bezahlte Einzeltermine werden dafür nicht rückwirkend zusammengerechnet.
```

## modes-de-034 · voice

Source task:

> Mach den Text kürzer, aber behalte den leichten Humor: Unser Kopierer hat heute beschlossen, nur halbe Seiten zu liefern. Bis er wieder ganze Geschichten mag, nutzt bitte den Drucker im Nebenraum. Eine Reparaturzeit kennen wir noch nicht.

### baseline: flagged

```text
Unser Kopierer macht heute halbe Sachen. Nutzt bitte den Drucker im Nebenraum. Wann er repariert ist, wissen wir noch nicht.
```

Review notes: Die allgemeine Redewendung lässt den konkreten Halbseitenfehler weg. / Die Redewendung ersetzt die konkrete Fehlerbeschreibung durch eine allgemeine Anspielung.

### lite: pass

```text
Unser Kopierer liefert heute nur halbe Geschichten. Nutzt bitte den Drucker im Nebenraum, bis er wieder ganze Seiten mag. Die Reparaturzeit ist noch unbekannt.
```

### full: pass

```text
Unser Kopierer liefert heute nur halbe Geschichten. Nutzt bitte den Drucker im Nebenraum, bis er wieder ganze Seiten schafft. Die Reparaturzeit ist noch unbekannt.
```

### ultra: pass

```text
Unser Kopierer mag heute nur halbe Seiten. Nutzt bitte den Drucker im Nebenraum, bis er wieder ganze mag. Die Reparaturzeit ist noch unbekannt.
```

### off: flagged

```text
Unser Kopierer liefert heute nur halbe Geschichten. Bitte nutzt den Drucker im Nebenraum. Wann der Kopierer repariert wird, wissen wir noch nicht.
```

Review notes: Der konkrete Defekt ist nur noch eine mehrdeutige Metapher; seine Erhaltung ist nicht gesichert. / Kürzer und humorvoll, aber die konkrete Störung mit halben Seiten bleibt unklar.

## modes-de-036 · ambiguity

Source task:

> Überarbeite diese Notiz, ohne die Uhrzeit umzudeuten: „Treffen um 7; morgens oder abends ist noch nicht geklärt.“ Erhalte die Unklarheit und fordere ihre Klärung statt eine Zeit festzulegen.

### baseline: pass

```text
Treffen um 7 Uhr. Ob morgens oder abends, ist noch offen. Bitte klärt, welche Uhrzeit gemeint ist.
```

### lite: pass

```text
Treffen um 7. Ob morgens oder abends, ist noch unklar. Bitte klären.
```

### full: pass

```text
Treffen um 7. Ob morgens oder abends, ist noch unklar. Bitte klären.
```

### ultra: pass

```text
Treffen um 7. Ob morgens oder abends, ist noch offen. Bitte klären.
```

### off: pass

```text
Treffen um 7 Uhr. Ob morgens oder abends, ist noch offen. Bitte klärt, welche Uhrzeit gemeint ist.
```

## modes-de-045 · summary

Source task:

> Fasse die Änderung zusammen: Ab 15. Juli werden Reparaturaufträge am Seiteneingang angenommen. Die Abholung bleibt an der Haupttheke. Bereits vereinbarte Abgabetermine ab dem 15. Juli nutzen ebenfalls den Seiteneingang.

### baseline: pass

```text
Ab dem 15. Juli werden Reparaturaufträge am Seiteneingang angenommen, auch bei bereits vereinbarten Abgabeterminen. Die Abholung bleibt an der Haupttheke.
```

### lite: pass

```text
Ab 15. Juli werden Reparaturaufträge am Seiteneingang angenommen. Das gilt auch für bereits vereinbarte Abgabetermine ab diesem Datum. Die Abholung bleibt an der Haupttheke.
```

### full: pass

```text
Ab 15. Juli werden Reparaturaufträge am Seiteneingang angenommen. Das gilt auch für bereits vereinbarte Abgabetermine ab diesem Datum. Die Abholung bleibt an der Haupttheke.
```

### ultra: pass

```text
Ab 15. Juli werden Reparaturaufträge am Seiteneingang angenommen, auch bei bereits vereinbarten Abgabeterminen ab diesem Datum. Die Abholung bleibt an der Haupttheke.
```

### off: pass

```text
Ab dem 15. Juli werden Reparaturaufträge am Seiteneingang angenommen. Das gilt auch für bereits vereinbarte Abgabetermine ab diesem Datum. Die Abholung bleibt an der Haupttheke.
```

## modes-de-055 · conflicting_notes

Source task:

> Formuliere für das Lagerbuch: Der Lieferschein nennt 65 Schrauben. In der geöffneten Tüte wurden 64 gezählt. Die Waage wurde nicht verwendet und eine zweite Zählung steht aus.

### baseline: pass

```text
Laut Lieferschein: 65 Schrauben. In der geöffneten Tüte wurden 64 Schrauben gezählt. Die Waage wurde nicht verwendet; eine zweite Zählung steht noch aus.
```

### lite: pass

```text
Laut Lieferschein: 65 Schrauben. In der geöffneten Tüte gezählt: 64 Schrauben. Die Waage wurde nicht verwendet. Eine zweite Zählung steht aus.
```

### full: pass

```text
Lieferschein: 65 Schrauben. In der geöffneten Tüte gezählt: 64 Schrauben. Die Waage wurde nicht verwendet. Eine zweite Zählung steht aus.
```

### ultra: pass

```text
Lieferschein: 65 Schrauben. In der geöffneten Tüte gezählt: 64. Waage nicht verwendet; zweite Zählung steht aus.
```

### off: pass

```text
Laut Lieferschein: 65 Schrauben. In der geöffneten Tüte gezählt: 64 Schrauben. Die Waage wurde nicht verwendet. Eine zweite Zählung steht noch aus.
```

## modes-de-061 · exact_format

Source task:

> Vereinfache den deutschen message-Wert. Antworte ausschließlich mit JSON und den Schlüsseln request, retries, message. request und retries bleiben gleich: {"request":"N-407","retries":1,"message":"Ihre Datei konnte nicht verarbeitet werden; bitte laden Sie sie als TXT-Datei erneut hoch."}

### baseline: pass

```text
{"request":"N-407","retries":1,"message":"Ihre Datei konnte nicht verarbeitet werden. Bitte laden Sie sie noch einmal als TXT-Datei hoch."}
```

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
Als Hannes in den Tauschraum kam, tropfte sein Schirm noch. In einer Blechdose brachte er alte Garnrollen mit, ungefähr vierzig, wie er sagte. Gezählt oder gewogen wurden sie nicht; manche waren fast voll, andere hatten nur noch wenige Windungen.

Die Dose hatte früher seinem Bruder gehört und sollte wieder mit nach Hause. Das Garn durfte bleiben. Mina legte die Rollen vorsichtig in eine Schale, ohne nach dem Grund für die späte Abgabe zu fragen.

Ein junger Besucher entdeckte eine grüne Rolle und fragte, ob er sie für seinen Stoffbeutel nehmen dürfe. Hannes stimmte zu. Woher diese Rolle stammte, wusste er nicht mehr. Der Besucher nahm nur diese eine Rolle.

Beim Abschied hatte der Regen nachgelassen. Hannes ging mit der leeren Dose nach Hause. Die übrigen Rollen blieben als Spende für Reparaturen im Tauschraum. Mina vermerkte die Spende im Buch, ohne den Besucher namentlich zu erfassen.
```

### lite: pass

```text
Als Hannes in den Tauschraum kam, tropfte Wasser von seinem Schirm. In einer Blechdose brachte er alte Garnrollen mit. Ungefähr vierzig seien es, sagte er; gezählt hatte er sie nicht. Manche waren fast voll, andere hatten nur wenige Windungen. Er stellte die Dose neben die Waage. Gewogen wurden die Rollen nicht.

Mina fragte, ob er auch die Dose abgeben wolle. Hannes verneinte: Sie hatte früher seinem Bruder gehört, und er wollte sie wieder mitnehmen. Das Garn durfte bleiben. Mina legte die Rollen vorsichtig in eine Schale. Sie fragte nicht nach dem Grund für die späte Abgabe und schrieb keine Geschichte über den Bruder dazu.

Ein junger Besucher fragte, ob er eine grüne Rolle für seinen Stoffbeutel nehmen dürfe. Hannes stimmte zu. Woher diese Rolle stammte, wusste er nicht mehr. Bekannt ist nur, dass er sie aufbewahrt hatte und nun weitergab – nicht, dass sie seinem Bruder gehört hatte. Der Besucher nahm diese eine Rolle.

Beim Abschied hatte der Regen nachgelassen. Hannes ging mit der leeren Dose nach Hause. Die übrigen Rollen blieben als Spende für Reparaturen im Tauschraum. Mina vermerkte die Spende im Buch, ohne den Besucher namentlich zu erfassen. Ob er den Stoffbeutel noch am selben Abend reparierte oder Hannes später wiederkam, ist nicht bekannt.
```

### full: pass

```text
Als Hannes den Tauschraum betrat, tropfte sein Schirm. Er brachte alte Garnrollen in einer Blechdose mit: ungefähr vierzig, sagte er, gezählt habe er sie nicht. Manche waren fast voll, andere hatten nur wenige Windungen. Er stellte die Dose neben die Waage; gewogen wurden die Rollen nicht.

Mina fragte, ob die Dose ebenfalls bleiben sollte. Hannes wollte sie wieder mitnehmen, denn sie hatte früher seinem Bruder gehört. Nur das Garn sollte bleiben. Mina legte die Rollen vorsichtig in eine Schale. Nach dem Grund für die späte Abgabe fragte sie nicht, und eine Geschichte über den Bruder schrieb sie nicht dazu.

Ein junger Besucher entdeckte eine grüne Rolle und fragte, ob er sie für seinen Stoffbeutel nehmen dürfe. Hannes stimmte zu. Woher diese Rolle stammte, wusste er nicht mehr. Er hatte sie aufbewahrt; ob sie seinem Bruder gehört hatte, war unbekannt. Der Besucher nahm nur diese eine Rolle.

Beim Abschied ließ der Regen nach. Hannes ging mit der leeren Dose nach Hause. Die übrigen Rollen blieben als Spende für Reparaturen im Tauschraum. Mina vermerkte die Spende im Buch, ohne den Besucher namentlich zu erfassen. Ob der Beutel noch am selben Abend repariert wurde oder Hannes später wiederkam, ist nicht bekannt.
```

### ultra: pass

```text
Als Hannes in den Tauschraum kam, tropfte sein Schirm. In einer Blechdose brachte er alte Garnrollen mit: ungefähr vierzig, sagte er, gezählt hatte er sie nicht. Manche waren fast voll, andere trugen nur wenige Windungen. Er stellte die Dose neben die Waage; gewogen wurden die Rollen nicht.

Mina fragte, ob die Dose ebenfalls bleiben sollte. Hannes wollte sie wieder mitnehmen: Sie hatte früher seinem Bruder gehört. Nur das Garn gab er ab. Mina legte die Rollen vorsichtig in eine Schale. Nach dem Grund für die späte Abgabe fragte sie nicht; eine Geschichte über den Bruder fügte sie nicht hinzu.

Ein junger Besucher bat um eine grüne Rolle für seinen Stoffbeutel. Hannes stimmte zu. Woher sie stammte, wusste er nicht mehr. Er hatte sie aufbewahrt und gab sie nun weiter; als Garn seines Bruders lässt sie sich nicht bezeichnen. Der Besucher nahm nur diese eine Rolle.

Beim Abschied ließ der Regen nach. Hannes ging mit der leeren Dose nach Hause. Die übrigen Rollen blieben als Spende für Reparaturen. Mina vermerkte die Spende im Buch, ohne den Besucher namentlich zu erfassen. Ob der Beutel noch am selben Abend repariert wurde oder Hannes später wiederkam, ist nicht bekannt.
```

### off: pass

```text
Als Hannes in den Tauschraum kam, tropfte Wasser von seinem Schirm. In einer Blechdose brachte er alte Garnrollen mit: ungefähr vierzig, wie er sagte, gezählt hatte er sie nicht. Manche waren fast voll, andere hatten nur noch wenige Windungen. Er stellte die Dose neben die Waage; gewogen wurden die Rollen nicht.

Mina fragte, ob die Dose ebenfalls bleiben sollte. Hannes wollte sie wieder mitnehmen, denn sie hatte früher seinem Bruder gehört. Nur das Garn gab er ab. Mina legte die Rollen vorsichtig in eine Schale, ohne nach dem Grund für die späte Abgabe zu fragen.

Ein junger Besucher entdeckte eine grüne Rolle und fragte, ob er sie für seinen Stoffbeutel nehmen dürfe. Hannes stimmte zu. Woher diese Rolle stammte, wusste er nicht mehr. Er hatte sie aufbewahrt und gab sie nun weiter. Der Besucher nahm diese eine Rolle mit.

Beim Abschied hatte der Regen nachgelassen. Hannes ging mit der leeren Dose nach Hause. Die übrigen Rollen blieben als Spende für Reparaturen im Tauschraum. Mina vermerkte die Spende im Buch, ohne den Besucher namentlich zu erfassen.
```

## modes-de-085 · translation_json

Source task:

> Translate the note value into German. Return only valid JSON with the original keys, code, and quantity: {"code":"DE-K31","quantity":4,"note":"Four seals are missing. Do not open the containers until replacement seals are ready."}

### baseline: pass

```text
{"code":"DE-K31","quantity":4,"note":"Vier Siegel fehlen. Öffnen Sie die Behälter erst, wenn Ersatzsiegel bereitstehen."}
```

### lite: pass

```text
{"code":"DE-K31","quantity":4,"note":"Vier Siegel fehlen. Öffnen Sie die Behälter erst, wenn Ersatzsiegel bereitliegen."}
```

### full: pass

```text
{"code":"DE-K31","quantity":4,"note":"Vier Siegel fehlen. Öffnen Sie die Behälter erst, wenn Ersatzsiegel bereitliegen."}
```

### ultra: pass

```text
{"code":"DE-K31","quantity":4,"note":"Vier Siegel fehlen. Öffnen Sie die Behälter nicht, bevor Ersatzsiegel bereitliegen."}
```

### off: pass

```text
{"code":"DE-K31","quantity":4,"note":"Vier Siegel fehlen. Öffnen Sie die Behälter nicht, bevor Ersatzsiegel bereitstehen."}
```

## modes-de-087 · translation_conditions

Source task:

> Translate this fictional room rule into German: The rehearsal room may be used only after the floor has dried and the caretaker has unlocked the door. An unlocked door alone is not permission to enter.

### baseline: pass

```text
Der Proberaum darf erst benutzt werden, wenn der Boden getrocknet ist und der Hausmeister die Tür aufgeschlossen hat. Eine aufgeschlossene Tür allein ist keine Erlaubnis zum Betreten.
```

### lite: pass

```text
Der Proberaum darf erst genutzt werden, wenn der Boden getrocknet ist und die Hausmeisterin oder der Hausmeister die Tür aufgeschlossen hat. Eine aufgeschlossene Tür allein ist keine Erlaubnis, den Raum zu betreten.
```

### full: pass

```text
Der Proberaum darf erst benutzt werden, wenn der Boden getrocknet ist und die für die Hausbetreuung zuständige Person die Tür aufgeschlossen hat. Eine aufgeschlossene Tür allein ist keine Erlaubnis zum Betreten.
```

### ultra: pass

```text
Der Proberaum darf erst benutzt werden, wenn der Boden getrocknet ist und die für die Hausbetreuung zuständige Person die Tür aufgeschlossen hat. Eine aufgeschlossene Tür allein ist keine Erlaubnis zum Betreten.
```

### off: pass

```text
Der Proberaum darf erst benutzt werden, wenn der Boden getrocknet ist und die Hausmeisterin oder der Hausmeister die Tür aufgeschlossen hat. Eine aufgeschlossene Tür allein ist keine Erlaubnis, den Raum zu betreten.
```

