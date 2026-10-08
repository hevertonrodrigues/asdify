# ASDify

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[Essayer](#essayer-sans-installation) · [Installation](#installer-pour-votre-agent) · [Langues](docs/LANGUAGES.md) · [Assistance](SUPPORT.md) · [Cas pratiques](examples/recipes.md) · [Contribuer](CONTRIBUTING.md)

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

| Méthode | Quand la choisir | Prérequis |
| --- | --- | --- |
| Skills CLI | Découverte, plusieurs agents et installation gérée | Node.js/npm et réseau pour les téléchargements |
| Installateur local | Copie vérifiée sans npm | Clone ou ZIP extrait, Bash et outils POSIX |
| Copie manuelle | Sans installateur, y compris sur Windows | Dossier complet et chemin documenté par l'agent |
| Instructions du projet / règle Cursor | L'agent lit des instructions persistantes | Fichier d'instructions ou dossier de règles |
| Plugin Claude Code | Vous utilisez son gestionnaire de plugins | Claude Code avec prise en charge des plugins |
| [Chat manuel](#essayer-sans-installation) | Essai sans installation | Chat acceptant des instructions |

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

### Portée et confirmations

La CLI utilise le projet courant par défaut. `--global` choisit la portée utilisateur ; `--copy` demande des copies plutôt que des liens symboliques. Pour plusieurs agents, utilisez `--agent claude-code cursor codex`. `--yes` avant `skills` accepte le téléchargement npm ; à la fin, il accepte les confirmations de la CLI :

```bash
DISABLE_TELEMETRY=1 npx --yes skills add hevertonrodrigues/asdify --skill asdify --agent cursor --global --copy --yes
```

Les téléchargements ont toujours lieu si nécessaire. La CLI accepte aussi une source locale : `npx skills add /path/to/asdify --skill asdify --agent cursor`. Consultez [toutes les options](INSTALL.md#scope-copies-and-multiple-agents).

Sans Git, utilisez **Code → Download ZIP** sur GitHub, extrayez l'archive et lancez l'installateur depuis ce dossier. `--list` affiche les destinations ; `--help` affiche les options. Pour une compétence native Cursor limitée au projet, exécutez depuis le projet cible, en remplaçant le chemin :

```bash
bash "/path/to/asdify/scripts/install.sh" --agent cursor-skill --scope project
```

La destination est `.agents/skills/asdify/` ; `--scope user` utilise `~/.cursor/skills/asdify/`. Vérifiez une copie existante avant `--force`. L'identifiant local `cursor` installe la règle compacte ; l'identifiant `cursor` de la Skills CLI installe la compétence native.

### Copie manuelle et instructions persistantes

Copiez tout le dossier [skills/asdify/](skills/asdify/), dont `SKILL.md` et `references/`, vers la [destination documentée](docs/HARNESSES.md). Créez les dossiers nécessaires et vérifiez une installation existante avant de la remplacer. Une fois les fichiers disponibles, ni npm, ni Git, ni Bash ne sont nécessaires.

Si l'agent lit des instructions de projet, intégrez [AGENTS.md](AGENTS.md) sans remplacer les autres règles. Pour Cursor, utilisez `bash "/path/to/asdify/scripts/install.sh" --agent cursor-rule --scope project` depuis le projet cible, ou copiez [cursor-rule.mdc](integrations/cursor-rule.mdc) vers `.cursor/rules/asdify.mdc`. Les adaptateurs compacts contiennent moins de détails que la compétence complète.

### Plugin Claude Code

Le dépôt contient les manifestes du plugin et du marketplace. Dans une session Claude Code :

```text
/plugin marketplace add hevertonrodrigues/asdify
/plugin install asdify@asdify
```

Choisissez la portée dans le gestionnaire ; un [clone local](INSTALL.md#claude-code-plugin) est aussi possible. Les manifestes passent la validation, mais une installation et activation réelles du plugin n'ont pas été vérifiées.

## Environnements pris en charge

La [table complète](docs/HARNESSES.md) compte **82 identifiants : 79 correspondances d'agents et 3 identifiants de compatibilité**, avec chemins, portées et sources. Elle couvre Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, OpenCode, Windsurf, Cline, Continue et d'autres.

Sur Windows, utilisez la CLI ou la copie manuelle. Le script nécessite Bash/POSIX ; avec WSL, installez là où l'agent lit ses fichiers. La matrice automatisée couvre Linux/macOS ; l'exécution sur Windows n'a pas été vérifiée. Pour les agents distants ou dans le cloud, utilisez les compétences de projet dans le dépôt ou leur mécanisme documenté. `universal` est une convention de dossier, pas une garantie de découverte dans toute application.

Après installation, ouvrez une nouvelle session et demandez `Utilise asdify full`. Dans Cursor, consultez **Customize → Skills**. Une copie réussie ne prouve pas à elle seule l'activation ; voir [compatibilité](docs/COMPATIBILITY.md).

## Mises à jour et suppression

| Méthode | Mettre à jour | Supprimer |
| --- | --- | --- |
| Skills CLI | `npx skills update asdify` | `npx skills remove asdify --agent <id>` ; ajoutez `--global` pour l'utilisateur |
| Installateur local | Obtenez les fichiers actualisés, vérifiez et réinstallez avec le même agent/la même portée et `--force` | Supprimez uniquement le dossier ou la règle ASDify indiqué |
| Copie manuelle / instructions | Vérifiez et remplacez le dossier ou le texte ASDify | Supprimez seulement ce dossier ou ces instructions |
| Plugin Claude Code | Utilisez l'action de mise à jour du gestionnaire | Désactivez ou désinstallez `asdify@asdify` |

Dans la Skills CLI, ajoutez aussi `--global` pour mettre à jour une installation utilisateur. Les dossiers partagés affectent tous les agents qui les lisent. Conservez vos modifications avant remplacement. [Commandes et chemins](INSTALL.md#removal-and-updates).

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

| Problème | Où trouver de l'aide |
| --- | --- |
| Confirmation npm, identifiant, chemin, écrasement ou découverte | [Diagnostic](INSTALL.md#troubleshooting) · [Rapport d'installation](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md) |
| Faits perdus, obligation modifiée, mauvaise langue ou contenu inventé | [Modification du sens](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) |
| README traduit incorrect ou obsolète | [Traduction documentaire](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml) |
| Nouvelle langue, nouvel agent, exemple ou amélioration | [Demande](https://github.com/hevertonrodrigues/asdify/issues/new?template=feature_request.md) · [Contribuer](CONTRIBUTING.md) |
| Vulnérabilité ou informations privées | [Sécurité et signalement privé](SECURITY.md) |

Incluez commande ou prompt, résultat réel, versions du système/de l'agent, mode, portée et langues source/cible si pertinent. Retirez les informations privées. Un texte déjà clair peut rester inchangé. Consultez [SUPPORT.md](SUPPORT.md) et l'[assistance linguistique](docs/LANGUAGES.md). Les problèmes de compte, facturation ou service de l'agent relèvent de son fournisseur.

Les guides complémentaires liés sont en anglais, sauf les exemples indiqués en PT-BR. Cette traduction n'a pas encore fait l'objet d'une revue indépendante par une personne de langue maternelle française.

[Feuille de route](docs/ROADMAP.md) · [Historique des changements](CHANGELOG.md) · [Licence MIT](LICENSE)
