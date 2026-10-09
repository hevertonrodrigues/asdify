# fr: all source tasks and answers

Labels below are unblinded after review. Pass requires both meaning reviews and exact checks. A flagged answer is retained unchanged.

## modes-fr-028 · numbers_units

Source task:

> Rends cette fiche plus directe : Chaque recharge contient 750 mL. La consommation estimée est de 25 mL par passage. Les chiffres concernent le distributeur d’essai, pas tous les modèles.

### baseline: pass

```text
Chaque recharge contient 750 mL. Consommation estimée : 25 mL par passage. Ces chiffres s’appliquent uniquement au distributeur d’essai.
```

### lite: pass

```text
Chaque recharge contient 750 mL. La consommation est estimée à 25 mL par passage. Ces chiffres concernent le distributeur d’essai, pas tous les modèles.
```

### full: pass

```text
Chaque recharge contient 750 mL. La consommation est estimée à 25 mL par passage. Ces chiffres concernent uniquement le distributeur d’essai, pas tous les modèles.
```

### ultra: pass

```text
Chaque recharge contient 750 mL. Consommation estimée : 25 mL par passage. Ces chiffres concernent le distributeur d’essai, pas tous les modèles.
```

### off: pass

```text
Chaque recharge contient 750 mL. La consommation est estimée à 25 mL par passage. Ces chiffres s’appliquent au distributeur d’essai, pas à tous les modèles.
```

## modes-fr-039 · exceptions

Source task:

> Clarifie cette règle fictive de concours : Chaque équipe peut présenter deux projets. Un troisième est admis uniquement si l’un des deux premiers a été retiré avant la clôture. Aucun retrait après la clôture ne libère de place.

### baseline: flagged

```text
Chaque équipe peut présenter deux projets. Elle peut en présenter un troisième uniquement si elle a retiré l’un des deux premiers avant la clôture. Un retrait après la clôture ne libère aucune place.
```

Review notes: La reformulation ajoute une restriction sur l’auteur du retrait, absent de la règle source. / Attribue à l’équipe un retrait dont l’acteur n’était pas précisé, restreignant la condition d’admission.

### lite: pass

```text
Chaque équipe peut présenter deux projets. Un troisième projet est admis uniquement si l’un des deux premiers a été retiré avant la clôture. Un retrait après la clôture ne libère aucune place.
```

### full: pass

```text
Chaque équipe peut présenter deux projets. Un troisième projet est admis uniquement si l’un des deux premiers a été retiré avant la clôture. Un retrait après la clôture ne libère aucune place.
```

### ultra: pass

```text
Chaque équipe peut présenter deux projets. Un troisième n’est admis que si l’un des deux premiers a été retiré avant la clôture. Un retrait après la clôture ne libère aucune place.
```

### off: pass

```text
Chaque équipe peut présenter deux projets. Elle ne peut en présenter un troisième que si l’un des deux premiers a été retiré avant la clôture. Un retrait après la clôture ne libère aucune place.
```

## modes-fr-048 · analysis

Source task:

> Deux descriptions d’un essai fictif : A dit « aucune panne pendant 40 heures » ; B dit « aucun incident observé pendant les 40 heures où le capteur enregistrait ». Pourquoi B est-elle plus précise, sachant que le capteur n’enregistrait pas en continu ?

### baseline: pass

```text
B limite le constat aux 40 heures d’enregistrement du capteur. Comme celui-ci n’enregistrait pas en continu, une panne a pu survenir hors de ces périodes sans être détectée. A laisse entendre qu’aucune panne n’a eu lieu pendant 40 heures, sans préciser cette limite.
```

### lite: pass

```text
B limite le constat aux 40 heures où le capteur enregistrait et précise qu’aucun incident n’a été observé. Comme l’enregistrement n’était pas continu, elle ne permet pas d’exclure une panne pendant les périodes non enregistrées. A ne précise pas cette limite.
```

### full: pass

```text
B limite le constat aux 40 heures d’enregistrement et précise qu’aucun incident n’a été observé. Comme le capteur n’enregistrait pas en continu, elle ne permet pas d’exclure des incidents hors de ces périodes. A affirme une absence de panne sans préciser cette limite d’observation.
```

### ultra: pass

