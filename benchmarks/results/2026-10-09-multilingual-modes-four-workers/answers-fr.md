# fr: all source tasks and answers

Labels below are unblinded after review. Pass requires both meaning reviews and exact checks. A flagged answer is retained unchanged.

## modes-fr-001 · already_clear

Source task:

> Relis cette consigne. Si elle est déjà claire, rends-la sans changement : « Fermez la fenêtre avant de quitter la salle. »

### baseline: pass

```text
Fermez la fenêtre avant de quitter la salle.
```

### lite: pass

```text
Fermez la fenêtre avant de quitter la salle.
```

### full: pass

```text
Fermez la fenêtre avant de quitter la salle.
```

### ultra: pass

```text
Fermez la fenêtre avant de quitter la salle.
```

### off: pass

```text
Fermez la fenêtre avant de quitter la salle.
```

## modes-fr-002 · permissions

Source task:

> Réécris pour les bénévoles : Vous pouvez prendre une deuxième permanence, mais cela reste facultatif. Chaque bénévole doit confirmer sa première permanence avant vendredi à 18 h.

### baseline: pass

```text
Chaque bénévole doit confirmer sa première permanence avant vendredi à 18 h. Vous pouvez prendre une deuxième permanence, mais ce n’est pas obligatoire.
```

### lite: pass

```text
Vous pouvez prendre une deuxième permanence, mais c’est facultatif. Chaque bénévole doit confirmer sa première permanence avant vendredi à 18 h.
```

### full: pass

```text
Chaque bénévole doit confirmer sa première permanence avant vendredi à 18 h. Vous pouvez prendre une deuxième permanence, mais ce n’est pas obligatoire.
```

### ultra: pass

```text
Chaque bénévole doit confirmer sa première permanence avant vendredi à 18 h. Une deuxième permanence est facultative.
```

### off: pass

```text
Chaque bénévole doit confirmer sa première permanence avant vendredi à 18 h. Vous pouvez prendre une deuxième permanence, mais ce n’est pas obligatoire.
```

## modes-fr-003 · conditions

Source task:

> Simplifie : La salle peut être ouverte au public seulement si le contrôle de ventilation est terminé et si la personne responsable a signé la fiche. Un seul de ces deux éléments ne suffit pas.

### baseline: pass

```text
La salle peut ouvrir au public uniquement lorsque les deux conditions sont remplies : le contrôle de ventilation est terminé et la personne responsable a signé la fiche.
```

### lite: pass

```text
La salle peut être ouverte au public seulement si le contrôle de ventilation est terminé et si la personne responsable a signé la fiche. Les deux conditions doivent être remplies.
```

### full: pass

```text
La salle peut être ouverte au public uniquement si les deux conditions sont remplies : le contrôle de ventilation est terminé et la personne responsable a signé la fiche.
```

### ultra: pass

```text
La salle peut être ouverte au public seulement si les deux conditions sont remplies : le contrôle de ventilation est terminé et la personne responsable a signé la fiche.
```

### off: pass

```text
La salle peut être ouverte au public seulement si les deux conditions sont remplies : le contrôle de ventilation est terminé et la personne responsable a signé la fiche. Une seule condition remplie ne suffit pas.
```

## modes-fr-004 · negation

Source task:

> Rends ce message plus clair : Ne supprimez pas le compte lorsque la carte est expirée. Désactivez uniquement le renouvellement automatique ; les accès déjà payés restent valables jusqu’au 30 novembre.

### baseline: pass

```text
Si la carte est expirée, ne supprimez pas le compte. Désactivez seulement le renouvellement automatique. Les accès déjà payés restent valables jusqu’au 30 novembre.
```

### lite: pass

```text
Ne supprimez pas le compte lorsque la carte est expirée. Désactivez uniquement le renouvellement automatique. Les accès déjà payés restent valables jusqu’au 30 novembre.
```

### full: pass

```text
Si la carte est expirée, ne supprimez pas le compte. Désactivez uniquement le renouvellement automatique. Les accès déjà payés restent valables jusqu’au 30 novembre.
```

### ultra: pass

```text
Si la carte est expirée, ne supprimez pas le compte : désactivez uniquement le renouvellement automatique. Les accès déjà payés restent valables jusqu’au 30 novembre.
```

### off: pass

```text
Lorsque la carte est expirée, ne supprimez pas le compte : désactivez uniquement le renouvellement automatique. Les accès déjà payés restent valables jusqu’au 30 novembre.
```

## modes-fr-005 · exceptions

Source task:

> Réécris : Les visiteurs doivent réserver leur place, sauf les accompagnateurs d’un groupe scolaire déjà inscrit. Cette dispense ne concerne pas les autres membres de la famille.

### baseline: pass

```text
Les visiteurs doivent réserver leur place. Seuls les accompagnateurs d’un groupe scolaire déjà inscrit n’ont pas besoin de réserver. Les autres membres de la famille doivent réserver.
```

### lite: pass

```text
Les visiteurs doivent réserver leur place, sauf les accompagnateurs d’un groupe scolaire déjà inscrit. Les autres membres de la famille doivent réserver leur place.
```

### full: pass

```text
Les visiteurs doivent réserver leur place. Seuls les accompagnateurs d’un groupe scolaire déjà inscrit sont dispensés de réservation, pas les autres membres de la famille.
```

### ultra: pass

```text
Les visiteurs doivent réserver leur place, sauf les accompagnateurs d’un groupe scolaire déjà inscrit. Les autres membres de la famille doivent réserver.
```

### off: pass

```text
Les visiteurs doivent réserver leur place. Seuls les accompagnateurs d’un groupe scolaire déjà inscrit sont dispensés de réservation. Les autres membres de la famille doivent réserver.
```

## modes-fr-006 · unknown_actor

Source task:

> Clarifie sans attribuer d’action supplémentaire : Le colis a été déplacé après que Nadia a fermé le guichet. Nadia a retrouvé le colis dans la réserve le lendemain.

### baseline: pass

```text
Le colis a été déplacé après la fermeture du guichet par Nadia. Le lendemain, Nadia l’a retrouvé dans la réserve.
```

### lite: pass

```text
Le colis a été déplacé après la fermeture du guichet par Nadia. Le lendemain, Nadia l’a retrouvé dans la réserve.
```

### full: pass

```text
Après la fermeture du guichet par Nadia, le colis a été déplacé. Le lendemain, Nadia l’a retrouvé dans la réserve.
```

### ultra: pass

```text
Le colis a été déplacé après la fermeture du guichet par Nadia. Le lendemain, Nadia l’a retrouvé dans la réserve.
```

### off: pass

```text
Le colis a été déplacé après la fermeture du guichet par Nadia. Le lendemain, Nadia l’a retrouvé dans la réserve.
```

## modes-fr-007 · sequence

Source task:

> Transforme en trois étapes : Enregistrez d’abord le brouillon. Faites ensuite relire le document par une autre personne. Envoyez la version finale seulement après cette relecture.

### baseline: pass

```text
1. Enregistrez le brouillon.
2. Faites relire le document par une autre personne.
3. Envoyez la version finale uniquement après cette relecture.
```

### lite: pass

```text
1. Enregistrez le brouillon.
2. Faites relire le document par une autre personne.
3. Envoyez la version finale seulement après cette relecture.
```

### full: pass

```text
1. Enregistrez le brouillon.
2. Faites relire le document par une autre personne.
3. Envoyez la version finale seulement après cette relecture.
```

### ultra: pass

```text
1. Enregistrez le brouillon.
2. Faites relire le document par une autre personne.
3. Envoyez la version finale seulement après cette relecture.
```

### off: pass

```text
1. Enregistrez le brouillon.
2. Faites relire le document par une autre personne.
3. Envoyez la version finale seulement après cette relecture.
```

## modes-fr-008 · uncertainty

Source task:

> Réécris ce point de suivi : La fuite semble venir du joint inférieur, mais cette hypothèse n’a pas été vérifiée. Deux essais ont été faits à froid ; aucun essai à chaud n’est encore disponible.

### baseline: pass

```text
L’origine de la fuite pourrait être le joint inférieur, mais cette hypothèse reste à vérifier. Deux essais ont été réalisés à froid ; aucun essai à chaud n’est encore disponible.
```

### lite: pass

```text
La fuite semble venir du joint inférieur, mais cette hypothèse reste à vérifier. Deux essais ont été réalisés à froid ; aucun essai à chaud n’est encore disponible.
```

### full: pass

```text
La fuite semble provenir du joint inférieur, mais cette hypothèse reste à vérifier. Deux essais ont été réalisés à froid ; aucun essai à chaud n’est encore disponible.
```

### ultra: pass

```text
La fuite semble venir du joint inférieur, mais cette hypothèse reste non vérifiée. Deux essais à froid ont été réalisés ; aucun essai à chaud n’est encore disponible.
```

### off: pass

```text
La fuite semble provenir du joint inférieur, mais cette hypothèse reste à vérifier. Deux essais ont été réalisés à froid ; aucun essai à chaud n’est encore disponible.
```

## modes-fr-009 · estimates

Source task:

> Raccourcis sans transformer une estimation en engagement : Nous prévoyons environ 6 à 8 jours ouvrés pour restaurer les archives, sous réserve que le disque de remplacement arrive mardi. Aucune date de fin n’est garantie.

### baseline: pass

```text
Restauration estimée à 6 à 8 jours ouvrés, sous réserve de l’arrivée du disque de remplacement mardi. Aucune date de fin garantie.
```

### lite: pass

```text
La restauration des archives est estimée à environ 6 à 8 jours ouvrés, sous réserve que le disque de remplacement arrive mardi. Aucune date de fin n’est garantie.
```

### full: pass

```text
La restauration des archives est estimée à environ 6 à 8 jours ouvrés, sous réserve que le disque de remplacement arrive mardi. Aucune date de fin n’est garantie.
```

### ultra: pass

```text
Restauration des archives estimée à environ 6 à 8 jours ouvrés, si le disque de remplacement arrive mardi. Aucune date de fin garantie.
```

### off: pass

```text
La restauration des archives est estimée à environ 6 à 8 jours ouvrés, sous réserve que le disque de remplacement arrive mardi. Aucune date de fin n’est garantie.
```

## modes-fr-010 · numbers_units

Source task:

> Reformule pour un devis : Le forfait coûte 245 € HT par atelier, matériel inclus. Le déplacement est facturé séparément à 0,48 € par kilomètre, aller et retour compris.

### baseline: pass

```text
Forfait par atelier : 245 € HT, matériel inclus.
Déplacement facturé séparément : 0,48 €/km, sur la distance aller-retour.
```

### lite: pass

```text
Forfait : 245 € HT par atelier, matériel inclus. Déplacement facturé séparément : 0,48 € par kilomètre, aller et retour compris.
```

### full: pass

```text
Forfait par atelier : 245 € HT, matériel inclus.
Déplacement facturé séparément : 0,48 € par kilomètre, aller et retour compris.
```

### ultra: pass

```text
Forfait : 245 € HT par atelier, matériel inclus.
Déplacement facturé séparément : 0,48 € par kilomètre, aller et retour compris.
```

### off: pass

```text
Forfait par atelier : 245 € HT, matériel inclus.
Déplacement facturé séparément : 0,48 € par kilomètre, aller et retour compris.
```

## modes-fr-011 · denominators

Source task:

> Explique en une phrase ce résultat interne : 18 demandes sur 72 ont été traitées le jour même. Parmi ces 18 demandes, 6 provenaient du formulaire en ligne.

### baseline: pass

```text
Sur les 72 demandes, 18 ont été traitées le jour même, soit 25 %, et parmi ces 18 demandes, 6 provenaient du formulaire en ligne, soit un tiers.
```

### lite: pass

```text
Sur 72 demandes, 18 ont été traitées le jour même, dont 6 provenaient du formulaire en ligne.
```

### full: pass

```text
Sur 72 demandes, 18 ont été traitées le jour même, dont 6 provenaient du formulaire en ligne.
```

### ultra: pass

```text
18 demandes sur 72 (25 %) ont été traitées le jour même, dont 6 provenaient du formulaire en ligne.
```

### off: pass

```text
Sur les 72 demandes, 18 ont été traitées le jour même, soit 25 %, et parmi ces 18 demandes, 6 provenaient du formulaire en ligne.
```

## modes-fr-012 · sampling

Source task:

> Résume la portée de cette enquête : 43 personnes ont répondu volontairement à un questionnaire affiché dans un atelier de réparation. Aucun tirage au sort n’a été réalisé et les clients absents ce jour-là n’ont pas été contactés.

### baseline: pass

```text
L’enquête reflète les réponses de 43 volontaires présents dans un atelier de réparation ; sans tirage au sort ni contact avec les clients absents ce jour-là, elle ne permet pas de généraliser les résultats à l’ensemble des clients.
```

### lite: pass

```text
L’enquête porte sur 43 personnes ayant répondu volontairement à un questionnaire affiché dans un atelier de réparation, sans tirage au sort ni contact avec les clients absents ce jour-là ; elle ne permet donc pas de conclure pour l’ensemble des clients.
```

### full: pass

```text
L’enquête porte sur 43 personnes ayant répondu volontairement à un questionnaire affiché dans un atelier de réparation, sans tirage au sort ni contact avec les clients absents ce jour-là ; ses résultats ne peuvent donc pas être généralisés à l’ensemble des clients.
```

### ultra: pass

```text
L’enquête porte sur 43 réponses volontaires à un questionnaire affiché dans un atelier de réparation, sans tirage au sort ni contact avec les clients absents ce jour-là ; sa représentativité n’est donc pas établie.
```

### off: pass

```text
L’enquête porte sur 43 personnes ayant répondu volontairement à un questionnaire affiché dans un atelier de réparation, sans tirage au sort ni contact avec les clients absents ce jour-là ; ses résultats ne peuvent donc pas être considérés comme représentatifs de l’ensemble des clients.
```

## modes-fr-013 · calculation

Source task:

> Un club a acheté 7 jeux à 18 € chacun et a payé 12 € de livraison pour toute la commande. Quel est le coût total ? Donne le calcul et le montant.

### baseline: pass

```text
7 × 18 € + 12 € = 126 € + 12 € = 138 € au total.
```

### lite: pass

```text
(7 × 18 €) + 12 € = 126 € + 12 € = 138 € au total.
```

### full: pass

```text
(7 × 18 €) + 12 € = 126 € + 12 € = 138 € au total.
```

### ultra: pass

```text
7 × 18 € + 12 € de livraison = 138 € au total.
```

### off: pass

```text
Le coût total est de (7 × 18 €) + 12 € = 126 € + 12 € = 138 €.
```

## modes-fr-014 · percentage_points

Source task:

> Rédige une phrase exacte : dans cet exercice fictif, le taux passe de 32 % à 38 %. Donne la hausse en points de pourcentage, pas la hausse relative.

### baseline: pass

```text
Dans cet exercice fictif, le taux passe de 32 % à 38 %, soit une hausse de 6 points de pourcentage.
```

### lite: pass

```text
Dans cet exercice fictif, le taux passe de 32 % à 38 %, soit une hausse de 6 points de pourcentage.
```

### full: pass

```text
Dans cet exercice fictif, le taux passe de 32 % à 38 %, soit une hausse de 6 points de pourcentage.
```

### ultra: pass

```text
Dans cet exercice fictif, le taux passe de 32 % à 38 %, soit une hausse de 6 points de pourcentage.
```

### off: pass

```text
Dans cet exercice fictif, le taux passe de 32 % à 38 %, soit une hausse de 6 points de pourcentage.
```

## modes-fr-015 · conflicting_notes

Source task:

> Prépare un point de situation sans trancher le désaccord : le compte rendu indique 14 sièges disponibles ; le plan de salle daté du même jour en montre 16. Aucun des deux documents n’a été validé.

### baseline: pass

```text
Le compte rendu indique 14 sièges disponibles, tandis que le plan de salle daté du même jour en montre 16 ; aucun des deux documents n’ayant été validé, le nombre de sièges disponibles reste à confirmer.
```

### lite: pass

```text
Le compte rendu indique 14 sièges disponibles, tandis que le plan de salle daté du même jour en montre 16. Aucun des deux documents n’a été validé ; le nombre de sièges disponibles reste donc à confirmer.
```

### full: pass

```text
Le compte rendu indique 14 sièges disponibles, tandis que le plan de salle daté du même jour en montre 16. Aucun des deux documents n’a été validé : le nombre de sièges disponibles reste à confirmer.
```

### ultra: pass

```text
Le compte rendu indique 14 sièges disponibles, contre 16 sur le plan de salle daté du même jour ; aucun des deux documents n’a été validé, et l’écart reste non résolu.
```

### off: pass

```text
Le compte rendu indique 14 sièges disponibles, tandis que le plan de salle daté du même jour en montre 16. Aucun des deux documents n’a été validé : le nombre de sièges disponibles reste donc à confirmer.
```

## modes-fr-016 · technical

Source task:

> Réécris cette aide : Si le serveur répond HTTP 503, réessayez après le délai indiqué dans Retry-After. Si cet en-tête manque, attendez 20 secondes. Ne relancez pas une requête POST sans clé d’idempotence.

### baseline: pass

```text
Si le serveur renvoie une erreur HTTP 503, attendez le délai indiqué dans l’en-tête Retry-After avant de réessayer. Si cet en-tête est absent, attendez 20 secondes. Ne réessayez jamais une requête POST sans clé d’idempotence.
```

### lite: pass

```text
Si le serveur répond HTTP 503, attendez le délai indiqué dans Retry-After avant de réessayer. Si cet en-tête manque, attendez 20 secondes. Ne relancez pas une requête POST sans clé d’idempotence.
```

### full: pass

```text
Si le serveur répond HTTP 503, attendez le délai indiqué dans Retry-After avant de réessayer. Si cet en-tête manque, attendez 20 secondes. Ne relancez pas une requête POST sans clé d’idempotence.
```

### ultra: pass

```text
Si le serveur répond HTTP 503, attendez le délai indiqué dans Retry-After avant de réessayer. Si cet en-tête manque, attendez 20 secondes. Ne relancez pas une requête POST sans clé d’idempotence.
```

### off: pass

```text
Si le serveur renvoie HTTP 503, attendez le délai indiqué dans Retry-After avant de réessayer. Si cet en-tête est absent, attendez 20 secondes. Ne réessayez pas une requête POST sans clé d’idempotence.
```

## modes-fr-017 · technical

Source task:

> Explique simplement cette note de configuration : cache_ttl vaut 300 secondes pour les lectures réussies. Une réponse vide n’est pas mise en cache. Modifier cache_ttl ne supprime pas les entrées déjà présentes.

### baseline: pass

```text
Les résultats des lectures réussies sont conservés en cache pendant 300 secondes, soit 5 minutes. Les réponses vides ne sont pas mises en cache. Changer cache_ttl ne supprime pas les entrées déjà en cache.
```

### lite: pass

```text
cache_ttl fixe à 300 secondes la durée de mise en cache des lectures réussies. Une réponse vide n’est pas mise en cache. Modifier cache_ttl ne supprime pas les entrées déjà présentes.
```

### full: pass

```text
cache_ttl est fixé à 300 secondes : les lectures réussies sont conservées en cache pendant cette durée. Les réponses vides ne sont pas mises en cache. Modifier cache_ttl ne supprime pas les entrées déjà présentes.
```

### ultra: pass

```text
cache_ttl vaut 300 secondes : les lectures réussies sont mises en cache pendant ce délai, sauf les réponses vides. Modifier cache_ttl ne supprime pas les entrées déjà en cache.
```

### off: pass

```text
cache_ttl est fixé à 300 secondes, soit 5 minutes : les résultats des lectures réussies sont conservés en cache pendant cette durée. Une réponse vide n’est pas conservée en cache. Changer cache_ttl ne supprime pas les entrées qui sont déjà dans le cache.
```

## modes-fr-018 · summary

Source task:

> Résume en deux phrases pour les membres : Le local ouvrira samedi à 10 h. La table de prêt de livres sera prête, mais le coin cuisine restera fermé pendant la réparation du robinet. Les inscriptions habituelles continuent par téléphone.

### baseline: pass

```text
Le local ouvrira samedi à 10 h : la table de prêt de livres sera prête, mais le coin cuisine restera fermé pendant la réparation du robinet. Les inscriptions habituelles continuent par téléphone.
```

### lite: pass

```text
Le local ouvrira samedi à 10 h et la table de prêt de livres sera prête, mais le coin cuisine restera fermé pendant la réparation du robinet. Les inscriptions habituelles continuent par téléphone.
```

### full: pass

```text
Le local ouvrira samedi à 10 h : la table de prêt de livres sera prête, mais le coin cuisine restera fermé pendant la réparation du robinet. Les inscriptions habituelles continuent par téléphone.
```

### ultra: pass

```text
Le local ouvrira samedi à 10 h avec la table de prêt de livres prête, mais le coin cuisine restera fermé pendant la réparation du robinet. Les inscriptions habituelles continuent par téléphone.
```

### off: pass

```text
Le local ouvrira samedi à 10 h : la table de prêt de livres sera prête, mais le coin cuisine restera fermé pendant la réparation du robinet. Les inscriptions habituelles continuent par téléphone.
```

## modes-fr-019 · scope

Source task:

> Réponds aux deux questions : faut-il réserver pour rendre un livre, et à quelles heures peut-on le rendre ? Note : les nouveaux prêts exigent une réservation. Les retours se font sans réservation, de 9 h à 12 h. La boîte extérieure est hors service.

### baseline: pass

```text
Non, vous pouvez rendre un livre sans réservation, de 9 h à 12 h. La boîte extérieure étant hors service, vous ne pouvez pas l’utiliser pour le retour.
```

### lite: pass

```text
Non, les retours se font sans réservation, de 9 h à 12 h. La boîte extérieure est hors service. Seuls les nouveaux prêts exigent une réservation.
```

### full: pass

```text
Non, les retours se font sans réservation, de 9 h à 12 h. La boîte extérieure est hors service. Seuls les nouveaux prêts exigent une réservation.
```

### ultra: pass

```text
Non, les retours se font sans réservation, de 9 h à 12 h. La boîte extérieure est hors service.
```

### off: pass

```text
Non, vous n’avez pas besoin de réserver pour rendre un livre ; la réservation est obligatoire uniquement pour les nouveaux prêts. Vous pouvez rendre un livre de 9 h à 12 h, sans utiliser la boîte extérieure, qui est hors service.
```

## modes-fr-020 · analysis

Source task:

> Peut-on conclure que l’affiche a causé l’augmentation des visites ? Dans cette expérience fictive, les visites passent de 90 à 120 après la pose de l’affiche, mais un marché a aussi ouvert dans la rue cette semaine-là.

### baseline: pass

```text
Non. Les visites sont passées de 90 à 120 après la pose de l’affiche, mais l’ouverture du marché la même semaine pourrait aussi expliquer cette hausse. On ne peut donc pas attribuer l’augmentation à l’affiche seule.
```

### lite: pass

```text
Non. Les visites sont passées de 90 à 120 après la pose de l’affiche, mais un marché a aussi ouvert dans la rue cette semaine-là. Cette hausse ne suffit donc pas à établir que l’affiche en est la cause.
```

### full: pass

```text
Non. Dans cette expérience fictive, les visites passent de 90 à 120 après la pose de l’affiche, mais un marché a aussi ouvert dans la rue cette semaine-là. Cette hausse ne suffit donc pas à établir que l’affiche en est la cause.
```

### ultra: pass

```text
Non. Dans cette expérience fictive, les visites passent de 90 à 120 après la pose de l’affiche, mais un marché a aussi ouvert dans la rue cette semaine-là. On ne peut donc pas attribuer l’augmentation à l’affiche seule.
```

### off: pass

```text
Non. Les visites sont passées de 90 à 120 après la pose de l’affiche, mais cette succession ne prouve pas que l’affiche a causé l’augmentation. L’ouverture du marché dans la rue la même semaine pourrait aussi expliquer tout ou partie de cette hausse ; ces informations ne permettent pas d’isoler l’effet de l’affiche.
```

