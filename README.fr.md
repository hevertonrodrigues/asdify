# ASDify

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[Essayer](#essayer-sans-installation) · [Installation](#installer-pour-votre-agent) · [Langues](docs/LANGUAGES.md) · [Cas pratiques](examples/recipes.md) · [Contribuer](CONTRIBUTING.md)

Donnez à votre agent d'IA une méthode de révision : trouver le point principal, supprimer le remplissage et vérifier que les détails importants sont conservés. ASDify est une petite compétence portable en Markdown pour les réponses, traductions, points d'avancement, rapports et documents dans les agents de programmation et éditeurs compatibles.

## Voir la différence

**Avant**

> Nous souhaitons souligner que le chiffre d'affaires préliminaire des abonnements au Brésil a augmenté de 12% sur un an, hors remboursements. Ces chiffres n'ont pas encore été audités.

**Après (`full`)**

> Le chiffre d'affaires préliminaire des abonnements au Brésil a augmenté de 12% sur un an, hors remboursements. Les chiffres n'ont pas encore été audités.

*Exemple de révision illustratif, pas un résultat mesuré sur un modèle.* Il conserve le caractère préliminaire, les abonnements, le Brésil, les 12%, la période annuelle, l'exclusion des remboursements et l'absence d'audit. [Autres exemples avant/après](examples/before-after.md).

## Essayer sans installation

1. Ouvrez [SKILL.md](skills/asdify/SKILL.md), copiez son contenu et collez-le comme instructions dans un chat, par exemple ChatGPT ou Claude web. La compétence canonique est en anglais.
2. Envoyez ce prompt :

```text
Utilise asdify full. Réécris ce point d'avancement pour la direction.
Renvoie uniquement le texte révisé. Conserve tous les faits et réserves.

Nous souhaitons souligner que le chiffre d'affaires préliminaire des
abonnements au Brésil a augmenté de 12% sur un an, hors remboursements.
Ces chiffres n'ont pas encore été audités.
```

La formulation peut varier ; les faits et réserves doivent rester intacts. Il s'agit d'un essai manuel, sans installation automatique. Consultez [une exécution réelle dans Codex](docs/demos/codex-full-2026-10-08.md), avec le prompt, la réponse et les vérifications, en anglais.

## Installer pour votre agent

ASDify ne nécessite ni Node.js ni npm. La Skills CLI facultative peut demander confirmation avant de télécharger son paquet npm. Utilisez l'[installateur local](INSTALL.md#local-installer) pour éviter ce téléchargement ; consultez l'[installation de la compétence native de Cursor sans npm](INSTALL.md#cursor-without-nodejs-or-npm).

Utilisez la [Skills CLI](https://github.com/vercel-labs/skills) pour découvrir et installer ASDify :

```bash
npx skills add hevertonrodrigues/asdify --list
npx skills add hevertonrodrigues/asdify --skill asdify --agent claude-code
```

Remplacez `claude-code` par l'[identifiant de votre agent](docs/HARNESSES.md), tel que `codex`, `cursor`, `gemini-cli` ou `opencode`. Lancez la commande depuis le projet cible ; ajoutez `--global` pour une installation utilisateur lorsque celle-ci est prise en charge. Le [guide d'installation](INSTALL.md) détaille les portées, chemins et étapes de suppression.

Si vous préférez l'installateur local :

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
bash scripts/install.sh --list
bash scripts/install.sh --agent claude-code --scope user
```

Choisissez un identifiant dans `--list`. Cet installateur copie la compétence complète et ses références depuis le clone, sans téléchargement. Il refuse d'écraser des fichiers existants sans `--force`.

Pour les compétences natives de Cursor, l'identifiant local est `cursor-skill` ; `cursor` conserve l'ancien adaptateur de règle compacte du projet. La Skills CLI utilise `cursor` pour les compétences natives. [Différences et chemins](INSTALL.md#cursor-native-skill-or-compact-rule).

La [table des agents](docs/HARNESSES.md) couvre le registre de cette version. Les tests d'installation et les sessions réelles sont suivis séparément dans [compatibilité](docs/COMPATIBILITY.md). Pour un autre agent, utilisez son chemin documenté ou l'essai manuel ci-dessus.

## Comment ASDify révise

Identifiez le lecteur, repérez les éléments à conserver, faites la plus petite modification utile, puis vérifiez le sens. Préservez chiffres, dates, conditions, incertitudes et termes techniques nécessaires. Gardez le texte déjà clair. N'inventez ni conseils, ni décisions, ni échéances lors d'une révision.

| Mode | Quand l'utiliser | Ce qui change |
| --- | --- | --- |
| `lite` | Vous voulez une retouche légère | La formulation ; conserve structure, ordre et ton. |
| `full` · par défaut | Vous voulez une réponse plus claire | La formulation et la structure, si cela aide. |
| `ultra` | Le texte contient des introductions ou sections inutiles | Révision plus poussée, avec les mêmes règles de préservation. |

Demandez un mode avec `Utilise asdify lite`, `full` ou `ultra`. `asdify off` désactive ce processus facultatif, sous réserve des autres instructions de l'agent. Les modes sont des instructions ; la prise en charge des commandes natives varie.

## Langues et traduction

Des READMEs et cas de régression couvrent l'anglais, le portugais brésilien, l'espagnol, le français, l'allemand, le japonais, le chinois simplifié, l'italien et le russe. Installez la même compétence canonique pour toutes les langues ; aucun module linguistique n'est nécessaire. Une révision conserve la langue source sauf si vous demandez une traduction.

```text
Utilise asdify full. Traduis en français (fr).
Renvoie uniquement la traduction. Conserve tous les faits et réserves.

Preliminary subscription revenue grew 12% year over year in Brazil,
excluding refunds. These figures are unaudited.
```

Précisez la langue ou la variante cible. La traduction préserve le sens, les identifiants, les variables de substitution et le format demandé, en adaptant grammaire et registre. Consultez les [exemples multilingues](examples/multilingual.md) et la [couverture linguistique et l'assistance](docs/LANGUAGES.md). La qualité dépend du modèle de l'agent ; les tests du paquet ne la vérifient pas.

## Cas pratiques

| Tâche | À préserver | Prompt complet |
| --- | --- | --- |
| Point d'avancement pour la direction | État, responsables, dates provisoires et conditions | [`full` · EN](examples/recipes.md#1-executive-update-en) |
| Recommandation technique | Identifiants, acteur, ordre et recommandation versus obligation | [`lite` · PT-BR](examples/recipes.md#2-technical-recommendation-pt-br) |
| Note de décision dense | Estimations, exclusions et approbations requises | [`ultra` · EN](examples/recipes.md#3-dense-decision-brief-en) |
| Message déjà clair | La formulation d'origine si aucune retouche n'est utile | [Sans changement · EN](examples/recipes.md#4-leave-clear-text-alone-en) |

## Vérification et assistance

Une réponse plus courte qui modifie un fait important échoue à l'évaluation. Le dépôt contient des cas de révision et traduction dans neuf langues, une grille de revue humaine et un [protocole d'évaluation reproductible](benchmarks/README.md). **Les gains de qualité sur des modèles réels n'ont pas encore été établis.** Consultez la [vérification du paquet](docs/VERIFICATION.md) et la [compatibilité](docs/COMPATIBILITY.md).

Une condition a disparu, un nombre a changé ou une promesse a été inventée ? [Signalez la modification du sens](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) avec la source, la réponse réelle et les langues source et cible. Pour une erreur dans ce README, utilisez le [formulaire de traduction documentaire](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml). Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour contribuer.

Les guides complémentaires liés sont en anglais, sauf les exemples indiqués en PT-BR. Cette traduction n'a pas encore fait l'objet d'une revue indépendante par une personne de langue maternelle française.

[Feuille de route](docs/ROADMAP.md) · [Historique des changements](CHANGELOG.md) · [Licence MIT](LICENSE)