```text
B limite le constat aux 40 heures d’enregistrement : aucun incident n’y a été observé. Le capteur n’enregistrant pas en continu, des incidents ont pu survenir hors de ces périodes. A affirme une absence de panne sans préciser cette limite.
```

### off: pass

```text
B précise que l’absence d’incident observé concerne uniquement les 40 heures d’enregistrement du capteur. Comme celui-ci n’enregistrait pas en continu, on ne sait pas si des incidents ont eu lieu en dehors de ces périodes. A peut laisser croire qu’aucune panne ne s’est produite pendant 40 heures continues.
```

## modes-fr-063 · exact_format

Source task:

> Corrige seulement la faute « receu » dans cette ligne et renvoie la ligne seule : Dossier receu : AB_04 — aucun paiement demandé.

### baseline: pass

```text
Dossier reçu : AB_04 — aucun paiement demandé.
```

### lite: pass

```text
Dossier reçu : AB_04 — aucun paiement demandé.
```

### full: pass

```text
Dossier reçu : AB_04 — aucun paiement demandé.
```

### ultra: pass

```text
Dossier reçu : AB_04 — aucun paiement demandé.
```

### off: pass

```text
Dossier reçu : AB_04 — aucun paiement demandé.
```

## modes-fr-064 · exact_format

Source task:

> Prépare un message court : le destinataire {{prenom}} peut télécharger sa facture avec {{lien_facture}} jusqu’au 14 juin. Garde les deux variables telles quelles ; ne remplace pas leur contenu.

### baseline: pass

```text
Bonjour {{prenom}}, vous pouvez télécharger votre facture avec ce lien : {{lien_facture}} jusqu’au 14 juin.
```

### lite: pass

```text
Bonjour {{prenom}}, vous pouvez télécharger votre facture avec ce lien : {{lien_facture}}, jusqu’au 14 juin.
```

### full: pass

```text
Bonjour {{prenom}}, vous pouvez télécharger votre facture jusqu’au 14 juin : {{lien_facture}}
```

### ultra: pass

```text
Bonjour {{prenom}}, vous pouvez télécharger votre facture avec {{lien_facture}} jusqu’au 14 juin.
```

### off: pass

```text
Bonjour {{prenom}}, vous pouvez télécharger votre facture jusqu’au 14 juin : {{lien_facture}}.
```

## modes-fr-068 · exact_format

Source task:

> Rends ce message plus clair tout en conservant la citation anglaise exacte : Le journal affiche "buffer full". Cela décrit un tampon plein, pas une perte de données confirmée. Il faut examiner le journal complet avant de conclure.

### baseline: pass

```text
Le message "buffer full" dans le journal indique que le tampon est plein. Il ne confirme pas une perte de données. Il faut examiner le journal complet avant de conclure.
```

### lite: pass

```text
Le journal affiche "buffer full". Ce message indique que le tampon est plein, mais ne confirme pas une perte de données. Il faut examiner le journal complet avant de conclure.
```

### full: pass

```text
Le journal affiche "buffer full", ce qui indique un tampon plein, mais ne confirme pas une perte de données. Il faut examiner le journal complet avant de conclure.
```

### ultra: pass

```text
Le journal affiche "buffer full" : le tampon est plein, mais aucune perte de données n’est confirmée. Il faut examiner le journal complet avant de conclure.
```

### off: pass

```text
Le journal affiche "buffer full", ce qui indique que le tampon est plein, sans confirmer une perte de données. Il faut examiner le journal complet avant de tirer une conclusion.
```

## modes-fr-078 · long_voice

Source task:

> Écris une version plus courte de ce récit pour un bulletin d’association. Garde la voix douce et les faits qui donnent son sens à la rencontre. N’invente pas la suite de l’histoire ni une morale explicite.
> 
> Quand la porte s’est ouverte, il pleuvait assez pour que les manteaux brillent sous la lampe. Émile tenait une boîte à chaussures contre lui. Il n’était pas venu chercher un objet ; il voulait déposer les boutons qu’il avait gardés pendant des années. La boîte en contenait une centaine, disait-il, sans les avoir comptés. Certains étaient en bois, d’autres en métal, et plusieurs avaient encore un petit fil accroché au trou.
> 
> Au comptoir, Salomé lui a demandé s’il souhaitait garder la boîte. Il a répondu oui. Les boutons pouvaient rester, mais la boîte portait une inscription de sa sœur et il voulait la rapporter chez lui. Salomé a posé un plateau sur la table pour recevoir les boutons. Elle n’a pas lu l’inscription à voix haute et ne lui a pas demandé pourquoi il n’apportait ces boutons que maintenant.
> 
> Une enfant a choisi un bouton bleu pour réparer la poche de son manteau. Avant de le prendre, elle a demandé si elle pouvait. Émile a acquiescé. Il n’a pas raconté à qui le bouton avait appartenu, et personne ne l’a deviné à sa place. Dans le bulletin, on ne peut donc pas le présenter comme un bouton de sa sœur. Ce que l’on sait, c’est qu’il l’avait gardé et qu’il a accepté de le donner.
> 
> La pluie a cessé avant la fermeture. Émile est reparti avec sa boîte vide. Le plateau est resté sur la table, sans étiquette de prix : les boutons étaient un don pour les réparations de l’atelier. Salomé a noté le don dans le registre, sans écrire le nom de l’enfant. Le récit s’arrête à ce moment-là. Il ne dit ni si le manteau a été réparé le soir même, ni si Émile est revenu. Ce sont des fins possibles, mais elles n’ont pas été observées.

### baseline: flagged

```text
Un soir de pluie, Émile est venu déposer les boutons qu’il gardait depuis des années : une centaine, selon lui, dans une boîte à chaussures. Il souhaitait conserver la boîte, qui portait une inscription de sa sœur.

Salomé a installé un plateau pour recevoir les boutons, sans lire l’inscription à voix haute ni lui demander pourquoi il les apportait maintenant. Une enfant a demandé la permission de prendre un bouton bleu pour réparer la poche de son manteau. Émile a acquiescé. Il n’a pas précisé à qui ce bouton avait appartenu.

La pluie avait cessé lorsqu’Émile est reparti avec sa boîte vide. Les boutons sont restés sur le plateau, offerts pour les réparations de l’atelier. Salomé a inscrit le don au registre, sans noter le nom de l’enfant.
```

Review notes: Résumé doux et substantiellement fidèle, mais omission de l’absence d’étiquette de prix et ajout d’un moment non établi. / Résumé fluide, mais omet l’absence d’étiquette de prix et ajoute un moment de la journée non établi.

### lite: pass

```text
Quand la porte s’est ouverte, la pluie faisait briller les manteaux sous la lampe. Émile tenait une boîte à chaussures contre lui. Il venait déposer les boutons gardés pendant des années : une centaine, disait-il, sans les avoir comptés. Certains étaient en bois, d’autres en métal ; plusieurs portaient encore un petit fil.

Au comptoir, Salomé lui a demandé s’il souhaitait garder la boîte. Oui : elle portait une inscription de sa sœur, et il voulait la rapporter chez lui. Salomé a posé un plateau pour recevoir les boutons, sans lire l’inscription à voix haute ni demander pourquoi il les apportait seulement maintenant.

Une enfant a choisi un bouton bleu pour réparer la poche de son manteau. Avant de le prendre, elle a demandé la permission. Émile a acquiescé. Il n’a pas dit à qui ce bouton avait appartenu, et personne ne l’a deviné à sa place. On ne peut donc pas le présenter comme un bouton de sa sœur : on sait seulement qu’il l’avait gardé et avait accepté de le donner.

La pluie a cessé avant la fermeture. Émile est reparti avec sa boîte vide. Le plateau est resté sur la table, sans étiquette de prix : les boutons étaient un don pour les réparations de l’atelier. Salomé l’a inscrit au registre, sans noter le nom de l’enfant. Le récit s’arrête là : on ne sait ni si le manteau a été réparé le soir même, ni si Émile est revenu.
```

### full: pass