## modes-fr-021 · voice

Source task:

> Réécris ce message en gardant un ton chaleureux et le tutoiement : J’ai bien reçu ton dessin. Je ne pourrai pas l’encadrer cette semaine, mais je le garderai à plat dans une pochette jusqu’à notre rendez-vous de lundi.

### baseline: pass

```text
J’ai bien reçu ton dessin, merci ! Je ne pourrai pas l’encadrer cette semaine, mais je le garderai bien à plat dans une pochette jusqu’à notre rendez-vous de lundi.
```

### lite: pass

```text
J’ai bien reçu ton dessin. Je ne pourrai pas l’encadrer cette semaine, mais je le garderai à plat dans une pochette jusqu’à notre rendez-vous de lundi.
```

### full: pass

```text
J’ai bien reçu ton dessin. Je ne pourrai pas l’encadrer cette semaine, mais je le garderai à plat dans une pochette jusqu’à notre rendez-vous de lundi.
```

### ultra: pass

```text
J’ai bien reçu ton dessin. Je ne pourrai pas l’encadrer cette semaine, mais je le garderai à plat dans une pochette jusqu’à notre rendez-vous de lundi.
```

### off: pass

```text
J’ai bien reçu ton dessin ! Je ne pourrai pas l’encadrer cette semaine, mais je le garderai à plat dans une pochette jusqu’à notre rendez-vous de lundi.
```

## modes-fr-022 · ambiguity

Source task:

> Améliore la clarté sans deviner : « Après son appel à Louise, Camille a modifié sa réservation. » On ne sait pas à qui appartient la réservation. Signale seulement cette ambiguïté et propose deux lectures possibles.

### baseline: pass

```text
« Sa réservation » est ambigu : on ne sait pas à qui elle appartient. Deux lectures sont possibles :
- Après son appel à Louise, Camille a modifié sa propre réservation.
- Après son appel à Louise, Camille a modifié la réservation de Louise.
```

### lite: pass

```text
« Sa réservation » est ambigu : on ne sait pas à qui elle appartient. Deux lectures possibles :
- Après son appel à Louise, Camille a modifié sa propre réservation.
- Après son appel à Louise, Camille a modifié la réservation de Louise.
```

### full: pass

```text
« Sa réservation » est ambigu : elle peut appartenir à Camille ou à Louise. Deux lectures possibles :
- Après son appel à Louise, Camille a modifié sa propre réservation.
- Après son appel à Louise, Camille a modifié la réservation de Louise.
```

### ultra: pass

```text
« Sa réservation » est ambigu : il peut s’agir de celle de Camille ou de celle de Louise.
```

### off: pass

```text
« Sa réservation » est ambigu : on ne sait pas à qui elle appartient. Deux lectures possibles :
- Après son appel à Louise, Camille a modifié sa propre réservation.
- Après son appel à Louise, Camille a modifié la réservation de Louise.
```

## modes-fr-023 · permissions

Source task:

> Allège cette note de règlement fictif : Les locataires peuvent demander une copie de l’état des lieux. La demande n’est pas obligatoire pour conserver leur exemplaire initial et aucun paiement n’est prévu dans ce règlement.

### baseline: pass

```text
Les locataires peuvent demander une copie de l’état des lieux, mais n’ont pas à le faire pour conserver leur exemplaire initial. Ce règlement ne prévoit aucun paiement.
```

### lite: pass

```text
Les locataires peuvent demander une copie de l’état des lieux. Cette demande n’est pas obligatoire pour conserver leur exemplaire initial. Ce règlement ne prévoit aucun paiement.
```

### full: pass

```text
Les locataires peuvent demander une copie de l’état des lieux. Cette demande n’est pas nécessaire pour conserver leur exemplaire initial. Le règlement ne prévoit aucun paiement.
```

### ultra: pass

```text
Les locataires peuvent demander une copie de l’état des lieux, sans obligation pour conserver leur exemplaire initial. Ce règlement ne prévoit aucun paiement.
```

### off: pass

```text
Les locataires peuvent demander une copie de l’état des lieux, sans obligation pour conserver leur exemplaire initial. Ce règlement ne prévoit aucun paiement.
```

## modes-fr-024 · conditions

Source task:

> Réécris : La livraison gratuite s’applique aux commandes d’au moins 60 € livrées dans la zone A. Elle ne s’applique ni à la zone B ni aux commandes contenant un meuble, même si le total dépasse 60 €.

### baseline: pass

```text
La livraison est gratuite pour les commandes d’au moins 60 € livrées en zone A, à condition qu’elles ne contiennent aucun meuble. Les livraisons en zone B et les commandes contenant un meuble sont exclues de cette offre, quel que soit le montant de la commande.
```

### lite: pass

```text
La livraison gratuite s’applique aux commandes d’au moins 60 € livrées dans la zone A. Elle ne s’applique ni aux livraisons dans la zone B ni aux commandes contenant un meuble, même si le total dépasse 60 €.
```

### full: pass

```text
La livraison est gratuite pour les commandes d’au moins 60 € livrées dans la zone A. Elle est exclue pour la zone B et pour toute commande contenant un meuble, même si le total dépasse 60 €.
```

### ultra: pass

```text
La livraison est gratuite pour les commandes d’au moins 60 € livrées en zone A, sauf si elles contiennent un meuble. Elle ne s’applique jamais en zone B ni aux commandes contenant un meuble, même au-delà de 60 €.
```

### off: pass

```text
La livraison est gratuite pour les commandes d’au moins 60 € livrées dans la zone A, sauf si elles contiennent un meuble. Elle ne s’applique pas à la zone B ni aux commandes contenant un meuble, même si leur total dépasse 60 €.
```

## modes-fr-025 · negation

Source task:

> Clarifie : Le fait qu’une demande soit marquée « reçue » ne signifie pas qu’elle est acceptée. Seul un message portant la mention « acceptée » confirme l’inscription.

### baseline: pass

```text
La mention « reçue » indique seulement que la demande a été reçue, pas qu’elle a été acceptée. Seul un message portant la mention « acceptée » confirme l’inscription.
```

### lite: pass

```text
Une demande marquée « reçue » n’est pas nécessairement acceptée. Seul un message portant la mention « acceptée » confirme l’inscription.
```

### full: pass

```text
La mention « reçue » ne signifie pas que la demande est acceptée. Seul un message portant la mention « acceptée » confirme l’inscription.
```

### ultra: pass

```text
La mention « reçue » ne signifie pas que la demande est acceptée. Seul un message portant la mention « acceptée » confirme l’inscription.
```

### off: pass

```text
La mention « reçue » indique seulement que la demande a été reçue, pas qu’elle est acceptée. Seul un message portant la mention « acceptée » confirme l’inscription.
```

## modes-fr-026 · unknown_actor

Source task:

> Rends cette chronologie lisible : À 8 h 10, Martin a noté une erreur sur le tableau. La valeur a été corrigée à 8 h 25. À 8 h 40, Inès a envoyé le tableau au groupe. Qui a fait la correction n’est pas indiqué.

### baseline: pass

```text
- 8 h 10 : Martin note une erreur sur le tableau.
- 8 h 25 : la valeur est corrigée. L’auteur de la correction n’est pas indiqué.
- 8 h 40 : Inès envoie le tableau au groupe.
```

### lite: pass

```text
À 8 h 10, Martin a noté une erreur sur le tableau.
À 8 h 25, la valeur a été corrigée ; la personne ayant fait la correction n’est pas indiquée.
À 8 h 40, Inès a envoyé le tableau au groupe.
```

### full: pass

```text
- 8 h 10 : Martin a noté une erreur sur le tableau.
- 8 h 25 : la valeur a été corrigée. La personne ayant fait la correction n’est pas indiquée.
- 8 h 40 : Inès a envoyé le tableau au groupe.
```

### ultra: pass

```text
- 8 h 10 : Martin note une erreur sur le tableau.
- 8 h 25 : la valeur est corrigée ; l’auteur de la correction n’est pas indiqué.
- 8 h 40 : Inès envoie le tableau au groupe.
```

### off: pass

```text
- 8 h 10 : Martin a noté une erreur sur le tableau.
- 8 h 25 : la valeur a été corrigée. La personne ayant fait la correction n’est pas indiquée.
- 8 h 40 : Inès a envoyé le tableau au groupe.
```

## modes-fr-027 · uncertainty

Source task:

> Résume cette observation : Sur les cinq caisses inspectées, une présentait une trace d’humidité. Il est possible que d’autres caisses soient touchées, mais les vingt restantes n’ont pas été ouvertes.

### baseline: pass

```text
Une des cinq caisses inspectées présentait une trace d’humidité. Les vingt autres n’ayant pas été ouvertes, on ne sait pas si elles sont également touchées.
```

### lite: pass

```text
Une des cinq caisses inspectées présentait une trace d’humidité. D’autres pourraient être touchées, mais les vingt caisses restantes n’ont pas été ouvertes.
```

### full: pass

```text
Une des cinq caisses inspectées présentait une trace d’humidité. D’autres pourraient être touchées, mais les vingt caisses restantes n’ont pas été ouvertes.
```

### ultra: pass

```text
Une des cinq caisses inspectées présentait une trace d’humidité. D’autres pourraient être touchées, mais les vingt restantes n’ont pas été ouvertes.
```

### off: pass

```text
Une des cinq caisses inspectées présentait une trace d’humidité. D’autres pourraient être touchées, mais les vingt caisses restantes n’ont pas été ouvertes.
```

## modes-fr-028 · numbers_units

Source task:

> Rends cette fiche plus directe : Chaque recharge contient 750 mL. La consommation estimée est de 25 mL par passage. Les chiffres concernent le distributeur d’essai, pas tous les modèles.

### baseline: pass

```text
Pour le distributeur d’essai, chaque recharge contient 750 mL, soit environ 30 passages à une consommation estimée de 25 mL par passage. Ces chiffres ne s’appliquent pas à tous les modèles.
```

### lite: pass

```text
Chaque recharge contient 750 mL. La consommation estimée est de 25 mL par passage. Ces chiffres concernent uniquement le distributeur d’essai, pas tous les modèles.
```

### full: pass

```text
Chaque recharge contient 750 mL. La consommation est estimée à 25 mL par passage. Ces chiffres concernent uniquement le distributeur d’essai, pas tous les modèles.
```

### ultra: pass

```text
Chaque recharge contient 750 mL. La consommation estimée est de 25 mL par passage. Ces chiffres concernent uniquement le distributeur d’essai, pas tous les modèles.
```

### off: pass

```text
Chaque recharge contient 750 mL. La consommation est estimée à 25 mL par passage. Ces chiffres concernent uniquement le distributeur d’essai, pas tous les modèles.
```

## modes-fr-029 · calculation

Source task:

> Une équipe a travaillé 2 h 45 le matin et 1 h 50 l’après-midi. Quelle durée totale faut-il inscrire ? Explique brièvement le report des minutes.

### baseline: pass

```text
Il faut inscrire 4 h 35. Les minutes totalisent 45 + 50 = 95 min, soit 1 h 35. On reporte cette heure sur les 3 heures cumulées : 4 h 35.
```

### lite: pass

```text
Il faut inscrire 4 h 35. Les minutes donnent 45 + 50 = 95 minutes, soit 1 h 35. On ajoute cette heure aux 3 heures : le total est de 4 h 35.
```

### full: pass

```text
Il faut inscrire 4 h 35. Les minutes totalisent 45 + 50 = 95 min, soit 1 h 35. On reporte cette heure sur les 3 heures déjà comptées : 4 h 35.
```

### ultra: pass

```text
Inscrire 4 h 35 : 45 + 50 = 95 minutes, soit 1 h 35. On reporte cette heure sur les 3 heures cumulées (2 + 1).
```

### off: pass

```text
Il faut inscrire 4 h 35. Les minutes totalisent 45 + 50 = 95 minutes, soit 1 h 35. On reporte cette heure dans le total des heures : 2 + 1 + 1 = 4 heures.
```

## modes-fr-030 · sampling

Source task:

> Réécris cette conclusion avec ses limites : Les 12 responsables ayant participé à notre réunion préfèrent le créneau du matin. Ils ont été invités parce qu’ils géraient les plus grandes équipes ; les responsables des petites équipes n’ont pas été interrogés.

### baseline: flagged

```text
Les 12 responsables présents à la réunion préfèrent le créneau du matin. Toutefois, seuls des responsables des plus grandes équipes ont été invités : les responsables des petites équipes n’ont pas été interrogés. Cette préférence ne peut donc pas être généralisée à l’ensemble des responsables.
```

Review notes: La source explique pourquoi les participants ont été invités, sans décrire toutes les invitations ; le motif causal est perdu. / Preserves the preference and generalization limit but invents exclusivity of invitations.

### lite: pass

```text
Les 12 responsables ayant participé à notre réunion préfèrent le créneau du matin. Ils ont été invités parce qu’ils géraient les plus grandes équipes. Les responsables des petites équipes n’ont pas été interrogés.
```

### full: pass

```text
Les 12 responsables ayant participé à la réunion préfèrent le créneau du matin. Ils ont été invités parce qu’ils géraient les plus grandes équipes. Les responsables des petites équipes n’ont pas été interrogés : leur préférence reste inconnue.
```

### ultra: pass

```text
Les 12 responsables présents à la réunion préfèrent le créneau du matin. Invités parce qu’ils géraient les plus grandes équipes, ils ne représentent pas les responsables des petites équipes, qui n’ont pas été interrogés.
```

### off: pass

```text
Les 12 responsables ayant participé à la réunion préfèrent le créneau du matin. Ils ont été invités parce qu’ils géraient les plus grandes équipes. Les responsables des petites équipes n’ayant pas été interrogés, cette conclusion ne peut pas être généralisée à l’ensemble des responsables.
```

## modes-fr-031 · summary

Source task:

> Fais un résumé de passation : Sarah a terminé l’inventaire des outils, mais pas celui des consommables. Le registre est sur le bureau. La clé de l’armoire a été rendue ; la personne qui l’a reçue n’est pas précisée.

### baseline: pass

```text
Sarah a terminé l’inventaire des outils ; celui des consommables reste à faire. Le registre est sur le bureau. La clé de l’armoire a été rendue, mais le destinataire n’est pas précisé.
```

### lite: pass

```text
Sarah a terminé l’inventaire des outils, mais pas celui des consommables. Le registre est sur le bureau. La clé de l’armoire a été rendue ; la personne qui l’a reçue n’est pas précisée.
```

### full: pass

```text
Sarah a terminé l’inventaire des outils, mais celui des consommables reste à faire. Le registre est sur le bureau. La clé de l’armoire a été rendue ; la personne qui l’a reçue n’est pas précisée.
```

### ultra: pass

```text
Sarah a terminé l’inventaire des outils, mais pas celui des consommables. Le registre est sur le bureau. La clé de l’armoire a été rendue ; on ne sait pas à qui.
```

### off: pass

```text
Sarah a terminé l’inventaire des outils ; celui des consommables reste à faire. Le registre est sur le bureau. La clé de l’armoire a été rendue, mais la personne qui l’a reçue n’est pas précisée.
```

## modes-fr-032 · analysis

Source task:

> Choisis l’option la moins chère pour exactement 36 badges, en utilisant seulement ces tarifs : lot A de 12 badges à 21 € ; lot B de 18 badges à 33 €. On ne peut pas acheter de badge à l’unité. Justifie le choix.

### baseline: pass

```text
Choisir 3 lots A : 3 × 12 = 36 badges pour 63 €, contre 66 € pour 2 lots B. Ce sont les seules combinaisons permettant d’obtenir exactement 36 badges ; les lots A coûtent donc 3 € de moins.
```

### lite: pass

```text
Choisis 3 lots A : 36 badges pour 63 €, contre 66 € pour 2 lots B. Ce sont les deux seules combinaisons possibles pour exactement 36 badges ; les lots A coûtent 3 € de moins.
```

### full: pass

```text
Choisis 3 lots A : 36 badges pour 63 €, contre 66 € pour 2 lots B. Ce sont les seules combinaisons permettant d’obtenir exactement 36 badges ; les lots A coûtent 3 € de moins.
```

### ultra: pass

```text
Choisis 3 lots A : 36 badges pour 63 €, contre 66 € pour 2 lots B. Ce sont les seules combinaisons donnant exactement 36 badges ; les 3 lots A coûtent 3 € de moins.
```

### off: pass

```text
Choisis 3 lots A : 3 × 12 = 36 badges pour 63 €. L’autre combinaison possible est 2 lots B : 2 × 18 = 36 badges pour 66 €. Les 3 lots A coûtent donc 3 € de moins.
```

## modes-fr-033 · conflicting_notes

Source task:

> Écris un message interne : la fiche de réservation annonce un début à 17 h ; le courriel de confirmation indique 17 h 30. Le lieu est le même dans les deux documents. L’heure n’a pas encore été confirmée par l’organisateur.

### baseline: pass

```text
Bonjour, la fiche de réservation annonce un début à 17 h, tandis que le courriel de confirmation indique 17 h 30. Le lieu est identique dans les deux documents. L’heure reste à confirmer par l’organisateur.
```

### lite: pass

```text
La fiche de réservation annonce un début à 17 h, mais le courriel de confirmation indique 17 h 30. Le lieu est le même dans les deux documents. L’organisateur n’a pas encore confirmé l’heure.
```

### full: pass

```text
L’heure de début reste à confirmer : la fiche de réservation indique 17 h, le courriel de confirmation 17 h 30. Le lieu est identique dans les deux documents. L’organisateur n’a pas encore confirmé l’heure.
```

### ultra: pass

```text
L’heure de début reste à confirmer par l’organisateur : la fiche de réservation indique 17 h, le courriel de confirmation 17 h 30. Le lieu est identique dans les deux documents.
```

### off: pass

```text
L’heure de début reste à confirmer : la fiche de réservation annonce 17 h, tandis que le courriel de confirmation indique 17 h 30. Le lieu est identique dans les deux documents. L’organisateur n’a pas encore confirmé l’heure.
```

## modes-fr-034 · voice

Source task:

> Raccourcis cette invitation tout en gardant son humour discret : Notre plante de bureau a survécu à trois déménagements et mérite un pot moins cabossé. Apporte un pot si tu en as un ; surtout, n’en achète pas pour cette occasion. Rendez-vous jeudi à midi.

### baseline: pass

```text
Après trois déménagements, notre plante mérite un pot moins cabossé. Apporte un pot si tu en as un, mais n’en achète surtout pas ! Jeudi à midi.
```

### lite: pass

```text
Notre plante a survécu à trois déménagements : elle mérite un pot moins cabossé. Apporte un pot si tu en as un, mais n’en achète surtout pas pour l’occasion. Rendez-vous jeudi à midi.
```

### full: pass

```text
Après trois déménagements, notre plante mérite un pot moins cabossé. Apporte un pot si tu en as un, mais surtout n’en achète pas pour l’occasion. Rendez-vous jeudi à midi.
```

### ultra: pass

```text
Après trois déménagements, notre plante de bureau mérite un pot moins cabossé. Apporte un pot si tu en as un, mais surtout n’en achète pas pour l’occasion. Rendez-vous jeudi à midi.
```

### off: pass

```text
Après trois déménagements, notre plante de bureau mérite un pot moins cabossé. Apporte un pot si tu en as un, mais surtout n’en achète pas pour l’occasion. Rendez-vous jeudi à midi.
```

## modes-fr-035 · scope

Source task:

> Réponds en une phrase à « Quel document manque ? » : le dossier contient la facture, le formulaire signé et une photo. La procédure demande ces trois pièces et une attestation de domicile. Le reçu de paiement est facultatif.

### baseline: pass

```text
Il manque l’attestation de domicile.
```

### lite: pass

```text
Il manque l’attestation de domicile ; le reçu de paiement est facultatif.
```

### full: pass

```text
Il manque l’attestation de domicile ; le reçu de paiement est facultatif.
```

### ultra: pass

```text
Il manque l’attestation de domicile ; le reçu de paiement est facultatif.
```

### off: pass

```text
Il manque l’attestation de domicile ; le reçu de paiement est facultatif.
```

## modes-fr-036 · ambiguity

Source task:

> Réécris cette note sans interpréter la date : « Le dossier est attendu le 04/05 ; le pays d’origine du formulaire n’est pas connu. » Garde 04/05 et indique que le jour et le mois doivent être confirmés.

### baseline: pass

```text
Le dossier est attendu le 04/05. Le pays d’origine du formulaire étant inconnu, le jour et le mois doivent être confirmés.
```

### lite: pass

```text
Le dossier est attendu le 04/05 ; le pays d’origine du formulaire n’est pas connu. Le jour et le mois doivent être confirmés.
```

### full: pass

```text
Le dossier est attendu le 04/05. Le pays d’origine du formulaire est inconnu : le jour et le mois doivent être confirmés.
```

### ultra: pass

```text
Le dossier est attendu le 04/05. Le pays d’origine du formulaire est inconnu ; le jour et le mois doivent être confirmés.
```

### off: pass

```text
Le dossier est attendu le 04/05. Le pays d’origine du formulaire n’étant pas connu, le jour et le mois doivent être confirmés.
```

## modes-fr-037 · technical

Source task:

> Réécris pour une équipe de maintenance fictive : Avant de lancer verify_archive, copiez le fichier index.csv dans le dossier backup/. La commande vérifie les références ; elle ne restaure aucun fichier effacé.

### baseline: pass

```text
Avant de lancer verify_archive, copiez index.csv dans le dossier backup/. Cette commande vérifie les références, mais ne restaure aucun fichier effacé.
```

### lite: pass

```text
Avant de lancer verify_archive, copiez le fichier index.csv dans le dossier backup/. Cette commande vérifie les références ; elle ne restaure aucun fichier effacé.
```

### full: pass

```text
Avant de lancer verify_archive, copiez index.csv dans backup/. Cette commande vérifie les références, mais ne restaure aucun fichier effacé.
```

### ultra: pass

```text
Avant de lancer verify_archive, copiez index.csv dans backup/. La commande vérifie les références, mais ne restaure aucun fichier effacé.
```

### off: pass

```text
Avant de lancer verify_archive, copiez le fichier index.csv dans le dossier backup/. Cette commande vérifie les références, mais ne restaure aucun fichier effacé.
```

## modes-fr-038 · technical

Source task:

> Explique à un collègue : mode=read_only interdit les écritures dans le dossier partagé. Il n’empêche pas de télécharger les fichiers. Le réglage s’applique uniquement à la session actuelle.

### baseline: pass

```text
Le mode mode=read_only interdit toute écriture dans le dossier partagé, mais autorise le téléchargement des fichiers. Ce réglage s’applique uniquement à la session actuelle.
```

### lite: pass

```text
mode=read_only interdit les écritures dans le dossier partagé, mais permet de télécharger les fichiers. Ce réglage s’applique uniquement à la session actuelle.
```

### full: pass

```text
mode=read_only interdit les écritures dans le dossier partagé, mais permet de télécharger les fichiers. Ce réglage s’applique uniquement à la session actuelle.
```

### ultra: pass

```text
mode=read_only interdit les écritures dans le dossier partagé, mais permet de télécharger les fichiers. Ce réglage s’applique uniquement à la session actuelle.
```

### off: pass

```text
Le réglage mode=read_only interdit toute écriture dans le dossier partagé, mais permet de télécharger les fichiers. Il s’applique uniquement à la session actuelle.
```

## modes-fr-039 · exceptions

Source task:

> Clarifie cette règle fictive de concours : Chaque équipe peut présenter deux projets. Un troisième est admis uniquement si l’un des deux premiers a été retiré avant la clôture. Aucun retrait après la clôture ne libère de place.

### baseline: pass

