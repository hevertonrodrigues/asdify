# ASDify

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[Pruébalo](#pruébalo-sin-instalar) · [Instalación](#instala-en-tu-agente) · [Idiomas](docs/LANGUAGES.md) · [Ejemplos de uso](examples/recipes.md) · [Contribuye](CONTRIBUTING.md)

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

Una respuesta más corta que cambia un hecho importante falla la evaluación. El repositorio incluye casos de revisión y traducción en nueve idiomas, una rúbrica humana y un [protocolo de evaluación reproducible](benchmarks/README.md). **Todavía no se han demostrado mejoras de calidad en modelos reales.** Consulta la [verificación del paquete](docs/VERIFICATION.md) y la [compatibilidad](docs/COMPATIBILITY.md).

¿Se perdió una condición, cambió un número o se inventó una promesa? [Informa de un cambio de significado](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) con el texto original, la respuesta real y los idiomas de origen y destino. Para errores de este README, usa el [formulario de traducción de documentación](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml). Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para contribuir.

Las guías complementarias enlazadas están en inglés, salvo los ejemplos indicados en PT-BR. Esta traducción aún no cuenta con una revisión independiente de un hablante nativo.

[Hoja de ruta](docs/ROADMAP.md) · [Historial de cambios](CHANGELOG.md) · [Licencia MIT](LICENSE)