```text
Sous la pluie, les manteaux brillaient à la lumière de la lampe. Émile est entré avec une boîte à chaussures serrée contre lui. Il venait déposer des boutons gardés pendant des années : une centaine, disait-il, sans les avoir comptés. Certains étaient en bois, d’autres en métal ; plusieurs portaient encore un petit fil.

Salomé lui a demandé s’il voulait garder la boîte. Oui : elle portait une inscription de sa sœur. Salomé a posé un plateau pour les boutons, sans lire l’inscription à voix haute ni demander pourquoi il les apportait seulement maintenant.

Une enfant a demandé la permission de prendre un bouton bleu pour réparer la poche de son manteau. Émile a acquiescé. Il n’a pas dit à qui ce bouton avait appartenu, et personne ne l’a deviné à sa place. Rien ne permet donc de le présenter comme un bouton de sa sœur : on sait seulement qu’il l’avait gardé et acceptait de le donner.

La pluie a cessé avant la fermeture. Émile est reparti avec sa boîte vide. Le plateau est resté sans étiquette de prix : les boutons étaient un don pour les réparations de l’atelier. Salomé l’a inscrit au registre, sans nommer l’enfant. Le récit s’arrête là : on ne sait pas si le manteau a été réparé le soir même ni si Émile est revenu.
```

### ultra: pass

```text
Quand la porte s’est ouverte, la pluie faisait briller les manteaux sous la lampe. Émile tenait une boîte à chaussures. Il venait déposer des boutons gardés pendant des années : une centaine, disait-il, sans les avoir comptés. Certains étaient en bois, d’autres en métal ; plusieurs portaient encore un petit fil.

Salomé lui a demandé s’il souhaitait garder la boîte. Oui : elle portait une inscription de sa sœur. Les boutons pouvaient rester. Salomé a posé un plateau pour les recevoir, sans lire l’inscription à voix haute ni demander pourquoi il les apportait seulement maintenant.

Une enfant a demandé la permission de prendre un bouton bleu pour réparer la poche de son manteau. Émile a acquiescé. Il n’a pas dit à qui ce bouton avait appartenu, et personne ne l’a deviné à sa place. Rien ne permet donc de le présenter comme celui de sa sœur : on sait seulement qu’il l’avait gardé et acceptait de le donner.

La pluie a cessé avant la fermeture. Émile est reparti avec sa boîte vide. Le plateau est resté sur la table, sans étiquette de prix : les boutons étaient un don pour les réparations de l’atelier. Salomé l’a inscrit au registre, sans nommer l’enfant. Le récit s’arrête là : on ignore si le manteau a été réparé le soir même ou si Émile est revenu.
```

### off: pass

```text
Quand Émile est entré, la pluie faisait briller les manteaux sous la lampe. Il tenait contre lui une boîte à chaussures : il venait donner les boutons qu’il avait gardés pendant des années. Une centaine, disait-il, sans les avoir comptés. Il y en avait en bois, en métal, et plusieurs portaient encore un petit fil.

Salomé lui a demandé s’il voulait garder la boîte. Oui : elle portait une inscription de sa sœur. Salomé a posé un plateau pour les boutons, sans lire l’inscription à voix haute ni lui demander pourquoi il les apportait maintenant.

Une enfant a demandé la permission de prendre un bouton bleu pour réparer la poche de son manteau. Émile a acquiescé. Il n’a pas dit à qui ce bouton avait appartenu, et personne ne l’a deviné à sa place. On sait seulement qu’il l’avait gardé et qu’il acceptait de le donner.

La pluie avait cessé lorsqu’Émile est reparti avec sa boîte vide. Le plateau est resté sur la table, sans étiquette de prix : les boutons étaient un don pour les réparations de l’atelier. Salomé l’a inscrit au registre, sans noter le nom de l’enfant. Le récit s’arrête là : on ne sait pas si le manteau a été réparé le soir même, ni si Émile est revenu.
```

## modes-fr-080 · scope

Source task:

> Réponds seulement à la question : faut-il payer pour emprunter une couverture ? Dans cet accueil fictif, les couvertures sont prêtées gratuitement, avec un dépôt remboursable de 5 €. Le dépôt est rendu lorsque la couverture revient ; ce n’est pas un prix de location.

### baseline: pass

```text
Le prêt est gratuit, mais un dépôt de 5 € est demandé et remboursé au retour de la couverture.
```

### lite: pass

```text
Le prêt est gratuit, mais un dépôt de 5 € est demandé. Il est remboursé au retour de la couverture : ce n’est pas un prix de location.
```

### full: pass

```text
L’emprunt est gratuit, mais il faut verser un dépôt de 5 €, remboursé au retour de la couverture. Ce n’est pas un prix de location.
```

### ultra: pass

```text
Le prêt est gratuit, mais un dépôt de 5 € est demandé puis remboursé au retour de la couverture. Ce n’est pas un prix de location.
```