```text
Chaque équipe peut présenter deux projets. Un troisième projet n’est admis que si l’un des deux premiers a été retiré avant la clôture. Un retrait après la clôture ne libère aucune place.
```

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
Chaque équipe peut présenter deux projets. Un troisième est admis uniquement si l’un des deux premiers a été retiré avant la clôture. Un retrait après la clôture ne libère aucune place.
```

### off: pass

```text
Chaque équipe peut présenter deux projets. Un troisième projet est admis uniquement si l’un des deux premiers a été retiré avant la clôture. Un retrait effectué après la clôture ne libère aucune place.
```

## modes-fr-040 · conditions

Source task:

> Rédige une consigne courte : le coffre ne doit être déplacé qu’à vide. Même vide, il faut deux personnes pour le porter. La présence de roulettes ne supprime pas cette exigence.

### baseline: pass

```text
Déplacez le coffre uniquement à vide. Même vide et muni de roulettes, il doit être porté par deux personnes.
```

### lite: pass

```text
Ne déplacez le coffre qu’à vide. Même vide et équipé de roulettes, il doit être porté par deux personnes.
```

### full: pass

```text
Déplacez le coffre uniquement à vide. Même vide et équipé de roulettes, il doit être porté par deux personnes.
```

### ultra: pass

```text
Ne déplacez le coffre qu’à vide. Deux personnes sont nécessaires pour le porter, même vide et équipé de roulettes.
```

### off: pass

```text
Déplacez le coffre uniquement à vide. Deux personnes sont nécessaires pour le porter, même s’il est vide et équipé de roulettes.
```

## modes-fr-041 · denominators

Source task:

> Corrige seulement la formulation trompeuse : « 80 % des habitants ont choisi le bleu. » Données : 80 % des 50 réponses reçues choisissent le bleu ; 400 questionnaires ont été distribués et une personne pouvait répondre une seule fois.

### baseline: pass

```text
80 % des 50 réponses reçues choisissent le bleu.
```

### lite: pass

```text
80 % des 50 réponses reçues indiquent un choix pour le bleu.
```

### full: pass

```text
80 % des 50 réponses reçues choisissent le bleu.
```

### ultra: pass

```text
80 % des 50 réponses reçues choisissent le bleu, sur 400 questionnaires distribués, avec une seule réponse autorisée par personne.
```

### off: pass

```text
80 % des 50 réponses reçues choisissent le bleu, sur 400 questionnaires distribués ; chaque personne ne pouvait répondre qu’une seule fois.
```

## modes-fr-042 · estimates

Source task:

> Réécris : Le coût pourrait atteindre 1 900 € si les deux moteurs doivent être remplacés. Pour l’instant, seul le remplacement d’un capteur à 75 € est confirmé. Ces montants ne comprennent pas la main-d’œuvre.

### baseline: pass

```text
Pour l’instant, seul le remplacement d’un capteur, à 75 €, est confirmé. Si les deux moteurs doivent être remplacés, le coût pourrait atteindre 1 900 €. Ces montants sont hors main-d’œuvre.
```

### lite: pass

```text
Le coût pourrait atteindre 1 900 € si les deux moteurs doivent être remplacés. Pour l’instant, seul le remplacement d’un capteur à 75 € est confirmé. Ces montants ne comprennent pas la main-d’œuvre.
```

### full: pass

```text
Seul le remplacement d’un capteur à 75 € est confirmé pour l’instant. Le coût pourrait atteindre 1 900 € si les deux moteurs doivent être remplacés. Ces montants excluent la main-d’œuvre.
```

### ultra: pass

```text
Seul le remplacement d’un capteur à 75 € est confirmé pour l’instant. Le coût pourrait atteindre 1 900 € si les deux moteurs doivent être remplacés. Ces montants excluent la main-d’œuvre.
```

### off: pass

```text
Le coût pourrait atteindre 1 900 € si le remplacement des deux moteurs est nécessaire. Pour l’instant, seul le remplacement d’un capteur à 75 € est confirmé. Ces montants excluent la main-d’œuvre.
```

## modes-fr-043 · percentage_points

Source task:

> Le taux de présence passe de 75 % à 60 %. Quelle est la baisse en points de pourcentage ? Ne calcule pas la baisse relative.

### baseline: pass

```text
La baisse est de 75 − 60 = 15 points de pourcentage.
```

### lite: pass

```text
75 − 60 = 15 points de pourcentage.
```

### full: pass

```text
75 − 60 = 15 points de pourcentage.
```

### ultra: pass

```text
75 − 60 = 15 points de pourcentage.
```

### off: pass

```text
La baisse est de 15 points de pourcentage (75 − 60 = 15).
```

## modes-fr-044 · calculation

Source task:

> Pour une recette fictive, 4 portions nécessitent 180 g de riz sec. Combien en faut-il pour 10 portions à proportion constante ? Donne le calcul sans conseil nutritionnel.

### baseline: pass

```text
180 × 10 ÷ 4 = 450 g de riz sec pour 10 portions.
```

### lite: pass

```text
180 g × 10 ÷ 4 = 450 g de riz sec.
```

### full: pass

```text
180 g × 10 ÷ 4 = 450 g de riz sec.
```

### ultra: pass

```text
180 g × 10 ÷ 4 = 450 g de riz sec.
```

### off: pass

```text
180 g × (10 ÷ 4) = 450 g de riz sec.
```

## modes-fr-045 · summary

Source task:

> Résume le changement pour les clients : À partir du 2 décembre, les retraits se feront à la porte latérale. Le paiement reste au comptoir principal. Les commandes passées avant le 2 décembre utilisent aussi la nouvelle porte si elles sont retirées après cette date.

### baseline: pass

```text
À partir du 2 décembre, tous les retraits se feront à la porte latérale, y compris pour les commandes passées avant cette date. Le paiement reste au comptoir principal.
```

### lite: pass

```text
À partir du 2 décembre, les retraits se feront à la porte latérale. Le paiement reste au comptoir principal. Les commandes passées avant le 2 décembre seront aussi retirées à la nouvelle porte si le retrait a lieu après cette date.
```

### full: pass

```text
À partir du 2 décembre, les retraits se feront à la porte latérale. Cela concerne aussi les commandes passées avant le 2 décembre si elles sont retirées après cette date. Le paiement reste au comptoir principal.
```

### ultra: pass

```text
À partir du 2 décembre, les retraits se feront à la porte latérale ; le paiement reste au comptoir principal. Les commandes passées avant le 2 décembre sont aussi concernées si elles sont retirées après cette date.
```

### off: pass

```text
À partir du 2 décembre, les retraits se feront à la porte latérale, tandis que le paiement restera au comptoir principal. Les commandes passées avant le 2 décembre devront aussi être retirées à cette porte si le retrait a lieu après cette date.
```

## modes-fr-046 · permissions

Source task:

> Reformule cette clause fictive sans avis juridique : Un membre peut quitter le groupe sans préavis. Les sommes déjà versées pour une activité réalisée ne sont pas remboursables. Aucun frais de départ ne peut être demandé.

### baseline: pass

```text
Tout membre peut quitter le groupe sans préavis ni frais de départ. Les sommes déjà versées pour une activité réalisée ne sont pas remboursables.
```

### lite: pass

```text
Un membre peut quitter le groupe sans préavis. Les sommes déjà versées pour une activité réalisée ne sont pas remboursables. Aucun frais de départ ne peut être exigé.
```

### full: pass

```text
Un membre peut quitter le groupe sans préavis et sans frais de départ. Les sommes déjà versées pour une activité réalisée ne sont pas remboursables.
```

### ultra: pass

```text
Un membre peut quitter le groupe sans préavis ni frais de départ. Les sommes déjà versées pour une activité réalisée ne sont pas remboursables.
```

### off: pass

```text
Tout membre peut quitter le groupe sans préavis. Les sommes déjà versées pour une activité qui a eu lieu ne sont pas remboursables. Aucun frais ne peut être exigé pour le départ.
```

## modes-fr-047 · unknown_actor

Source task:

> Réécris : Le dossier a été approuvé pendant l’absence de Léa. À son retour, Léa a seulement ajouté la date sur la couverture. La note ne nomme pas la personne qui a approuvé le dossier.

### baseline: pass

```text
Le dossier a été approuvé en l’absence de Léa, sans que la note précise qui l’a approuvé. À son retour, Léa a uniquement ajouté la date sur la couverture.
```

### lite: pass

```text
Le dossier a été approuvé pendant l’absence de Léa. À son retour, Léa a uniquement ajouté la date sur la couverture. La note ne précise pas qui a approuvé le dossier.
```

### full: pass

```text
Le dossier a été approuvé pendant l’absence de Léa, mais la note ne précise pas par qui. À son retour, Léa a uniquement ajouté la date sur la couverture.
```

### ultra: pass

```text
Le dossier a été approuvé pendant l’absence de Léa, sans que la note précise par qui. À son retour, Léa a uniquement ajouté la date sur la couverture.
```

### off: pass

```text
Le dossier a été approuvé pendant l’absence de Léa, mais la note ne précise pas par qui. À son retour, Léa a uniquement ajouté la date sur la couverture.
```

## modes-fr-048 · analysis

Source task:

> Deux descriptions d’un essai fictif : A dit « aucune panne pendant 40 heures » ; B dit « aucun incident observé pendant les 40 heures où le capteur enregistrait ». Pourquoi B est-elle plus précise, sachant que le capteur n’enregistrait pas en continu ?

### baseline: pass

```text
B limite le constat aux 40 heures pendant lesquelles le capteur enregistrait. Comme l’enregistrement n’était pas continu, elle ne permet pas d’exclure des incidents pendant les périodes non enregistrées. Elle distingue aussi l’absence d’incident observé de l’absence réelle de panne.
```

### lite: pass

```text
B limite le constat aux 40 heures où le capteur enregistrait et précise qu’aucun incident n’a été observé. Comme l’enregistrement n’était pas continu, on ne peut pas exclure des incidents pendant les périodes sans enregistrement. A peut laisser croire qu’aucune panne n’a eu lieu pendant 40 heures continues.
```

### full: pass

```text
B limite le constat aux 40 heures où le capteur enregistrait et précise qu’aucun incident n’a été observé. Comme l’enregistrement n’était pas continu, on ne peut rien conclure sur les périodes non enregistrées. A laisse entendre qu’aucune panne n’a eu lieu pendant 40 heures, sans préciser cette limite.
```

### ultra: pass

```text
B limite le constat aux 40 heures d’enregistrement : aucun incident n’y a été observé. Comme le capteur n’enregistrait pas en continu, cela ne prouve pas l’absence de panne hors de ces périodes. A ne précise pas cette limite.
```

### off: pass

```text
B précise que l’absence d’incident observé concerne uniquement les 40 heures d’enregistrement du capteur. Comme celui-ci n’enregistrait pas en continu, cela ne permet pas d’exclure des incidents pendant les périodes sans enregistrement. A peut laisser croire qu’aucune panne n’a eu lieu pendant 40 heures continues, sans cette limite d’observation.
```

## modes-fr-049 · negation

Source task:

> Rends ce message plus lisible : Nous ne demandons pas de remplacer le formulaire signé. Nous demandons seulement de joindre la page manquante. La signature déjà fournie reste valable.

### baseline: pass

```text
Merci de joindre uniquement la page manquante. Il n’est pas nécessaire de remplacer le formulaire signé : la signature déjà fournie reste valable.
```

### lite: pass

```text
Nous ne demandons pas de remplacer le formulaire signé, mais seulement de joindre la page manquante. La signature déjà fournie reste valable.
```

### full: pass

```text
Nous demandons seulement de joindre la page manquante, pas de remplacer le formulaire signé. La signature déjà fournie reste valable.
```

### ultra: pass

```text
Nous demandons seulement de joindre la page manquante, pas de remplacer le formulaire signé. La signature déjà fournie reste valable.
```

### off: pass

```text
Nous vous demandons seulement de joindre la page manquante, et non de remplacer le formulaire signé. La signature déjà fournie reste valable.
```

## modes-fr-050 · voice

Source task:

> Rédige un SMS poli à partir de ces éléments, sans inventer de motif : je dois annuler notre rendez-vous de demain ; je ne sais pas encore quand je serai disponible ; je recontacterai la personne quand je le saurai.

### baseline: pass

```text
Bonjour, je dois malheureusement annuler notre rendez-vous de demain. Je ne sais pas encore quand je serai disponible, mais je vous recontacterai dès que je le saurai. Veuillez m’excuser pour cette annulation.
```

### lite: pass

```text
Bonjour, je dois annuler notre rendez-vous de demain. Je ne sais pas encore quand je serai disponible, mais je vous recontacterai dès que je le saurai. Veuillez m’excuser pour cette annulation.
```

### full: pass

```text
Bonjour, je dois annuler notre rendez-vous de demain. Je ne sais pas encore quand je serai disponible, mais je vous recontacterai dès que je le saurai. Merci de votre compréhension.
```

### ultra: pass

```text
Bonjour, je dois annuler notre rendez-vous de demain. Veuillez m’en excuser. Je ne connais pas encore mes disponibilités et vous recontacterai dès que je les connaîtrai.
```

### off: pass

```text
Bonjour, je dois annuler notre rendez-vous de demain. Je ne sais pas encore quand je serai disponible, mais je vous recontacterai dès que je le saurai. Merci de votre compréhension.
```

## modes-fr-051 · ambiguity

Source task:

> Explique la différence entre ces deux consignes fictives : « Vous pouvez envoyer le dossier lundi » et « Vous devez envoyer le dossier lundi ». Ne déduis aucune date limite supplémentaire.

### baseline: pass

```text
« Vous pouvez envoyer le dossier lundi » autorise l’envoi lundi, sans l’imposer. « Vous devez envoyer le dossier lundi » impose l’envoi lundi.
```

### lite: pass

```text
« Vous pouvez envoyer le dossier lundi » donne une permission. « Vous devez envoyer le dossier lundi » impose une obligation.
```

### full: pass

```text
« Vous pouvez envoyer le dossier lundi » autorise l’envoi lundi, sans l’imposer. « Vous devez envoyer le dossier lundi » impose l’envoi lundi.
```

### ultra: pass

```text
« Vous pouvez envoyer le dossier lundi » autorise l’envoi lundi, sans l’imposer. « Vous devez envoyer le dossier lundi » impose l’envoi lundi.
```

### off: pass

```text
« Vous pouvez envoyer le dossier lundi » autorise l’envoi lundi, sans l’imposer. « Vous devez envoyer le dossier lundi » impose l’envoi lundi.
```

## modes-fr-052 · conditions

Source task:

> Clarifie : Un remboursement est possible si la séance a été annulée par le club, ou si le billet a été payé deux fois. Il n’est pas nécessaire que ces deux événements se produisent.

### baseline: pass

```text
Un remboursement est possible si le club a annulé la séance ou si le billet a été payé deux fois : une seule de ces conditions suffit.
```

### lite: pass

```text
Un remboursement est possible si le club a annulé la séance ou si le billet a été payé deux fois. Une seule de ces conditions suffit.
```

### full: pass

```text
Un remboursement est possible si le club a annulé la séance ou si le billet a été payé deux fois. Une seule de ces conditions suffit.
```

### ultra: pass

```text
Un remboursement est possible si le club a annulé la séance ou si le billet a été payé deux fois. Une seule de ces conditions suffit.
```

### off: pass

```text
Un remboursement est possible si le club a annulé la séance ou si le billet a été payé deux fois. Une seule de ces conditions suffit ; les deux ne sont pas nécessaires.
```

## modes-fr-053 · scope

Source task:

> À partir de cette note, réponds brièvement : les vélos sont-ils admis dans le hall et, sinon, où doivent-ils rester ? Note : les poussettes sont admises ; les vélos doivent rester dans la cour ; les petits colis peuvent être déposés à l’accueil jusqu’à 16 h.

### baseline: pass

```text
Non, les vélos ne sont pas admis dans le hall ; ils doivent rester dans la cour.
```

### lite: pass

```text
Non, les vélos ne sont pas admis dans le hall. Ils doivent rester dans la cour.
```

### full: pass

```text
Non, les vélos ne sont pas admis dans le hall : ils doivent rester dans la cour.
```

### ultra: pass

```text
Non, les vélos doivent rester dans la cour.
```

### off: pass

```text
Non, les vélos ne sont pas admis dans le hall : ils doivent rester dans la cour.
```

## modes-fr-054 · sampling

Source task:

> Écris une limite de l’essai : 9 personnes déjà formées ont testé la notice. Elles ont toutes fini en moins de 5 minutes. Aucune personne débutante n’a participé.

### baseline: flagged

```text
L’essai ne permet pas de savoir si les débutants peuvent utiliser la notice en moins de 5 minutes, car seules 9 personnes déjà formées y ont participé.
```

Review notes: Limite correctement formulée, mais omission du résultat observé : tous ont fini en moins de cinq minutes. / Correct limitation, but omits that all nine trained participants finished under five minutes.

### lite: pass

```text
Les 9 personnes ayant testé la notice étaient déjà formées et ont toutes fini en moins de 5 minutes ; aucune personne débutante n’ayant participé, ce résultat ne permet pas de conclure pour les débutants.
```

### full: pass

```text
Les 9 personnes ayant testé la notice étaient déjà formées et ont toutes terminé en moins de 5 minutes ; sans participation de personnes débutantes, ce résultat ne permet pas de conclure pour ce public.
```

### ultra: pass

```text
Les 9 personnes ont toutes terminé en moins de 5 minutes, mais elles étaient déjà formées : l’essai ne permet pas d’évaluer la notice pour les débutants, dont aucun n’a participé.
```

### off: flagged

```text
L’essai ne permet pas de conclure qu’une personne débutante finirait en moins de 5 minutes : les 9 participants étaient déjà formés et aucune personne débutante n’a participé.
```

Review notes: Limite correctement formulée, mais omission du résultat observé : tous ont fini en moins de cinq minutes. / Correct limitation, but omits that all nine trained participants finished under five minutes.

## modes-fr-055 · conflicting_notes

Source task:

> Rédige une phrase pour le registre : le carton porte « 24 unités », mais le comptage manuel en trouve 23. Le carton est fermé à nouveau ; aucun recomptage indépendant n’a encore été fait.

### baseline: pass

```text
Le carton porte la mention « 24 unités », mais le comptage manuel en a trouvé 23 ; le carton a été refermé et aucun recomptage indépendant n’a encore été effectué.
```

### lite: pass

```text
Le carton porte la mention « 24 unités », mais le comptage manuel en trouve 23 ; le carton est refermé et aucun recomptage indépendant n’a encore été effectué.
```

### full: pass

```text
Le carton porte la mention « 24 unités », mais le comptage manuel en trouve 23 ; le carton a été refermé et aucun recomptage indépendant n’a encore été effectué.
```

### ultra: pass

```text
Le carton porte « 24 unités », mais le comptage manuel en trouve 23 ; il a été refermé et aucun recomptage indépendant n’a encore été effectué.
```

### off: pass

```text
Le carton porte la mention « 24 unités », mais le comptage manuel en trouve 23 ; le carton a été refermé et aucun recomptage indépendant n’a encore été effectué.
```

## modes-fr-056 · numbers_units

Source task:

> Réécris : La limite est de 12 kg par caisse, pas par expédition. Une expédition peut contenir trois caisses au maximum. Le poids du contenant est inclus dans les 12 kg.

### baseline: pass

```text
Chaque caisse peut peser au maximum 12 kg, contenant inclus. Une expédition peut comprendre jusqu’à trois caisses. La limite de 12 kg s’applique à chaque caisse, et non à l’expédition entière.
```

### lite: pass

```text
La limite est de 12 kg par caisse, et non par expédition. Une expédition peut contenir au maximum trois caisses. Le poids du contenant est inclus dans les 12 kg.
```

### full: pass

```text
Chaque caisse est limitée à 12 kg, poids du contenant inclus. Cette limite s’applique par caisse, pas par expédition. Une expédition peut contenir au maximum trois caisses.
```

### ultra: pass

```text
Chaque caisse est limitée à 12 kg, contenant inclus. Cette limite s’applique par caisse, pas par expédition. Une expédition peut contenir au maximum trois caisses.
```

### off: pass

```text
Chaque caisse peut peser au maximum 12 kg, poids du contenant inclus. Cette limite s’applique par caisse, et non par expédition. Une expédition peut contenir jusqu’à trois caisses.
```

## modes-fr-057 · technical

Source task:

> Rends cette note de version claire : Avec version 2.4, le filtre archived=false masque les éléments archivés ; il ne les supprime pas. Les exports lancés avant la mise à jour gardent l’ancien filtre jusqu’à leur fin.

### baseline: pass

```text
Dans la version 2.4, le filtre archived=false masque les éléments archivés sans les supprimer. Les exports lancés avant la mise à jour continuent d’utiliser l’ancien filtre jusqu’à leur fin.
```

### lite: pass

```text
Avec la version 2.4, le filtre archived=false masque les éléments archivés sans les supprimer. Les exports lancés avant la mise à jour conservent l’ancien filtre jusqu’à leur fin.
```

### full: pass

```text
Dans la version 2.4, le filtre archived=false masque les éléments archivés sans les supprimer. Les exports lancés avant la mise à jour conservent l’ancien filtre jusqu’à leur fin.
```

### ultra: pass

```text
Dans la version 2.4, le filtre archived=false masque les éléments archivés sans les supprimer. Les exports lancés avant la mise à jour conservent l’ancien filtre jusqu’à leur fin.
```

### off: pass

```text
Dans la version 2.4, le filtre archived=false masque les éléments archivés sans les supprimer. Les exports lancés avant la mise à jour conservent l’ancien filtre jusqu’à leur fin.
```

## modes-fr-058 · analysis

Source task:

> Peut-on affirmer que le délai médian a baissé pour chaque dossier ? Le délai médian de l’ensemble passe de 8 à 6 jours dans une simulation. Les délais individuels ne sont pas fournis.

### baseline: pass

```text
Non. Dans la simulation, le délai médian de l’ensemble passe de 8 à 6 jours, mais cela ne signifie pas que le délai de chaque dossier a baissé. Sans les délais individuels, on ne peut pas l’affirmer.
```

### lite: pass

```text
Non. Dans la simulation, le délai médian de l’ensemble passe de 8 à 6 jours. Cela ne signifie pas que le délai a baissé pour chaque dossier. Les délais individuels ne sont pas fournis.
```

### full: pass

```text
Non. Dans la simulation, le délai médian de l’ensemble passe de 8 à 6 jours. Cela ne signifie pas que le délai a baissé pour chaque dossier : les délais individuels ne sont pas fournis.
```

### ultra: pass

```text
Non. Dans la simulation, le délai médian de l’ensemble passe de 8 à 6 jours. Sans les délais individuels, on ne peut pas affirmer que le délai a baissé pour chaque dossier.
```

### off: pass

```text
Non. Dans la simulation, le délai médian de l’ensemble passe de 8 à 6 jours, mais cela ne signifie pas que le délai a baissé pour chaque dossier. Les délais individuels ne sont pas fournis.
```

## modes-fr-059 · voice

Source task:

> Réécris cette petite description en gardant la voix poétique et les faits : La pluie frappait doucement la vitre. Sur la table, trois tasses froides attendaient. Personne n’était revenu depuis le matin.

### baseline: pass

```text
La pluie tapait doucement à la vitre. Sur la table, trois tasses froides attendaient encore. Depuis le matin, personne n’était revenu.
```

### lite: pass

```text
La pluie frappait doucement la vitre. Sur la table, trois tasses froides attendaient. Personne n’était revenu depuis le matin.
```

### full: pass

```text
La pluie frappait doucement la vitre. Sur la table, trois tasses froides attendaient. Personne n’était revenu depuis le matin.
```

### ultra: pass

```text
La pluie frappait doucement la vitre. Sur la table, trois tasses froides attendaient. Personne n’était revenu depuis le matin.
```

### off: pass

```text
La pluie frappait la vitre à coups doux. Sur la table attendaient trois tasses froides. Depuis le matin, personne n’était revenu.
```

## modes-fr-060 · exact_format

Source task:

> Renvoie uniquement cette ligne, sans guillemets ni introduction : Réservation suspendue — référence R-28.

### baseline: pass

```text
Réservation suspendue — référence R-28.
```

### lite: pass

```text
Réservation suspendue — référence R-28.
```

### full: pass

```text
Réservation suspendue — référence R-28.
```

### ultra: pass

```text
Réservation suspendue — référence R-28.
```

### off: pass

```text
Réservation suspendue — référence R-28.
```

## modes-fr-061 · exact_format

Source task:

> Réécris la valeur de message en français plus simple. Renvoie seulement un objet JSON avec les clés ticket, attempts et message. Conserve ticket et attempts : {"ticket":"Q-613","attempts":2,"message":"Nous vous informons que votre pièce jointe n’a pas pu être ouverte ; veuillez la renvoyer au format PDF."}

### baseline: pass

```text
{"ticket":"Q-613","attempts":2,"message":"Nous n’avons pas pu ouvrir votre pièce jointe. Merci de la renvoyer au format PDF."}
```

### lite: pass

```text
{"ticket":"Q-613","attempts":2,"message":"Votre pièce jointe n’a pas pu être ouverte. Veuillez la renvoyer au format PDF."}
```

### full: pass

```text
{"ticket":"Q-613","attempts":2,"message":"Votre pièce jointe n’a pas pu être ouverte. Veuillez la renvoyer au format PDF."}
```

### ultra: pass

```text
{"ticket":"Q-613","attempts":2,"message":"Votre pièce jointe n’a pas pu être ouverte. Veuillez la renvoyer au format PDF."}
```

### off: pass

```text
{"ticket":"Q-613","attempts":2,"message":"Nous n’avons pas pu ouvrir votre pièce jointe. Merci de la renvoyer au format PDF."}
```

## modes-fr-062 · exact_format

Source task:

> Écris un avis de maintenance en deux phrases. Il doit dire que le dossier /srv/atelier reste accessible en lecture et que les écritures reprennent à 21:15 UTC. Conserve exactement le chemin et l’heure.

### baseline: pass

```text
Pendant la maintenance, le dossier /srv/atelier reste accessible en lecture. Les écritures reprennent à 21:15 UTC.
```

### lite: pass

```text
Pendant la maintenance, le dossier /srv/atelier reste accessible en lecture. Les écritures reprennent à 21:15 UTC.
```

### full: pass

```text
Pendant la maintenance, le dossier /srv/atelier reste accessible en lecture. Les écritures reprennent à 21:15 UTC.
```

### ultra: pass

```text
Pendant la maintenance, le dossier /srv/atelier reste accessible en lecture. Les écritures reprennent à 21:15 UTC.
```

### off: pass

```text
Pendant la maintenance, le dossier /srv/atelier reste accessible en lecture. Les écritures reprennent à 21:15 UTC.
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
Bonjour {{prenom}}, vous pouvez télécharger votre facture avec {{lien_facture}} jusqu’au 14 juin.
```

### lite: pass

```text
Bonjour {{prenom}}, vous pouvez télécharger votre facture avec {{lien_facture}} jusqu’au 14 juin.
```

### full: pass

```text
{{prenom}}, vous pouvez télécharger votre facture avec {{lien_facture}} jusqu’au 14 juin.
```

### ultra: pass

```text
{{prenom}}, vous pouvez télécharger votre facture avec {{lien_facture}} jusqu’au 14 juin.
```

### off: pass

```text
Bonjour {{prenom}}, vous pouvez télécharger votre facture avec {{lien_facture}} jusqu’au 14 juin.
```

## modes-fr-065 · exact_format

Source task:

> Résume le statut dans un objet JSON et rien d’autre. Clés requises : id, ready, note. Données : id = "LOT-8" ; ready = false ; l’inspection visuelle est terminée mais le test de charge reste à faire. La note doit être en français.

### baseline: pass

```text
{"id":"LOT-8","ready":false,"note":"L’inspection visuelle est terminée, mais le test de charge reste à faire."}
```

### lite: pass

```text
{"id":"LOT-8","ready":false,"note":"L’inspection visuelle est terminée, mais le test de charge reste à faire."}
```

### full: pass

```text
{"id":"LOT-8","ready":false,"note":"L’inspection visuelle est terminée, mais le test de charge reste à faire."}
```

### ultra: pass

```text
{"id":"LOT-8","ready":false,"note":"L’inspection visuelle est terminée, mais le test de charge reste à faire."}
```

### off: pass

```text
{"id":"LOT-8","ready":false,"note":"L’inspection visuelle est terminée, mais le test de charge reste à faire."}
```

## modes-fr-066 · exact_format

Source task:

> Reproduis exactement ces deux lignes, sans bloc de code :
> Accès provisoire : oui
> Export des données : non

### baseline: pass

```text
Accès provisoire : oui
Export des données : non
```

### lite: pass

```text
Accès provisoire : oui
Export des données : non
```

### full: pass

```text
Accès provisoire : oui
Export des données : non
```

### ultra: pass

```text
Accès provisoire : oui
Export des données : non
```

### off: pass

```text
Accès provisoire : oui
Export des données : non
```

## modes-fr-067 · exact_format

Source task:

> Écris une phrase qui explique cette commande sans la modifier : python verify.py --dry-run. Elle simule la vérification et ne change aucun fichier.

### baseline: pass

```text
La commande python verify.py --dry-run simule la vérification sans modifier aucun fichier.
```

### lite: pass

```text
La commande python verify.py --dry-run simule la vérification sans modifier aucun fichier.
```

### full: pass

```text
La commande python verify.py --dry-run simule la vérification sans modifier aucun fichier.
```

### ultra: pass

```text
La commande python verify.py --dry-run simule la vérification sans modifier aucun fichier.
```

### off: pass

```text
La commande python verify.py --dry-run simule la vérification sans modifier aucun fichier.
```

## modes-fr-068 · exact_format

Source task:

> Rends ce message plus clair tout en conservant la citation anglaise exacte : Le journal affiche "buffer full". Cela décrit un tampon plein, pas une perte de données confirmée. Il faut examiner le journal complet avant de conclure.

### baseline: pass

```text
Le journal affiche "buffer full", ce qui signifie que le tampon est plein, mais ne confirme pas une perte de données. Il faut examiner le journal complet avant de conclure.
```

### lite: pass

```text
Le journal affiche "buffer full". Ce message indique un tampon plein, mais ne confirme pas une perte de données. Il faut examiner le journal complet avant de conclure.
```

### full: pass

```text
Le journal affiche "buffer full" : le tampon est plein, mais aucune perte de données n’est confirmée. Il faut examiner le journal complet avant de conclure.
```

### ultra: pass

```text
Le journal affiche "buffer full" : le tampon est plein, mais aucune perte de données n’est confirmée. Il faut examiner le journal complet avant de conclure.
```

### off: pass

```text
Le journal affiche "buffer full", ce qui indique que le tampon est plein, sans confirmer une perte de données. Il faut examiner le journal complet avant de conclure.
```

## modes-fr-069 · exact_format

Source task:

> Renvoie uniquement un objet JSON avec batch, limit et notice. Garde batch="B-91" et limit=0. Notice à simplifier : « Aucun envoi n’est autorisé tant que la limite reste à zéro. »

### baseline: pass

```text
{"batch":"B-91","limit":0,"notice":"Aucun envoi n’est autorisé tant que la limite est à zéro."}
```

### lite: pass

```text
{"batch":"B-91","limit":0,"notice":"Aucun envoi n’est autorisé tant que la limite reste à zéro."}
```

### full: pass

```text
{"batch":"B-91","limit":0,"notice":"Aucun envoi n’est autorisé tant que la limite est à zéro."}
```

### ultra: pass

```text
{"batch":"B-91","limit":0,"notice":"Aucun envoi n’est autorisé tant que la limite reste à zéro."}
```

### off: pass

```text
{"batch":"B-91","limit":0,"notice":"Aucun envoi n’est autorisé tant que la limite est à zéro."}
```

## modes-fr-070 · long_summary

Source task:

> Prépare une synthèse de passation pour la personne qui ouvrira demain l’atelier associatif. Elle doit pouvoir décider ce qui est disponible et ce qui attend encore un contrôle. Ne transforme pas les propositions en décisions.
> 
> Notes du soir : l’inventaire porte sur 46 outils numérotés. Quarante-deux sont dans l’armoire, deux ont été prêtés avec une fiche signée et deux restent introuvables. Les fiches de prêt sont rangées dans le classeur bleu ; la date de retour prévue est le 18 mars. Les deux outils introuvables n’ont pas été déclarés volés. Le dernier inventaire était incomplet, ce qui laisse ouverte la possibilité qu’ils aient simplement été mal enregistrés.
> 
> Les trois perceuses présentes ont été nettoyées. Une seule, P-07, a subi le contrôle électrique. Elle peut être prêtée. Les deux autres ne doivent pas être prêtées tant que ce contrôle n’a pas été fait. L’étiquette verte signifie seulement que le nettoyage est terminé ; elle n’est pas une autorisation de prêt. La perceuse P-07 se trouve sur l’étagère du haut, avec sa batterie.
> 
> Le stock de vis est utilisable. Le poids noté, 4,8 kg, comprend les boîtes et ne permet pas de calculer le nombre de vis. Une commande de boîtes supplémentaires a été proposée, mais aucune commande n’a été passée. Le budget disponible pour les consommables est estimé à 110 € ; ce chiffre attend la vérification de deux reçus.
> 
> Rami a proposé de refaire les étiquettes samedi. Son aide n’a pas encore été confirmée. Une liste des étiquettes illisibles est sur le bureau, à côté du registre. Le nettoyage du sol est terminé. Le robinet de la réserve goutte encore et la cuisine reste fermée jusqu’à sa réparation. Le responsable du prêt doit utiliser les fiches habituelles ; aucun nouveau formulaire n’a été approuvé.

### baseline: pass

```text
## Passation pour l’ouverture de demain

