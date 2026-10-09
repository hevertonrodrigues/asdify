# ASDify

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[Pruébalo](#pruébalo-sin-instalar) · [Instalación](#instala-en-tu-agente) · [Idiomas](docs/LANGUAGES.md) · [Soporte](SUPPORT.md) · [Ejemplos de uso](examples/recipes.md) · [Contribuye](CONTRIBUTING.md)

Dale a tu agente de IA una rutina de edición: encontrar el punto principal, eliminar el relleno y comprobar que se conservan los detalles importantes. ASDify es una pequeña habilidad portátil en Markdown para respuestas, traducciones, actualizaciones, informes y documentación en agentes de programación y editores compatibles.

## Mira la diferencia

**Antes**

> Nos gustaría destacar que los ingresos preliminares por suscripciones en Brasil crecieron un 12% interanual, excluyendo los reembolsos. Estas cifras aún no se han auditado.

**Después (`full`)**

> Los ingresos preliminares por suscripciones en Brasil crecieron un 12% interanual, excluyendo los reembolsos. Las cifras aún no se han auditado.

*Ejemplo editorial ilustrativo, no un resultado medido en un modelo.* Conserva el carácter preliminar, las suscripciones, Brasil, el 12%, el periodo anual, la exclusión de reembolsos y la falta de auditoría. [Más ejemplos de antes y después](examples/before-after.md).

## Pruébalo sin instalar

1. Abre [SKILL.md](skills/asdify/SKILL.md), copia su contenido y pégalo como instrucciones en un chat, como ChatGPT o Claude web. La habilidad canónica está en inglés.
2. Envía este prompt:

```text
Usa asdify full. Reescribe esta actualización para la dirección.
Devuelve solo el texto revisado. Conserva todos los hechos y matices.

Nos gustaría destacar que los ingresos preliminares por suscripciones
en Brasil crecieron un 12% interanual, excluyendo los reembolsos.
Estas cifras aún no se han auditado.
```

La redacción puede variar; los hechos y matices deben conservarse. Es una prueba manual, sin instalación automática. Consulta [una ejecución real de Codex](docs/demos/codex-full-2026-10-08.md), con el prompt, la respuesta y las comprobaciones, en inglés.

## Instala en tu agente

| Método | Cuándo elegirlo | Requisitos |
| --- | --- | --- |
| Skills CLI | Descubrimiento, varios agentes e instalación gestionada | Node.js/npm y red para descargas |
| Instalador local | Copia comprobada sin npm | Clon o ZIP extraído, Bash y utilidades POSIX |
| Copia manual | Sin instalador, también en Windows | Carpeta completa y ruta documentada del agente |
| Instrucciones del proyecto / regla de Cursor | El agente usa instrucciones persistentes | Archivo de instrucciones o directorio de reglas |
| Plugin de Claude Code | Usas su gestor de plugins | Claude Code con soporte de plugins |
| [Chat manual](#pruébalo-sin-instalar) | Prueba sin instalación | Chat que admita instrucciones |

ASDify no requiere Node.js ni npm. La Skills CLI opcional puede pedir confirmación para descargar su paquete npm. Usa el [instalador local](INSTALL.md#local-installer) para evitar esa descarga; consulta la [instalación de la habilidad nativa de Cursor sin npm](INSTALL.md#cursor-without-nodejs-or-npm).

Usa la [Skills CLI](https://github.com/vercel-labs/skills) para descubrir ASDify e instalarlo:

```bash
npx skills add hevertonrodrigues/asdify --list
npx skills add hevertonrodrigues/asdify --skill asdify --agent claude-code
```

Sustituye `claude-code` por el [ID de tu agente](docs/HARNESSES.md), como `codex`, `cursor`, `gemini-cli` u `opencode`. Ejecuta desde el proyecto de destino; añade `--global` para instalar para el usuario cuando sea compatible. La [guía de instalación](INSTALL.md) explica los ámbitos, las rutas y la desinstalación.

Si prefieres el instalador local:

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
bash scripts/install.sh --list
bash scripts/install.sh --agent claude-code --scope user
```

Elige un ID de `--list`. Este instalador copia la habilidad completa y sus referencias desde el clon, sin descargar nada. Rechaza sobrescribir archivos existentes salvo que indiques `--force`.

Para habilidades nativas de Cursor, el ID local es `cursor-skill`; `cursor` conserva el adaptador anterior de reglas compactas del proyecto. La Skills CLI usa `cursor` para habilidades nativas. [Diferencias y rutas](INSTALL.md#cursor-native-skill-or-compact-rule).

La [tabla de agentes](docs/HARNESSES.md) cubre el registro de esta versión. Las pruebas de instalación y las sesiones reales se registran por separado en [compatibilidad](docs/COMPATIBILITY.md). Para otros agentes, usa su ruta documentada o la prueba manual anterior.

### Opciones de alcance y confirmación

La CLI usa el proyecto actual por defecto. `--global` elige el usuario; `--copy` solicita copias en lugar de enlaces simbólicos. Para varios agentes, usa `--agent claude-code cursor codex`. `--yes` antes de `skills` acepta la descarga del paquete npm; al final acepta las confirmaciones de la CLI:

```bash
DISABLE_TELEMETRY=1 npx --yes skills add hevertonrodrigues/asdify --skill asdify --agent cursor --global --copy --yes
```

Los archivos aún se descargan cuando hace falta. La CLI también admite una fuente local: `npx skills add /path/to/asdify --skill asdify --agent cursor`. Consulta [todas las opciones](INSTALL.md#scope-copies-and-multiple-agents).

Sin Git, usa **Code → Download ZIP** en GitHub, extrae el archivo y ejecuta el instalador desde esa carpeta. `--list` muestra los destinos; `--help` muestra las opciones. Para instalar la habilidad nativa de Cursor solo en un proyecto, ejecuta desde ese proyecto, sustituyendo la ruta:

```bash
bash "/path/to/asdify/scripts/install.sh" --agent cursor-skill --scope project
```

El destino es `.agents/skills/asdify/`; `--scope user` usa `~/.cursor/skills/asdify/`. Revisa una copia existente antes de usar `--force`. El ID local `cursor` es la regla compacta; el ID `cursor` de la Skills CLI es la habilidad nativa.

### Copia manual e instrucciones persistentes

Copia toda la carpeta [skills/asdify/](skills/asdify/), incluidos `SKILL.md` y `references/`, al [destino documentado](docs/HARNESSES.md). Crea las carpetas necesarias y revisa una instalación existente antes de reemplazarla. Con los archivos disponibles no necesitas npm, Git ni Bash.

Si el agente lee instrucciones del proyecto, integra [AGENTS.md](AGENTS.md) sin reemplazar otras reglas. Para Cursor, usa `bash "/path/to/asdify/scripts/install.sh" --agent cursor-rule --scope project` desde el proyecto de destino, o copia [cursor-rule.mdc](integrations/cursor-rule.mdc) a `.cursor/rules/asdify.mdc`. Los adaptadores compactos contienen menos detalles que la habilidad completa.

### Plugin de Claude Code

El repositorio incluye los manifiestos de plugin y marketplace. En una sesión de Claude Code:

```text
/plugin marketplace add hevertonrodrigues/asdify
/plugin install asdify@asdify
```

Elige el alcance en el gestor; también admite un [clon local](INSTALL.md#claude-code-plugin). Los manifiestos pasan la validación, pero no se ha verificado una instalación y activación reales del plugin.

## Entornos compatibles

La [tabla completa](docs/HARNESSES.md) incluye **82 IDs: 79 mapeos de agentes y 3 IDs de compatibilidad**, con destinos, alcances y fuentes. Abarca Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, OpenCode, Windsurf, Cline, Continue y otros.

En Windows, usa la CLI o la copia manual. El script requiere Bash/POSIX; con WSL, instala donde el agente lea sus archivos. La matriz automatizada cubre Linux/macOS; la ejecución en Windows no se ha verificado. Para agentes remotos o en la nube, usa habilidades de proyecto en el repositorio o el mecanismo documentado por el agente. `universal` es una convención de carpeta, no una garantía de descubrimiento en cualquier aplicación.

Después de instalar, abre una sesión nueva y pide `Usa asdify full`. En Cursor, consulta **Customize → Skills**. Copiar archivos no prueba por sí solo la activación; consulta [compatibilidad](docs/COMPATIBILITY.md).

## Actualizaciones y eliminación

| Método | Actualizar | Eliminar |
| --- | --- | --- |
| Skills CLI | `npx skills update asdify` | `npx skills remove asdify --agent <id>`; añade `--global` para el usuario |
| Instalador local | Obtén los archivos actualizados, revisa y repite con el mismo agente/alcance y `--force` | Borra solo la carpeta o regla ASDify indicada |
| Copia manual / instrucciones | Revisa y reemplaza la carpeta o el texto de ASDify | Borra solo esa carpeta o esas instrucciones |
| Plugin de Claude Code | Usa la acción de actualización del gestor | Desactiva o desinstala `asdify@asdify` |

En la Skills CLI, añade `--global` también al actualizar una instalación de usuario. Las carpetas compartidas afectan a todos los agentes que las leen. Conserva tus cambios antes de reemplazar una copia. [Comandos y rutas](INSTALL.md#removal-and-updates).

## Cómo edita ASDify

Identifica al lector, marca lo que debe conservarse, realiza la menor edición útil y comprueba el significado. Conserva números, fechas, condiciones, incertidumbre y términos técnicos necesarios. Deja intacto lo que ya está claro. No inventes consejos, decisiones ni plazos durante una revisión.

| Modo | Cuándo usarlo | Qué cambia |
| --- | --- | --- |
| `lite` | Quieres una edición ligera | La redacción; conserva estructura, orden y tono. |
| `full` · predeterminado | Quieres una respuesta más clara | La redacción y la estructura, cuando ayuda. |
| `ultra` | Sobran introducciones o secciones | Edición más intensa, con las mismas reglas de conservación. |

Pide un modo con `Usa asdify lite`, `full` o `ultra`. `asdify off` desactiva este flujo opcional, sujeto a las demás instrucciones del agente. Los modos son instrucciones; el soporte de comandos nativos varía.

## Idiomas y traducción

Hay READMEs y casos de regresión en inglés, portugués brasileño, español, francés, alemán, japonés, chino simplificado, italiano y ruso. Instala la misma habilidad canónica para todos; no necesitas paquetes de idiomas. Las revisiones conservan el idioma original salvo que pidas una traducción.

```text
Usa asdify full. Traduce al español (es).
Devuelve solo la traducción. Conserva todos los hechos y matices.

Preliminary subscription revenue grew 12% year over year in Brazil,
excluding refunds. These figures are unaudited.
```

Especifica el idioma o la variante de destino. La traducción conserva el significado, los identificadores, los marcadores y el formato solicitado, adaptando la gramática y el registro. Consulta los [ejemplos multilingües](examples/multilingual.md) y la [cobertura de idiomas y soporte](docs/LANGUAGES.md). La calidad depende del modelo del agente; las pruebas del paquete no la verifican.

## Ponlo en práctica

| Tarea | Qué conservar | Prompt completo |
| --- | --- | --- |
| Actualización ejecutiva | Estado, responsables, fechas tentativas y condiciones | [`full` · EN](examples/recipes.md#1-executive-update-en) |
| Recomendación técnica | Identificadores, actor, secuencia y recomendación frente a obligación | [`lite` · PT-BR](examples/recipes.md#2-technical-recommendation-pt-br) |
| Informe denso para decidir | Estimaciones, exclusiones y requisitos de aprobación | [`ultra` · EN](examples/recipes.md#3-dense-decision-brief-en) |
| Mensaje ya claro | La redacción original si no necesita cambios | [Sin cambios · EN](examples/recipes.md#4-leave-clear-text-alone-en) |

## Verificación y soporte

Una respuesta más corta que cambia un hecho importante falla la evaluación. El [estudio de los cuatro modos](benchmarks/multilingual-modes/README.md) usa 100 casos nuevos por cada uno de los nueve idiomas de salida: 900 casos distintos, ejecutados en `lite`, `full`, `ultra` y `off`, más un control sin la skill. Son 3.600 pruebas de los modos y 4.500 respuestas, con dos revisiones ciegas por un modelo de la misma familia que el generador. Consulta las [pruebas registradas](benchmarks/results/README.md) y el [protocolo de evaluación reproducible](benchmarks/README.md). Los casos son sintéticos y algunos patrones de escenario se repiten entre idiomas, por lo que las observaciones no son independientes. **La fiabilidad general y las mejoras amplias de calidad siguen sin demostrarse.** La [verificación del paquete](docs/VERIFICATION.md) y la [compatibilidad](docs/COMPATIBILITY.md) cubren comprobaciones separadas.

| Problema | Dónde obtener ayuda |
| --- | --- |
| Confirmación de npm, ID, ruta, sobrescritura o descubrimiento | [Diagnóstico](INSTALL.md#troubleshooting) · [Informe de instalación](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md) |
| Hechos perdidos, obligación cambiada, idioma incorrecto o contenido inventado | [Cambio de significado](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) |
| README traducido incorrecto o desactualizado | [Traducción de documentación](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml) |
| Nuevo idioma, agente, ejemplo o mejora | [Solicitud](https://github.com/hevertonrodrigues/asdify/issues/new?template=feature_request.md) · [Contribuir](CONTRIBUTING.md) |
| Vulnerabilidad o información privada | [Seguridad e informe privado](SECURITY.md) |

Incluye el comando o prompt, resultado real, versiones del sistema/agente, modo, alcance e idiomas de origen y destino cuando corresponda. Elimina información privada. Un texto ya claro puede quedar igual. Consulta [SUPPORT.md](SUPPORT.md) y [soporte de idiomas](docs/LANGUAGES.md). Los problemas de cuenta, facturación o servicio del agente corresponden a su proveedor.

Las guías complementarias enlazadas están en inglés, salvo los ejemplos indicados en PT-BR. Esta traducción aún no cuenta con una revisión independiente de un hablante nativo.

[Hoja de ruta](docs/ROADMAP.md) · [Historial de cambios](CHANGELOG.md) · [Licencia MIT](LICENSE)