### off: pass

```text
Le prêt est gratuit, mais il faut verser un dépôt de 5 €, remboursé lorsque la couverture est rendue. Ce n’est pas un prix de location.
```

## modes-fr-083 · translation_actor

Source task:

> Translate into French: Ana checked the contents on Monday. The box was sealed on Tuesday, but the record does not say by whom. On Wednesday, Luca collected the sealed box.

### baseline: pass

```text
Ana a vérifié le contenu lundi. La boîte a été scellée mardi, mais le registre ne précise pas par qui. Mercredi, Luca a récupéré la boîte scellée.
```

### lite: pass

```text
Ana a vérifié le contenu lundi. La boîte a été scellée mardi, mais le registre ne précise pas par qui. Mercredi, Luca a récupéré la boîte scellée.
```

### full: pass

```text
Ana a vérifié le contenu lundi. La boîte a été scellée mardi, mais le registre ne précise pas par qui. Mercredi, Luca a récupéré la boîte scellée.
```

### ultra: pass

```text
Ana a vérifié le contenu lundi. La boîte a été scellée mardi, mais le registre ne précise pas par qui. Mercredi, Luca a récupéré la boîte scellée.
```

### off: pass

```text
Ana a vérifié le contenu lundi. La boîte a été scellée mardi, mais le registre ne précise pas par qui. Mercredi, Luca a récupéré la boîte scellée.
```

## modes-fr-092 · translation_exceptions

Source task:

> Translate this fictional workshop policy into French: Fees are non-refundable after a session has taken place. If the organiser cancels before the session, participants may request a refund. They do not have to accept a credit instead.

### baseline: pass

```text
Les frais ne sont pas remboursables une fois la séance passée. Si l’organisateur annule avant la séance, les participants peuvent demander un remboursement. Ils ne sont pas obligés d’accepter un avoir à la place.
```

### lite: pass

```text
Les frais ne sont plus remboursables une fois la séance tenue. Si l’organisateur annule avant la séance, les participants peuvent demander un remboursement. Ils ne sont pas obligés d’accepter un avoir à la place.
```

### full: pass

```text
Les frais ne sont pas remboursables une fois la séance tenue. Si l’organisateur annule avant la séance, les participants peuvent demander un remboursement. Ils ne sont pas obligés d’accepter un avoir à la place.
```

### ultra: pass

```text
Les frais ne sont pas remboursables une fois la séance terminée. Si l’organisateur annule avant la séance, les participants peuvent demander un remboursement. Ils ne sont pas obligés d’accepter un avoir à la place.
```

### off: pass

```text
Les frais ne sont pas remboursables après la tenue d’une séance. Si l’organisateur annule avant la séance, les participants peuvent demander un remboursement. Ils ne sont pas obligés d’accepter un avoir à la place.
```

## modes-fr-097 · translation_scope

Source task:

> Translate into French: The new opening time applies to the repair counter only. The shop still opens at 09:00. Repairs are accepted from 10:30, including appointments booked before the change.

### baseline: pass

```text
Le nouvel horaire d’ouverture s’applique uniquement au comptoir de réparation. Le magasin ouvre toujours à 09 h 00. Les réparations sont prises en charge à partir de 10 h 30, y compris pour les rendez-vous pris avant le changement.
```

### lite: pass

```text
Le nouvel horaire d’ouverture s’applique uniquement au comptoir de réparation. Le magasin ouvre toujours à 09:00. Les réparations sont acceptées à partir de 10:30, y compris pour les rendez-vous pris avant ce changement.
```

### full: pass

```text
Le nouvel horaire d’ouverture s’applique uniquement au comptoir de réparation. Le magasin ouvre toujours à 09:00. Les réparations sont acceptées à partir de 10:30, y compris pour les rendez-vous pris avant le changement.
```

### ultra: pass

```text
Le nouvel horaire d’ouverture s’applique uniquement au comptoir de réparation. Le magasin ouvre toujours à 09:00. Les réparations sont acceptées à partir de 10:30, y compris pour les rendez-vous pris avant le changement.
```

### off: pass

```text
Le nouvel horaire d’ouverture s’applique uniquement au comptoir de réparation. Le magasin ouvre toujours à 09:00. Les réparations sont acceptées à partir de 10:30, y compris pour les rendez-vous pris avant le changement.
```