### Disponible
- **Perceuse P-07** : nettoyée et contrôlée électriquement, elle peut être prêtée. Elle est sur l’étagère du haut, avec sa batterie.
- **Stock de vis** : utilisable. Le poids de 4,8 kg inclut les boîtes et ne permet pas de déterminer le nombre de vis.
- Le nettoyage du sol est terminé.

### En attente ou indisponible
- **Deux autres perceuses présentes** : nettoyées, mais à ne pas prêter avant leur contrôle électrique. L’étiquette verte atteste uniquement le nettoyage, pas l’autorisation de prêt.
- **Cuisine** : reste fermée jusqu’à la réparation du robinet de la réserve, qui goutte encore.
- **Budget consommables** : estimé à 110 €, à confirmer après vérification de deux reçus.

### Inventaire et prêts
- Sur 46 outils numérotés : 42 sont dans l’armoire, 2 sont prêtés avec une fiche signée et 2 restent introuvables.
- Les fiches de prêt sont dans le classeur bleu ; le retour est prévu le 18 mars.
- Les outils introuvables n’ont pas été déclarés volés. Le dernier inventaire étant incomplet, un mauvais enregistrement reste possible.
- Pour les prêts, utiliser les fiches habituelles : aucun nouveau formulaire n’a été approuvé.

### Propositions non confirmées
- Une commande de boîtes supplémentaires a été proposée, mais aucune commande n’a été passée.
- Rami a proposé de refaire les étiquettes samedi ; son aide n’est pas encore confirmée. La liste des étiquettes illisibles est sur le bureau, à côté du registre.
```

### lite: pass

```text
## Passation pour l’ouverture de demain

### Inventaire et prêts
L’inventaire porte sur 46 outils numérotés : 42 sont dans l’armoire, deux ont été prêtés avec une fiche signée et deux restent introuvables. Les fiches de prêt sont dans le classeur bleu. Le retour est prévu le 18 mars.

Les deux outils introuvables n’ont pas été déclarés volés. Le dernier inventaire était incomplet : ils ont peut-être simplement été mal enregistrés.

### Perceuses : disponibilité et contrôles
Les trois perceuses présentes ont été nettoyées. Seule P-07 a subi le contrôle électrique et peut être prêtée. Elle est sur l’étagère du haut, avec sa batterie.

Les deux autres ne doivent pas être prêtées avant leur contrôle électrique. L’étiquette verte indique uniquement que le nettoyage est terminé ; elle n’autorise pas le prêt.

### Consommables
Le stock de vis est utilisable. Le poids indiqué, 4,8 kg, comprend les boîtes et ne permet pas de calculer le nombre de vis.

Une commande de boîtes supplémentaires a été proposée, mais aucune commande n’a été passée. Le budget disponible pour les consommables est estimé à 110 €, sous réserve de la vérification de deux reçus.

### Étiquettes, locaux et procédure
Rami a proposé de refaire les étiquettes samedi, mais son aide n’est pas encore confirmée. La liste des étiquettes illisibles est sur le bureau, à côté du registre.

Le nettoyage du sol est terminé. Le robinet de la réserve goutte encore. La cuisine reste fermée jusqu’à sa réparation.

Le responsable du prêt doit utiliser les fiches habituelles : aucun nouveau formulaire n’a été approuvé.
```

### full: pass

```text
## Disponible demain
- **Perceuse P-07 : prêt autorisé.** Elle a été nettoyée et a passé le contrôle électrique. Elle se trouve sur l’étagère du haut, avec sa batterie.
- **Stock de vis : utilisable.** Les 4,8 kg notés comprennent les boîtes et ne permettent pas de calculer le nombre de vis.
- Le nettoyage du sol est terminé.

## En attente de contrôle ou de réparation
- Les deux autres perceuses présentes ont été nettoyées, mais ne doivent pas être prêtées avant leur contrôle électrique. L’étiquette verte confirme uniquement le nettoyage, pas l’autorisation de prêt.
- Le robinet de la réserve goutte encore. La cuisine reste fermée jusqu’à sa réparation.
- Le budget disponible pour les consommables est estimé à 110 € ; deux reçus restent à vérifier pour confirmer ce montant.

## Inventaire et prêts
L’inventaire porte sur 46 outils numérotés : 42 sont dans l’armoire, deux sont prêtés avec une fiche signée et deux restent introuvables. Les fiches de prêt sont dans le classeur bleu ; le retour est prévu le 18 mars.

Les deux outils introuvables n’ont pas été déclarés volés. Le dernier inventaire étant incomplet, ils peuvent avoir été mal enregistrés.

Le responsable du prêt doit utiliser les fiches habituelles : aucun nouveau formulaire n’a été approuvé.

## Propositions non confirmées
- Une commande de boîtes supplémentaires a été proposée, mais aucune commande n’a été passée.
- Rami a proposé de refaire les étiquettes samedi ; son aide n’est pas encore confirmée. La liste des étiquettes illisibles est sur le bureau, à côté du registre.
```

### ultra: pass

```text
## Passation pour l’ouverture de demain

### Disponible ou en attente de contrôle
- **Perceuses :** les trois présentes sont nettoyées. Seule **P-07**, contrôlée électriquement, peut être prêtée ; elle est sur l’étagère du haut, avec sa batterie. Les deux autres ne doivent pas être prêtées avant leur contrôle électrique. L’étiquette verte atteste seulement le nettoyage, pas l’autorisation de prêt.
- **Vis :** stock utilisable. Les **4,8 kg** incluent les boîtes et ne permettent pas de calculer le nombre de vis.
- **Locaux :** nettoyage du sol terminé. Le robinet de la réserve goutte encore ; la cuisine reste fermée jusqu’à sa réparation.

### Inventaire et prêts
- **46 outils numérotés :** 42 dans l’armoire, 2 prêtés avec une fiche signée, 2 introuvables.
- Fiches de prêt dans le **classeur bleu** ; retour prévu le **18 mars**.
- Les outils introuvables n’ont pas été déclarés volés. Le dernier inventaire était incomplet : un mauvais enregistrement reste possible.
- Le responsable du prêt doit utiliser les fiches habituelles ; aucun nouveau formulaire n’a été approuvé.

### À vérifier ou à confirmer
- Budget consommables estimé à **110 €**, en attente de vérification de **deux reçus**.
- Commande de boîtes supplémentaires proposée, mais aucune commande passée.
- Rami a proposé de refaire les étiquettes samedi ; son aide n’est pas confirmée. La liste des étiquettes illisibles est sur le bureau, à côté du registre.
```

### off: pass

```text
## Passation pour l’ouverture de demain

### Disponible et autorisé
- **Perceuse P-07** : nettoyée et contrôlée électriquement, elle peut être prêtée. Elle est sur l’étagère du haut, avec sa batterie.
- **Stock de vis** : utilisable. Le poids de 4,8 kg comprend les boîtes et ne permet pas de calculer le nombre de vis.
- Le nettoyage du sol est terminé.

### Contrôles et restrictions
- Les deux autres perceuses présentes ont été nettoyées, mais ne doivent pas être prêtées avant leur contrôle électrique. L’étiquette verte atteste uniquement le nettoyage, pas l’autorisation de prêt.
- Le robinet de la réserve goutte encore. La cuisine reste fermée jusqu’à sa réparation.
- Le budget disponible pour les consommables est estimé à 110 €, sous réserve de la vérification de deux reçus.

### Inventaire et prêts
L’inventaire porte sur 46 outils numérotés : 42 sont dans l’armoire, deux sont prêtés avec une fiche signée et deux restent introuvables. La présence dans l’armoire ne constitue pas, à elle seule, une autorisation de prêt.

Les fiches de prêt sont dans le classeur bleu. Le retour des deux outils prêtés est prévu le 18 mars. Les deux outils introuvables n’ont pas été déclarés volés : le dernier inventaire était incomplet, et un mauvais enregistrement reste possible.

Le responsable du prêt doit utiliser les fiches habituelles. Aucun nouveau formulaire n’a été approuvé.

### Propositions non confirmées
- Une commande de boîtes supplémentaires a été proposée, mais aucune commande n’a été passée.
- Rami a proposé de refaire les étiquettes samedi ; son aide n’est pas encore confirmée. La liste des étiquettes illisibles est sur le bureau, à côté du registre.
```

## modes-fr-071 · long_sampling

Source task:

> Rédige un bilan de cette consultation fictive pour un comité de quartier. Présente le résultat principal, puis ce qu’on peut et ce qu’on ne peut pas en déduire. Le comité n’a pas demandé de recommandation sur le choix final.
> 
> Le questionnaire portait sur l’usage d’un ancien kiosque : salle de lecture, atelier partagé ou local de rangement. Il a été diffusé pendant deux après-midi sur la place et pendant une matinée à la sortie du cours de dessin. Il n’a pas été envoyé aux habitants par courrier et n’était pas disponible dans les autres rues. Les personnes choisissaient elles-mêmes de répondre ; aucune liste d’habitants n’a servi à tirer un échantillon.
> 
> Cent vingt fiches ont été distribuées. Soixante fiches exploitables ont été rendues. Douze autres fiches étaient vides ou comportaient plusieurs choix alors qu’un seul était demandé ; elles ont été exclues des résultats. Sur les 60 réponses exploitables, 33 préfèrent la salle de lecture, 18 l’atelier partagé et 9 le rangement. La salle de lecture représente donc 55 % des réponses exploitables. Le nombre total d’habitants du quartier n’est pas fourni.
> 
> Vingt-huit personnes ont laissé un commentaire. Dix de ces commentaires disent manquer d’un lieu calme. Cela ne veut pas dire que dix personnes seulement dans le quartier ont ce besoin, ni que tous les partisans de la salle de lecture ont donné cette raison. Les commentaires ne peuvent pas être rattachés aux choix individuels parce qu’ils ont été déposés dans une autre boîte.
> 
> Le groupe qui a distribué les fiches signale une forte présence de participants au cours de dessin, mais il ne les a pas comptés séparément. Certaines personnes ont demandé une version audio ; elle n’avait pas été prévue. Le coût des trois projets n’a pas été étudié. Les réponses décrivent des préférences exprimées dans ce dispositif, pas une décision du comité ni une comparaison complète des projets.

### baseline: pass

```text
## Résultat principal
La salle de lecture arrive en tête avec 33 choix sur 60 réponses exploitables, soit 55 %. L’atelier partagé recueille 18 choix (30 %) et le rangement 9 (15 %).

Sur 120 fiches distribuées, 60 étaient exploitables et 12 autres ont été exclues parce qu’elles étaient vides ou comportaient plusieurs choix.

## Ce qu’on peut en déduire
La salle de lecture est l’option préférée de la majorité des personnes ayant fourni une réponse exploitable dans ce dispositif. Parmi les 28 commentaires déposés, 10 évoquent le manque d’un lieu calme.

## Ce qu’on ne peut pas en déduire
Ces résultats ne permettent pas d’établir les préférences de l’ensemble du quartier : la participation était volontaire, sans tirage au sort, et la diffusion était limitée à deux après-midi sur la place et une matinée à la sortie du cours de dessin. Le questionnaire n’était proposé ni par courrier ni dans les autres rues. Le nombre total d’habitants est inconnu.

La forte présence signalée de participants au cours de dessin n’a pas été quantifiée. L’absence de version audio a également limité les possibilités de participation.

Les commentaires étant déposés séparément, on ne peut pas relier le besoin de calme à un choix individuel. Les 10 commentaires ne mesurent ni le nombre total d’habitants ayant ce besoin ni les raisons de tous les partisans de la salle de lecture.

Enfin, les coûts n’ont pas été étudiés. Cette consultation décrit des préférences exprimées ; elle ne constitue ni une comparaison complète des projets ni une décision du comité.
```

### lite: pass

```text
Résultat principal

La salle de lecture arrive en tête avec 33 des 60 réponses exploitables, soit 55 %. L’atelier partagé recueille 18 réponses et le local de rangement, 9. Sur 120 fiches distribuées, 60 fiches exploitables ont été rendues. Douze autres fiches ont été exclues parce qu’elles étaient vides ou comportaient plusieurs choix alors qu’un seul était demandé.

Ce qu’on peut en déduire

La salle de lecture est le choix majoritaire parmi les réponses exploitables recueillies dans ce dispositif. Parmi les 28 personnes ayant laissé un commentaire, 10 disent manquer d’un lieu calme. Ces commentaires montrent que ce besoin a été exprimé, sans permettre d’en mesurer l’étendue dans le quartier.

Ce qu’on ne peut pas en déduire

Ces résultats ne permettent pas d’établir la préférence de l’ensemble des habitants. Les personnes choisissaient elles-mêmes de répondre ; aucun échantillon n’a été tiré à partir d’une liste d’habitants. Le questionnaire a été diffusé pendant deux après-midi sur la place et une matinée à la sortie du cours de dessin. Il n’a été ni envoyé par courrier ni proposé dans les autres rues. Le nombre total d’habitants n’est pas fourni.

Le groupe chargé de la distribution signale une forte présence de participants au cours de dessin, sans les avoir comptés séparément. Certaines personnes ont demandé une version audio, qui n’avait pas été prévue.

Les 10 commentaires sur le manque d’un lieu calme ne signifient ni que seules 10 personnes du quartier ont ce besoin, ni que tous les partisans de la salle de lecture ont donné cette raison. Déposés dans une autre boîte, les commentaires ne peuvent pas être rattachés aux choix individuels.

Enfin, le coût des trois projets n’a pas été étudié. Les réponses décrivent des préférences exprimées dans cette consultation, pas une décision du comité ni une comparaison complète des projets.
```

### full: pass

```text
## Résultat principal

La salle de lecture arrive en tête avec 33 des 60 réponses exploitables, soit 55 %. L’atelier partagé recueille 18 préférences et le local de rangement, 9.

Sur 120 fiches distribuées, 60 fiches exploitables ont été rendues. Douze autres fiches, vides ou comportant plusieurs choix alors qu’un seul était demandé, ont été exclues.

## Ce qu’on peut en déduire

La salle de lecture est le choix majoritaire parmi les réponses exploitables recueillies dans ce dispositif.

Vingt-huit personnes ont laissé un commentaire ; dix commentaires évoquent le manque d’un lieu calme. Ce besoin apparaît donc dans les commentaires, mais ceux-ci ont été déposés dans une boîte séparée et ne peuvent pas être rattachés aux choix individuels.

## Ce qu’on ne peut pas en déduire

Ces résultats ne permettent pas d’établir les préférences de l’ensemble du quartier. La participation était volontaire, sans tirage d’un échantillon à partir d’une liste d’habitants. Le questionnaire a été diffusé pendant deux après-midi sur la place et une matinée à la sortie du cours de dessin, sans envoi postal ni disponibilité dans les autres rues. Le nombre total d’habitants n’est pas fourni.

Le groupe distributeur signale une forte présence de participants au cours de dessin, sans les avoir comptés séparément. Certaines personnes ont demandé une version audio, qui n’avait pas été prévue.

Les dix commentaires sur le besoin de calme ne signifient ni que seules dix personnes du quartier ont ce besoin, ni que tous les partisans de la salle de lecture ont donné cette raison.

Enfin, le coût des trois projets n’a pas été étudié. La consultation décrit des préférences exprimées dans ce dispositif : elle ne constitue ni une décision du comité ni une comparaison complète des projets.
```

### ultra: pass

```text
La salle de lecture arrive en tête : 33 des 60 réponses exploitables, soit 55 %, contre 18 pour l’atelier partagé et 9 pour le rangement.

Ce que la consultation montre
Sur 120 fiches distribuées, 60 réponses exploitables ont été rendues. Douze autres fiches, vides ou comportant plusieurs choix au lieu d’un, ont été exclues. Parmi les 28 personnes ayant laissé un commentaire, 10 signalent le manque d’un lieu calme.

Ce qu’elle ne permet pas de conclure
Ces résultats décrivent les préférences exprimées dans ce dispositif, pas celles de tout le quartier. La participation était volontaire, sans échantillon tiré d’une liste d’habitants. Le questionnaire a été diffusé pendant deux après-midi sur la place et une matinée à la sortie du cours de dessin, sans envoi postal ni disponibilité dans les autres rues. Le nombre total d’habitants est inconnu.

Le groupe distributeur signale une forte présence de participants au cours de dessin, sans comptage séparé. Certaines personnes ont demandé une version audio, non prévue.

Les 10 commentaires sur le besoin de calme ne dénombrent pas tous les habitants ayant ce besoin. Ils ne donnent pas non plus la raison de tous les soutiens à la salle de lecture : déposés dans une autre boîte, les commentaires ne peuvent pas être reliés aux choix individuels.

Le coût des trois projets n’a pas été étudié. La consultation ne constitue donc ni une comparaison complète des projets ni une décision du comité.
```

### off: pass

```text
## Résultat principal

La salle de lecture arrive en tête avec 33 choix sur 60 réponses exploitables, soit 55 %. L’atelier partagé recueille 18 choix et le local de rangement 9.

Sur 120 fiches distribuées, 60 fiches exploitables ont été rendues. Douze autres fiches, vides ou comportant plusieurs choix alors qu’un seul était demandé, ont été exclues.

## Ce que l’on peut en déduire

La salle de lecture est l’option préférée par la majorité des personnes ayant fourni une réponse exploitable dans ce dispositif de consultation.

Vingt-huit personnes ont laissé un commentaire. Dix commentaires mentionnent le manque d’un lieu calme : ce besoin apparaît donc dans les commentaires recueillis.

## Ce que l’on ne peut pas en déduire

Ces résultats ne permettent pas d’établir la préférence de l’ensemble du quartier. La participation était volontaire, sans tirage au sort à partir d’une liste d’habitants. Le questionnaire a été diffusé pendant deux après-midi sur la place et une matinée à la sortie du cours de dessin, mais pas par courrier ni dans les autres rues. Le nombre total d’habitants n’est pas fourni.

Le groupe distributeur signale une forte présence de participants au cours de dessin, sans les avoir comptés séparément. Certaines personnes ont demandé une version audio, qui n’avait pas été prévue. Ces éléments limitent la portée des résultats.

Les dix commentaires sur le manque d’un lieu calme ne signifient ni que seules dix personnes du quartier ont ce besoin, ni que tous les partisans de la salle de lecture ont donné cette raison. Les commentaires ayant été déposés dans une autre boîte, ils ne peuvent pas être rattachés aux choix individuels.

Enfin, le coût des trois projets n’a pas été étudié. Cette consultation décrit des préférences exprimées dans un dispositif particulier ; elle ne constitue ni une décision du comité ni une comparaison complète des projets.
```

## modes-fr-072 · long_scope

Source task:

> Réponds à la seule question du président : « Pouvons-nous ouvrir l’exposition vendredi matin selon cette note ? » Explique les conditions encore manquantes. Les détails de budget servent de contexte et ne demandent pas une nouvelle analyse financière.
> 
> La note préparatoire concerne une petite exposition fictive dans un ancien bureau. L’accrochage des 24 cadres est terminé et les cartels sont imprimés. Deux cartels ont été réimprimés pour corriger une faute dans le nom d’une œuvre. Les bénévoles ont vérifié les supports, mais cette vérification ne remplace pas le contrôle technique exigé par le règlement interne.
> 
> Le règlement exige, avant toute ouverture au public, un contrôle technique signé et la présence de deux bénévoles d’accueil. Le contrôle doit couvrir le montage et l’éclairage. La personne chargée du contrôle a annoncé qu’elle pourrait passer jeudi soir ; elle n’a confirmé ni sa venue ni la signature. La signature d’un contrôle réalisé l’an dernier dans une autre salle ne vaut pas pour cette exposition. Le second bénévole du vendredi matin n’a pas encore accepté le créneau. Une personne inscrite pour vendredi après-midi ne peut pas être comptée pour le matin.
> 
> Le budget prévisionnel est de 620 €. Les achats déjà justifiés représentent 480 €, et une facture de location reste attendue. Le trésorier pense que le budget sera respecté, mais n’a pas validé le total. Ces chiffres ne créent aucune dispense des conditions d’ouverture. Les invitations imprimées indiquent vendredi à 9 h ; elles peuvent être remplacées si l’ouverture est décalée.
> 
> Le jeudi est réservé au rangement et aux essais de lumière. Les bénévoles peuvent entrer pour ces préparatifs, sans public et sans vente. Une autorisation d’entrer pour préparer la salle ne constitue pas une autorisation d’ouvrir l’exposition. La décision finale doit être prise à partir des conditions effectivement remplies, et non à partir d’une visite promise ou d’un nom inscrit au mauvais créneau.

### baseline: pass

```text
Pas encore : selon cette note, l’ouverture vendredi matin ne peut pas être confirmée. Elle sera possible uniquement si, avant l’accueil du public :

- un contrôle technique couvrant le montage et l’éclairage a été réalisé et signé ; la visite envisagée jeudi soir n’est pas confirmée, pas plus que la signature. La vérification des bénévoles et le contrôle signé l’an dernier dans une autre salle ne suffisent pas ;
- deux bénévoles d’accueil sont effectivement disponibles vendredi matin. Le second n’a pas encore accepté ce créneau, et la personne inscrite l’après-midi ne peut pas être comptée pour le matin.

Les préparatifs du jeudi restent autorisés sans public ni vente, mais n’autorisent pas l’ouverture. Le budget et les invitations annonçant 9 h ne dispensent d’aucune de ces conditions. Si elles ne sont pas remplies à temps, l’ouverture devra être décalée et les invitations pourront être remplacées.
```

### lite: pass

```text
Pas en l’état. L’ouverture vendredi à 9 h reste possible seulement si les deux conditions exigées sont effectivement remplies avant l’accueil du public :

- Un contrôle technique couvrant le montage et l’éclairage doit être réalisé et signé. La personne chargée du contrôle a seulement annoncé qu’elle pourrait passer jeudi soir ; ni sa venue ni la signature ne sont confirmées. La vérification des supports par les bénévoles ne remplace pas ce contrôle. La signature obtenue l’an dernier pour une autre salle ne vaut pas non plus pour cette exposition.
- Deux bénévoles d’accueil doivent être présents vendredi matin. Le second n’a pas encore accepté ce créneau. Une personne inscrite pour vendredi après-midi ne peut pas être comptée pour le matin.

L’accrochage terminé et les cartels imprimés ne suffisent donc pas à autoriser l’ouverture. Les éléments budgétaires ne dispensent d’aucune de ces conditions.

Jeudi, les bénévoles peuvent entrer pour le rangement et les essais de lumière, sans public ni vente. Cette autorisation de préparation n’autorise pas l’ouverture de l’exposition. La décision doit reposer sur les conditions effectivement remplies, et non sur une visite promise ou une inscription à un autre créneau. Si l’ouverture est décalée, les invitations annonçant vendredi à 9 h peuvent être remplacées.
```

### full: pass

```text
Pas encore : selon la note, l’ouverture vendredi à 9 h reste conditionnée à deux exigences qui ne sont pas confirmées.

- **Un contrôle technique réalisé et signé avant l’ouverture**, couvrant le montage et l’éclairage. La visite annoncée pour jeudi soir reste incertaine, tout comme la signature. La vérification des supports par les bénévoles ne remplace pas ce contrôle ; la signature obtenue l’an dernier pour une autre salle ne vaut pas non plus pour cette exposition.
- **La présence de deux bénévoles d’accueil vendredi matin.** Le second bénévole n’a pas encore accepté ce créneau. La personne inscrite pour l’après-midi ne peut pas être comptée pour le matin.

L’accrochage terminé et les cartels imprimés ne suffisent donc pas à autoriser l’ouverture. Les préparatifs du jeudi peuvent se dérouler avec les bénévoles, sans public ni vente, mais l’autorisation d’entrer pour préparer la salle n’autorise pas son ouverture au public. Le budget ne dispense d’aucune de ces conditions.

La décision doit reposer sur les conditions effectivement remplies, et non sur une visite promise ou une inscription à un autre créneau. Si l’ouverture est décalée, les invitations annonçant vendredi à 9 h peuvent être remplacées.
```

### ultra: pass

```text
Pas encore : selon la note, l’ouverture vendredi à 9 h reste conditionnelle. Deux exigences doivent être effectivement remplies avant l’accueil du public :

- Un contrôle technique du montage et de l’éclairage, réalisé et signé. La visite envisagée jeudi soir n’est pas confirmée, ni la signature. La vérification des supports par les bénévoles et le contrôle signé l’an dernier dans une autre salle ne le remplacent pas.
- La présence de deux bénévoles d’accueil vendredi matin. Le second n’a pas encore accepté ce créneau ; une inscription pour l’après-midi ne compte pas pour le matin.

L’accrochage et les cartels sont prêts, mais cela ne suffit pas. Jeudi, les bénévoles peuvent ranger et tester l’éclairage, sans public ni vente : cette autorisation de préparation n’autorise pas l’ouverture.

Le budget ne dispense d’aucune de ces exigences. La décision doit reposer sur les conditions réellement remplies, pas sur une visite promise. Si l’ouverture est décalée, les invitations annonçant vendredi à 9 h peuvent être remplacées.
```

### off: pass

```text
L’ouverture vendredi matin n’est pas encore confirmée selon cette note. Elle sera possible uniquement si les deux conditions exigées sont effectivement remplies avant l’accueil du public :

- Un contrôle technique couvrant le montage et l’éclairage doit être réalisé et signé. La personne chargée du contrôle a seulement annoncé qu’elle pourrait passer jeudi soir ; ni sa venue ni la signature ne sont confirmées. La vérification des supports par les bénévoles et le contrôle signé l’an dernier dans une autre salle ne remplacent pas ce contrôle.
- Deux bénévoles d’accueil doivent être présents vendredi matin. Le second n’a pas encore accepté le créneau. La personne inscrite pour vendredi après-midi ne peut pas être comptée pour le matin.

L’accrochage terminé, les cartels imprimés et corrigés, le budget prévu et les invitations annonçant vendredi à 9 h ne dispensent pas de ces conditions. Les invitations peuvent être remplacées si l’ouverture est décalée.

Les préparatifs du jeudi restent autorisés sans public et sans vente, mais cette autorisation ne permet pas d’ouvrir l’exposition. La décision doit donc reposer sur le contrôle effectivement signé et la présence effective des deux bénévoles, et non sur une visite promise ou une inscription à un autre créneau.
```

## modes-fr-073 · long_technical

Source task:

> Rends cette procédure fictive plus facile à suivre pour une personne déjà formée. Conserve les commandes, leur ordre et les limites du contrôle. N’ajoute pas de commande.
> 
> Le dossier de travail est /opt/archives/session-6. Avant toute vérification, la personne doit fermer l’application de consultation pour éviter qu’elle ne modifie l’index pendant la copie. Il faut ensuite copier index.json dans le sous-dossier snapshot/. Cette copie sert de point de comparaison ; elle n’est pas une sauvegarde complète des documents. Les images et les fichiers audio ne sont pas copiés par cette opération.
> 
> Lancer ensuite scan_links --index index.json --report report.txt. Cette commande recherche les références qui ne pointent plus vers un fichier accessible. Elle ne répare rien et n’efface rien. Un rapport vide indique qu’aucune référence inaccessible n’a été trouvée pendant ce passage. Il ne prouve pas que les fichiers sont intacts, que leur contenu est exact ou que tous les droits d’accès sont corrects. Un fichier inaccessible à ce compte peut exister et être accessible à un autre compte.
> 
> Si la commande signale ERROR_LOCK, arrêter la procédure et conserver report.txt, même si ce fichier est partiel. Ne pas supprimer le verrou manuellement. Le service de support décidera de la suite après avoir examiné le contexte. Si aucune erreur de verrou n’apparaît, comparer le nombre de références du rapport avec celui de snapshot/index.json. Une différence doit être notée, sans corriger automatiquement l’index.
> 
> Enfin, enregistrer l’heure du passage en UTC et le nom du compte utilisé. Le nom d’une personne ne doit pas être déduit du seul nom de compte partagé. L’application peut être rouverte seulement après l’enregistrement du rapport et de ces informations. Cette procédure porte sur une vérification locale ; elle ne confirme pas l’état de la copie distante, qui suit un contrôle séparé.

### baseline: pass

````text
## Procédure de vérification locale

Dossier de travail : `/opt/archives/session-6`.

1. **Fermer l’application de consultation**, avant toute vérification, pour éviter qu’elle modifie l’index pendant la copie.

2. **Copier `index.json` dans `snapshot/`.** Cette copie constitue un point de comparaison, pas une sauvegarde complète : les images et les fichiers audio ne sont pas copiés.

3. **Lancer la commande :**
   ```text
   scan_links --index index.json --report report.txt
   ```
   Elle recherche les références vers des fichiers inaccessibles. Elle ne répare et n’efface rien.

4. **Vérifier la présence de `ERROR_LOCK`.**
   - Si cette erreur apparaît : arrêter la procédure et conserver `report.txt`, même partiel. Ne pas supprimer le verrou manuellement. Le support décidera de la suite après examen du contexte.
   - Sinon : comparer le nombre de références du rapport avec celui de `snapshot/index.json`. Noter toute différence, sans corriger automatiquement l’index.

5. **Enregistrer le rapport, l’heure du passage en UTC et le nom du compte utilisé.** Ne pas déduire l’identité d’une personne du seul nom d’un compte partagé.

6. **Rouvrir l’application seulement après cet enregistrement.**

## Limites du contrôle
Un rapport vide signifie seulement qu’aucune référence inaccessible n’a été trouvée pendant ce passage. Il ne garantit ni l’intégrité des fichiers, ni l’exactitude de leur contenu, ni la conformité de tous les droits d’accès. Un fichier inaccessible au compte utilisé peut exister et être accessible à un autre compte.

Cette vérification est locale : elle ne confirme pas l’état de la copie distante, qui fait l’objet d’un contrôle séparé.
````

### lite: pass

```text
Dossier de travail : /opt/archives/session-6.

1. Avant toute vérification, fermer l’application de consultation pour éviter qu’elle ne modifie l’index pendant la copie. Copier ensuite index.json dans le sous-dossier snapshot/.

   Cette copie sert de point de comparaison. Ce n’est pas une sauvegarde complète des documents : les images et les fichiers audio ne sont pas copiés.

2. Lancer :

   `scan_links --index index.json --report report.txt`

   La commande recherche les références qui ne pointent plus vers un fichier accessible. Elle ne répare rien et n’efface rien.

   Un rapport vide signifie qu’aucune référence inaccessible n’a été trouvée pendant ce passage. Il ne prouve pas que les fichiers sont intacts, que leur contenu est exact ou que tous les droits d’accès sont corrects. Un fichier inaccessible au compte utilisé peut exister et être accessible à un autre compte.

3. Si la commande signale `ERROR_LOCK`, arrêter la procédure et conserver report.txt, même s’il est partiel. Ne pas supprimer le verrou manuellement. Le service de support décidera de la suite après examen du contexte.

   Si aucune erreur de verrou n’apparaît, comparer le nombre de références du rapport avec celui de snapshot/index.json. Noter toute différence, sans corriger automatiquement l’index.

4. Enregistrer l’heure du passage en UTC et le nom du compte utilisé. Ne pas déduire le nom d’une personne du seul nom d’un compte partagé.

5. Rouvrir l’application seulement après l’enregistrement du rapport et de ces informations.

Cette procédure vérifie uniquement l’état local. Elle ne confirme pas l’état de la copie distante, qui fait l’objet d’un contrôle séparé.
```

### full: pass

````text
## Procédure

Dossier de travail : `/opt/archives/session-6`.

1. **Fermer l’application de consultation avant toute vérification**, pour éviter qu’elle ne modifie l’index pendant la copie.
2. Copier `index.json` dans le sous-dossier `snapshot/`. Cette copie sert de point de comparaison, pas de sauvegarde complète des documents : elle ne copie ni les images ni les fichiers audio.
3. Lancer :
   ```
   scan_links --index index.json --report report.txt
   ```
   Cette commande recherche les références qui ne pointent plus vers un fichier accessible. Elle ne répare et n’efface rien.
4. **Si la commande signale `ERROR_LOCK`, arrêter la procédure.** Conserver `report.txt`, même partiel. Ne pas supprimer le verrou manuellement. Le service de support décidera de la suite après examen du contexte.
5. Si aucune erreur de verrou n’apparaît, comparer le nombre de références du rapport avec celui de `snapshot/index.json`. Noter toute différence, sans corriger automatiquement l’index.
6. Enregistrer l’heure du passage en UTC et le nom du compte utilisé. Ne pas déduire le nom d’une personne du seul nom d’un compte partagé.
7. Rouvrir l’application seulement après l’enregistrement du rapport et de ces informations.

## Limites du contrôle

Un rapport vide signifie qu’aucune référence inaccessible n’a été trouvée pendant ce passage. Il ne prouve ni que les fichiers sont intacts, ni que leur contenu est exact, ni que tous les droits d’accès sont corrects. Un fichier inaccessible au compte utilisé peut exister et être accessible à un autre compte.

Cette vérification est locale. Elle ne confirme pas l’état de la copie distante, qui fait l’objet d’un contrôle séparé.
````

### ultra: pass

```text
Dossier de travail : /opt/archives/session-6.

1. Avant toute vérification, fermer l’application de consultation pour empêcher qu’elle modifie l’index pendant la copie.
2. Copier index.json dans snapshot/. Cette copie sert de comparaison, pas de sauvegarde complète : elle ne copie ni les images ni les fichiers audio.
3. Lancer scan_links --index index.json --report report.txt.
   La commande recherche les références vers des fichiers inaccessibles. Elle ne répare et n’efface rien. Un rapport vide signifie seulement qu’aucune référence inaccessible n’a été trouvée pendant ce passage : il ne garantit ni l’intégrité des fichiers, ni l’exactitude de leur contenu, ni la validité de tous les droits d’accès. Un fichier inaccessible au compte utilisé peut exister et être accessible à un autre compte.
4. Si ERROR_LOCK apparaît, arrêter la procédure et conserver report.txt, même partiel. Ne pas supprimer le verrou manuellement. Le support décidera de la suite après examen du contexte.
5. Sans erreur de verrou, comparer le nombre de références du rapport à celui de snapshot/index.json. Noter toute différence, sans corriger automatiquement l’index.
6. Enregistrer le rapport, l’heure du passage en UTC et le nom du compte utilisé. Ne pas déduire l’identité d’une personne du seul nom d’un compte partagé.
7. Rouvrir l’application seulement après l’enregistrement du rapport et de ces informations.

Cette vérification est locale. Elle ne confirme pas l’état de la copie distante, soumis à un contrôle séparé.
```

### off: pass

```text
## Procédure de vérification locale

Dossier de travail : `/opt/archives/session-6`.

1. **Fermer l’application de consultation avant toute vérification.** Cela évite qu’elle modifie l’index pendant la copie.

2. **Copier `index.json` dans le sous-dossier `snapshot/`.** Cette copie sert de point de comparaison. Ce n’est pas une sauvegarde complète des documents : les images et les fichiers audio ne sont pas copiés.

3. **Lancer la commande :**

   `scan_links --index index.json --report report.txt`

   Elle recherche les références qui ne pointent plus vers un fichier accessible. Elle ne répare et n’efface rien.

   Un rapport vide signifie qu’aucune référence inaccessible n’a été trouvée pendant ce passage. Il ne garantit ni l’intégrité des fichiers, ni l’exactitude de leur contenu, ni la validité de tous les droits d’accès. Un fichier inaccessible au compte utilisé peut exister et être accessible à un autre compte.

4. **Vérifier si la commande signale `ERROR_LOCK`.**

   - Si oui, arrêter la procédure et conserver `report.txt`, même s’il est partiel. Ne pas supprimer le verrou manuellement. Le service de support décidera de la suite après examen du contexte.
   - Sinon, comparer le nombre de références du rapport avec celui de `snapshot/index.json`. Noter toute différence, sans corriger automatiquement l’index.

5. **Enregistrer l’heure du passage en UTC et le nom du compte utilisé.** Ne pas déduire le nom d’une personne du seul nom d’un compte partagé.

6. **Rouvrir l’application seulement après avoir enregistré le rapport et ces informations.**

Cette vérification est locale. Elle ne confirme pas l’état de la copie distante, qui fait l’objet d’un contrôle séparé.
```

## modes-fr-074 · long_conflicting_notes

Source task:

> Fais une synthèse pour la réunion, en distinguant les points concordants des points non résolus. Tout ce qui suit appartient à un projet fictif ; ne cherche pas à compléter les notes avec une source extérieure.
> 
> Le projet concerne le transfert d’une collection de maquettes vers un local provisoire. Le courriel de lundi annonce 38 caisses à transporter. Le tableau de mardi en prévoit 40. Le tableau ajoute deux lignes intitulées « matériel d’emballage », mais personne n’a confirmé si ces lignes correspondent à des caisses supplémentaires ou à du matériel déjà rangé dans les 38 caisses. Les deux documents indiquent un trajet unique avec le même transporteur.
> 
> Le courriel fixe l’enlèvement au 11 avril à 8 h. Le tableau porte la date du 12 avril à 8 h. Le transporteur a accusé réception des deux documents sans confirmer lequel remplace l’autre. Le message le plus récent n’est donc pas, à lui seul, une confirmation de la date. Les personnes chargées de l’accueil ont réservé les deux matinées à titre provisoire ; cela ne signifie pas que deux enlèvements auront lieu.
> 
> L’offre signée indique 540 € hors taxes pour un trajet avec au plus 38 caisses. Le tableau budgétaire indique 590 € hors taxes, mais ne cite aucune nouvelle offre. Il est possible que les 50 € couvrent un supplément pour les deux caisses, mais cette explication n’a pas été vérifiée. Le budget réservé est de 650 € hors taxes ; ce plafond ne valide pas le montant facturé.
> 
> Les maquettes fragiles doivent être marquées avant le chargement. Cette consigne figure dans les deux documents. Nora a terminé la liste des objets fragiles ; les étiquettes n’ont pas encore été posées. Le changement d’adresse est confirmé, mais l’équipe n’a pas encore transmis le code d’accès du local au transporteur. La réunion doit clarifier le nombre de caisses, la date et le prix, sans présenter les hypothèses comme des accords déjà obtenus.

### baseline: pass

```text
## Points concordants
- Les deux documents prévoient un seul trajet avec le même transporteur.
- Le changement d’adresse est confirmé.
- Les maquettes fragiles doivent être marquées avant le chargement. Nora a terminé leur liste, mais les étiquettes restent à poser.

## Points non résolus
- **Nombre de caisses :** le courriel de lundi annonce 38 caisses, contre 40 dans le tableau de mardi. Les deux lignes « matériel d’emballage » pourraient désigner des caisses supplémentaires ou du matériel déjà inclus dans les 38 ; rien ne le confirme.
- **Date :** le courriel indique le 11 avril à 8 h, le tableau le 12 avril à 8 h. Le transporteur a reçu les deux documents sans confirmer lequel prévaut. Le document le plus récent ne suffit donc pas à fixer la date. Les deux matinées réservées pour l’accueil sont provisoires et ne signifient pas deux enlèvements.
- **Prix :** l’offre signée prévoit 540 € HT pour un trajet avec au plus 38 caisses. Le tableau budgétaire mentionne 590 € HT sans nouvelle offre. L’hypothèse d’un supplément de 50 € pour deux caisses n’est pas vérifiée. Le budget réservé de 650 € HT ne valide pas le montant facturé.
- **Accès au local :** le code n’a pas encore été transmis au transporteur.

La réunion doit clarifier le nombre de caisses, la date et le prix, en distinguant les accords confirmés des hypothèses. La pose des étiquettes et la transmission du code d’accès restent à effectuer.
```

### lite: pass

```text
Points concordants

Le transfert de la collection de maquettes vers un local provisoire prévoit un trajet unique avec le même transporteur. Les deux documents exigent de marquer les maquettes fragiles avant le chargement. Nora a terminé la liste des objets fragiles, mais les étiquettes n’ont pas encore été posées.

Le changement d’adresse est confirmé. Le code d’accès du local n’a toutefois pas encore été transmis au transporteur.

Points non résolus

- Nombre de caisses : le courriel de lundi annonce 38 caisses ; le tableau de mardi en prévoit 40. Le tableau ajoute deux lignes « matériel d’emballage », sans confirmation qu’il s’agit de caisses supplémentaires plutôt que de matériel déjà rangé dans les 38 caisses.
- Date d’enlèvement : le courriel indique le 11 avril à 8 h ; le tableau, le 12 avril à 8 h. Le transporteur a accusé réception des deux documents sans confirmer lequel remplace l’autre. Le document le plus récent ne confirme donc pas, à lui seul, la date. Les deux matinées sont réservées provisoirement par les personnes chargées de l’accueil ; cela ne signifie pas que deux enlèvements sont prévus.
- Prix : l’offre signée prévoit 540 € hors taxes pour un trajet avec au plus 38 caisses. Le tableau budgétaire indique 590 € hors taxes sans citer de nouvelle offre. Les 50 € pourraient correspondre à un supplément pour deux caisses, mais cette explication n’est pas vérifiée. Le budget réservé de 650 € hors taxes constitue un plafond, pas une validation du montant facturé.

La réunion doit clarifier le nombre de caisses, la date et le prix. Les hypothèses ne doivent pas être présentées comme des accords déjà obtenus.
```

### full: pass

```text
## Synthèse pour la réunion

Le transfert de la collection de maquettes vers un local provisoire est prévu, mais **le nombre de caisses, la date d’enlèvement et le prix restent à clarifier**.

### Points concordants ou confirmés

- Le courriel de lundi et le tableau de mardi prévoient un trajet unique avec le même transporteur.
- Les deux documents exigent le marquage des maquettes fragiles avant le chargement. Nora a terminé la liste des objets fragiles ; les étiquettes n’ont pas encore été posées.
- Le changement d’adresse est confirmé. L’équipe n’a toutefois pas encore transmis le code d’accès du local au transporteur.

### Points non résolus

- **Nombre de caisses :** le courriel annonce 38 caisses ; le tableau en prévoit 40. Ses deux lignes « matériel d’emballage » pourraient correspondre à des caisses supplémentaires ou à du matériel déjà contenu dans les 38 caisses. Aucune interprétation n’est confirmée.
- **Date :** le courriel fixe l’enlèvement au 11 avril à 8 h ; le tableau indique le 12 avril à 8 h. Le transporteur a accusé réception des deux documents sans confirmer lequel remplace l’autre. Le document le plus récent ne confirme donc pas, à lui seul, la date. Les deux matinées réservées provisoirement par les personnes chargées de l’accueil ne signifient pas que deux enlèvements auront lieu.
- **Prix :** l’offre signée prévoit 540 € hors taxes pour un trajet avec au plus 38 caisses. Le tableau budgétaire indique 590 € hors taxes, sans citer de nouvelle offre. Les 50 € supplémentaires pourraient couvrir deux caisses de plus, mais cette explication n’a pas été vérifiée. Le budget réservé de 650 € hors taxes ne valide pas le montant facturé.

La réunion doit clarifier ces trois points sans présenter les hypothèses comme des accords déjà obtenus.
```

### ultra: pass

```text
Le transfert de la collection de maquettes vers le local provisoire comporte trois points à clarifier : le nombre de caisses, la date et le prix.

Points concordants
- Les deux documents prévoient un trajet unique avec le même transporteur.
- Les maquettes fragiles doivent être marquées avant le chargement. Nora a terminé leur liste ; les étiquettes ne sont pas encore posées.
- Le changement d’adresse est confirmé. L’équipe n’a pas encore transmis le code d’accès du local au transporteur.

Points non résolus
- Nombre de caisses : le courriel de lundi en annonce 38, le tableau de mardi 40. Les deux lignes « matériel d’emballage » du tableau pourraient désigner des caisses supplémentaires ou du matériel déjà inclus dans les 38 ; rien ne le confirme.
- Date : le courriel fixe l’enlèvement au 11 avril à 8 h, le tableau au 12 avril à 8 h. Le transporteur a accusé réception des deux sans confirmer lequel remplace l’autre. Le document le plus récent ne confirme donc pas, à lui seul, la date. Les deux matinées réservées provisoirement par l’accueil ne signifient pas deux enlèvements.
- Prix : l’offre signée prévoit 540 € hors taxes pour un trajet avec au plus 38 caisses. Le tableau budgétaire indique 590 € hors taxes sans nouvelle offre citée. L’hypothèse d’un supplément de 50 € pour deux caisses reste non vérifiée. Le budget réservé de 650 € hors taxes ne valide pas le montant facturé.

La réunion doit clarifier ces trois écarts sans présenter les hypothèses comme des accords.
```

### off: pass

```text
## Points concordants

- Le transfert de la collection de maquettes vers un local provisoire prévoit un trajet unique avec le même transporteur dans les deux documents.
- Le changement d’adresse est confirmé. Le code d’accès du local n’a toutefois pas encore été transmis au transporteur par l’équipe.
- Les maquettes fragiles doivent être marquées avant le chargement : cette consigne figure dans les deux documents. Nora a terminé la liste des objets fragiles, mais les étiquettes ne sont pas encore posées.

## Points non résolus

**Nombre de caisses.** Le courriel de lundi annonce 38 caisses ; le tableau de mardi en prévoit 40. Ses deux lignes « matériel d’emballage » pourraient correspondre à des caisses supplémentaires ou à du matériel déjà contenu dans les 38 caisses. Personne n’a confirmé l’interprétation.

**Date d’enlèvement.** Le courriel indique le 11 avril à 8 h ; le tableau, le 12 avril à 8 h. Le transporteur a accusé réception des deux documents sans préciser lequel remplace l’autre. Le document le plus récent ne suffit donc pas à confirmer la date. Les deux matinées ont été réservées provisoirement par les personnes chargées de l’accueil ; cela ne signifie pas que deux enlèvements sont prévus.

**Prix.** L’offre signée prévoit 540 € hors taxes pour un trajet avec au plus 38 caisses. Le tableau budgétaire indique 590 € hors taxes sans citer de nouvelle offre. Les 50 € supplémentaires pourraient correspondre à deux caisses de plus, mais cette explication n’a pas été vérifiée. Le budget réservé de 650 € hors taxes constitue un plafond, pas une validation du montant facturé.

La réunion doit clarifier le nombre de caisses, la date d’enlèvement et le prix, en distinguant les confirmations des hypothèses.
```

## modes-fr-075 · long_policy

Source task:

> Simplifie ce règlement fictif pour les participants d’un atelier de céramique. Il faut conserver les permissions, les obligations et les exceptions ; ne donne pas d’avis juridique.
> 
> L’inscription réserve une place pour quatre séances. Le participant peut demander à déplacer une seule séance, à condition de prévenir au moins 48 heures avant son début et qu’une place soit disponible dans un autre groupe du même cycle. Une demande reçue à temps ne garantit pas le déplacement. Si aucune place n’est disponible, la séance initiale reste réservée. Il n’est pas possible de transférer cette place à une autre personne sans l’accord écrit de l’association.
> 
> Si l’association annule une séance, elle doit proposer une séance de remplacement. Le participant peut refuser cette proposition et recevoir le remboursement de la séance annulée. Cette possibilité ne s’applique pas à une absence du participant, sauf si l’association a accepté par écrit une dérogation particulière. Une dérogation donnée pour une séance ne vaut pas automatiquement pour les suivantes.
> 
> Les outils communs peuvent être utilisés sur place pendant les séances. Ils ne peuvent pas être emportés, même pour terminer une pièce commencée au cours. Le participant doit inscrire son nom sur sa boîte personnelle et ranger les outils communs avant de partir. Le rangement ne dispense pas de signaler un outil abîmé ; le signalement sert au suivi et ne constitue pas à lui seul une reconnaissance de responsabilité.
> 
> Les pièces sont conservées pendant six semaines après la dernière séance. L’association doit envoyer un rappel avant la fin de ce délai. Le règlement ne précise pas de procédure si le rappel n’a pas été envoyé ; il faut laisser ce point ouvert plutôt que d’en inventer une. Les photos d’une pièce peuvent être utilisées dans le bulletin uniquement avec l’accord du participant. L’accord pour une photo ne couvre pas toutes les photos futures et peut être refusé sans perte de la place à l’atelier.

### baseline: pass

```text
## Inscription et déplacement d’une séance
- Votre inscription réserve une place pour quatre séances.
- Vous pouvez demander à déplacer une seule séance, en prévenant au moins 48 heures avant son début. Une place doit être disponible dans un autre groupe du même cycle.
- Même faite à temps, la demande ne garantit pas le déplacement. Sans place disponible, votre séance initiale reste réservée.
- Vous ne pouvez pas transférer votre place à quelqu’un d’autre sans l’accord écrit de l’association.

## Annulation et absence
- Si l’association annule une séance, elle doit vous proposer une séance de remplacement.
- Vous pouvez refuser ce remplacement et obtenir le remboursement de la séance annulée.
- Cette possibilité ne s’applique pas à votre absence, sauf dérogation particulière acceptée par écrit par l’association. Une dérogation pour une séance ne s’applique pas automatiquement aux suivantes.

## Outils et rangement
- Vous pouvez utiliser les outils communs sur place pendant les séances, mais pas les emporter, même pour terminer une pièce commencée au cours.
- Inscrivez votre nom sur votre boîte personnelle et rangez les outils communs avant de partir.
- Signalez tout outil abîmé, même si vous avez rangé. Ce signalement permet le suivi ; à lui seul, il ne signifie pas que vous reconnaissez une responsabilité.

## Conservation des pièces
- Les pièces sont conservées pendant six semaines après la dernière séance.
- L’association doit envoyer un rappel avant la fin de ce délai.
- Le règlement ne précise pas ce qui se passe si le rappel n’est pas envoyé : ce point reste ouvert.

## Photos
- Une photo de votre pièce peut être utilisée dans le bulletin uniquement avec votre accord.
- Votre accord pour une photo ne vaut pas pour toutes les photos futures.
- Vous pouvez refuser sans perdre votre place à l’atelier.
```

### lite: pass

```text
Inscription et déplacement d’une séance

L’inscription réserve une place pour quatre séances. Vous pouvez demander à déplacer une seule séance si vous prévenez au moins 48 heures avant son début et si une place est disponible dans un autre groupe du même cycle.

Une demande faite à temps ne garantit pas le déplacement. Si aucune place n’est disponible, votre séance initiale reste réservée. Vous ne pouvez pas transférer cette place à une autre personne sans l’accord écrit de l’association.

Annulation et absence

Si l’association annule une séance, elle doit proposer une séance de remplacement. Vous pouvez refuser cette proposition et recevoir le remboursement de la séance annulée.

Cette possibilité ne s’applique pas à votre absence, sauf si l’association a accepté par écrit une dérogation particulière. Une dérogation accordée pour une séance ne s’applique pas automatiquement aux suivantes.

Utilisation et rangement des outils

Vous pouvez utiliser les outils communs sur place pendant les séances. Vous ne pouvez pas les emporter, même pour terminer une pièce commencée au cours.

Vous devez inscrire votre nom sur votre boîte personnelle et ranger les outils communs avant de partir. Vous devez aussi signaler tout outil abîmé : le rangement ne remplace pas ce signalement. Le signalement sert au suivi et ne constitue pas, à lui seul, une reconnaissance de responsabilité.

Conservation des pièces

Les pièces sont conservées pendant six semaines après la dernière séance. L’association doit envoyer un rappel avant la fin de ce délai. Le règlement ne précise pas la procédure si ce rappel n’a pas été envoyé ; ce point reste ouvert.

Photos

Les photos d’une pièce peuvent être utilisées dans le bulletin uniquement avec votre accord. L’accord donné pour une photo ne couvre pas toutes les photos futures. Vous pouvez refuser sans perdre votre place à l’atelier.
```

### full: pass

```text
## Inscription et déplacement d’une séance

L’inscription réserve une place pour quatre séances.

Vous pouvez demander à déplacer une seule séance si vous prévenez au moins 48 heures avant son début et si une place est disponible dans un autre groupe du même cycle. Une demande faite à temps ne garantit pas le déplacement. Sans place disponible, votre séance initiale reste réservée.

Vous ne pouvez pas transférer votre place à une autre personne sans l’accord écrit de l’association.

## Annulation et absence

Si l’association annule une séance, elle doit proposer une séance de remplacement. Vous pouvez la refuser et obtenir le remboursement de la séance annulée.

Cette possibilité ne s’applique pas à votre absence, sauf dérogation particulière acceptée par écrit par l’association. Une dérogation pour une séance ne s’applique pas automatiquement aux suivantes.

## Utilisation et rangement des outils

Vous pouvez utiliser les outils communs sur place pendant les séances. Vous ne pouvez pas les emporter, même pour terminer une pièce commencée au cours.

Vous devez inscrire votre nom sur votre boîte personnelle et ranger les outils communs avant de partir. Vous devez aussi signaler tout outil abîmé : le rangement ne remplace pas ce signalement. Celui-ci sert au suivi et ne constitue pas, à lui seul, une reconnaissance de responsabilité.

## Conservation des pièces

Les pièces sont conservées pendant six semaines après la dernière séance. L’association doit envoyer un rappel avant la fin de ce délai.

Le règlement ne précise pas la procédure à suivre si ce rappel n’a pas été envoyé ; ce point reste ouvert.

## Photos

Les photos d’une pièce peuvent être utilisées dans le bulletin uniquement avec votre accord. L’accord pour une photo ne couvre pas toutes les photos futures. Vous pouvez le refuser sans perdre votre place à l’atelier.
```

### ultra: pass

```text
Inscription et déplacement
Votre inscription réserve une place pour quatre séances. Vous pouvez demander à déplacer une seule séance si vous prévenez au moins 48 heures avant son début et si une place est disponible dans un autre groupe du même cycle. Une demande faite à temps ne garantit pas le déplacement. Sans place disponible, votre séance initiale reste réservée. Le transfert de votre place à une autre personne exige l’accord écrit de l’association.

Annulation et absence
Si l’association annule une séance, elle doit proposer une séance de remplacement. Vous pouvez la refuser et obtenir le remboursement de la séance annulée. Cette possibilité ne s’applique pas à votre absence, sauf dérogation particulière acceptée par écrit par l’association. Une dérogation pour une séance ne s’étend pas automatiquement aux suivantes.

Outils et rangement
Vous pouvez utiliser les outils communs sur place pendant les séances, mais pas les emporter, même pour terminer une pièce commencée au cours. Vous devez inscrire votre nom sur votre boîte personnelle et ranger les outils communs avant de partir. Vous devez aussi signaler tout outil abîmé : le rangement ne remplace pas ce signalement. Celui-ci sert au suivi et ne constitue pas, à lui seul, une reconnaissance de responsabilité.

Conservation des pièces
Les pièces sont conservées six semaines après la dernière séance. L’association doit envoyer un rappel avant la fin de ce délai. Le règlement ne précise pas la procédure si ce rappel n’a pas été envoyé ; ce point reste ouvert.

Photos
L’utilisation de photos de votre pièce dans le bulletin exige votre accord. L’accord pour une photo ne couvre pas toutes les photos futures. Vous pouvez refuser sans perdre votre place à l’atelier.
```

### off: pass

```text
## Inscription et déplacement d’une séance

Votre inscription réserve une place pour quatre séances.

Vous pouvez demander à déplacer une seule séance si vous prévenez au moins 48 heures avant son début et si une place est disponible dans un autre groupe du même cycle. Une demande faite dans les délais ne garantit pas le déplacement. Sans place disponible, votre séance initiale reste réservée.

Vous ne pouvez pas transférer votre place à une autre personne sans l’accord écrit de l’association.

## Annulation et absence

Si l’association annule une séance, elle doit proposer une séance de remplacement. Vous pouvez la refuser et obtenir le remboursement de la séance annulée.

Cette possibilité ne s’applique pas à votre absence, sauf dérogation particulière acceptée par écrit par l’association. Une dérogation pour une séance ne s’applique pas automatiquement aux suivantes.

## Utilisation et rangement des outils

Vous pouvez utiliser les outils communs sur place pendant les séances. Vous ne pouvez pas les emporter, même pour terminer une pièce commencée au cours.

Vous devez inscrire votre nom sur votre boîte personnelle et ranger les outils communs avant de partir. Vous devez aussi signaler tout outil abîmé : le rangement ne remplace pas ce signalement. Signaler un outil abîmé sert au suivi et ne constitue pas, à lui seul, une reconnaissance de responsabilité.

## Conservation des pièces

Les pièces sont conservées pendant six semaines après la dernière séance. L’association doit envoyer un rappel avant la fin de ce délai.

Le règlement ne précise pas ce qui se passe si le rappel n’a pas été envoyé. Ce point reste ouvert.

## Photos

Les photos d’une pièce peuvent être utilisées dans le bulletin uniquement avec votre accord. Votre accord pour une photo ne couvre pas toutes les photos futures. Vous pouvez refuser sans perdre votre place à l’atelier.
```

## modes-fr-076 · long_calculation

Source task:

> Réponds uniquement à la demande financière à la fin de cette note : quel montant reste-t-il sur l’enveloppe de fournitures après les dépenses confirmées, et quelle marge resterait-il si l’achat proposé était approuvé ? Montre les calculs. Les autres informations expliquent le contexte, mais ne sont pas des achats à ajouter.
> 
> Une petite équipe prépare une journée de fabrication de carnets. L’enveloppe de fournitures est de 480 €. Les frais de location de la salle sont couverts par un autre budget et ne doivent pas être soustraits de cette enveloppe. Les recettes possibles de la journée ne sont pas encore connues ; aucun revenu attendu ne doit être ajouté au calcul.
> 
> Les dépenses confirmées sont les suivantes : 12 paquets de papier à 8 € chacun, 6 bouteilles de colle à 7 € chacune et 4 boîtes de pinces à 15 € chacune. La livraison de toute cette commande coûte 18 € une seule fois. Tous ces montants incluent les taxes. La facture est payée et aucune remise n’a été accordée. Les boîtes de pinces contiennent des quantités différentes, ce qui n’affecte pas leur prix dans ce calcul.
> 
> Un achat de 10 rouleaux de ruban à 9 € chacun a été proposé, avec un second frais de livraison de 12 €. Cette proposition n’est pas encore approuvée et ne figure pas dans les dépenses confirmées. Le fournisseur ne prévoit aucun frais supplémentaire dans l’offre. Il ne faut pas compter le ruban comme déjà acheté, ni l’oublier dans le scénario conditionnel.
> 
> Pour le déroulement de l’activité, deux tables ont été empruntées gratuitement et trois rallonges seront apportées par des bénévoles. Une personne a évoqué l’achat futur d’une perforatrice, sans prix ni demande formelle. Ces objets ne modifient pas le calcul demandé. Le bilan doit séparer le solde actuel du solde possible après le ruban, en gardant les euros et sans conclure que l’achat a été décidé.

### baseline: pass

```text
Dépenses confirmées :
- Papier : 12 × 8 € = 96 €
- Colle : 6 × 7 € = 42 €
- Pinces : 4 × 15 € = 60 €
- Livraison : 18 €

Total : 96 + 42 + 60 + 18 = 216 €.
Solde actuel : 480 − 216 = 264 €.

Si l’achat proposé était approuvé :
- Ruban : 10 × 9 € = 90 €
- Seconde livraison : 12 €
Soit 90 + 12 = 102 € supplémentaires.

Marge restante dans ce scénario : 264 − 102 = 162 €. L’achat n’est pas encore approuvé.
```

### lite: pass

```text
Dépenses confirmées :
- Papier : 12 × 8 € = 96 €
- Colle : 6 × 7 € = 42 €
- Pinces : 4 × 15 € = 60 €
- Livraison unique : 18 €

Total : 96 € + 42 € + 60 € + 18 € = 216 €.
Solde actuel : 480 € − 216 € = 264 €.

Si l’achat de ruban était approuvé :
- Ruban : 10 × 9 € = 90 €
- Seconde livraison : 12 €
- Coût supplémentaire : 90 € + 12 € = 102 €

Marge restante : 264 € − 102 € = 162 €.
L’achat de ruban n’est pas encore approuvé.
```

### full: pass

```text
Le solde actuel est de 264 €.

Dépenses confirmées :
- Papier : 12 × 8 € = 96 €
- Colle : 6 × 7 € = 42 €
- Pinces : 4 × 15 € = 60 €
- Livraison unique : 18 €

Total : 96 € + 42 € + 60 € + 18 € = 216 €.
Solde actuel : 480 € − 216 € = 264 €.

Si l’achat de ruban était approuvé :
- Ruban : 10 × 9 € = 90 €
- Seconde livraison : 12 €
- Coût supplémentaire : 90 € + 12 € = 102 €

La marge restante serait de 264 € − 102 € = 162 €. Cet achat n’est pas encore approuvé.
```

### ultra: pass

```text
Dépenses confirmées :
12 × 8 € + 6 × 7 € + 4 × 15 € + 18 € = 216 €.

Solde actuel : 480 € − 216 € = 264 €.

Achat proposé, livraison comprise : 10 × 9 € + 12 € = 102 €.

Si cet achat était approuvé, il resterait : 264 € − 102 € = 162 €.
```

### off: pass

```text
Dépenses confirmées :
- Papier : 12 × 8 € = 96 €
- Colle : 6 × 7 € = 42 €
- Pinces : 4 × 15 € = 60 €
- Livraison unique : 18 €

Total : 96 € + 42 € + 60 € + 18 € = 216 €.
Solde actuel : 480 € − 216 € = 264 €.

Si l’achat proposé était approuvé :
- Ruban : 10 × 9 € = 90 €
- Seconde livraison : 12 €

Coût supplémentaire : 90 € + 12 € = 102 €.
Marge restante : 264 € − 102 € = 162 €.

L’achat de ruban n’est pas encore approuvé ; le solde actuel reste donc de 264 €.
```

## modes-fr-077 · long_analysis

Source task:

> Explique si cette note suffit à choisir le nouveau formulaire pour tous les usagers. Donne une réponse directe et ses limites, sans proposer une étude détaillée ni inventer des résultats.
> 
> Le service fictif a testé un formulaire raccourci pendant trois jours. Vingt personnes l’ont utilisé et dix-huit ont terminé sans demander d’aide. Le formulaire habituel a été utilisé par vingt autres personnes la semaine précédente ; quatorze ont terminé sans aide. Les chiffres permettent de décrire 90 % et 70 % de réussite sans aide dans ces deux groupes. Ils ne proviennent pas d’une répartition aléatoire des personnes entre les formulaires.
> 
> Les personnes du premier groupe étaient déjà inscrites au service et connaissaient le type de justificatif demandé. Les personnes du second groupe venaient pour la première fois. Le premier groupe a utilisé des ordinateurs de bureau, le second un mélange de téléphones et d’ordinateurs. Le nombre exact de téléphones n’a pas été relevé. Le service a également simplifié l’affichage des consignes entre les deux semaines, indépendamment du formulaire.
> 
> Le formulaire raccourci ne comprend pas la rubrique destinée aux personnes agissant pour le compte d’un tiers. Personne dans son groupe n’avait besoin de cette rubrique. On ne sait donc pas si le formulaire convient à ces usagers. Aucun test avec lecteur d’écran n’a été effectué. Les temps individuels ont été notés, mais la note ne donne ni les valeurs ni leur moyenne ; on ne peut pas chiffrer un gain de temps à partir de ce document.
> 
> La responsable souhaite savoir ce qui a été observé, ce qui peut être une explication possible et ce qui reste inconnu. Elle n’a pas encore décidé de remplacer le formulaire. Un meilleur résultat observé dans un groupe n’est pas une preuve que tous les usagers réussiront mieux, ni que le changement de formulaire est l’unique cause de l’écart. La note doit rester utilisable sans masquer ces différences de population et de conditions.

### baseline: flagged

```text
Non, cette note ne suffit pas à choisir le nouveau formulaire pour tous les usagers.

Le résultat observé est meilleur dans le groupe ayant utilisé le formulaire raccourci : 18 personnes sur 20 ont terminé sans aide (90 %), contre 14 sur 20 (70 %) avec le formulaire habituel.

Mais ces petits groupes n’ont pas été répartis aléatoirement et leurs conditions diffèrent : usagers déjà inscrits contre nouveaux usagers, ordinateurs de bureau contre mélange de téléphones et d’ordinateurs, et consignes simplifiées entre les deux semaines. Ces différences peuvent expliquer une partie de l’écart ; on ne peut pas l’attribuer au seul formulaire.

L’adéquation aux personnes agissant pour un tiers reste inconnue, puisque la rubrique correspondante manque et qu’aucun participant n’en avait besoin. L’utilisation avec un lecteur d’écran n’a pas été testée. Enfin, aucun gain de temps ne peut être chiffré avec les données présentées. Le résultat est encourageant, mais ne prouve pas une amélioration pour tous les usagers.
```

Review notes: Les principales limites sont justes, mais l’état encore indécis du remplacement est omis. / Les principales limites sont conservées, mais le statut de la décision de remplacement est omis.

### lite: pass

```text
Non, cette note ne suffit pas à choisir le formulaire raccourci pour tous les usagers.

Pendant les trois jours de test, 18 personnes sur 20 ont terminé sans aide avec le formulaire raccourci, soit 90 %. La semaine précédente, 14 personnes sur 20 avaient terminé sans aide avec le formulaire habituel, soit 70 %. L’écart observé est de 20 points de pourcentage, mais les personnes n’ont pas été réparties aléatoirement entre les formulaires.

Plusieurs différences peuvent expliquer cet écart : le premier groupe était déjà inscrit et connaissait le justificatif demandé, tandis que le second venait pour la première fois. Le premier utilisait des ordinateurs de bureau ; le second, des téléphones et des ordinateurs, sans décompte exact des téléphones. L’affichage des consignes a aussi été simplifié entre les deux semaines, indépendamment du formulaire. On ne peut donc pas attribuer l’écart au seul formulaire.

Le formulaire raccourci omet la rubrique pour les personnes agissant pour un tiers. Aucun participant de son groupe n’en avait besoin : son adéquation à ces usagers reste inconnue. Aucun test avec lecteur d’écran n’a été effectué. Enfin, les temps ont été notés, mais leurs valeurs et leur moyenne ne figurent pas dans la note ; aucun gain de temps ne peut être chiffré.

Le meilleur résultat observé dans ce petit groupe ne prouve donc pas que tous les usagers réussiront mieux. Le remplacement n’a pas encore été décidé.
```

### full: pass

```text
Non. La note montre un meilleur résultat avec le formulaire raccourci dans le groupe testé, mais ne suffit pas à le choisir pour tous les usagers.

**Ce qui a été observé :** pendant trois jours, 18 personnes sur 20 ont terminé le formulaire raccourci sans aide, soit 90 %. La semaine précédente, 14 autres personnes sur 20 avaient terminé le formulaire habituel sans aide, soit 70 %. L’écart est de 20 points de pourcentage.

**Les explications possibles :** les personnes n’ont pas été réparties aléatoirement. Le premier groupe était déjà inscrit et connaissait le justificatif demandé ; le second découvrait le service. Le premier utilisait des ordinateurs de bureau, le second des téléphones et des ordinateurs, sans décompte exact des téléphones. L’affichage des consignes a aussi été simplifié entre les deux semaines, indépendamment du formulaire. Ces différences peuvent contribuer à l’écart : le formulaire n’en est pas nécessairement l’unique cause.

**Ce qui reste inconnu :** le formulaire raccourci omet la rubrique pour les personnes agissant pour un tiers, dont aucun participant de son groupe n’avait besoin. Son adéquation à ces usagers n’est donc pas établie. Aucun test avec lecteur d’écran n’a été effectué. Les temps individuels ont été notés, mais leurs valeurs et leur moyenne ne figurent pas dans la note : aucun gain de temps ne peut être chiffré.

Ces petits groupes et ces conditions différentes ne permettent pas de conclure que tous les usagers réussiront mieux. Le remplacement du formulaire n’est pas encore décidé.
```

### ultra: pass

```text
Non. La note montre un meilleur résultat dans le groupe ayant utilisé le formulaire raccourci, mais ne suffit pas à le choisir pour tous les usagers.

Observation : pendant trois jours, 18 personnes sur 20 ont terminé le formulaire raccourci sans aide, soit 90 %. La semaine précédente, 14 autres personnes sur 20 avaient terminé le formulaire habituel sans aide, soit 70 %. L’écart observé est de 20 points de pourcentage.

Explications possibles : les groupes n’ont pas été répartis au hasard. Le premier connaissait déjà le service et le justificatif demandé ; le second venait pour la première fois. Le premier utilisait des ordinateurs de bureau, le second des téléphones et des ordinateurs, sans décompte des téléphones. L’affichage des consignes a aussi été simplifié entre les deux semaines, indépendamment du formulaire. L’écart ne peut donc pas être attribué au seul formulaire.

Inconnues : le formulaire raccourci omet la rubrique pour les personnes agissant pour un tiers, dont aucun participant de son groupe n’avait besoin. Son adéquation à ces usagers reste inconnue. Aucun test avec lecteur d’écran n’a été effectué. Les temps ont été relevés, mais leurs valeurs et leur moyenne ne sont pas fournies : aucun gain de temps ne peut être chiffré.

Ces résultats ne prouvent pas que tous les usagers réussiront mieux. Le remplacement n’a pas encore été décidé.
```

### off: pass

```text
Non, cette note ne suffit pas à choisir le formulaire raccourci pour tous les usagers.

Ce qui a été observé : pendant les trois jours de test, 18 personnes sur 20 ont terminé le formulaire raccourci sans aide, soit 90 %. La semaine précédente, 14 personnes sur 20 avaient terminé le formulaire habituel sans aide, soit 70 %. L’écart observé est de 20 points de pourcentage.

Les explications possibles ne se limitent pas au formulaire. Sans répartition aléatoire, les groupes ne sont pas directement comparables : les premiers usagers étaient déjà inscrits et connaissaient le justificatif demandé, tandis que les seconds venaient pour la première fois. Les premiers utilisaient des ordinateurs de bureau ; les seconds, des téléphones et des ordinateurs, sans décompte précis des téléphones. L’affichage des consignes a aussi été simplifié entre les deux semaines, indépendamment du formulaire. Ces différences pourraient contribuer à l’écart, sans que la note permette de déterminer leur rôle respectif.

Ce qui reste inconnu : le formulaire raccourci omet la rubrique pour les personnes agissant pour un tiers, dont aucun participant au test n’avait besoin. Son adéquation à ces usagers n’est donc pas établie. Aucun test avec lecteur d’écran n’a été effectué. Enfin, les temps individuels ont été notés mais ne sont pas fournis, pas plus que leur moyenne : aucun gain de temps ne peut être chiffré.

Le résultat observé est meilleur dans le groupe ayant utilisé le formulaire raccourci, mais il ne prouve ni que ce formulaire en est l’unique cause, ni que tous les usagers réussiront mieux. Le remplacement n’a pas encore été décidé.
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

### baseline: pass

```text
Émile est arrivé sous la pluie, une boîte à chaussures contre lui. Il venait donner les boutons gardés pendant des années : une centaine, disait-il, certains en bois, d’autres en métal, parfois encore garnis d’un petit fil.

Il souhaitait conserver la boîte, qui portait une inscription de sa sœur. Salomé a posé un plateau pour recevoir les boutons, sans lire l’inscription à voix haute ni lui demander pourquoi il les apportait maintenant.

Une enfant a demandé à prendre un bouton bleu pour réparer la poche de son manteau. Émile a acquiescé, sans raconter à qui il avait appartenu.

La pluie avait cessé lorsqu’il est reparti avec sa boîte vide. Le plateau est resté sur la table, sans étiquette de prix : les boutons étaient offerts pour les réparations de l’atelier. Salomé a inscrit le don au registre, sans noter le nom de l’enfant.
```

### lite: pass

```text
Quand la porte s’est ouverte, la pluie faisait briller les manteaux sous la lampe. Émile tenait une boîte à chaussures contre lui. Il venait donner les boutons gardés pendant des années : une centaine, disait-il, sans les avoir comptés. Certains étaient en bois, d’autres en métal ; plusieurs portaient encore un petit fil.

Salomé lui a demandé s’il souhaitait garder la boîte. Oui : elle portait une inscription de sa sœur. Salomé a posé un plateau pour recevoir les boutons, sans lire l’inscription à voix haute ni lui demander pourquoi il les apportait seulement maintenant.

Une enfant a choisi un bouton bleu pour réparer la poche de son manteau. Elle a demandé la permission avant de le prendre. Émile a acquiescé, sans dire à qui le bouton avait appartenu. Personne ne l’a deviné à sa place.

La pluie a cessé avant la fermeture. Émile est reparti avec sa boîte vide. Le plateau est resté sur la table, sans étiquette de prix : les boutons étaient un don pour les réparations de l’atelier. Salomé l’a inscrit dans le registre, sans noter le nom de l’enfant.
```

### full: pass

```text
Sous la pluie, Émile est entré avec une boîte à chaussures contre lui. Il venait donner les boutons gardés pendant des années : une centaine, disait-il, sans les avoir comptés. Certains étaient en bois, d’autres en métal ; plusieurs portaient encore un petit fil.

Salomé lui a demandé s’il souhaitait garder la boîte. Oui : elle portait une inscription de sa sœur. Salomé a posé un plateau pour les boutons, sans lire l’inscription à voix haute ni demander pourquoi il les apportait maintenant.

Une enfant a choisi un bouton bleu pour réparer la poche de son manteau. Avant de le prendre, elle a demandé la permission. Émile a acquiescé. Il n’a pas dit à qui ce bouton avait appartenu, et personne ne l’a deviné à sa place.

La pluie avait cessé quand Émile est reparti avec sa boîte vide. Le plateau est resté sur la table, sans étiquette de prix : les boutons étaient un don pour les réparations de l’atelier. Salomé l’a inscrit au registre, sans noter le nom de l’enfant.
```

### ultra: flagged

```text
Quand Émile est entré, la pluie faisait briller les manteaux sous la lampe. Il ne venait rien chercher : il apportait les boutons gardés pendant des années dans une boîte à chaussures. Une centaine, disait-il, sans les avoir comptés. Certains étaient en bois, d’autres en métal ; plusieurs portaient encore un petit fil.

Salomé lui a demandé s’il voulait garder la boîte. Oui : elle portait une inscription de sa sœur. Elle a posé un plateau pour les boutons, sans lire l’inscription à voix haute ni lui demander pourquoi il les apportait maintenant.

Une enfant a demandé la permission de prendre un bouton bleu pour réparer la poche de son manteau. Émile a acquiescé. Il n’a pas dit à qui ce bouton avait appartenu ; personne ne l’a deviné à sa place.

La pluie avait cessé quand Émile est reparti avec sa boîte vide, avant la fermeture. Le plateau est resté sur la table, sans prix : les boutons étaient un don pour les réparations de l’atelier. Salomé l’a inscrit au registre, sans noter le nom de l’enfant.
```

Review notes: Les invariants sont conservés, mais l’heure relative du départ est affirmée sans appui. / Les invariants sont conservés, mais une précision chronologique non établie est ajoutée au départ.

### off: pass

```text
Quand Émile est entré, la pluie faisait briller les manteaux sous la lampe. Il tenait une boîte à chaussures contre lui, non pour chercher un objet, mais pour donner les boutons gardés pendant des années : une centaine, disait-il, sans les avoir comptés. Certains étaient en bois, d’autres en métal ; plusieurs portaient encore un petit fil.

Salomé lui a demandé s’il souhaitait garder la boîte. Oui : elle portait une inscription de sa sœur. Elle a posé un plateau pour les boutons, sans lire l’inscription à voix haute ni demander pourquoi il les apportait maintenant.

Une enfant a demandé la permission de prendre un bouton bleu pour réparer la poche de son manteau. Émile a acquiescé. Il n’a pas dit à qui ce bouton avait appartenu, et personne ne l’a deviné à sa place.

La pluie avait cessé quand Émile est reparti avec sa boîte vide. Le plateau est resté sur la table, sans étiquette de prix : les boutons étaient un don pour les réparations de l’atelier. Salomé l’a inscrit dans le registre, sans noter le nom de l’enfant.
```

## modes-fr-079 · long_uncertainty

Source task:

> Rédige un point de suivi pour la réunion de demain. Le lecteur doit comprendre l’état des faits et les hypothèses sans confondre le problème signalé avec sa cause. La note concerne un système fictif d’enregistrement de température ; aucune conclusion générale sur la sécurité des produits n’est demandée.
> 
> Pendant le passage de lundi, le fichier de suivi contient une interruption de 17 minutes, de 14 h 03 à 14 h 20. Le fichier reprend ensuite normalement. Les valeurs avant et après l’interruption sont comprises entre 3,8 °C et 4,2 °C. Ces valeurs ne prouvent pas ce qui s’est passé pendant la période sans enregistrement. Aucun second capteur n’était installé dans la même armoire.
> 
> L’équipe a trouvé un câble mal fixé mardi matin. Un câble mal fixé pourrait interrompre l’enregistrement, mais le document ne montre pas que ce câble s’est débranché lundi. La connexion a été resserrée. Depuis cette intervention, deux passages de 30 minutes chacun n’ont montré aucune interruption. Ces essais courts ne démontrent pas que le problème ne reviendra jamais. Ils portent seulement sur le comportement observé après l’intervention.
> 
> Une interruption du fichier ne signifie pas nécessairement une interruption de l’alimentation de l’armoire. Le témoin d’alimentation n’était pas enregistré à ce moment-là. Aucun contrôle du contenu de l’armoire n’est décrit dans cette note. Il ne faut donc ni affirmer que le contenu a été affecté, ni garantir qu’il ne l’a pas été. La note est limitée au système d’enregistrement.
> 
> Le technicien estime qu’une observation continue de 24 heures pourrait aider à vérifier la stabilité. Cette observation est proposée et n’a pas encore commencé. Aucune personne n’a été désignée pour l’assurer et aucune date de fin n’a été fixée. La réunion pourra discuter de cette proposition ; le point de suivi ne doit pas la présenter comme une mesure déjà décidée, ni attribuer la cause de l’incident au seul câble sur la base de la proximité dans le temps.

### baseline: pass

```text
Point de suivi — système d’enregistrement de température

Faits constatés : lundi, le fichier présente une interruption de 17 minutes, de 14 h 03 à 14 h 20, puis reprend normalement. Les valeurs avant et après sont comprises entre 3,8 °C et 4,2 °C ; elles ne renseignent pas sur la période sans enregistrement. Aucun second capteur n’était installé dans l’armoire.

Hypothèse et intervention : un câble mal fixé a été trouvé mardi matin, puis la connexion a été resserrée. Ce défaut pourrait interrompre l’enregistrement, mais rien ne démontre que le câble s’est débranché lundi ni qu’il est la cause de l’incident. Depuis l’intervention, deux passages de 30 minutes chacun n’ont montré aucune interruption. Ces observations courtes ne garantissent pas l’absence de récidive.

Limites : l’interruption du fichier ne prouve pas une coupure d’alimentation de l’armoire. Le témoin d’alimentation n’était pas enregistré et aucun contrôle du contenu n’est décrit. Cette note, limitée à l’enregistrement, ne permet donc ni d’affirmer que le contenu a été affecté ni de garantir le contraire.

À discuter demain : le technicien propose une observation continue de 24 heures pour vérifier la stabilité. Elle n’a pas commencé ; aucun responsable ni aucune date de fin n’ont été fixés.
```

### lite: pass

```text
Point de suivi pour la réunion de demain

Faits observés
Lundi, le fichier de suivi présente une interruption de 17 minutes, de 14 h 03 à 14 h 20, puis reprend normalement. Les valeurs avant et après sont comprises entre 3,8 °C et 4,2 °C. Elles ne permettent pas de connaître la température pendant l’interruption. Aucun second capteur n’était installé dans la même armoire.

Mardi matin, l’équipe a trouvé un câble mal fixé. La connexion a été resserrée. Depuis, deux passages de 30 minutes chacun n’ont montré aucune interruption. Ces essais courts décrivent le comportement après l’intervention, sans démontrer que le problème ne reviendra pas.

Hypothèse et limites
Un câble mal fixé pourrait interrompre l’enregistrement, mais rien dans le document ne montre qu’il s’est débranché lundi. La cause de l’incident n’est donc pas établie.

Une interruption du fichier ne signifie pas nécessairement une coupure de l’alimentation de l’armoire. Le témoin d’alimentation n’était pas enregistré et aucun contrôle du contenu n’est décrit. Cette note, limitée au système d’enregistrement, ne permet ni d’affirmer que le contenu a été affecté, ni de garantir le contraire.

Proposition à discuter
Le technicien estime qu’une observation continue de 24 heures pourrait aider à vérifier la stabilité. Elle n’a pas commencé, personne n’a été désigné pour l’assurer et aucune date de fin n’a été fixée. La réunion pourra discuter de cette proposition, qui n’est pas encore une mesure décidée.
```

### full: pass

```text
**Point de suivi pour la réunion de demain — système d’enregistrement de température**

**Constat.** Lundi, le fichier présente une interruption de 17 minutes, de 14 h 03 à 14 h 20, puis reprend normalement. Les valeurs avant et après sont comprises entre 3,8 °C et 4,2 °C. Elles ne permettent pas de connaître la température pendant l’interruption. Aucun second capteur n’était installé dans la même armoire.

**Hypothèse et intervention.** Un câble mal fixé a été trouvé mardi matin. Il pourrait expliquer une interruption de l’enregistrement, mais rien ne montre qu’il s’est débranché lundi. La connexion a été resserrée. Depuis, deux passages de 30 minutes chacun n’ont montré aucune interruption. Ces essais courts décrivent le comportement après l’intervention ; ils ne prouvent ni la cause de l’incident ni l’absence de récidive.

**Limites.** Une interruption du fichier ne signifie pas nécessairement une coupure d’alimentation de l’armoire. Le témoin d’alimentation n’était pas enregistré et aucun contrôle du contenu n’est décrit. Cette note, limitée au système d’enregistrement, ne permet donc ni d’affirmer que le contenu a été affecté ni de garantir le contraire.

**Proposition à discuter.** Le technicien estime qu’une observation continue de 24 heures pourrait aider à vérifier la stabilité. Elle n’a pas commencé et n’est pas encore décidée. Aucune personne n’a été désignée pour l’assurer et aucune date de fin n’a été fixée.
```

### ultra: pass

```text
Le suivi confirme une interruption de l’enregistrement, pas sa cause.

**Faits observés.** Lundi, le fichier présente une interruption de 17 minutes, de 14 h 03 à 14 h 20, puis reprend normalement. Les valeurs avant et après sont comprises entre 3,8 °C et 4,2 °C ; elles ne renseignent pas sur la période sans enregistrement. Aucun second capteur n’était installé dans la même armoire.

**Hypothèse et intervention.** Un câble mal fixé a été trouvé mardi matin, puis la connexion a été resserrée. Ce défaut pourrait interrompre l’enregistrement, mais rien ne montre que le câble s’est débranché lundi. Depuis l’intervention, deux passages de 30 minutes chacun n’ont montré aucune interruption. Ces essais courts décrivent le comportement observé, sans exclure une récidive ni confirmer la cause.

**Limites.** Une interruption du fichier ne signifie pas nécessairement une coupure d’alimentation de l’armoire. Le témoin d’alimentation n’était pas enregistré et aucun contrôle du contenu n’est décrit. Cette note porte uniquement sur l’enregistrement : elle ne permet ni d’affirmer que le contenu a été affecté ni de garantir le contraire.

**Proposition à discuter demain.** Le technicien estime qu’une observation continue de 24 heures pourrait aider à vérifier la stabilité. Elle n’est ni décidée ni commencée ; personne n’a été désigné pour l’assurer et aucune date de fin n’a été fixée.
```

### off: pass

```text
Point de suivi pour la réunion de demain — système d’enregistrement de température

Faits constatés
Le fichier de lundi présente une interruption de 17 minutes, de 14 h 03 à 14 h 20, puis reprend normalement. Les valeurs avant et après cette interruption sont comprises entre 3,8 °C et 4,2 °C. Elles ne permettent pas de connaître la température pendant la période sans enregistrement. Aucun second capteur n’était installé dans la même armoire.

Mardi matin, l’équipe a trouvé un câble mal fixé. La connexion a été resserrée. Depuis cette intervention, deux passages de 30 minutes chacun n’ont montré aucune interruption. Ces essais décrivent le comportement observé après l’intervention, mais ne garantissent pas l’absence de récidive.

Hypothèse et limites
Un câble mal fixé pourrait interrompre l’enregistrement. Toutefois, le document ne montre pas que ce câble s’est débranché lundi : la cause de l’incident n’est donc pas établie.

L’interruption du fichier ne signifie pas nécessairement que l’alimentation de l’armoire a été interrompue. Le témoin d’alimentation n’était pas enregistré, et aucun contrôle du contenu de l’armoire n’est décrit. Cette note, limitée au système d’enregistrement, ne permet ni d’affirmer que le contenu a été affecté, ni de garantir qu’il ne l’a pas été.

Proposition à discuter
Le technicien estime qu’une observation continue de 24 heures pourrait aider à vérifier la stabilité. Elle n’a pas encore commencé et n’est pas présentée comme une mesure décidée. Aucune personne n’a été désignée pour l’assurer et aucune date de fin n’a été fixée. La réunion pourra discuter de cette proposition.
```

## modes-fr-080 · scope

Source task:

> Réponds seulement à la question : faut-il payer pour emprunter une couverture ? Dans cet accueil fictif, les couvertures sont prêtées gratuitement, avec un dépôt remboursable de 5 €. Le dépôt est rendu lorsque la couverture revient ; ce n’est pas un prix de location.

### baseline: pass

```text
Le prêt est gratuit, mais il faut verser un dépôt de 5 €, rendu au retour de la couverture. Ce n’est pas un prix de location.
```

### lite: pass

```text
Le prêt est gratuit, mais il faut verser un dépôt de 5 €, rendu au retour de la couverture. Ce n’est pas un prix de location.
```

### full: pass

```text
L’emprunt est gratuit, mais il faut verser un dépôt de 5 €, rendu au retour de la couverture. Ce n’est pas un prix de location.
```

### ultra: pass

```text
Le prêt est gratuit, mais il faut verser un dépôt de 5 €, remboursé au retour de la couverture. Ce n’est pas un prix de location.
```

### off: pass

```text
Le prêt est gratuit, mais il faut verser un dépôt de 5 €, remboursé au retour de la couverture. Ce n’est pas un prix de location.
```

## modes-fr-081 · translation_permissions

Source task:

> Translate this fictional club notice into French: You may borrow a stool for the afternoon. You must return it before the hall closes at 19:00. Borrowing is optional and does not reserve a place at the evening event.

### baseline: pass

```text
Vous pouvez emprunter un tabouret pour l’après-midi. Vous devez le rendre avant la fermeture de la salle à 19 h. L’emprunt est facultatif et ne réserve pas de place à l’événement du soir.
```

### lite: pass

```text
Vous pouvez emprunter un tabouret pour l’après-midi. Vous devez le rendre avant la fermeture de la salle à 19 h 00. L’emprunt est facultatif et ne réserve pas de place à l’événement du soir.
```

### full: pass

```text
Vous pouvez emprunter un tabouret pour l’après-midi. Vous devez le rendre avant la fermeture de la salle à 19 h 00. L’emprunt est facultatif et ne réserve pas de place à l’événement du soir.
```

### ultra: pass

```text
Vous pouvez emprunter un tabouret pour l’après-midi. Vous devez le rendre avant la fermeture de la salle à 19 h 00. L’emprunt est facultatif et ne réserve pas de place à l’événement du soir.
```

### off: pass

```text
Vous pouvez emprunter un tabouret pour l’après-midi. Vous devez le rendre avant la fermeture de la salle à 19 h 00. L’emprunt est facultatif et ne réserve pas de place à l’événement du soir.
```

## modes-fr-082 · translation_negation

Source task:

> Translate into French: Do not cancel the order because the tracking page is blank. The parcel may already be in transit. We have not yet received confirmation from the carrier.

### baseline: pass

```text
N’annulez pas la commande parce que la page de suivi est vide. Le colis est peut-être déjà en cours d’acheminement. Nous n’avons pas encore reçu de confirmation du transporteur.
```

### lite: pass

```text
N’annulez pas la commande parce que la page de suivi est vide. Le colis est peut-être déjà en cours d’acheminement. Nous n’avons pas encore reçu de confirmation du transporteur.
```

### full: pass

```text
N’annulez pas la commande au motif que la page de suivi est vide. Le colis est peut-être déjà en cours d’acheminement. Nous n’avons pas encore reçu de confirmation du transporteur.
```

### ultra: pass

```text
N’annulez pas la commande parce que la page de suivi est vide. Le colis est peut-être déjà en transit. Nous n’avons pas encore reçu de confirmation du transporteur.
```

### off: pass

```text
N’annulez pas la commande parce que la page de suivi est vide. Le colis est peut-être déjà en cours d’acheminement. Nous n’avons pas encore reçu de confirmation du transporteur.
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

## modes-fr-084 · translation_uncertainty

Source task:

> Translate into French: The stain is probably from the old pipe, but no test has confirmed this. Only the outer panel was inspected. The wall behind it has not been opened.

### baseline: pass

```text
La tache provient probablement du vieux tuyau, mais aucun test ne l’a confirmé. Seul le panneau extérieur a été inspecté. Le mur derrière n’a pas été ouvert.
```

### lite: pass

```text
La tache provient probablement de l’ancien tuyau, mais aucun test ne l’a confirmé. Seul le panneau extérieur a été inspecté. Le mur derrière ce panneau n’a pas été ouvert.
```

### full: pass

```text
La tache provient probablement de l’ancien tuyau, mais aucun test ne l’a confirmé. Seul le panneau extérieur a été inspecté. Le mur derrière ce panneau n’a pas été ouvert.
```

### ultra: pass

```text
La tache provient probablement de l’ancien tuyau, mais aucun test ne l’a confirmé. Seul le panneau extérieur a été inspecté. Le mur derrière n’a pas été ouvert.
```

### off: pass

```text
La tache provient probablement de l’ancien tuyau, mais aucun test ne l’a confirmé. Seul le panneau extérieur a été inspecté. Le mur derrière ce panneau n’a pas été ouvert.
```

## modes-fr-085 · translation_json

Source task:

> Translate only the text value into French. Return valid JSON alone with the same keys, identifier, and count: {"id":"FR-A19","count":3,"text":"Three labels are missing. The boxes must stay closed until the labels are replaced."}

### baseline: pass

```text
{"id":"FR-A19","count":3,"text":"Trois étiquettes manquent. Les boîtes doivent rester fermées jusqu’à ce que les étiquettes soient remplacées."}
```

### lite: pass

```text
{"id":"FR-A19","count":3,"text":"Trois étiquettes manquent. Les boîtes doivent rester fermées jusqu’à ce que les étiquettes soient remplacées."}
```

### full: pass

```text
{"id":"FR-A19","count":3,"text":"Trois étiquettes manquent. Les boîtes doivent rester fermées jusqu’au remplacement des étiquettes."}
```

### ultra: pass

```text
{"id":"FR-A19","count":3,"text":"Trois étiquettes manquent. Les boîtes doivent rester fermées jusqu’au remplacement des étiquettes."}
```

### off: pass

```text
{"id":"FR-A19","count":3,"text":"Trois étiquettes manquent. Les boîtes doivent rester fermées jusqu’à ce que les étiquettes soient remplacées."}
```

## modes-fr-086 · translation_format

Source task:

> Translate into French, retaining two bullet points and the literal placeholders:
> - Hello, {{guest}}. Your visit is confirmed for 16 May.
> - You may change the time using {{visit_link}}, but you cannot add another guest.

### baseline: pass

```text
- Bonjour, {{guest}}. Votre visite est confirmée pour le 16 mai.
- Vous pouvez modifier l’heure à l’aide de {{visit_link}}, mais vous ne pouvez pas ajouter une autre personne.
```

### lite: pass

```text
- Bonjour, {{guest}}. Votre visite est confirmée pour le 16 mai.
- Vous pouvez modifier l’heure en utilisant {{visit_link}}, mais vous ne pouvez pas ajouter une autre personne.
```

### full: pass

```text
- Bonjour, {{guest}}. Votre visite est confirmée pour le 16 mai.
- Vous pouvez modifier l’heure via {{visit_link}}, mais vous ne pouvez pas ajouter une autre personne invitée.
```

### ultra: pass

```text
- Bonjour, {{guest}}. Votre visite est confirmée pour le 16 mai.
- Vous pouvez modifier l’heure via {{visit_link}}, mais vous ne pouvez pas ajouter d’autre personne.
```

### off: pass

```text
- Bonjour, {{guest}}. Votre visite est confirmée pour le 16 mai.
- Vous pouvez modifier l’heure à l’aide de {{visit_link}}, mais vous ne pouvez pas ajouter une autre personne.
```

## modes-fr-087 · translation_conditions

Source task:

> Translate this fictional access rule into French: The store room may be entered only after the lights are checked and the supervisor gives permission. A light check alone is not enough.

### baseline: pass

```text
L’accès au local de stockage n’est autorisé qu’après vérification des lumières et avec la permission du responsable. La seule vérification des lumières ne suffit pas.
```

### lite: pass

```text
L’accès à la réserve n’est autorisé qu’après la vérification des lumières et l’autorisation du responsable. La seule vérification des lumières ne suffit pas.
```

### full: pass

```text
L’accès à la réserve n’est autorisé qu’après la vérification des lumières et l’autorisation du responsable. La vérification des lumières seule ne suffit pas.
```

### ultra: pass

```text
L’accès à la réserve n’est autorisé qu’après vérification des lumières et autorisation du responsable. La seule vérification des lumières ne suffit pas.
```

### off: pass

```text
L’accès à la réserve n’est autorisé qu’après la vérification de l’éclairage et l’autorisation du responsable. La seule vérification de l’éclairage ne suffit pas.
```

## modes-fr-088 · translation_estimates

Source task:

> Translate into French: Packing should take about 4 to 6 hours if all the crates arrive before noon. This is an estimate, not a delivery promise. Missing crates could extend the work.

### baseline: pass

```text
L’emballage devrait prendre environ 4 à 6 heures si toutes les caisses arrivent avant midi. Il s’agit d’une estimation, et non d’une promesse de livraison. Des caisses manquantes pourraient prolonger le travail.
```

### lite: pass

```text
L’emballage devrait prendre environ 4 à 6 heures si toutes les caisses arrivent avant midi. Il s’agit d’une estimation, et non d’une promesse de livraison. Des caisses manquantes pourraient prolonger le travail.
```

### full: pass

```text
L’emballage devrait prendre environ 4 à 6 heures si toutes les caisses arrivent avant midi. Il s’agit d’une estimation, pas d’une promesse de livraison. Des caisses manquantes pourraient prolonger le travail.
```

### ultra: pass

```text
L’emballage devrait prendre environ 4 à 6 heures si toutes les caisses arrivent avant midi. C’est une estimation, pas une promesse de livraison. Des caisses manquantes pourraient prolonger le travail.
```

### off: pass

```text
L’emballage devrait prendre environ 4 à 6 heures si toutes les caisses arrivent avant midi. Il s’agit d’une estimation, et non d’une promesse de livraison. Des caisses manquantes pourraient prolonger le travail.
```

## modes-fr-089 · translation_units

Source task:

> Translate into French without converting units or currency: Each roll is 25 m long and costs GBP 14 excluding tax. Delivery costs GBP 9 per order, regardless of the number of rolls.

### baseline: pass

```text
Chaque rouleau mesure 25 m de long et coûte GBP 14 hors taxes. La livraison coûte GBP 9 par commande, quel que soit le nombre de rouleaux.
```

### lite: pass

```text
Chaque rouleau mesure 25 m de long et coûte GBP 14 hors taxes. La livraison coûte GBP 9 par commande, quel que soit le nombre de rouleaux.
```

### full: pass

```text
Chaque rouleau mesure 25 m de long et coûte GBP 14 hors taxes. La livraison coûte GBP 9 par commande, quel que soit le nombre de rouleaux.
```

### ultra: pass

```text
Chaque rouleau mesure 25 m et coûte GBP 14 hors taxes. La livraison coûte GBP 9 par commande, quel que soit le nombre de rouleaux.
```

### off: pass

```text
Chaque rouleau mesure 25 m de long et coûte GBP 14 hors taxes. La livraison coûte GBP 9 par commande, quel que soit le nombre de rouleaux.
```

## modes-fr-090 · translation_sampling

Source task:

> Translate into French: We interviewed 22 people who volunteered at the morning market. They were not randomly selected. Their answers cannot establish what all shoppers prefer.

### baseline: pass

```text
Nous avons interrogé 22 personnes qui se sont portées volontaires au marché du matin. Elles n’ont pas été sélectionnées au hasard. Leurs réponses ne permettent pas d’établir les préférences de l’ensemble des clients.
```

### lite: pass

```text
Nous avons interrogé 22 personnes qui se sont portées volontaires au marché du matin. Elles n’ont pas été sélectionnées au hasard. Leurs réponses ne permettent pas d’établir les préférences de l’ensemble des acheteurs.
```

### full: pass

```text
Nous avons interrogé 22 personnes qui se sont portées volontaires au marché du matin. Elles n’ont pas été sélectionnées au hasard. Leurs réponses ne permettent pas d’établir les préférences de l’ensemble des clients.
```

### ultra: pass

```text
Nous avons interrogé 22 personnes qui se sont portées volontaires au marché du matin. Elles n’ont pas été sélectionnées au hasard. Leurs réponses ne permettent pas d’établir les préférences de l’ensemble des acheteurs.
```

### off: pass

```text
Nous avons interrogé 22 personnes qui se sont portées volontaires au marché du matin. Elles n’ont pas été sélectionnées au hasard. Leurs réponses ne permettent pas d’établir les préférences de l’ensemble des clients.
```

## modes-fr-091 · translation_percentage_points

Source task:

> Translate into French: In this fictional exercise, the share rose from 28% to 35%, an increase of 7 percentage points. This is not a 7% relative increase.

### baseline: pass

```text
Dans cet exercice fictif, la part est passée de 28 % à 35 %, soit une hausse de 7 points de pourcentage. Il ne s’agit pas d’une hausse relative de 7 %.
```

### lite: pass

```text
Dans cet exercice fictif, la part est passée de 28 % à 35 %, soit une hausse de 7 points de pourcentage. Il ne s’agit pas d’une hausse relative de 7 %.
```

### full: pass

```text
Dans cet exercice fictif, la part est passée de 28 % à 35 %, soit une hausse de 7 points de pourcentage. Il ne s’agit pas d’une hausse relative de 7 %.
```

### ultra: pass

```text
Dans cet exercice fictif, la part est passée de 28 % à 35 %, soit une hausse de 7 points de pourcentage. Ce n’est pas une hausse relative de 7 %.
```

### off: pass

```text
Dans cet exercice fictif, la part est passée de 28 % à 35 %, soit une hausse de 7 points de pourcentage. Il ne s’agit pas d’une augmentation relative de 7 %.
```

## modes-fr-092 · translation_exceptions

Source task:

> Translate this fictional workshop policy into French: Fees are non-refundable after a session has taken place. If the organiser cancels before the session, participants may request a refund. They do not have to accept a credit instead.

### baseline: pass

```text
Les frais ne sont pas remboursables une fois la séance tenue. Si l’organisateur annule avant la séance, les participants peuvent demander un remboursement. Ils ne sont pas obligés d’accepter un avoir à la place.
```

### lite: pass

```text
Les frais ne sont pas remboursables une fois la séance tenue. Si l’organisateur annule avant la séance, les participants peuvent demander un remboursement. Ils ne sont pas obligés d’accepter un avoir à la place.
```

### full: pass

```text
Les frais ne sont pas remboursables une fois la séance tenue. Si l’organisateur annule avant la séance, les participants peuvent demander un remboursement. Ils ne sont pas obligés d’accepter un avoir à la place.
```

### ultra: pass

```text
Les frais ne sont pas remboursables après la tenue d’une séance. Si l’organisateur annule avant la séance, les participants peuvent demander un remboursement. Ils ne sont pas obligés d’accepter un avoir à la place.
```

### off: pass

```text
Les frais ne sont pas remboursables une fois qu’une séance a eu lieu. Si l’organisateur annule avant la séance, les participants peuvent demander un remboursement. Ils ne sont pas obligés d’accepter un avoir à la place.
```

## modes-fr-093 · translation_ambiguity

Source task:

> Translate into French without resolving the date: The form says 08/09. We do not know which date convention was used. Please confirm the day and month before arranging collection.

### baseline: pass

```text
Le formulaire indique 08/09. Nous ne savons pas quelle convention de date a été utilisée. Veuillez confirmer le jour et le mois avant d’organiser la collecte.
```

### lite: pass

```text
Le formulaire indique 08/09. Nous ne savons pas quelle convention de date a été utilisée. Veuillez confirmer le jour et le mois avant d’organiser la collecte.
```

### full: pass

```text
Le formulaire indique 08/09. Nous ne savons pas quelle convention de date a été utilisée. Veuillez confirmer le jour et le mois avant d’organiser la collecte.
```

### ultra: pass

```text
Le formulaire indique 08/09. Nous ne savons pas quelle convention de date a été utilisée. Veuillez confirmer le jour et le mois avant d’organiser la collecte.
```

### off: pass

```text
Le formulaire indique 08/09. Nous ne savons pas quelle convention de date a été utilisée. Veuillez confirmer le jour et le mois avant d’organiser la collecte.
```

## modes-fr-094 · translation_technical

Source task:

> Translate into French, keeping the command unchanged: Run folder-audit --read-only before making edits. It lists inconsistent names; it does not rename files. Keep audit.log even if no issue is listed.

### baseline: pass

```text
Exécutez folder-audit --read-only avant d’effectuer des modifications. Cette commande répertorie les noms incohérents ; elle ne renomme pas les fichiers. Conservez audit.log même si aucun problème n’est signalé.
```

### lite: pass

```text
Exécutez folder-audit --read-only avant toute modification. Cette commande répertorie les noms incohérents ; elle ne renomme pas les fichiers. Conservez audit.log même si aucun problème n’est signalé.
```

### full: pass

```text
Exécutez folder-audit --read-only avant toute modification. Cette commande répertorie les noms incohérents ; elle ne renomme pas les fichiers. Conservez audit.log même si aucun problème n’est signalé.
```

### ultra: pass

```text
Exécutez folder-audit --read-only avant toute modification. Cette commande répertorie les noms incohérents ; elle ne renomme pas les fichiers. Conservez audit.log même si aucun problème n’est signalé.
```

### off: pass

```text
Exécutez folder-audit --read-only avant d’effectuer des modifications. Cette commande répertorie les noms incohérents ; elle ne renomme pas les fichiers. Conservez audit.log même si aucun problème n’est signalé.
```

## modes-fr-095 · translation_voice

Source task:

> Translate into French with a quiet, poetic tone: The last lamp stayed on. Two empty chairs faced the window. I waited for a knock, but nobody came before dawn.

### baseline: pass

```text
La dernière lampe est restée allumée. Deux chaises vides faisaient face à la fenêtre. J’attendais qu’on frappe à la porte, mais personne n’est venu avant l’aube.
```

### lite: pass

```text
La dernière lampe est restée allumée. Deux chaises vides faisaient face à la fenêtre. J’attendais qu’on frappe à la porte, mais personne n’est venu avant l’aube.
```

### full: pass

```text
La dernière lampe est restée allumée. Deux chaises vides faisaient face à la fenêtre. J’attendais qu’on frappe à la porte, mais personne n’est venu avant l’aube.
```

### ultra: pass

```text
La dernière lampe est restée allumée. Deux chaises vides faisaient face à la fenêtre. J’attendais qu’on frappe à la porte, mais personne n’est venu avant l’aube.
```

### off: pass

```text
La dernière lampe est restée allumée. Deux chaises vides faisaient face à la fenêtre. J’attendais qu’on frappe à la porte, mais personne n’est venu avant l’aube.
```

## modes-fr-096 · translation_quotation

Source task:

> Translate the explanation into French and leave the quoted error exactly as written: The screen says "sync pending". This means that synchronisation is waiting; it does not confirm that any file has been lost.

### baseline: pass

```text
L’écran affiche "sync pending". Cela signifie que la synchronisation est en attente ; cela ne confirme pas qu’un fichier a été perdu.
```

### lite: pass

```text
L’écran affiche "sync pending". Cela signifie que la synchronisation est en attente ; cela ne confirme pas qu’un fichier a été perdu.
```

### full: pass

```text
L’écran affiche "sync pending". Cela signifie que la synchronisation est en attente ; ce message ne confirme pas qu’un fichier a été perdu.
```

### ultra: pass

```text
L’écran affiche "sync pending". Cela signifie que la synchronisation est en attente ; ce message ne confirme la perte d’aucun fichier.
```

### off: pass

```text
L’écran affiche "sync pending". Cela signifie que la synchronisation est en attente ; cela ne confirme pas qu’un fichier a été perdu.
```

## modes-fr-097 · translation_scope

Source task:

> Translate into French: The new opening time applies to the repair counter only. The shop still opens at 09:00. Repairs are accepted from 10:30, including appointments booked before the change.

### baseline: pass

```text
Le nouvel horaire d’ouverture s’applique uniquement au comptoir de réparation. Le magasin ouvre toujours à 09:00. Les réparations sont acceptées à partir de 10:30, y compris pour les rendez-vous pris avant le changement.
```

### lite: pass

```text
Le nouvel horaire d’ouverture s’applique uniquement au comptoir de réparation. Le magasin ouvre toujours à 09:00. Les réparations sont acceptées à partir de 10:30, y compris pour les rendez-vous pris avant le changement.
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

## modes-fr-098 · translation_sequence

Source task:

> Translate into French: First save the draft, then ask another person to check the totals. Send the final invoice only after that check. Do not treat saving the draft as approval.

### baseline: pass

```text
Enregistrez d’abord le brouillon, puis demandez à une autre personne de vérifier les totaux. N’envoyez la facture définitive qu’après cette vérification. Ne considérez pas l’enregistrement du brouillon comme une approbation.
```

### lite: pass

```text
Enregistrez d’abord le brouillon, puis demandez à une autre personne de vérifier les totaux. N’envoyez la facture définitive qu’après cette vérification. Ne considérez pas l’enregistrement du brouillon comme une approbation.
```

### full: pass

```text
Enregistrez d’abord le brouillon, puis demandez à une autre personne de vérifier les totaux. N’envoyez la facture définitive qu’après cette vérification. L’enregistrement du brouillon ne vaut pas approbation.
```

### ultra: pass

```text
Enregistrez d’abord le brouillon, puis demandez à une autre personne de vérifier les totaux. N’envoyez la facture définitive qu’après cette vérification. L’enregistrement du brouillon ne vaut pas approbation.
```

### off: pass

```text
Enregistrez d’abord le brouillon, puis demandez à une autre personne de vérifier les totaux. N’envoyez la facture définitive qu’après cette vérification. Ne considérez pas l’enregistrement du brouillon comme une approbation.
```

## modes-fr-099 · translation_conflict

Source task:

> Translate into French: The label says 48 sheets, while the manual count found 47. No second count has been done. Neither number should be described as the confirmed quantity yet.

### baseline: pass

```text
L’étiquette indique 48 feuilles, tandis que le comptage manuel en a trouvé 47. Aucun second comptage n’a été effectué. Aucun de ces deux nombres ne doit encore être présenté comme la quantité confirmée.
```

### lite: pass

```text
L’étiquette indique 48 feuilles, tandis que le comptage manuel en a relevé 47. Aucun second comptage n’a été effectué. Aucun de ces deux nombres ne devrait être présenté comme la quantité confirmée pour le moment.
```

### full: pass

```text
L’étiquette indique 48 feuilles, mais le comptage manuel en a relevé 47. Aucun second comptage n’a été effectué. Aucun de ces deux nombres ne doit encore être présenté comme la quantité confirmée.
```

### ultra: pass

```text
L’étiquette indique 48 feuilles, mais le comptage manuel en a trouvé 47. Aucun second comptage n’a été effectué. Aucun de ces deux nombres ne doit encore être présenté comme la quantité confirmée.
```

### off: pass

```text
L’étiquette indique 48 feuilles, tandis que le comptage manuel en a relevé 47. Aucun second comptage n’a été effectué. Aucun de ces deux nombres ne doit encore être présenté comme la quantité confirmée.
```

## modes-fr-100 · translation_denominators

Source task:

> Translate into French: Of the 84 tickets reviewed, 21 were duplicates. Five of those 21 came from the mobile form. We do not know the total number of tickets submitted through that form.

### baseline: pass

```text
Sur les 84 tickets examinés, 21 étaient des doublons. Cinq de ces 21 tickets provenaient du formulaire mobile. Nous ne connaissons pas le nombre total de tickets soumis via ce formulaire.
```

### lite: pass

```text
Sur les 84 tickets examinés, 21 étaient des doublons. Cinq de ces 21 tickets provenaient du formulaire mobile. Nous ne connaissons pas le nombre total de tickets soumis via ce formulaire.
```

### full: pass

```text
Sur les 84 tickets examinés, 21 étaient des doublons. Cinq de ces 21 doublons provenaient du formulaire mobile. Nous ne connaissons pas le nombre total de tickets soumis via ce formulaire.
```

### ultra: pass

```text
Sur les 84 tickets examinés, 21 étaient des doublons. Cinq de ces 21 provenaient du formulaire mobile. Nous ne connaissons pas le nombre total de tickets soumis via ce formulaire.
```

### off: pass

```text
Sur les 84 tickets examinés, 21 étaient des doublons. Cinq de ces 21 tickets provenaient du formulaire mobile. Nous ne connaissons pas le nombre total de tickets soumis via ce formulaire.
```

