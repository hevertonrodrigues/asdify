# es: all source tasks and answers

Labels below are unblinded after review. Pass requires both meaning reviews and exact checks. A flagged answer is retained unchanged.

## modes-es-001 · numbers

Source task:

> Reescribe el informe para la responsable del invernadero. Explica el cambio medido y sus límites, sin proponer actuaciones nuevas.
> 
> Durante las dos primeras semanas de marzo de 2029 se midió el agua de riego de 80 bandejas con el sistema anterior. Durante las dos semanas siguientes se midieron otras 80 bandejas con el sistema nuevo. Cada bandeja tenía 24 plantas. La media pasó de 330 mL a 270 mL por bandeja y día, una reducción aproximada del 18,2%. La medición cubre solo las bandejas incluidas y no todo el consumo del invernadero. No se midió el agua usada para limpiar pasillos ni para otras variedades.
> 
> En el primer grupo había 50 bandejas con sustrato A y 30 con sustrato B. En el segundo había 40 de cada tipo. La responsable cree que el sustrato puede modificar la retención de agua, pero no ha calculado ese efecto. La temperatura media también fue distinta: 19 °C en el primer periodo y 22 °C en el segundo. No hay un grupo con el sistema antiguo a 22 °C. Por tanto, los registros no aíslan el efecto del sistema de riego de las diferencias de sustrato o temperatura.
> 
> Se excluyeron cinco bandejas del primer periodo y tres del segundo porque faltaban lecturas diarias. Los promedios citados se calcularon después de esas exclusiones. Una nota de publicidad afirma que el invernadero “ahorra casi una quinta parte de toda su agua”. Esa frase amplía el alcance de los datos. El resultado observado es una reducción de agua por bandeja y día entre los grupos registrados. No se midió el crecimiento de las plantas, el rendimiento final o el consumo total del edificio.
> 
> El equipo quiere saber si el cambio observado justifica estudiar el sistema durante más tiempo, pero todavía no ha tomado una decisión. El informe solicitado debe describir el resultado, no aprobar un despliegue ni asignar una fecha. No hay responsables o plazos registrados para una ampliación. Distingue las mediciones de las hipótesis y evita presentar el 18,2% como una reducción demostrada en cualquier condición futura.

### baseline: pass

```text
Durante las dos primeras semanas de marzo de 2029 se midieron 80 bandejas con el sistema de riego anterior y, durante las dos siguientes, otras 80 con el nuevo. Cada bandeja contenía 24 plantas. Tras excluir cinco bandejas del primer periodo y tres del segundo por falta de lecturas diarias, la media pasó de 330 a 270 mL por bandeja y día: una reducción observada de 60 mL, aproximadamente el 18,2%.

La comparación no permite atribuir toda esa diferencia al sistema de riego. El primer grupo tenía 50 bandejas con sustrato A y 30 con B; el segundo, 40 de cada tipo. La posible influencia del sustrato en la retención de agua es una hipótesis cuyo efecto no se ha calculado. Además, la temperatura media pasó de 19 °C a 22 °C y no hubo un grupo con el sistema anterior a 22 °C. Por tanto, no se ha aislado el efecto del sistema de las diferencias de sustrato o temperatura.

La medición corresponde únicamente al agua de riego de las bandejas incluidas. No cubre la limpieza de pasillos, otras variedades ni el consumo total del invernadero. Tampoco se midieron el crecimiento de las plantas o el rendimiento final. La afirmación publicitaria de que el invernadero «ahorra casi una quinta parte de toda su agua» excede lo que muestran los registros. El 18,2% describe la diferencia entre estos grupos, no una reducción demostrada en cualquier condición futura.

El equipo todavía no ha decidido si este resultado justifica estudiar el sistema durante más tiempo. No consta aprobación de un despliegue ni responsables o plazos para una ampliación.
```

### lite: pass

```text
Durante las dos primeras semanas de marzo de 2029 se midió el agua de riego de 80 bandejas con el sistema anterior. Durante las dos semanas siguientes se midieron otras 80 bandejas con el sistema nuevo. Cada bandeja tenía 24 plantas. La media pasó de 330 a 270 mL por bandeja y día: una reducción aproximada del 18,2% entre los grupos registrados. La medición cubre solo esas bandejas, no todo el consumo del invernadero. No se midió el agua usada para limpiar pasillos ni para otras variedades.

El primer grupo tenía 50 bandejas con sustrato A y 30 con sustrato B; el segundo, 40 de cada tipo. La responsable cree que el sustrato puede modificar la retención de agua, pero ese efecto no se ha calculado. La temperatura media fue de 19 °C en el primer periodo y de 22 °C en el segundo. No hubo un grupo con el sistema antiguo a 22 °C. Por tanto, los registros no permiten separar el efecto del sistema de riego de las diferencias de sustrato o temperatura.

Se excluyeron cinco bandejas del primer periodo y tres del segundo por falta de lecturas diarias. Los promedios se calcularon después de esas exclusiones. La afirmación publicitaria de que el invernadero “ahorra casi una quinta parte de toda su agua” amplía el alcance de los datos. Solo se observó una reducción del agua por bandeja y día entre los grupos registrados. No se midieron el crecimiento de las plantas, el rendimiento final ni el consumo total del edificio. El 18,2% no es una reducción demostrada para cualquier condición futura.

El equipo quiere saber si este cambio justifica estudiar el sistema durante más tiempo, pero aún no ha tomado una decisión. Este informe describe el resultado; no aprueba un despliegue ni fija una fecha. No hay responsables ni plazos registrados para una ampliación.
```

### full: pass

```text
El agua de riego medida bajó de 330 a 270 mL por bandeja y día: una reducción aproximada del 18,2% entre los grupos registrados. Este resultado no demuestra una reducción del consumo total del invernadero ni garantiza el mismo ahorro en condiciones futuras.

Durante las dos primeras semanas de marzo de 2029 se midieron 80 bandejas con el sistema anterior; durante las dos siguientes, otras 80 con el sistema nuevo. Cada bandeja tenía 24 plantas. Se excluyeron cinco bandejas del primer periodo y tres del segundo por falta de lecturas diarias. Los promedios se calcularon después de estas exclusiones.

Los grupos también diferían en sustrato y temperatura. El primero tenía 50 bandejas con sustrato A y 30 con B; el segundo, 40 de cada tipo. La responsable cree que el sustrato puede modificar la retención de agua, pero ese efecto no se ha calculado. La temperatura media fue de 19 °C en el primer periodo y 22 °C en el segundo. No hubo un grupo con el sistema antiguo a 22 °C. Por tanto, los registros no permiten separar el efecto del sistema de riego de las diferencias de sustrato o temperatura.

La medición cubre solo las bandejas incluidas. No se midió el agua para limpiar pasillos o regar otras variedades, ni el consumo total del edificio. Tampoco se midieron el crecimiento de las plantas o el rendimiento final. La afirmación publicitaria de que el invernadero “ahorra casi una quinta parte de toda su agua” amplía indebidamente el alcance de los datos.

El equipo quiere saber si el cambio observado justifica estudiar el sistema durante más tiempo, pero aún no ha decidido hacerlo. Este informe describe el resultado: no aprueba un despliegue ni fija una fecha. No hay responsables ni plazos registrados para una ampliación.
```

### ultra: pass

```text
El agua de riego medida bajó de 330 a 270 mL por bandeja y día: una reducción aproximada del 18,2% entre los grupos registrados, no una reducción demostrada del consumo total del invernadero ni en cualquier condición futura.

Durante las dos primeras semanas de marzo de 2029 se midieron 80 bandejas con el sistema anterior; durante las dos siguientes, otras 80 con el nuevo. Cada bandeja tenía 24 plantas. Se excluyeron cinco bandejas del primer periodo y tres del segundo por faltar lecturas diarias; las medias se calcularon después de esas exclusiones.

Los grupos y las temperaturas fueron distintos: el primero tenía 50 bandejas con sustrato A y 30 con B, a una temperatura media de 19 °C; el segundo, 40 de cada tipo, a 22 °C. La responsable cree que el sustrato puede modificar la retención de agua, pero ese efecto no se ha calculado. No hubo un grupo con el sistema anterior a 22 °C. Por ello, los registros no permiten separar el efecto del sistema de las diferencias de sustrato o temperatura.

La medición solo cubre las bandejas incluidas. No se midió el agua para limpiar pasillos ni para otras variedades, el crecimiento de las plantas, el rendimiento final o el consumo total del edificio. La afirmación publicitaria de que el invernadero “ahorra casi una quinta parte de toda su agua” excede estos datos.

El equipo quiere saber si el resultado justifica estudiar el sistema durante más tiempo, pero no ha decidido hacerlo. Este informe describe el resultado: no aprueba un despliegue ni fija una fecha. No hay responsables ni plazos registrados para una ampliación.
```

### off: pass

```text
Durante marzo de 2029, el consumo medio de agua de riego registrado pasó de 330 a 270 mL por bandeja y día: una disminución de 60 mL, aproximadamente el 18,2%. En las dos primeras semanas se midieron 80 bandejas con el sistema anterior y, en las dos siguientes, otras 80 con el sistema nuevo. Cada bandeja tenía 24 plantas. Se excluyeron cinco bandejas del primer periodo y tres del segundo por falta de lecturas diarias; los promedios se calcularon después de esas exclusiones.

Los grupos también diferían en sustrato y temperatura. El primero incluía 50 bandejas con sustrato A y 30 con B; el segundo, 40 de cada tipo. La temperatura media fue de 19 °C y 22 °C, respectivamente. La responsable considera que el sustrato puede afectar a la retención de agua, pero ese efecto no se ha calculado. Tampoco hubo un grupo con el sistema anterior a 22 °C. Por ello, los registros no permiten separar el efecto del sistema de riego de las diferencias de sustrato o temperatura.

La reducción observada corresponde al agua por bandeja y día de los grupos registrados, no al consumo total del invernadero. No se midió el agua utilizada para limpiar pasillos ni para otras variedades, ni el crecimiento de las plantas, el rendimiento final o el consumo total del edificio. La afirmación publicitaria de que el invernadero “ahorra casi una quinta parte de toda su agua” amplía indebidamente el alcance de los datos. El 18,2% tampoco demuestra una reducción aplicable a cualquier condición futura.

El equipo quiere determinar si este resultado justifica estudiar el sistema durante más tiempo, pero todavía no ha tomado una decisión. Este informe describe lo observado: no aprueba un despliegue ni establece responsables, fechas o plazos para una ampliación.
```

## modes-es-002 · conditions

Source task:

> Simplifica este reglamento ficticio de un taller de navegación para las personas inscritas. Conserva sus condiciones y excepciones. No añadas consejos de seguridad ajenos al texto.
> 
> Las personas inscritas pueden usar el embarcadero para las actividades programadas, pero no para salidas particulares. Para participar en la práctica con embarcación se exige inscripción confirmada y haber completado la sesión introductoria. Son necesarias ambas condiciones. Estar en la lista de espera no equivale a tener una inscripción confirmada. La dirección puede admitir una persona adicional si queda material disponible y hay un segundo instructor. La existencia de material por sí sola no garantiza la plaza, y abrirla sigue siendo opcional para la dirección.
> 
> Las personas menores de 13 años deben estar acompañadas por una persona adulta durante toda la actividad. Las de 13 a 16 años pueden asistir sin acompañante únicamente si presentan autorización escrita. A partir de los 17 años no se exige esa autorización. Toda persona acompañante debe registrarse, aunque no participe en la práctica. La autorización para asistir sin acompañante no permite entrar en las zonas cerradas del almacén.
> 
> Los bolsos deben quedarse en las taquillas. La recepción puede autorizar que un bolso con material de apoyo necesario permanezca junto a la persona que lo usa. Esta excepción no convierte todos los bolsos en material autorizado. Las fotografías son opcionales y solo se permiten en el área señalada. Para publicar una imagen de otra persona participante se requiere su permiso. El permiso para tomar una fotografía no es, por sí mismo, permiso para publicarla.
> 
> Si se descubre un desperfecto en una pieza del taller, se debe dejar de usar esa pieza y avisar al instructor. Antes de enviarla a revisión debe redactarse un registro del desperfecto. El reglamento no identifica quién lo causó ni quién redactará el registro. La dirección decidirá si la actividad puede continuar con otro material. Esa función no significa que la dirección haya causado el desperfecto o realizado la revisión. No atribuyas esas acciones a una persona por aparecer en una frase cercana.

### baseline: pass

```text
### Uso del embarcadero y participación
- El embarcadero solo puede usarse para las actividades programadas, no para salidas particulares.
- Para participar en la práctica con embarcación debes tener la inscripción confirmada y haber completado la sesión introductoria. Debes cumplir ambas condiciones; estar en lista de espera no es tener una inscripción confirmada.
- La dirección puede admitir a una persona adicional si queda material disponible y hay un segundo instructor. Aunque se cumplan esas condiciones, abrir la plaza es opcional; disponer de material no garantiza la admisión.

### Edad y acompañantes
- Menores de 13 años: deben estar acompañados por una persona adulta durante toda la actividad.
- De 13 a 16 años: solo pueden asistir sin acompañante si presentan autorización escrita.
- Desde los 17 años: no se exige esa autorización.
- Toda persona acompañante debe registrarse, aunque no participe en la práctica.
- La autorización para asistir sin acompañante no permite acceder a las zonas cerradas del almacén.

### Bolsos y fotografías
- Los bolsos deben quedarse en las taquillas. La recepción puede permitir que un bolso con material de apoyo necesario permanezca junto a quien lo usa. Esta excepción no autoriza otros bolsos automáticamente.
- Hacer fotografías es opcional y solo está permitido en el área señalada.
- Para publicar una imagen de otra persona participante necesitas su permiso. El permiso para tomar la fotografía no basta para publicarla.

### Desperfectos
- Si descubres un desperfecto, deja de usar la pieza afectada y avisa al instructor.
- Antes de enviarla a revisión debe redactarse un registro del desperfecto. El reglamento no indica quién lo causó ni quién redactará el registro.
- La dirección decidirá si la actividad puede continuar con otro material. Esa responsabilidad no implica que haya causado el desperfecto ni realizado la revisión.
```

### lite: pass

```text
Las personas inscritas pueden usar el embarcadero para las actividades programadas, no para salidas particulares. Para participar en la práctica con embarcación deben cumplir ambas condiciones: tener la inscripción confirmada y haber completado la sesión introductoria. Estar en la lista de espera no equivale a tener la inscripción confirmada. La dirección puede admitir a una persona adicional si queda material disponible y hay un segundo instructor. El material disponible por sí solo no garantiza la plaza; abrirla sigue siendo opcional para la dirección.

Las personas menores de 13 años deben estar acompañadas por una persona adulta durante toda la actividad. Las de 13 a 16 años solo pueden asistir sin acompañante si presentan autorización escrita. A partir de los 17 años no se exige esa autorización. Toda persona acompañante debe registrarse, aunque no participe en la práctica. La autorización para asistir sin acompañante no permite entrar en las zonas cerradas del almacén.

Los bolsos deben quedarse en las taquillas. La recepción puede autorizar que un bolso con material de apoyo necesario permanezca junto a la persona que lo usa. Esta excepción no autoriza todos los bolsos. Las fotografías son opcionales y solo se permiten en el área señalada. Para publicar una imagen de otra persona participante se necesita su permiso. El permiso para tomar una fotografía no basta para publicarla.

Si se descubre un desperfecto en una pieza del taller, se debe dejar de usar esa pieza y avisar al instructor. Antes de enviarla a revisión debe redactarse un registro del desperfecto. El reglamento no indica quién lo causó ni quién redactará el registro. La dirección decidirá si la actividad puede continuar con otro material. Esa función no implica que la dirección haya causado el desperfecto o realizado la revisión.
```

### full: pass

```text
### Acceso y participación
Las personas inscritas pueden usar el embarcadero para las actividades programadas, no para salidas particulares.

Para participar en la práctica con embarcación deben cumplirse ambas condiciones:
- Tener la inscripción confirmada. Estar en lista de espera no basta.
- Haber completado la sesión introductoria.

La dirección puede admitir a una persona adicional si queda material disponible y hay un segundo instructor. Deben cumplirse ambas condiciones, pero la dirección no está obligada a abrir esa plaza. Tener material disponible por sí solo no garantiza la admisión.

### Edad y acompañamiento
- Menores de 13 años: deben estar acompañados por una persona adulta durante toda la actividad.
- De 13 a 16 años: pueden asistir sin acompañante solo con autorización escrita.
- A partir de los 17 años: no se exige esa autorización.

Toda persona acompañante debe registrarse, aunque no participe en la práctica. La autorización para asistir sin acompañante no permite entrar en las zonas cerradas del almacén.

### Bolsos y fotografías
Los bolsos deben quedarse en las taquillas. La recepción puede autorizar que un bolso con material de apoyo necesario permanezca junto a quien lo usa. La excepción no autoriza todos los bolsos.

Las fotografías son opcionales y solo se permiten en el área señalada. Para publicar una imagen de otra persona participante hace falta su permiso. El permiso para tomar una fotografía no equivale al permiso para publicarla.

### Desperfectos
Si se descubre un desperfecto, se debe dejar de usar la pieza afectada y avisar al instructor. Antes de enviarla a revisión debe redactarse un registro del desperfecto. El reglamento no identifica quién causó el daño ni quién redactará el registro.

La dirección decidirá si la actividad puede continuar con otro material. Esta función no implica que haya causado el desperfecto o realizado la revisión.
```

### ultra: pass

```text
**Acceso y participación**
- El embarcadero solo puede usarse para actividades programadas, no para salidas particulares.
- Para la práctica con embarcación se necesitan ambas condiciones: inscripción confirmada y sesión introductoria completada. La lista de espera no equivale a inscripción confirmada.
- La dirección puede admitir una persona adicional si hay material disponible y un segundo instructor. Cumplir esas condiciones no obliga a abrir la plaza; disponer solo de material no la garantiza.

**Edad y acompañamiento**
- Menores de 13 años: acompañamiento de una persona adulta durante toda la actividad.
- De 13 a 16 años: pueden asistir sin acompañante únicamente con autorización escrita.
- A partir de 17 años: no se exige esa autorización.
- Toda persona acompañante debe registrarse, participe o no en la práctica.
- La autorización para asistir sin acompañante no permite entrar en las zonas cerradas del almacén.

**Bolsos y fotografías**
- Los bolsos deben quedarse en las taquillas. Recepción puede autorizar que un bolso con material de apoyo necesario permanezca junto a quien lo usa. La excepción no autoriza todos los bolsos.
- Las fotografías son opcionales y solo se permiten en el área señalada. Publicar una imagen de otra persona participante requiere su permiso. El permiso para fotografiar no implica permiso para publicar.

**Desperfectos**
Si se descubre un desperfecto, debe dejar de usarse la pieza y avisarse al instructor. Antes de enviarla a revisión, debe redactarse un registro del desperfecto. No se identifica quién lo causó ni quién redactará el registro.

La dirección decidirá si la actividad puede continuar con otro material. Esa función no implica que haya causado el desperfecto ni realizado la revisión.
```

### off: pass

```text
### Uso del embarcadero y participación

Las personas inscritas pueden usar el embarcadero para las actividades programadas, no para salidas particulares.

Para participar en la práctica con embarcación hay que cumplir ambas condiciones:
- Tener la inscripción confirmada.
- Haber completado la sesión introductoria.

Estar en la lista de espera no significa tener una inscripción confirmada. La dirección puede admitir a una persona adicional si queda material disponible y hay un segundo instructor. Aunque se cumplan estas condiciones, admitirla es opcional; disponer de material por sí solo no garantiza una plaza.

### Edad y acompañamiento

- Menores de 13 años: deben estar acompañados por una persona adulta durante toda la actividad.
- De 13 a 16 años: pueden asistir sin acompañante solo si presentan autorización escrita.
- A partir de los 17 años: no se exige esa autorización.

Toda persona acompañante debe registrarse, aunque no participe en la práctica. La autorización para asistir sin acompañante no permite entrar en las zonas cerradas del almacén.

### Bolsos y fotografías

Los bolsos deben quedarse en las taquillas. La recepción puede permitir que un bolso con material de apoyo necesario permanezca junto a quien lo usa. Esta excepción no autoriza los demás bolsos.

Las fotografías son opcionales y solo pueden tomarse en el área señalada. Para publicar una imagen de otra persona participante se necesita su permiso. El permiso para tomar la fotografía no supone permiso para publicarla.

### Desperfectos

Si se descubre un desperfecto en una pieza, se debe dejar de usar esa pieza y avisar al instructor. Antes de enviarla a revisión, debe redactarse un registro del desperfecto. El reglamento no indica quién causó el desperfecto ni quién redactará el registro.

La dirección decidirá si la actividad puede continuar con otro material. Esa responsabilidad no significa que haya causado el desperfecto o realizado la revisión.
```

## modes-es-003 · technical

Source task:

> Convierte estas notas en una entrega de turno clara. Al final, indica los asuntos pendientes sin añadir soluciones no autorizadas.
> 
> El servicio de telemetría recibe lecturas de estaciones remotas. Cada lectura incluye station_id y seq. La combinación de esos dos campos permite reconocer una lectura ya recibida. El nombre visible de la estación no se usa para deduplicar porque puede cambiar. Una lectura se guarda antes de enviar la confirmación a la estación. Si el proceso se detiene después de guardar pero antes de confirmar, la estación puede reenviarla. Ese reenvío no demuestra que la lectura se haya guardado dos veces.
> 
> HTTP 202 significa que el servidor ha aceptado la lectura para procesarla, no que ya esté en el resumen diario. HTTP 200 en la consulta del resumen significa que la consulta terminó correctamente, no que todas las estaciones hayan enviado datos. La ausencia de una estación en el resumen puede deberse a retraso, falta de envío u otra causa aún no comprobada. La etiqueta “estación caída” del panel es una categoría visual y no una prueba del estado físico de la estación.
> 
> A las 06:45 UTC del 9 de febrero de 2029 se recibieron 180 mensajes: 150 lecturas nuevas, 24 reenvíos de lecturas existentes y 6 mensajes sin seq, que se rechazaron. Los 150 registros nuevos se confirmaron en la base. El resumen mostraba inicialmente 142 porque se actualiza cada 10 minutos. Aún no se ha revisado el siguiente resumen. La diferencia inicial no prueba que falten ocho registros en la base. Los seis mensajes rechazados no se convirtieron en lecturas nuevas.
> 
> La siguiente persona de turno debe comprobar el resumen después de la próxima actualización. El equipo de campo debe investigar los mensajes sin seq, pero las notas no identifican a una persona ni dan plazo. No se ha autorizado inventar números de secuencia, borrar reenvíos o cambiar el intervalo de actualización. Mantén separados aceptación, almacenamiento, confirmación y presencia en el resumen. No conviertas una comprobación pendiente en una comprobación ya realizada.

### baseline: pass

```text
## Entrega de turno — 9 de febrero de 2029, 06:45 UTC

### Recepción y almacenamiento
Se recibieron 180 mensajes:
- 150 lecturas nuevas, cuyos registros se confirmaron en la base de datos.
- 24 reenvíos de lecturas existentes.
- 6 mensajes sin seq, rechazados; no se convirtieron en lecturas nuevas.

La deduplicación utiliza la combinación station_id y seq, no el nombre visible de la estación, que puede cambiar. Una lectura se guarda antes de enviar la confirmación a la estación. Si el proceso se detiene entre ambos pasos, puede haber un reenvío; esto no demuestra un almacenamiento duplicado.

### Interpretación de respuestas y resumen
HTTP 202 indica aceptación para procesar la lectura, no su presencia en el resumen diario. HTTP 200 al consultar el resumen indica que la consulta terminó correctamente, no que todas las estaciones hayan enviado datos.

El resumen inicial mostraba 142 lecturas y se actualiza cada 10 minutos. Todavía no se ha revisado el siguiente resumen. La diferencia respecto a los 150 registros nuevos confirmados no prueba que falten ocho registros en la base.

La ausencia de una estación en el resumen puede deberse a retraso, falta de envío u otra causa no comprobada. La etiqueta visual «estación caída» no demuestra el estado físico de la estación.

### Asuntos pendientes
- La siguiente persona de turno debe comprobar el resumen después de la próxima actualización; la comprobación sigue pendiente.
- El equipo de campo debe investigar los seis mensajes sin seq. No consta una persona concreta asignada ni un plazo.
- No está autorizado inventar números de secuencia, borrar reenvíos ni cambiar el intervalo de actualización.
```

### lite: pass

```text
Entrega de turno — 9 de febrero de 2029, 06:45 UTC

El servicio de telemetría recibe lecturas de estaciones remotas. Cada lectura incluye station_id y seq; la combinación permite reconocer una lectura ya recibida. El nombre visible de la estación no se usa para deduplicar porque puede cambiar. La lectura se guarda antes de enviar la confirmación a la estación. Si el proceso se detiene entre ambos pasos, la estación puede reenviarla. Ese reenvío no demuestra que se haya guardado dos veces.

HTTP 202 indica que el servidor ha aceptado la lectura para procesarla, no que ya aparezca en el resumen diario. HTTP 200 en la consulta del resumen indica que la consulta terminó correctamente, no que todas las estaciones hayan enviado datos. Una estación puede faltar en el resumen por retraso, falta de envío u otra causa aún no comprobada. La etiqueta “estación caída” del panel es una categoría visual, no una prueba del estado físico de la estación.

A las 06:45 UTC se recibieron 180 mensajes: 150 lecturas nuevas, 24 reenvíos de lecturas existentes y 6 mensajes sin seq, que se rechazaron. Los 150 registros nuevos se confirmaron en la base. Los seis mensajes rechazados no se convirtieron en lecturas nuevas. El resumen mostraba inicialmente 142 registros y se actualiza cada 10 minutos. Aún no se ha revisado el siguiente resumen. La diferencia inicial no prueba que falten ocho registros en la base.

Asuntos pendientes

- La siguiente persona de turno debe comprobar el resumen después de la próxima actualización. Esta comprobación aún no se ha realizado.
- El equipo de campo debe investigar los mensajes sin seq. No se ha identificado a una persona responsable ni fijado un plazo.

No se ha autorizado inventar números de secuencia, borrar reenvíos ni cambiar el intervalo de actualización.
```

### full: pass

```text
## Entrega de turno

### Estado registrado
A las 06:45 UTC del 9 de febrero de 2029 se recibieron 180 mensajes:
- 150 lecturas nuevas, cuyos registros se confirmaron en la base.
- 24 reenvíos de lecturas existentes.
- 6 mensajes sin seq, que se rechazaron y no se convirtieron en lecturas nuevas.

El resumen mostraba inicialmente 142 registros y se actualiza cada 10 minutos. Aún no se ha revisado el siguiente resumen. La diferencia inicial de ocho registros no demuestra que falten registros en la base.

### Cómo interpretar el procesamiento
Cada lectura incluye station_id y seq. Su combinación permite reconocer una lectura ya recibida. El nombre visible de la estación no se usa para deduplicar porque puede cambiar.

La lectura se guarda antes de enviar la confirmación a la estación. Si el proceso se detiene entre ambos pasos, la estación puede reenviarla. Ese reenvío no demuestra que se haya guardado dos veces.

La aceptación, el almacenamiento, la confirmación a la estación y la presencia en el resumen son estados distintos:
- HTTP 202 indica que el servidor aceptó la lectura para procesarla, no que ya figure en el resumen diario.
- HTTP 200 en la consulta del resumen indica que la consulta terminó correctamente, no que todas las estaciones hayan enviado datos.

Una estación ausente del resumen puede tener retraso, no haber enviado datos o estar ausente por otra causa aún no comprobada. La etiqueta “estación caída” es una categoría visual del panel, no una prueba del estado físico de la estación.

### Asuntos pendientes
- La siguiente persona de turno debe comprobar el resumen después de la próxima actualización. Esta comprobación sigue pendiente.
- El equipo de campo debe investigar los mensajes sin seq. No se identifica una persona responsable ni un plazo.

No se ha autorizado inventar números de secuencia, borrar reenvíos ni cambiar el intervalo de actualización.
```

### ultra: pass

```text
**Entrega de turno — 9 de febrero de 2029, 06:45 UTC**

Se recibieron 180 mensajes: 150 lecturas nuevas, 24 reenvíos de lecturas existentes y 6 mensajes sin seq, que se rechazaron y no generaron lecturas nuevas. Los 150 registros nuevos se confirmaron en la base. El resumen mostraba inicialmente 142; se actualiza cada 10 minutos. Aún no se ha revisado el siguiente resumen: la diferencia inicial no demuestra que falten ocho registros en la base.

**Interpretación del servicio**
- El servicio recibe lecturas de estaciones remotas. Cada lectura incluye station_id y seq; su combinación identifica lecturas ya recibidas. El nombre visible no se usa para deduplicar porque puede cambiar.
- La lectura se guarda antes de enviar la confirmación a la estación. Si el proceso se detiene entre ambos pasos, la estación puede reenviarla. El reenvío no demuestra un almacenamiento duplicado.
- HTTP 202 indica aceptación para procesamiento, no presencia en el resumen diario. Aceptación, almacenamiento, confirmación a la estación y presencia en el resumen son estados distintos.
- HTTP 200 al consultar el resumen indica que la consulta terminó correctamente, no que todas las estaciones hayan enviado datos.
- Una estación ausente del resumen puede tener retraso, no haber enviado datos u otra causa aún no comprobada. La etiqueta “estación caída” es una categoría visual, no una prueba de su estado físico.

**Pendientes**
- La siguiente persona de turno debe comprobar el resumen después de la próxima actualización.
- El equipo de campo debe investigar los mensajes sin seq. No se identifica una persona concreta ni un plazo.
- No se ha autorizado inventar números de secuencia, borrar reenvíos ni cambiar el intervalo de actualización.
```

### off: pass

```text
## Entrega de turno — 9 de febrero de 2029

### Registro de las 06:45 UTC

Se recibieron 180 mensajes:
- 150 lecturas nuevas, cuyos registros se confirmaron en la base.
- 24 reenvíos de lecturas existentes.
- 6 mensajes sin seq, que se rechazaron y no se convirtieron en lecturas nuevas.

El resumen mostraba inicialmente 142 lecturas. Se actualiza cada 10 minutos y aún no se ha revisado el siguiente resumen. La diferencia inicial de ocho no demuestra que falten registros en la base.

### Funcionamiento e interpretación

Cada lectura incluye station_id y seq. La combinación de ambos campos permite reconocer una lectura ya recibida. El nombre visible de la estación no se utiliza para deduplicar porque puede cambiar.

La lectura se guarda antes de enviar la confirmación a la estación. Si el proceso se detiene entre el almacenamiento y la confirmación, la estación puede reenviarla. Ese reenvío no demuestra que se haya almacenado dos veces.

HTTP 202 indica que el servidor ha aceptado la lectura para procesarla; no acredita su almacenamiento, el envío de la confirmación a la estación ni su presencia en el resumen diario. HTTP 200 al consultar el resumen indica que la consulta terminó correctamente, no que todas las estaciones hayan enviado datos.

La ausencia de una estación en el resumen puede deberse a un retraso, a falta de envío o a otra causa todavía no comprobada. La etiqueta “estación caída” es una categoría visual del panel, no una prueba del estado físico de la estación.

### Asuntos pendientes

- La siguiente persona de turno debe comprobar el resumen después de la próxima actualización. Esta comprobación todavía no se ha realizado.
- El equipo de campo debe investigar los seis mensajes sin seq. No se identifica a una persona concreta ni se establece un plazo.

No se ha autorizado inventar números de secuencia, borrar reenvíos ni modificar el intervalo de actualización.
```

## modes-es-004 · summary

Source task:

> Resume el estudio para el responsable de transporte en dos párrafos como máximo. Conserva las limitaciones que afectan a la conclusión.
> 
> Durante una semana se colocó un cartel con un código QR en la salida este de la estación Central. Respondieron 210 personas de forma voluntaria. No se eligió a las personas al azar y no se recogieron respuestas en otras salidas. El formulario solo estaba en español. Quienes no usaban esa salida, no tenían acceso al formulario o no quisieron responder no aparecen en los datos. No hay un recuento de cuántas personas vieron el cartel, por lo que no se puede calcular una tasa de respuesta respecto a quienes pasaron por allí.
> 
> De las 210 respuestas, 147 apoyaban añadir una salida de autobús a las 22:30, 42 no la apoyaban y 21 no tenían una preferencia definida. El 70% de apoyo corresponde a quienes respondieron, no a todas las personas usuarias de la estación ni a toda la ciudad. La pregunta trataba de una salida adicional de lunes a viernes. No preguntaba por sábados, domingos o cambios en otras líneas. El apoyo declarado no demuestra cuántas personas usarían realmente el autobús.
> 
> La unidad de planificación ha propuesto una prueba de seis semanas. La propuesta depende de disponer de vehículo y conductor y todavía no está aprobada. No se ha indicado fecha de inicio. Una presentación antigua decía que el servicio nocturno “se ampliará de forma permanente”; ese compromiso no consta en el estudio. El informe tampoco calcula el coste de la prueba o el efecto sobre otras salidas.
> 
> Un campo opcional recibió comentarios de 56 personas. Veinticuatro mencionaron trabajo, 17 estudios y 12 ocio. Una respuesta podía mencionar varios motivos. Los grupos no son exclusivos y sus números no deben presentarse como una distribución de las 210 personas. La planificación no comparó las respuestas con horarios laborales ni con registros de viajes. El estudio describe preferencias de un grupo autoseleccionado y puede orientar una prueba, pero no establece demanda real o representatividad de todas las personas usuarias.

### baseline: pass

```text
Durante una semana, 210 personas respondieron voluntariamente a un formulario en español accesible mediante un QR en la salida este de la estación Central. De ellas, 147 (70%) apoyaban añadir una salida de autobús a las 22:30 de lunes a viernes, 42 no la apoyaban y 21 no tenían una preferencia definida. La muestra no fue aleatoria ni incluyó otras salidas; quedan fuera quienes no usaron esa salida, no accedieron al formulario o no quisieron responder. Sin un recuento de quienes vieron el cartel, no puede calcularse la tasa de respuesta. El 70% corresponde solo a quienes respondieron: no representa a todas las personas usuarias ni demuestra uso real del servicio. Tampoco se preguntó por fines de semana u otras líneas. En el campo opcional comentaron 56 personas: 24 mencionaron trabajo, 17 estudios y 12 ocio. Los motivos podían solaparse y no constituyen una distribución de las 210 respuestas; no se contrastaron con horarios laborales ni registros de viajes.

La unidad de planificación propone una prueba de seis semanas, condicionada a disponer de vehículo y conductor, pero aún no está aprobada ni tiene fecha de inicio. El estudio no respalda el compromiso de ampliación permanente que figuraba en una presentación antigua y no calcula el coste de la prueba ni su efecto sobre otras salidas. Las preferencias de este grupo autoseleccionado pueden orientar una prueba, pero no establecen demanda real ni representatividad del conjunto de personas usuarias.
```

### lite: pass

```text
Durante una semana, un cartel con un código QR en la salida este de la estación Central recogió 210 respuestas voluntarias: 147 personas (70%) apoyaban una salida adicional de autobús a las 22:30 de lunes a viernes, 42 no la apoyaban y 21 no tenían una preferencia definida. No se preguntó por fines de semana ni por cambios en otras líneas. El 70% corresponde solo a quienes respondieron, no a todas las personas usuarias ni a toda la ciudad; tampoco demuestra cuántas usarían el autobús. La muestra fue autoseleccionada, no aleatoria: no se recogieron respuestas en otras salidas y el formulario solo estaba en español. Quedan fuera quienes no usaban esa salida, no tenían acceso al formulario o no quisieron responder. No se contó cuántas personas vieron el cartel, por lo que no puede calcularse una tasa de respuesta respecto a quienes pasaron por allí. En el campo opcional comentaron 56 personas: 24 mencionaron trabajo, 17 estudios y 12 ocio. Una respuesta podía incluir varios motivos; los grupos no son exclusivos ni representan una distribución de las 210 personas. No se contrastaron las respuestas con horarios laborales ni con registros de viajes.

La unidad de planificación propone una prueba de seis semanas, condicionada a disponer de vehículo y conductor. Todavía no está aprobada ni tiene fecha de inicio. El compromiso de una presentación antigua de que el servicio nocturno “se ampliará de forma permanente” no consta en el estudio. Tampoco se calcularon el coste de la prueba ni su efecto sobre otras salidas. El estudio describe preferencias de un grupo autoseleccionado y puede orientar una prueba, pero no establece la demanda real ni la representatividad de todas las personas usuarias.
```

### full: pass

```text
El estudio recoge preferencias de un grupo autoseleccionado, no demuestra demanda real ni representa a todas las personas usuarias. Durante una semana, 210 personas respondieron voluntariamente mediante un cartel con código QR en la salida este de la estación Central: 147 (70%) apoyaban una salida adicional de autobús a las 22:30 de lunes a viernes, 42 no la apoyaban y 21 no tenían una preferencia definida. No se preguntó por fines de semana ni cambios en otras líneas; el apoyo declarado no indica cuántas personas usarían el autobús. No hubo selección aleatoria ni recogida de respuestas en otras salidas. El formulario solo estaba en español y excluye a quienes no usaban esa salida, no tenían acceso al formulario o no quisieron responder. No se contó cuántas personas vieron el cartel, por lo que no puede calcularse una tasa de respuesta respecto a quienes pasaron por allí. En el campo opcional comentaron 56 personas: 24 mencionaron trabajo, 17 estudios y 12 ocio. Una respuesta podía incluir varios motivos; estos grupos se solapan y no son una distribución de las 210 personas. No se contrastaron las respuestas con horarios laborales ni registros de viajes.

El estudio puede orientar una prueba. La unidad de planificación propone una de seis semanas, condicionada a disponer de vehículo y conductor, pero todavía no está aprobada ni tiene fecha de inicio. No se calcularon su coste ni el efecto sobre otras salidas. La afirmación de una presentación antigua de que el servicio nocturno “se ampliará de forma permanente” no es un compromiso recogido en el estudio.
```

### ultra: pass

```text
De las 210 personas que respondieron voluntariamente durante una semana al formulario del cartel con código QR en la salida este de la estación Central, 147 (70%) apoyaban una salida adicional de autobús a las 22:30 de lunes a viernes, 42 no la apoyaban y 21 no tenían preferencia definida. Ese 70% corresponde solo a quienes respondieron, no a todas las personas usuarias ni a toda la ciudad. La muestra fue autoseleccionada, no aleatoria; no se recogieron respuestas en otras salidas y el formulario solo estaba en español. Quedaron fuera quienes no usaban esa salida, no tenían acceso al formulario o no quisieron responder. No se contó cuántas personas vieron el cartel, por lo que no puede calcularse la tasa de respuesta respecto a quienes pasaron por allí. No se preguntó por fines de semana ni cambios en otras líneas; el apoyo declarado no demuestra uso real. En el campo opcional comentaron 56 personas: 24 mencionaron trabajo, 17 estudios y 12 ocio. Podían mencionar varios motivos: los grupos se solapan y no representan una distribución de las 210 personas. No se contrastaron las respuestas con horarios laborales ni registros de viajes.

El estudio describe preferencias de ese grupo y puede orientar una prueba, pero no establece demanda real ni representatividad de todas las personas usuarias. Planificación propone una prueba de seis semanas, condicionada a disponer de vehículo y conductor, aún sin aprobar ni fecha de inicio. El estudio no respalda el compromiso de una presentación antigua de que el servicio nocturno “se ampliará de forma permanente”, ni calcula el coste de la prueba o su efecto sobre otras salidas.
```

### off: pass

```text
Durante una semana, un cartel con un código QR en la salida este de la estación Central obtuvo 210 respuestas voluntarias: 147 apoyaban una salida adicional de autobús a las 22:30 de lunes a viernes, 42 no la apoyaban y 21 no tenían una preferencia definida. El 70% de apoyo corresponde únicamente a quienes respondieron. La muestra fue autoseleccionada, no aleatoria; no se recogieron respuestas en otras salidas y el formulario solo estaba en español. Quedan fuera quienes no usaban esa salida, no tenían acceso al formulario o no quisieron responder. Como no se contó cuántas personas vieron el cartel, no puede calcularse una tasa de respuesta respecto a quienes pasaron por allí. No se preguntó por fines de semana ni por cambios en otras líneas, y el apoyo declarado no demuestra uso real ni representatividad de todas las personas usuarias o de la ciudad. En el campo opcional comentaron 56 personas: 24 mencionaron trabajo, 17 estudios y 12 ocio. Los motivos podían coincidir en una misma respuesta y no constituyen una distribución de las 210 personas. Tampoco se compararon las respuestas con horarios laborales o registros de viajes.

La unidad de planificación ha propuesto una prueba de seis semanas, condicionada a disponer de vehículo y conductor; todavía no está aprobada ni tiene fecha de inicio. El estudio puede orientar esa prueba, pero no establece demanda real. No calcula su coste ni el efecto sobre otras salidas. La afirmación de una presentación antigua de que el servicio nocturno “se ampliará de forma permanente” no es un compromiso que conste en el estudio.
```

## modes-es-005 · analysis

Source task:

> Responde a la tesorera: ¿el fondo operativo cubre la exposición confirmada sin usar la reserva? Incluye el cálculo y la incertidumbre pertinente. No recomiendes nuevas fuentes de dinero.
> 
> La asociación dispone de 6.900 euros en su fondo operativo. La reserva separada de 1.800 euros no entra en esta comparación. El saldo ya incluye las cuotas recibidas este trimestre, así que no deben sumarse otra vez. Los gastos confirmados pendientes son 2.100 euros por la sala, 850 por iluminación, 540 por impresión y 390 por seguro. La sala se pagará en una señal de 600 euros y un resto de 1.500: ambos importes forman los 2.100 euros, no son cargos adicionales.
> 
> El transporte de las obras se ha contratado por 1.250 euros. Un vehículo extra costaría 450 euros si se añadieran más de seis obras grandes. Por ahora se han confirmado cuatro obras grandes; el vehículo extra no está contratado. No se sabe si llegarán más propuestas. Una empresa ha mencionado una aportación de 900 euros, pero no hay acuerdo firmado ni dinero recibido. Esa posibilidad no es ingreso confirmado.
> 
> Una versión anterior del presupuesto incluía 300 euros para una inauguración con refrigerio. La comisión eliminó esa partida y no debe recuperarse en la comparación. La impresión incluye ya los carteles; una línea informativa sobre 120 carteles no es otra compra. Tampoco hay un valor asignado al trabajo voluntario, y no se puede tratar como efectivo disponible. La pregunta no pide elegir proveedores o calcular el valor de las obras.
> 
> El resultado debe sumar una sola vez los cinco gastos confirmados y compararlos con el fondo operativo. Después debe señalar el posible vehículo extra como una condición que puede cambiar el saldo, sin convertirla en gasto ya aprobado. No hay fecha de pago de las facturas ni autorización para usar la reserva. No inventes un plazo, una aprobación de gasto adicional o una promesa de la empresa. La tesorera necesita una conclusión respaldada por esta lista, no un plan de financiación.

### baseline: flagged

```text
Sí. El fondo operativo cubre los gastos confirmados de la exposición sin usar la reserva:

2.100 € (sala) + 850 € (iluminación) + 540 € (impresión) + 390 € (seguro) + 1.250 € (transporte) = 5.130 €.

Frente a los 6.900 € disponibles, quedan 1.770 €. La señal de 600 € y el resto de 1.500 € ya forman parte del coste de la sala; los carteles están incluidos en impresión. Las cuotas recibidas ya están en el saldo. No se incluyen el refrigerio eliminado, el trabajo voluntario como efectivo ni la aportación empresarial de 900 €, que no está firmada ni recibida. La reserva separada de 1.800 € queda fuera del cálculo.

El vehículo extra de 450 € solo sería necesario si se añadieran más de seis obras grandes. Actualmente hay cuatro confirmadas y no está contratado; se desconoce si llegarán más propuestas. Si ese gasto se añadiera, el total sería 5.580 € y quedarían 1.320 € del fondo operativo. No consta aprobación de ese gasto adicional, fechas de pago ni autorización para usar la reserva.
```

Review notes: El cálculo es correcto, pero atribuye necesidad al vehículo extra sin respaldo en la fuente. / El cálculo es correcto, pero introduce una necesidad del vehículo extra que la fuente no establece.

### lite: pass

```text
Sí. El fondo operativo de 6.900 euros cubre los cinco gastos confirmados sin usar la reserva separada de 1.800 euros.

Gastos confirmados: 2.100 euros de sala + 850 de iluminación + 540 de impresión + 390 de seguro + 1.250 de transporte = 5.130 euros.

Saldo restante: 6.900 − 5.130 = 1.770 euros.

La señal de 600 euros y el resto de 1.500 ya forman los 2.100 euros de la sala. Las cuotas recibidas este trimestre ya están incluidas en el fondo. Los carteles están incluidos en la impresión; la referencia a 120 carteles no añade otra compra. No se incluye la partida eliminada de 300 euros para refrigerio ni se trata el trabajo voluntario como efectivo disponible.

El vehículo extra costaría 450 euros si se añadieran más de seis obras grandes. Ahora hay cuatro confirmadas y el vehículo extra no está contratado. No se sabe si llegarán más propuestas. Si se contratara ese vehículo, el saldo restante sería de 1.320 euros. La posible aportación empresarial de 900 euros no se cuenta: no hay acuerdo firmado ni dinero recibido.

No constan fechas de pago de las facturas ni autorización para usar la reserva.
```

### full: pass

```text
Sí. El fondo operativo de 6.900 euros cubre los cinco gastos confirmados de la exposición sin usar la reserva separada de 1.800 euros.

Gastos confirmados pendientes:
- Sala: 2.100 euros, incluidos la señal de 600 y el resto de 1.500.
- Iluminación: 850 euros.
- Impresión: 540 euros, incluidos los carteles; la referencia a 120 carteles no es otra compra.
- Seguro: 390 euros.
- Transporte contratado: 1.250 euros.

Total: 2.100 + 850 + 540 + 390 + 1.250 = 5.130 euros.
Saldo restante: 6.900 − 5.130 = 1.770 euros.

El vehículo extra costaría 450 euros si se añadieran más de seis obras grandes. Por ahora hay cuatro confirmadas, no se sabe si llegarán más propuestas y el vehículo extra no está contratado. Si se cumpliera esa condición y se añadiera el vehículo, el saldo quedaría en 1.320 euros; no es un gasto ya aprobado.

La posible aportación empresarial de 900 euros no se cuenta: no hay acuerdo firmado ni dinero recibido. Las cuotas del trimestre ya están incluidas en el saldo y no se suman de nuevo. Se excluyen los 300 euros de refrigerio eliminados por la comisión y el trabajo voluntario, que no tiene valor asignado ni constituye efectivo disponible.

La conclusión se limita a los importes registrados. No constan fechas de pago de las facturas ni autorización para usar la reserva.
```

### ultra: pass

```text
Sí. El fondo operativo cubre los cinco gastos confirmados sin usar la reserva:

2.100 € (sala) + 850 € (iluminación) + 540 € (impresión) + 390 € (seguro) + 1.250 € (transporte) = **5.130 €**.

6.900 € − 5.130 € = **1.770 € de saldo restante**. La reserva separada de 1.800 € queda fuera de la comparación y no hay autorización para usarla.

El vehículo extra costaría 450 € si se añadieran más de seis obras grandes. Hay cuatro confirmadas; el vehículo no está contratado y se desconoce si llegarán más propuestas. Si ese gasto se incorporara, el saldo sería 1.320 €; no es un gasto ya aprobado.

No se suman de nuevo las cuotas del trimestre, ya incluidas en el fondo. La señal de 600 € y el resto de 1.500 € forman los 2.100 € de la sala. Los 120 carteles están incluidos en impresión. Se excluyen los 300 € de refrigerio eliminados, la posible aportación empresarial de 900 € —sin acuerdo firmado ni dinero recibido— y el trabajo voluntario, sin valor asignado y no disponible como efectivo. No constan fechas de pago de las facturas.
```

### off: pass

```text
Sí. El fondo operativo de 6.900 euros cubre los cinco gastos confirmados sin utilizar la reserva separada de 1.800 euros.

Gastos confirmados: 2.100 euros de sala + 850 de iluminación + 540 de impresión + 390 de seguro + 1.250 de transporte = 5.130 euros.

Saldo restante: 6.900 − 5.130 = 1.770 euros.

La señal de 600 euros y el resto de 1.500 ya forman los 2.100 euros de la sala. Las cuotas recibidas ya están en el saldo y los carteles están incluidos en la impresión. No se suman nuevamente esos conceptos, ni se incluye el refrigerio eliminado, ni se trata el trabajo voluntario como efectivo disponible.

El vehículo extra costaría 450 euros si se añadieran más de seis obras grandes. Por ahora hay cuatro confirmadas y el vehículo extra no está contratado. Si esa condición se cumpliera y se contratara, el saldo bajaría a 1.320 euros. No se sabe si llegarán más propuestas. La posible aportación empresarial de 900 euros no se incluye porque no hay acuerdo firmado ni dinero recibido. No constan fechas de pago de las facturas ni autorización para utilizar la reserva.
```

## modes-es-006 · exact-format

Source task:

> Devuelve solamente un objeto JSON con las claves "room_id", "seats", "open" y "note". Copia los tres valores fijos del registro final. Escribe la nota en español, basada únicamente en el estado confirmado.
> 
> Historial: El primer plano de la sala "Lectura-4" indicaba 18 asientos. Se trataba de una propuesta antes de instalar los muebles. Después se discutió dejar un pasillo más ancho. Esa conversación no aprobó abrir la sala al público. La revisión de mobiliario contó 16 asientos utilizables y concluyó que los otros dos propuestos no se instalarían con la distribución actual. El valor antiguo de 18 no representa la capacidad registrada al final.
> 
> La coordinadora señaló que la sala seguiría cerrada hasta recibir la revisión del sistema de ventilación. La revisión de asientos no sustituye a la de ventilación. El informe de mobiliario llegó ayer, pero el de ventilación no está disponible. La sala aparece en el catálogo de espacios porque el sistema permite registrar salas cerradas. Ese registro no es prueba de apertura. Un borrador de un cartel decía “ya disponible”; la coordinadora no confirmó esa frase y no forma parte del registro final.
> 
> Registro final: room_id = "Lectura-4"; seats = 16; open = false. La capacidad registrada es de 16 personas y la sala sigue cerrada a la espera de la revisión de ventilación. No hay fecha de apertura aprobada. Tampoco se ha autorizado otra redistribución de muebles. La nota debe describir este estado sin repetir toda la historia de planificación o confundir una sala cerrada temporalmente con una cancelación definitiva.
> 
> En note, explica en una o dos frases que hay 16 asientos registrados y que la sala no está abierta porque la revisión de ventilación sigue pendiente. No afirmes que esa revisión ya se ha superado. seats debe ser un número y open un booleano, no cadenas de texto. Las claves pertenecen a una interfaz y deben mantenerse en inglés. No añadas un bloque de código, una introducción o comentarios fuera del objeto.

### baseline: pass

```text
{"room_id":"Lectura-4","seats":16,"open":false,"note":"Hay 16 asientos registrados y la sala sigue cerrada porque la revisión de ventilación está pendiente. No hay fecha de apertura aprobada."}
```

### lite: pass

```text
{"room_id":"Lectura-4","seats":16,"open":false,"note":"Hay 16 asientos registrados. La sala sigue cerrada porque la revisión de ventilación está pendiente."}
```

### full: pass

```text
{"room_id":"Lectura-4","seats":16,"open":false,"note":"Hay 16 asientos registrados. La sala sigue cerrada porque la revisión de ventilación está pendiente."}
```

### ultra: pass

```text
{"room_id":"Lectura-4","seats":16,"open":false,"note":"Hay 16 asientos registrados y la sala sigue cerrada porque la revisión de ventilación está pendiente. No hay fecha de apertura aprobada."}
```

### off: pass

```text
{"room_id":"Lectura-4","seats":16,"open":false,"note":"Hay 16 asientos registrados y la sala sigue cerrada porque la revisión de ventilación está pendiente. No hay fecha de apertura aprobada."}
```

## modes-es-007 · voice

Source task:

> Edita este texto en primera persona para que sea más fluido. Mantén el humor suave y la diferencia entre lo que sé y lo que supongo. No lo conviertas en publicidad de la librería.
> 
> Abrí la trastienda con una lista de tareas y la confianza de quien todavía no ha visto la trastienda. En la mesa había trece sujetalibros y una caja de etiquetas sin ordenar. Los sujetalibros parecían preparados para sostener una biblioteca o una conversación incómoda. Mi encargo era contarlos, no comprobar su resistencia. Anoté trece. No sé si todos pueden sujetar libros pesados: no hice esa prueba y su aspecto solemne no es una certificación.
> 
> Esperamos volver a abrir la sala de lectura en septiembre. La esperanza es necesaria porque la ventana sigue pendiente de reparación y aún no han llegado dos estanterías. Sol aprobó el texto de la invitación, pero eso no autoriza abrir la sala ni fija una fecha. No se han enviado invitaciones. Podría adornar el párrafo con un día exacto, pero ni la lista ni los sujetalibros parecen dispuestos a proporcionarlo.
> 
> Una clienta antigua recordó que las etiquetas procedían de una feria de 2004. La ficha del almacén dice “origen sin confirmar”, y no hay factura o fotografía fechada que permita unir ambas cosas. Guardé el recuerdo junto a la ficha sin sustituirla. Es una pista, no una procedencia comprobada. Tampoco sabemos quién metió las etiquetas en la caja. La clienta las reconoció, pero eso no significa que las guardara.
> 
> Antes de salir, devolví los trece sujetalibros a la mesa. Nadie los ha trasladado aún a la nueva sala. Si se hace el traslado, habrá que actualizar su ubicación en el registro. Por ahora, el avance más concreto es que la puerta ya no tropieza con la caja de etiquetas porque la moví unos centímetros. Conserva ese final pequeño y práctico. No añadas promesas sobre actividades futuras, plazas disponibles o experiencias inolvidables para el público.

### baseline: flagged

```text
Abrí la trastienda con una lista de tareas y la confianza de quien todavía no ha visto la trastienda. Sobre la mesa había trece sujetalibros y una caja de etiquetas sin ordenar. Los sujetalibros parecían listos para sostener una biblioteca o una conversación incómoda. Mi encargo era contarlos, no probar su resistencia, así que anoté trece. No sé si todos pueden sujetar libros pesados: no hice esa prueba, y su aspecto solemne no es una certificación.

Esperamos volver a abrir la sala de lectura en septiembre, aunque la ventana sigue pendiente de reparación y todavía faltan dos estanterías por llegar. Sol aprobó el texto de la invitación, pero esa aprobación no autoriza la apertura ni fija una fecha. No hemos enviado invitaciones. Podría adornar este párrafo con un día exacto, pero ni la lista ni los sujetalibros parecen dispuestos a proporcionarlo.

Una clienta antigua recordó que las etiquetas procedían de una feria de 2004. La ficha del almacén dice «origen sin confirmar», y no hay factura ni fotografía fechada que permita vincularlas con aquella feria. Guardé el recuerdo junto a la ficha, sin sustituirla: es una pista, no una procedencia comprobada. Tampoco sabemos quién puso las etiquetas en la caja. Que la clienta las reconociera no significa que las guardara.

Antes de salir, devolví los trece sujetalibros a la mesa. Nadie los ha trasladado todavía a la nueva sala; si se hace, habrá que actualizar su ubicación en el registro. Por ahora, el avance más concreto es que la puerta ya no tropieza con la caja de etiquetas: la moví unos centímetros.
```

Review notes: Otherwise faithful and fluent, but changes the actor and scope of the unsent-invitations statement. / Edición fluida que mantiene humor, incertidumbres, condiciones y cierre práctico.

### lite: pass

```text
Abrí la trastienda con una lista de tareas y la confianza de quien todavía no ha visto la trastienda. En la mesa había trece sujetalibros y una caja de etiquetas sin ordenar. Los sujetalibros parecían preparados para sostener una biblioteca o una conversación incómoda. Mi encargo era contarlos, no comprobar su resistencia. Anoté trece. No sé si todos pueden sujetar libros pesados: no hice esa prueba, y su aspecto solemne no es una certificación.

Esperamos volver a abrir la sala de lectura en septiembre. La esperanza es necesaria porque la ventana sigue pendiente de reparación y aún no han llegado dos estanterías. Sol aprobó el texto de la invitación, pero eso no autoriza abrir la sala ni fija una fecha. No se han enviado invitaciones. Podría adornar el párrafo con un día exacto, pero ni la lista ni los sujetalibros parecen dispuestos a proporcionarlo.

Una clienta antigua recordó que las etiquetas procedían de una feria de 2004. La ficha del almacén dice “origen sin confirmar”, y no hay factura ni fotografía fechada que permita vincular las etiquetas con esa feria. Guardé el recuerdo junto a la ficha, sin sustituirla. Es una pista, no una procedencia comprobada. Tampoco sabemos quién metió las etiquetas en la caja. La clienta las reconoció, pero eso no significa que las guardara.

Antes de salir, devolví los trece sujetalibros a la mesa. Nadie los ha trasladado aún a la nueva sala. Si se hace el traslado, habrá que actualizar su ubicación en el registro. Por ahora, el avance más concreto es que la puerta ya no tropieza con la caja de etiquetas porque la moví unos centímetros.
```

### full: pass

```text
Abrí la trastienda con una lista de tareas y la confianza de quien todavía no ha visto la trastienda. En la mesa había trece sujetalibros y una caja de etiquetas sin ordenar. Los sujetalibros parecían preparados para sostener una biblioteca o una conversación incómoda. Mi encargo era contarlos, no comprobar su resistencia. Anoté trece. No sé si todos pueden sujetar libros pesados: no los probé, y su aspecto solemne no es una certificación.

Esperamos volver a abrir la sala de lectura en septiembre, aunque la ventana sigue pendiente de reparación y aún faltan dos estanterías por llegar. Sol aprobó el texto de la invitación, pero eso no autoriza la apertura ni fija una fecha. No se han enviado invitaciones. Podría adornar este párrafo con un día exacto, pero ni la lista ni los sujetalibros parecen dispuestos a proporcionarlo.

Una antigua clienta recordó que las etiquetas procedían de una feria de 2004. La ficha del almacén dice “origen sin confirmar”, y no hay factura ni fotografía fechada que vincule las etiquetas con esa feria. Guardé el recuerdo junto a la ficha, sin sustituirla: es una pista, no una procedencia comprobada. Tampoco sabemos quién metió las etiquetas en la caja. Que la clienta las reconociera no significa que las guardara.

Antes de salir, devolví los trece sujetalibros a la mesa. Nadie los ha trasladado aún a la nueva sala. Si se trasladan, habrá que actualizar su ubicación en el registro. Por ahora, el avance más concreto es que la puerta ya no tropieza con la caja de etiquetas: la moví unos centímetros.
```

### ultra: pass

```text
Abrí la trastienda con una lista de tareas y la confianza de quien aún no la ha visto. Sobre la mesa había trece sujetalibros y una caja de etiquetas sin ordenar. Parecían capaces de sostener una biblioteca o una conversación incómoda. Mi encargo era contarlos, no probar su resistencia: anoté trece. No sé si aguantan libros pesados; no lo comprobé y su aspecto solemne no es una certificación.

Esperamos reabrir la sala de lectura en septiembre, aunque la ventana sigue pendiente de reparación y faltan dos estanterías por llegar. Sol aprobó el texto de la invitación, no la apertura ni una fecha. No se han enviado invitaciones. Podría añadir un día exacto, pero ni la lista ni los sujetalibros parecen dispuestos a proporcionarlo.

Una clienta antigua recordó que las etiquetas procedían de una feria de 2004. La ficha del almacén dice “origen sin confirmar”; no hay factura ni fotografía fechada que vincule las etiquetas con esa feria. Guardé el recuerdo junto a la ficha, sin sustituirla: es una pista, no una procedencia comprobada. Tampoco sabemos quién las metió en la caja. Reconocerlas no significa haberlas guardado.

Antes de salir, devolví los trece sujetalibros a la mesa. Nadie los ha trasladado aún a la nueva sala; si se trasladan, habrá que actualizar su ubicación en el registro. Por ahora, el avance más concreto es que la puerta ya no tropieza con la caja de etiquetas: la moví unos centímetros.
```

### off: pass

```text
Abrí la trastienda con una lista de tareas y la confianza de quien todavía no ha visto la trastienda. Sobre la mesa había trece sujetalibros y una caja de etiquetas sin ordenar. Los sujetalibros parecían preparados para sostener una biblioteca o una conversación incómoda, pero mi encargo era contarlos, no comprobar su resistencia. Anoté trece. No sé si todos pueden sostener libros pesados: no hice esa prueba, y su aspecto solemne no es una certificación.

Esperamos volver a abrir la sala de lectura en septiembre. De momento, necesitamos esa esperanza: la ventana sigue pendiente de reparación y aún no han llegado dos estanterías. Sol aprobó el texto de la invitación, pero eso no autoriza la apertura ni fija una fecha. No se han enviado invitaciones. Podría adornar el párrafo con un día exacto, pero ni la lista ni los sujetalibros parecen dispuestos a proporcionarlo.

Una clienta antigua recordó que las etiquetas procedían de una feria de 2004. La ficha del almacén dice «origen sin confirmar», y no hay factura ni fotografía fechada que permita vincular las etiquetas con aquella feria. Guardé el recuerdo junto a la ficha, sin sustituirla: es una pista, no una procedencia comprobada. Tampoco sabemos quién metió las etiquetas en la caja. La clienta las reconoció, pero eso no significa que las guardara.

Antes de salir, devolví los trece sujetalibros a la mesa. Nadie los ha trasladado aún a la nueva sala. Si se hace el traslado, habrá que actualizar su ubicación en el registro. Por ahora, el avance más concreto es que la puerta ya no tropieza con la caja de etiquetas porque la moví unos centímetros.
```

## modes-es-008 · scope

Source task:

> Con el texto siguiente, responde solo a esta pregunta en tres frases como máximo: ¿debe recibirse la solicitud el miércoles y qué ocurre si llega después? No resumas los demás trámites del premio.
> 
> Regla vigente: La solicitud de participación debe recibirse antes de las 18:00 UTC del miércoles para entrar en la revisión del lunes siguiente. Enviar antes de esa hora no basta si el sistema la recibe después. Las solicitudes tardías pasan al siguiente periodo de revisión disponible. La secretaría no garantiza que ese periodo sea el lunes de la semana posterior. El plazo se refiere a la solicitud, no al envío de las imágenes en alta resolución. Estas imágenes pueden entregarse hasta las 12:00 UTC del día anterior a la revisión, siempre que la solicitud haya llegado a tiempo.
> 
> La convocatoria admite series de entre cuatro y ocho fotografías. El grupo tiene seis listas y está valorando añadir una séptima. Cada archivo debe incluir título y autoría. La regla permite una sola solicitud por grupo. La secretaría ha reservado dos jornadas para comprobar que los archivos se abren, pero no ha asignado horarios individuales. El jurado tendrá cinco integrantes. Esos datos no modifican el límite de recepción de la solicitud.
> 
> En la edición anterior se aceptaban solicitudes hasta el jueves. Ese calendario ya no está vigente. Una nota informal del grupo dice “todo para el miércoles”, pero la norma distingue solicitud e imágenes. No conviertas las imágenes en un requisito del miércoles. Tampoco atribuyas a la secretaría la decisión sobre el mérito de las fotografías: su revisión inicial comprueba que los archivos se pueden abrir.
> 
> La persona que pregunta solo necesita entender el plazo y la consecuencia de una llegada tardía. Los tamaños de serie, metadatos, composición del jurado y plazo de imágenes son contexto que puede omitirse. La solicitud aún no se ha recibido, y no hay autorización para pedir una excepción o dar por confirmada la participación. Mantén la diferencia entre enviar y recibir, así como la ausencia de una fecha garantizada para las solicitudes tardías.

### baseline: pass

```text
Para entrar en la revisión del lunes siguiente, la solicitud debe recibirse antes de las 18:00 UTC del miércoles; enviarla antes no basta si el sistema la recibe después. Si llega fuera de plazo, pasa al siguiente periodo de revisión disponible, sin garantía de que sea el lunes de la semana posterior.
```

### lite: pass

```text
Para entrar en la revisión del lunes siguiente, la solicitud debe recibirse antes de las 18:00 UTC del miércoles; enviarla antes de esa hora no basta si el sistema la recibe después. Si llega fuera de plazo, pasa al siguiente periodo de revisión disponible. La secretaría no garantiza que ese periodo sea el lunes de la semana posterior.
```

### full: pass

```text
Para entrar en la revisión del lunes siguiente, la solicitud debe recibirse antes de las 18:00 UTC del miércoles; no basta con enviarla antes si el sistema la recibe después. Si llega tarde, pasa al siguiente periodo de revisión disponible, sin garantía de que sea el lunes de la semana posterior.
```

### ultra: pass

```text
Para entrar en la revisión del lunes siguiente, la solicitud debe recibirse antes de las 18:00 UTC del miércoles; enviarla antes no basta si el sistema la recibe después. Si llega fuera de plazo, pasa al siguiente periodo de revisión disponible, sin garantía de que sea el lunes de la semana posterior.
```

### off: pass

```text
Para entrar en la revisión del lunes siguiente, la solicitud debe recibirse antes de las 18:00 UTC del miércoles; enviarla antes no basta si el sistema la recibe después. Si llega fuera de plazo, pasa al siguiente periodo de revisión disponible, sin garantía de que sea el lunes de la semana posterior.
```

## modes-es-009 · ambiguity

Source task:

> Reescribe esta nota para la comunidad del edificio. Conserva las lagunas y los conflictos sin escoger una versión.
> 
> El registro dice: “El 03/11, René habló con Vale después de que se cambiara el contador.” No consta el año ni el formato de la fecha. El registro reúne mensajes locales con día/mes y mensajes de un proveedor que usa mes/día. La frase se pegó sin indicar su origen. Por eso 03/11 puede ser 3 de noviembre u 11 de marzo. No se especifica la función de René o Vale. La forma pasiva indica un cambio anterior a la conversación, pero no identifica a quien cambió el contador.
> 
> Una factura del 11 de marzo de 2029 menciona el equipo C-32 y una visita. No dice cuándo se instaló el equipo. Un parte de acceso del 3 de noviembre de 2029 menciona C-23 y tiene una firma ilegible. El equipo no ha confirmado que esos documentos correspondan al cambio del registro. No existe una corrección que iguale C-32 y C-23. Que una fecha sea compatible con una interpretación no demuestra que esa interpretación sea la correcta.
> 
> El panel mostró cuatro lecturas interrumpidas en el día anterior al registro y ninguna en el día posterior. No hay hora del cambio físico. La desaparición de las interrupciones en ese periodo es una observación, no prueba de que el cambio haya sido la causa o de que el problema no vaya a repetirse. Un técnico escribió “posible desgaste”, pero no adjuntó el resultado de examinar el contador. El desgaste no se ha confirmado.
> 
> Un borrador anterior decía que Vale cambió el contador desgastado el 3 de noviembre y René confirmó la reparación. Ese borrador añade persona responsable, fecha interpretada, diagnóstico y confirmación que el registro no proporciona. La comunidad pidió contrastar los documentos, pero no asignó a nadie esa tarea ni fijó plazo. La nueva nota debe conservar la conversación posterior al cambio y hacer visibles la fecha, el actor, la relación entre documentos, la causa y el resultado duradero como cuestiones pendientes.

### baseline: pass

```text
Nota para la comunidad

El registro indica que René habló con Vale después de que se cambiara el contador, con fecha «03/11». No consta el año ni el origen de la frase: como el registro mezcla formatos día/mes y mes/día, podría tratarse del 3 de noviembre o del 11 de marzo. Tampoco se especifican las funciones de René y Vale ni quién realizó el cambio.

La factura del 11 de marzo de 2029 menciona el equipo C-32 y una visita, pero no una fecha de instalación. El parte de acceso del 3 de noviembre de 2029 menciona C-23 y lleva una firma ilegible. No se ha confirmado que ninguno corresponda al cambio registrado ni existe una corrección que permita equiparar ambos identificadores. La coincidencia con una posible interpretación de la fecha no resuelve la duda.

El panel mostró cuatro lecturas interrumpidas el día anterior al registro y ninguna el posterior. No consta la hora del cambio físico, por lo que esta observación no demuestra que el cambio eliminara las interrupciones ni que el problema no vaya a repetirse. La anotación técnica «posible desgaste» no incluye resultados de un examen del contador; el diagnóstico sigue sin confirmar.

El borrador anterior atribuía el cambio a Vale, lo fechaba el 3 de noviembre, daba por confirmado el desgaste y afirmaba que René había confirmado la reparación. Esos datos no están acreditados por el registro. Siguen pendientes la fecha, la persona responsable del cambio, la relación entre los documentos, la causa del problema y la duración del resultado observado. La comunidad pidió contrastar los documentos, pero no asignó responsable ni plazo.
```

### lite: pass

```text
El registro dice: “El 03/11, René habló con Vale después de que se cambiara el contador.” No consta el año ni el formato de la fecha. El registro reúne mensajes locales con formato día/mes y mensajes de un proveedor que usa mes/día; la frase se pegó sin indicar su origen. Por tanto, 03/11 puede ser 3 de noviembre u 11 de marzo. No se especifican las funciones de René y Vale ni quién cambió el contador. Solo consta que el cambio fue anterior a la conversación.

Una factura del 11 de marzo de 2029 menciona el equipo C-32 y una visita, pero no indica cuándo se instaló. Un parte de acceso del 3 de noviembre de 2029 menciona C-23 y tiene una firma ilegible. El equipo no ha confirmado que estos documentos correspondan al cambio del registro. Tampoco existe una corrección que iguale C-32 y C-23. Que una fecha sea compatible con una interpretación no demuestra que esa interpretación sea correcta.

El panel mostró cuatro lecturas interrumpidas el día anterior al registro y ninguna el día posterior. No consta la hora del cambio físico. La desaparición de las interrupciones en ese periodo es una observación: no prueba que el cambio fuera la causa ni que el problema no vaya a repetirse. Un técnico escribió “posible desgaste”, pero no adjuntó el resultado de examinar el contador. El desgaste no está confirmado.

Un borrador anterior afirmaba que Vale cambió el contador desgastado el 3 de noviembre y que René confirmó la reparación. El registro no proporciona esa persona responsable, esa interpretación de la fecha, ese diagnóstico ni esa confirmación. La comunidad pidió contrastar los documentos, pero no asignó la tarea ni fijó un plazo. Siguen pendientes la fecha del cambio, quién lo realizó, la relación entre los documentos, la causa de las interrupciones y la confirmación de un resultado duradero.
```

### full: pass

```text
El registro dice: “El 03/11, René habló con Vale después de que se cambiara el contador.” Confirma que la conversación fue posterior al cambio, pero no identifica a quien cambió el contador ni las funciones de René y Vale. Tampoco consta el año o el formato de la fecha: 03/11 puede ser 3 de noviembre u 11 de marzo. El registro mezcla mensajes locales con formato día/mes y mensajes de un proveedor que usa mes/día; se desconoce el origen de esta frase.

Los documentos no resuelven esas dudas. Una factura del 11 de marzo de 2029 menciona el equipo C-32 y una visita, pero no la fecha de instalación. Un parte de acceso del 3 de noviembre de 2029 menciona C-23 y lleva una firma ilegible. El equipo no ha confirmado que estos documentos correspondan al cambio registrado, y no existe una corrección que iguale C-32 y C-23. La coincidencia de una fecha con una interpretación posible no demuestra que sea la correcta.

El panel mostró cuatro lecturas interrumpidas el día anterior al registro y ninguna el día posterior. No consta la hora del cambio físico. Esta observación no demuestra que el cambio eliminara las interrupciones ni que el problema no vaya a repetirse. Un técnico escribió “posible desgaste”, pero no adjuntó resultados del examen del contador: el desgaste sigue sin confirmarse.

El borrador anterior atribuía el cambio a Vale, lo fechaba el 3 de noviembre, daba por confirmado el desgaste y decía que René había confirmado la reparación. El registro no respalda esas afirmaciones. Siguen pendientes la fecha, la persona responsable del cambio, la relación entre los documentos, la causa del problema y el resultado duradero. La comunidad pidió contrastar los documentos, pero no asignó la tarea ni fijó un plazo.
```

### ultra: pass

```text
El registro dice: “El 03/11, René habló con Vale después de que se cambiara el contador.” No consta el año ni el origen de la frase: el registro mezcla mensajes locales con formato día/mes y mensajes del proveedor con mes/día. Por tanto, 03/11 puede ser 3 de noviembre u 11 de marzo. El cambio fue anterior a la conversación, pero no se identifica quién lo hizo ni qué función tenían René o Vale.

La factura del 11 de marzo de 2029 menciona C-32 y una visita, no la fecha de instalación. El parte de acceso del 3 de noviembre de 2029 menciona C-23 y lleva una firma ilegible. No se ha confirmado que estos documentos correspondan al cambio registrado ni existe una corrección que iguale C-32 y C-23. La coincidencia con una posible fecha no resuelve la ambigüedad.

El panel mostró cuatro lecturas interrumpidas el día anterior al registro y ninguna el posterior. Sin la hora del cambio físico, esta observación no demuestra que el cambio eliminara las interrupciones ni que no vayan a repetirse. Un técnico escribió “posible desgaste”, sin adjuntar resultados de un examen del contador: el desgaste sigue sin confirmar.

El borrador anterior atribuía el cambio a Vale, fijaba el 3 de noviembre, afirmaba desgaste y decía que René confirmó la reparación. El registro no respalda esas afirmaciones. Siguen pendientes la fecha, la persona responsable del cambio, la relación entre los documentos, la causa y el resultado duradero. La comunidad pidió contrastar los documentos, pero no asignó responsable ni plazo.
```

### off: pass

```text
El registro dice: «El 03/11, René habló con Vale después de que se cambiara el contador». La conversación fue posterior al cambio, pero no se identifica a quien lo realizó ni se especifican las funciones de René y Vale. Tampoco consta el año ni el formato de la fecha: el registro mezcla mensajes locales con día/mes y mensajes de un proveedor con mes/día, y esta frase se incorporó sin indicar su origen. Por tanto, 03/11 puede significar 3 de noviembre u 11 de marzo.

Una factura del 11 de marzo de 2029 menciona el equipo C-32 y una visita, pero no indica cuándo se instaló. Un parte de acceso del 3 de noviembre de 2029 menciona C-23 y tiene una firma ilegible. No se ha confirmado que estos documentos correspondan al cambio descrito en el registro, ni existe una corrección que equipare C-32 y C-23. La coincidencia de una fecha con alguna de las interpretaciones posibles no permite elegirla como correcta.

El panel mostró cuatro lecturas interrumpidas el día anterior al registro y ninguna el día posterior. No se conoce la hora del cambio físico. Esta desaparición de las interrupciones es una observación: no demuestra que el cambio fuera su causa ni que el problema no vaya a repetirse. Un técnico escribió «posible desgaste», pero no adjuntó resultados de un examen del contador; el desgaste sigue sin confirmarse.

El borrador anterior atribuía el cambio a Vale, lo fechaba el 3 de noviembre, daba por confirmado el desgaste y afirmaba que René había confirmado la reparación. El registro no respalda esas afirmaciones. Siguen pendientes la fecha, la identidad de quien cambió el contador, la relación entre los documentos, la causa de las interrupciones y la confirmación de un resultado duradero. La comunidad pidió contrastar los documentos, pero no asignó esa tarea ni fijó un plazo.
```

## modes-es-010 · evidence

Source task:

> Prepara una nota breve para una reunión de compras sobre el ensayo de dos embalajes. Describe lo que se observó y lo que queda sin comprobar. No recomiendes una compra.
> 
> El proveedor ensayó Embalaje Uno y Embalaje Dos con cinco cajas de cada modelo. Todas se fabricaron con cartón del mismo lote. En la prueba de compresión, la carga media registrada antes de deformación fue de 820 N para Uno y 910 N para Dos. No se proporcionaron valores por caja, desviaciones, intervalos de confianza o pruebas estadísticas. La media mayor de Dos es una observación en estas condiciones, no evidencia de significación estadística.
> 
> Las cinco cajas de Uno se ensayaron antes de las de Dos. La humedad se midió únicamente al comienzo de la mañana. Las cajas tenían formas distintas, aunque el volumen interior era igual. Por tanto, el ensayo no separa el efecto del material del de la forma, el orden o una posible variación de humedad. Lo realizó un empleado del proveedor; no figura una persona observadora independiente.
> 
> El almacén exige que cada caja aceptada soporte al menos 850 N antes de deformarse. La media de Uno está por debajo y la de Dos por encima, pero sin datos individuales no se sabe cuántas cajas de cada grupo cumplieron. Una media superior al umbral no garantiza que todas las cajas lo alcancen. El almacén apila cajas durante varios días y a veces recibe mercancía húmeda. El ensayo no evaluó duración del apilamiento, cartón húmedo o vibración durante el transporte.
> 
> El folleto dice que Dos es “apto para las rutas más exigentes”. El ensayo no define esa expresión ni mide todas las condiciones de una ruta. No se han suministrado precios, tasas de rotura reales o costes de reutilización, así que no se puede comparar el coste de uso con estos datos. La nota debe separar la diferencia de medias de las limitaciones del diseño. No afirme cumplimiento garantizado de todas las cajas, verificación independiente, durabilidad a largo plazo o mejor relación entre coste y resultado.

### baseline: pass

```text
Nota para la reunión de compras

El proveedor ensayó cinco cajas de cada embalaje, fabricadas con cartón del mismo lote. La carga media antes de deformación fue de 820 N para Uno y 910 N para Dos. La media de Dos fue mayor en este ensayo, pero no se aportaron datos individuales, medidas de dispersión ni pruebas estadísticas que permitan valorar la significación de la diferencia.

Uno se ensayó primero; la humedad solo se midió al comienzo y las formas eran distintas, aunque el volumen interior era igual. El diseño no permite separar el efecto del material del de la forma, el orden o posibles cambios de humedad. No consta observación independiente: realizó el ensayo un empleado del proveedor.

El requisito del almacén es de al menos 850 N por caja. Aunque las medias quedan a ambos lados del umbral, se desconoce cuántas cajas cumplieron. Tampoco se evaluaron el apilamiento durante varios días, el cartón húmedo ni la vibración del transporte. La afirmación «apto para las rutas más exigentes» no queda verificada. Sin precios, tasas reales de rotura ni costes de reutilización, no puede compararse el coste de uso.
```

### lite: pass

```text
El proveedor ensayó cinco cajas de Embalaje Uno y cinco de Embalaje Dos, todas fabricadas con cartón del mismo lote. En compresión, la carga media antes de deformarse fue de 820 N para Uno y 910 N para Dos. La media de Dos fue mayor en estas condiciones, pero no se aportaron valores individuales, desviaciones, intervalos de confianza ni pruebas estadísticas que permitan establecer significación estadística.

Las cinco cajas de Uno se ensayaron antes que las de Dos y la humedad solo se midió al comienzo de la mañana. Las formas eran distintas, aunque el volumen interior era igual. El diseño no separa el efecto del material del de la forma, el orden o una posible variación de humedad. El ensayo lo realizó un empleado del proveedor; no consta una persona observadora independiente.

El almacén exige que cada caja aceptada soporte al menos 850 N antes de deformarse. La media de Uno queda por debajo y la de Dos por encima, pero sin datos individuales no se sabe cuántas cajas cumplieron. Una media superior al umbral no garantiza que todas lo alcancen. Tampoco se evaluaron el apilamiento durante varios días, el cartón húmedo ni la vibración durante el transporte, aunque el almacén apila cajas durante varios días y a veces recibe mercancía húmeda.

El folleto describe Dos como “apto para las rutas más exigentes”, pero el ensayo no define esa expresión ni mide todas las condiciones de una ruta. Sin precios, tasas de rotura reales ni costes de reutilización, estos datos tampoco permiten comparar el coste de uso.
```

### full: pass

```text
El proveedor ensayó cinco cajas de Embalaje Uno y cinco de Embalaje Dos, todas fabricadas con cartón del mismo lote. La carga media antes de deformarse fue de 820 N para Uno y 910 N para Dos. La mayor media de Dos es una observación de este ensayo, no evidencia de significación estadística: no se aportaron valores individuales, desviaciones, intervalos de confianza ni pruebas estadísticas.

El diseño no permite separar el efecto del material del de la forma, el orden o una posible variación de humedad. Las cajas tenían formas distintas y el mismo volumen interior; las cinco de Uno se probaron antes que las de Dos, y la humedad solo se midió al comienzo de la mañana. El ensayo lo realizó un empleado del proveedor y no consta una persona observadora independiente.

El almacén exige que cada caja aceptada soporte al menos 850 N antes de deformarse. La media de Uno queda por debajo y la de Dos por encima, pero sin datos individuales no se sabe cuántas cajas cumplieron; una media superior no garantiza que todas alcancen el umbral. No se evaluaron el apilamiento durante varios días, el cartón húmedo ni la vibración del transporte, aunque el almacén apila durante días y a veces recibe mercancía húmeda.

La frase del folleto sobre Dos, “apto para las rutas más exigentes”, no está definida ni queda demostrada por un ensayo que no mide todas las condiciones de una ruta. Sin precios, tasas de rotura reales ni costes de reutilización, tampoco puede compararse el coste de uso.
```

### ultra: pass

```text
El proveedor ensayó cinco cajas de Embalaje Uno y cinco de Embalaje Dos, todas con cartón del mismo lote. La carga media antes de deformarse fue de 820 N para Uno y 910 N para Dos. La mayor media de Dos es una observación del ensayo, no evidencia de significación estadística: faltan datos por caja, desviaciones, intervalos de confianza y pruebas estadísticas.

Se ensayaron primero las cinco cajas de Uno; la humedad solo se midió al comienzo de la mañana. Las formas eran distintas, aunque el volumen interior era igual. El diseño no separa los efectos del material, la forma, el orden y una posible variación de humedad. Lo realizó un empleado del proveedor y no consta una persona observadora independiente.

El almacén exige al menos 850 N por caja aceptada. La media de Uno queda por debajo y la de Dos por encima, pero se desconoce cuántas cajas cumplieron: la media no garantiza el cumplimiento individual. Tampoco se evaluaron el apilamiento durante varios días, el cartón húmedo ni la vibración del transporte, aunque el almacén apila durante días y a veces recibe mercancía húmeda.

La afirmación del folleto de que Dos es “apto para las rutas más exigentes” no queda comprobada: el ensayo no define la expresión ni cubre todas las condiciones de una ruta. Sin precios, tasas reales de rotura ni costes de reutilización, tampoco puede compararse el coste de uso.
```

### off: pass

```text
El proveedor ensayó cinco cajas de Embalaje Uno y cinco de Embalaje Dos, todas fabricadas con cartón del mismo lote. La carga media antes de deformación fue de 820 N para Uno y 910 N para Dos. Dos presentó una media mayor en estas condiciones, pero no se facilitaron datos individuales, desviaciones, intervalos de confianza ni pruebas estadísticas que permitan establecer significación estadística.

Se ensayaron primero las cinco cajas de Uno y la humedad solo se midió al inicio de la mañana. Las formas eran distintas, aunque el volumen interior era igual. El diseño no permite separar el efecto del material de los de la forma, el orden o una posible variación de humedad. La prueba la realizó un empleado del proveedor; no consta una persona observadora independiente.

El almacén exige al menos 850 N por caja antes de deformarse. La media de Uno quedó por debajo y la de Dos por encima, pero se desconoce cuántas cajas cumplieron: superar el umbral en promedio no garantiza que todas lo alcancen. No se evaluaron el apilamiento durante varios días, el cartón húmedo ni la vibración del transporte, condiciones relevantes para el uso del almacén.

La afirmación del folleto de que Dos es «apto para las rutas más exigentes» no queda acreditada: el ensayo no define esa expresión ni evalúa todas las condiciones de una ruta. Sin precios, tasas de rotura reales ni costes de reutilización, tampoco puede compararse el coste de uso.
```

## modes-es-011 · numbers

Source task:

> Reescribe: “La proporción de solicitudes incompletas pasó del 15% al 12%. Bajó 3 puntos porcentuales, o un 20% respecto a la proporción inicial. Se revisaron 200 solicitudes cada mes, solo del canal presencial.”

### baseline: pass

```text
La proporción de solicitudes incompletas se redujo del 15% al 12%: una bajada de 3 puntos porcentuales, equivalente al 20% de la proporción inicial. Cada mes se revisaron 200 solicitudes, exclusivamente del canal presencial.
```

### lite: pass

```text
La proporción de solicitudes incompletas pasó del 15% al 12%. Bajó 3 puntos porcentuales, equivalentes a un 20% de la proporción inicial. Cada mes se revisaron 200 solicitudes, solo del canal presencial.
```

### full: pass

```text
La proporción de solicitudes incompletas bajó del 15% al 12%: una reducción de 3 puntos porcentuales, equivalente al 20% de la proporción inicial. Cada mes se revisaron 200 solicitudes, todas del canal presencial.
```

### ultra: pass

```text
La proporción de solicitudes incompletas bajó del 15% al 12%: 3 puntos porcentuales, equivalentes al 20% de la proporción inicial. Se revisaron 200 solicitudes al mes, solo del canal presencial.
```

### off: pass

```text
La proporción de solicitudes incompletas disminuyó del 15% al 12%: una reducción de 3 puntos porcentuales, equivalente al 20% de la proporción inicial. Cada mes se revisaron 200 solicitudes, exclusivamente del canal presencial.
```

## modes-es-012 · numbers

Source task:

> ¿Cuántas sillas quedan para alquilar? Hay 180 en el almacén. Veintiséis están reservadas y 14 pendientes de reparación; los grupos no se solapan. Otras 30 llegarán la semana próxima y no están incluidas en las 180. Da el cálculo.

### baseline: flagged

```text
Quedan 140 sillas disponibles para alquilar: 180 − 26 reservadas − 14 pendientes de reparación = 140. Las 30 que llegarán la semana próxima no se cuentan como disponibles ahora.
```

Review notes: El cálculo conserva operativamente la separación de grupos, aunque no la declara expresamente. / El cálculo es correcto, pero omite la condición que permite descontar ambos grupos íntegramente.

### lite: pass

```text
Quedan 140 sillas disponibles para alquilar: 180 − 26 reservadas − 14 pendientes de reparación = 140. Los grupos no se solapan. Las otras 30 llegarán la semana próxima y no se cuentan entre las disponibles ahora.
```

### full: pass

```text
Quedan 140 sillas disponibles para alquilar: 180 − 26 reservadas − 14 pendientes de reparación = 140. Los dos grupos no se solapan. Las 30 que llegarán la semana próxima no están incluidas en las 180 ni se cuentan como disponibles ahora.
```

### ultra: pass

```text
Quedan 140 sillas para alquilar: 180 − 26 reservadas − 14 pendientes de reparación = 140. Los grupos no se solapan. Las otras 30 llegarán la semana próxima y no están incluidas en las 180.
```

### off: pass

```text
Quedan 140 sillas disponibles para alquilar: 180 − 26 reservadas − 14 pendientes de reparación = 140. Como los grupos no se solapan, se descuentan ambos. Las 30 que llegarán la semana próxima no cuentan para la disponibilidad actual.
```

## modes-es-013 · numbers

Source task:

> Aclara la nota: “Las ventas fueron de 25.000 euros en abril y 27.500 en mayo, un aumento del 10%. Ambos importes incluyen el impuesto. Mayo es provisional porque pueden anularse pedidos por hasta 900 euros; todavía no se ha descontado esa posibilidad.”

### baseline: pass

```text
Las ventas, con el impuesto incluido, pasaron de 25.000 euros en abril a 27.500 euros en mayo: un aumento de 2.500 euros, equivalente al 10%. El importe de mayo es provisional y aún no descuenta posibles anulaciones de hasta 900 euros. Si se anulara ese máximo, mayo quedaría en 26.600 euros y el aumento respecto a abril sería del 6,4%.
```

### lite: pass

```text
Las ventas fueron de 25.000 euros en abril y 27.500 euros en mayo, un aumento del 10%. Ambos importes incluyen el impuesto. El importe de mayo es provisional: pueden anularse pedidos por hasta 900 euros, y esa posible reducción aún no se ha descontado.
```

### full: pass

```text
Las ventas, con el impuesto incluido, fueron de 25.000 euros en abril y 27.500 euros en mayo: un aumento del 10%. La cifra de mayo es provisional: podrían anularse pedidos por hasta 900 euros. Ese posible importe aún no se ha descontado.
```

### ultra: pass

```text
Las ventas, con el impuesto incluido, pasaron de 25.000 euros en abril a 27.500 en mayo: un aumento del 10%. El importe de mayo es provisional: pueden anularse pedidos por hasta 900 euros, aún no descontados.
```

### off: pass

```text
Las ventas, con el impuesto incluido, fueron de 25.000 euros en abril y 27.500 euros en mayo. El aumento fue de 2.500 euros, equivalente al 10%. La cifra de mayo es provisional: podrían anularse pedidos por hasta 900 euros, y ese posible importe aún no se ha descontado.
```

## modes-es-014 · numbers

Source task:

> Tenemos un máximo de 780 euros. Necesitamos cinco taburetes de 130 euros cada uno y un transporte único de 65 euros. Los protectores cuestan 8 euros por taburete, son opcionales y no se han pedido. ¿Cabe lo necesario? Da la conclusión y la cuenta.

### baseline: pass

```text
Sí, lo necesario cabe en el presupuesto: 5 × 130 + 65 = 715 euros. Sobran 780 − 715 = 65 euros. Los protectores son opcionales y no se incluyen porque no se han pedido.
```

### lite: pass

```text
Sí, lo necesario cabe en el presupuesto: 5 × 130 + 65 = 715 euros. Sobran 65 euros del máximo de 780. Los protectores cuestan 8 euros por taburete, pero son opcionales y no se han pedido; no se incluyen en la cuenta.
```

### full: pass

```text
Sí, lo necesario cabe en el presupuesto de 780 euros: 5 × 130 euros + 65 euros de transporte único = 715 euros. Sobran 65 euros. La cuenta no incluye los protectores de 8 euros por taburete, porque son opcionales y no se han pedido.
```

### ultra: pass

```text
Sí. Lo necesario cuesta 5 × 130 + 65 = 715 euros, dentro del máximo de 780 euros. Sobran 65 euros. Los protectores, a 8 euros por taburete, son opcionales, no se han pedido y no se incluyen en la cuenta.
```

### off: pass

```text
Sí, lo necesario cabe en el presupuesto. Los cinco taburetes cuestan 5 × 130 = 650 euros; con el transporte único de 65 euros, el total es 715 euros. Quedan 780 − 715 = 65 euros. Los protectores no se incluyen porque son opcionales y no se han pedido.
```

## modes-es-015 · numbers

Source task:

> Compara el uso diario: en junio se registraron 96 m³ de agua en 24 días de actividad y en julio 88 m³ en 22 días. Ambos promedian 4 m³ por día de actividad. No se conoce el número de visitantes. Explica por qué el total menor no prueba una mejora diaria.

### baseline: pass

```text
El consumo por día de actividad fue el mismo: junio, 96 ÷ 24 = 4 m³; julio, 88 ÷ 22 = 4 m³. El menor total de julio se explica por los dos días menos de actividad, no por una reducción del consumo diario. Además, sin conocer el número de visitantes, no se puede comparar el consumo por visitante.
```

### lite: pass

```text
En junio se registraron 96 m³ en 24 días de actividad: 96 ÷ 24 = 4 m³ por día. En julio se registraron 88 m³ en 22 días: 88 ÷ 22 = 4 m³ por día. El total menor de julio no prueba una mejora diaria: hubo menos días de actividad y el promedio diario fue el mismo. Como no se conoce el número de visitantes, tampoco puede compararse el consumo por visitante.
```

### full: pass

```text
El consumo por día de actividad no mejoró: fue de 4 m³ en ambos meses.

- Junio: 96 m³ ÷ 24 días = 4 m³/día.
- Julio: 88 m³ ÷ 22 días = 4 m³/día.

El total de julio fue menor porque hubo menos días de actividad, no porque se consumiera menos agua al día. Como no se conoce el número de visitantes, tampoco puede compararse el consumo por visitante.
```

### ultra: pass

```text
El consumo diario no bajó: junio registró 96 ÷ 24 = 4 m³ por día de actividad; julio, 88 ÷ 22 = 4 m³. El menor total de julio corresponde a menos días de actividad, no a una mejora diaria. Sin conocer el número de visitantes, tampoco puede compararse el consumo por visitante.
```

### off: pass

```text
En junio, el consumo diario fue de 96 ÷ 24 = 4 m³ por día de actividad. En julio fue de 88 ÷ 22 = 4 m³ por día de actividad. Aunque el total de julio fue menor, hubo dos días menos de actividad y el promedio diario no cambió. Por tanto, el total menor no demuestra una mejora diaria. Como no se conoce el número de visitantes, tampoco puede compararse el consumo por visitante.
```

## modes-es-016 · numbers

Source task:

> Reescribe: “La duración media fue de 52 minutos y la mediana de 35 minutos. Se midieron 45 visitas terminadas, incluidas dos de más de dos horas. Las visitas interrumpidas quedaron fuera. Estas cifras no son un límite de duración.”

### baseline: pass

```text
En las 45 visitas terminadas que se midieron, la duración media fue de 52 minutos y la mediana de 35 minutos. Dos duraron más de dos horas. Las visitas interrumpidas no se incluyeron y estas cifras no representan un límite de duración.
```

### lite: pass

```text
La duración media fue de 52 minutos y la mediana de 35 minutos. Se midieron 45 visitas terminadas, incluidas dos de más de dos horas. Las visitas interrumpidas quedaron fuera. Estas cifras no son un límite de duración.
```

### full: pass

```text
La duración media fue de 52 minutos y la mediana, de 35 minutos. Se midieron 45 visitas terminadas, incluidas dos de más de dos horas; se excluyeron las visitas interrumpidas. Estas cifras no son un límite de duración.
```

### ultra: pass

```text
La duración media fue de 52 minutos y la mediana, de 35. Se midieron 45 visitas terminadas, incluidas dos de más de dos horas; se excluyeron las interrumpidas. Estas cifras no son un límite de duración.
```

### off: pass

```text
La duración media de las 45 visitas terminadas fue de 52 minutos y la mediana, de 35 minutos. Se incluyeron dos visitas de más de dos horas y se excluyeron las visitas interrumpidas. Estas cifras no representan un límite de duración.
```

## modes-es-017 · numbers

Source task:

> Responde solo qué actividad tuvo mayor tasa de asistencia. A tuvo 28 asistentes de 40 inscritos. B tuvo 36 de 60. No atribuyas causas ni compares la calidad de las actividades.

### baseline: flagged

```text
La actividad A, con una tasa de asistencia del 70%.
```

Review notes: Direct, correct answer with a supported percentage. / La respuesta identifica correctamente A; la tasa de B queda fuera del alcance necesario.

### lite: flagged

```text
La actividad A: 70% de asistencia.
```

Review notes: Correctly identifies A with its supported rate and no unrelated comparison. / Identifica la actividad correcta con un cálculo respaldado; no necesita informar la tasa de B.

### full: flagged

```text
La actividad A.
```

Review notes: Answers exactly the narrow question; supporting calculations are not required. / Cumple exactamente la petición de responder solo qué actividad; los porcentajes no son necesarios para ese alcance.

### ultra: flagged

```text
La actividad A.
```

Review notes: Answers exactly the narrow question; supporting calculations are not required. / La respuesta mínima conserva la conclusión requerida; omitir los cálculos no constituye una omisión material.

### off: flagged

```text
La actividad A tuvo la mayor tasa de asistencia: 70%.
```

Review notes: Correctly answers the rate question without discussing counts, causes, or quality. / Responde correctamente al alcance solicitado; omitir la tasa de B no es una omisión material en esta pregunta restringida.

## modes-es-018 · numbers

Source task:

> Edita para el cliente: “Estimamos entre 6 y 9 minutos para transferir unos 4 GB en la red de prueba. No es un máximo garantizado. No hemos probado su conexión. El tamaño corresponde al archivo comprimido.”

### baseline: flagged

```text
Estimamos que la transferencia del archivo comprimido de unos 4 GB tardará entre 6 y 9 minutos, según las pruebas realizadas en nuestra red de prueba. Este intervalo no es un máximo garantizado y no hemos probado su conexión.
```

Review notes: Adds a completed-testing basis for the estimate, overstating what the source establishes. / Conserva las condiciones esenciales, pero añade que la estimación procede de pruebas realizadas, reforzando sin respaldo su fundamento.

### lite: pass

```text
Estimamos entre 6 y 9 minutos para transferir unos 4 GB en la red de prueba. Este tiempo no es un máximo garantizado. No hemos probado su conexión. El tamaño corresponde al archivo comprimido.
```

### full: pass

```text
Estimamos entre 6 y 9 minutos para transferir un archivo comprimido de unos 4 GB en la red de prueba. No es un máximo garantizado y no hemos probado su conexión.
```

### ultra: pass

```text
Estimamos entre 6 y 9 minutos para transferir el archivo comprimido de unos 4 GB en la red de prueba. No es un máximo garantizado y no hemos probado su conexión.
```

### off: pass

```text
Estimamos que la transferencia de un archivo comprimido de unos 4 GB tardará entre 6 y 9 minutos en la red de prueba. Este intervalo no es un máximo garantizado. No hemos probado su conexión.
```

## modes-es-019 · numbers

Source task:

> Escribe una nota sin valorar riesgos: una muestra de la fuente tomada a las 16:00 contenía 0,6 mg/L de cobre. El límite de cuantificación era 0,05 mg/L. No se aporta un límite de seguridad ni muestras de otros días.

### baseline: pass

```text
La muestra de la fuente tomada a las 16:00 contenía 0,6 mg/L de cobre, con un límite de cuantificación de 0,05 mg/L. No se aporta un límite de seguridad ni muestras de otros días.
```

### lite: pass

```text
Una muestra de la fuente tomada a las 16:00 contenía 0,6 mg/L de cobre. El límite de cuantificación era de 0,05 mg/L. No se aporta un límite de seguridad ni muestras de otros días.
```

### full: pass

```text
Una muestra de la fuente tomada a las 16:00 contenía 0,6 mg/L de cobre. El límite de cuantificación era de 0,05 mg/L. No se aporta un límite de seguridad ni muestras de otros días.
```

### ultra: pass

```text
Una muestra de la fuente tomada a las 16:00 contenía 0,6 mg/L de cobre. El límite de cuantificación era de 0,05 mg/L. No se aporta un límite de seguridad ni muestras de otros días.
```

### off: pass

```text
Una muestra de la fuente tomada a las 16:00 contenía 0,6 mg/L de cobre. El límite de cuantificación era de 0,05 mg/L. No se aporta un límite de seguridad ni muestras de otros días.
```

## modes-es-020 · numbers

Source task:

> Corrige esta afirmación en dos frases como máximo: “Participaron 27 de las 180 personas invitadas, por lo que la participación fue del 27%.” Las 180 invitaciones fueron individuales y no se contaron acompañantes.

### baseline: pass

```text
Participaron 27 de las 180 personas invitadas, por lo que la participación fue del 15%. Las invitaciones fueron individuales y no se contaron acompañantes.
```

### lite: pass

```text
Participaron 27 de las 180 personas invitadas, por lo que la participación fue del 15%. Las 180 invitaciones fueron individuales y no se contaron acompañantes.
```

### full: pass

```text
Participaron 27 de las 180 personas invitadas, por lo que la participación fue del 15%. Las invitaciones fueron individuales y no se contaron acompañantes.
```

### ultra: pass

```text
Participaron 27 de las 180 personas invitadas: la participación fue del 15%, no del 27%. Las invitaciones fueron individuales y no se contaron acompañantes.
```

### off: pass

```text
Participaron 27 de las 180 personas invitadas, por lo que la participación fue del 15%. Las 180 invitaciones fueron individuales y no se contaron acompañantes.
```

## modes-es-021 · conditions

Source task:

> Reescribe la norma: “Puede cambiar de grupo en línea solo si quedan más de 48 horas y el nuevo grupo tiene plazas. Si falla cualquiera de las condiciones, consulte la oficina. El cambio en línea es opcional aun cuando cumpla ambas.”

### baseline: pass

```text
Puede cambiar de grupo en línea si faltan más de 48 horas y hay plazas en el nuevo grupo. Aunque cumpla ambas condiciones, no está obligado a hacerlo en línea. Si alguna no se cumple, consulte la oficina.
```

### lite: pass

```text
Puede cambiar de grupo en línea solo si quedan más de 48 horas y el nuevo grupo tiene plazas. Si no se cumple alguna de estas condiciones, consulte la oficina. El cambio en línea es opcional, incluso si cumple ambas.
```

### full: pass

```text
Puede cambiar de grupo en línea solo si quedan más de 48 horas y hay plazas en el nuevo grupo. Si no se cumple alguna de estas condiciones, consulte la oficina. El cambio en línea es opcional, incluso si cumple ambas.
```

### ultra: pass

```text
Puede cambiar de grupo en línea solo si quedan más de 48 horas y hay plazas en el nuevo grupo. Si alguna condición no se cumple, consulte la oficina. Aunque cumpla ambas, el cambio en línea es opcional.
```

### off: pass

```text
Puede cambiar de grupo en línea únicamente si faltan más de 48 horas y hay plazas disponibles en el nuevo grupo. Si no se cumple alguna de estas condiciones, consulte la oficina. Aunque se cumplan ambas, el cambio en línea es opcional.
```

## modes-es-022 · conditions

Source task:

> Explica esta política aportada sin añadir derechos legales: los productos sin abrir se pueden devolver hasta 21 días naturales desde la recepción. Los abiertos solo si se confirma un fallo de fabricación. Se necesita un número de devolución antes de enviar cualquiera de ellos. El reintegro del envío se decide aparte.

### baseline: pass

```text
Los productos sin abrir se pueden devolver hasta 21 días naturales desde su recepción. Los productos abiertos solo se pueden devolver si se confirma un fallo de fabricación. En ambos casos, debe obtener un número de devolución antes de enviarlos. El reintegro de los gastos de envío se decide por separado.
```

### lite: pass

```text
Los productos sin abrir se pueden devolver hasta 21 días naturales desde la recepción. Los productos abiertos solo se pueden devolver si se confirma un fallo de fabricación. En ambos casos, necesita un número de devolución antes de enviarlos. El reintegro del envío se decide por separado.
```

### full: pass

```text
Puede devolver productos sin abrir hasta 21 días naturales desde la recepción. Los productos abiertos solo se pueden devolver si se confirma un fallo de fabricación.

Antes de enviar cualquier devolución, necesita un número de devolución. El reintegro del envío se decide por separado.
```

### ultra: pass

```text
Puede devolver productos sin abrir hasta 21 días naturales desde la recepción. Los abiertos solo se pueden devolver si se confirma un fallo de fabricación. Antes de enviar cualquier devolución, necesita un número de devolución. El reintegro del envío se decide aparte.
```

### off: pass

```text
Los productos sin abrir se pueden devolver hasta 21 días naturales desde su recepción. Los productos abiertos solo se pueden devolver si se confirma un fallo de fabricación.

En ambos casos, necesita un número de devolución antes de enviar el producto. El reintegro de los gastos de envío se decide por separado.
```

## modes-es-023 · conditions

Source task:

> Acorta: “No quite la tarjeta hasta que termine la copia y el indicador esté azul. Se necesitan ambas señales. Puede dejar la pantalla abierta después de la copia. Si el indicador sigue naranja, avise al mostrador aunque la copia figure completa.”

### baseline: pass

```text
No retire la tarjeta hasta que la copia termine y el indicador esté azul. Puede dejar la pantalla abierta después. Si el indicador sigue naranja, avise al mostrador, aunque la copia figure completa.
```

### lite: pass

```text
No quite la tarjeta hasta que termine la copia y el indicador esté azul: deben cumplirse ambas condiciones. Puede dejar la pantalla abierta después de la copia. Si el indicador sigue naranja, avise al mostrador aunque la copia figure completa.
```

### full: pass

```text
No quite la tarjeta hasta que termine la copia y el indicador esté azul: deben cumplirse ambas condiciones. Puede dejar la pantalla abierta después de la copia. Si el indicador sigue naranja, avise al mostrador aunque la copia figure completa.
```

### ultra: pass

```text
No quite la tarjeta hasta que termine la copia y el indicador esté azul: deben cumplirse ambas condiciones. Puede dejar la pantalla abierta después de la copia. Si el indicador sigue naranja, avise al mostrador aunque la copia figure completa.
```

### off: pass

```text
No quite la tarjeta hasta que la copia termine y el indicador esté azul; deben cumplirse ambas condiciones. Puede dejar la pantalla abierta después. Si el indicador sigue naranja, avise al mostrador aunque la copia figure completa.
```

## modes-es-024 · conditions

Source task:

> Organiza estas reglas: menores de 11 años deben venir con una persona adulta. De 11 a 15 pueden venir sin acompañante solo con autorización escrita. A partir de 16 no necesitan esa autorización. Todo acompañante debe tener entrada propia.

### baseline: pass

```text
- Menores de 11 años: deben venir con una persona adulta.
- De 11 a 15 años: pueden venir sin acompañante solo con autorización escrita.
- A partir de 16 años: no necesitan esa autorización.
- Todo acompañante debe tener entrada propia.
```

### lite: pass

```text
- Menores de 11 años: deben venir con una persona adulta.
- De 11 a 15 años: pueden venir sin acompañante solo con autorización escrita.
- A partir de 16 años: no necesitan esa autorización.
- Todo acompañante debe tener entrada propia.
```

### full: pass

```text
- Menores de 11 años: deben venir con una persona adulta.
- De 11 a 15 años: pueden venir sin acompañante solo con autorización escrita.
- A partir de 16 años: no necesitan esa autorización.
- Todo acompañante debe tener entrada propia.
```

### ultra: pass

```text
- Menores de 11 años: deben venir con una persona adulta.
- De 11 a 15 años: pueden venir sin acompañante solo con autorización escrita.
- A partir de 16 años: no necesitan esa autorización.
- Todo acompañante debe tener entrada propia.
```

### off: pass

```text
- Menores de 11 años: deben venir con una persona adulta.
- De 11 a 15 años: pueden venir sin acompañante solo con autorización escrita.
- A partir de 16 años: no necesitan esa autorización.
- Todo acompañante debe tener entrada propia.
```

## modes-es-025 · conditions

Source task:

> Reescribe para la plantilla: “El turno extra admite como máximo cuatro personas voluntarias acreditadas. Quienes tengan turno nocturno ese día no pueden participar. Apuntarse no garantiza asignación. La jefatura puede decidir no abrirlo.”

### baseline: pass

```text
El turno extra admite un máximo de cuatro personas voluntarias acreditadas. No pueden participar quienes tengan turno nocturno ese día. Apuntarse no garantiza la asignación de una plaza y la jefatura puede decidir no abrir el turno.
```

### lite: pass

```text
El turno extra admite un máximo de cuatro personas voluntarias acreditadas. Quienes tengan turno nocturno ese día no pueden participar. Apuntarse no garantiza la asignación. La jefatura puede decidir no abrir el turno extra.
```

### full: pass

```text
El turno extra admite un máximo de cuatro personas voluntarias acreditadas. Quienes tengan turno nocturno ese día no pueden participar. Apuntarse no garantiza la asignación. La jefatura puede decidir no abrir el turno extra.
```

### ultra: pass

```text
El turno extra admite un máximo de cuatro personas voluntarias acreditadas. No pueden participar quienes tengan turno nocturno ese día. Apuntarse no garantiza la asignación. La jefatura puede decidir no abrir el turno extra.
```

### off: pass

```text
El turno extra admite un máximo de cuatro personas voluntarias acreditadas. No pueden participar quienes tengan turno nocturno ese día. Apuntarse no garantiza la asignación de una plaza. La jefatura puede decidir no abrir el turno extra.
```

## modes-es-026 · conditions

Source task:

> Una regla interna ficticia exige revisión después de mover una vitrina, salvo movimientos de menos de 15 cm dentro del mismo rectángulo marcado. Se propone moverla exactamente 15 cm dentro del rectángulo. ¿La revisión es obligatoria? Respeta el límite del texto.

### baseline: pass

```text
Sí, la revisión es obligatoria: la excepción solo cubre movimientos de menos de 15 cm, no de exactamente 15 cm.
```

### lite: pass

```text
Sí. La excepción solo cubre movimientos de menos de 15 cm; exactamente 15 cm exige revisión, aunque sea dentro del mismo rectángulo marcado.
```

### full: pass

```text
Sí. La excepción solo cubre movimientos de menos de 15 cm dentro del mismo rectángulo marcado. Un movimiento de exactamente 15 cm exige revisión.
```

### ultra: pass

```text
Sí. La excepción solo cubre movimientos de menos de 15 cm; exactamente 15 cm exige revisión.
```

### off: pass

```text
Sí, la revisión es obligatoria. La excepción solo cubre movimientos de menos de 15 cm dentro del mismo rectángulo marcado; exactamente 15 cm queda fuera de ese límite.
```

## modes-es-027 · conditions

Source task:

> Reescribe: “La plaza se confirma cuando se recibe el dinero, no al enviar un justificante. Los nombres deben llegar antes de la actividad, pero no son necesarios para cobrar. Si falla el cobro, la plaza se conserva durante 36 horas más.”

### baseline: pass

```text
La plaza se confirma al recibir el dinero, no al enviar un justificante. Los nombres deben entregarse antes de la actividad, pero se puede cobrar sin ellos. Si el cobro falla, la plaza se mantiene durante 36 horas más.
```

### lite: pass

```text
La plaza se confirma al recibir el dinero, no al enviar un justificante. Los nombres deben llegar antes de la actividad, pero no son necesarios para cobrar. Si falla el cobro, la plaza se conserva durante 36 horas más.
```

### full: pass

```text
La plaza se confirma al recibir el dinero, no al enviar un justificante. Los nombres deben recibirse antes de la actividad, pero no hacen falta para cobrar. Si falla el cobro, la plaza se conserva durante 36 horas más.
```

### ultra: pass

```text
La plaza se confirma al recibir el dinero, no al enviar un justificante. Los nombres deben llegar antes de la actividad, pero no hacen falta para cobrar. Si falla el cobro, la plaza se conserva 36 horas más.
```

### off: pass

```text
La plaza se confirma al recibir el dinero, no al enviar un justificante. Los nombres deben recibirse antes de la actividad, aunque no son necesarios para cobrar. Si el cobro falla, la plaza se mantiene durante 36 horas más.
```

## modes-es-028 · conditions

Source task:

> Simplifica esta cláusula ficticia sin asesoramiento jurídico: no se pueden compartir borradores fuera del equipo salvo permiso escrito de su autoría. Aunque haya permiso, deben quitarse los correos personales. Los recuentos sin nombres pueden enviarse a coordinación.

### baseline: pass

```text
Solo se pueden compartir borradores fuera del equipo con permiso escrito de quien los haya creado. Incluso con permiso, hay que eliminar los correos personales. Los recuentos sin nombres pueden enviarse a coordinación.
```

### lite: pass

```text
No se pueden compartir borradores fuera del equipo sin permiso escrito de su autoría. Incluso con permiso, deben quitarse los correos personales. Los recuentos sin nombres pueden enviarse a coordinación.
```

### full: pass

```text
No se pueden compartir borradores fuera del equipo sin permiso escrito de quien los haya creado. Incluso con permiso, deben eliminarse los correos personales. Los recuentos sin nombres pueden enviarse a coordinación.
```

### ultra: pass

```text
Solo se pueden compartir borradores fuera del equipo con permiso escrito de su autoría. Incluso con permiso, deben quitarse los correos personales. Los recuentos sin nombres pueden enviarse a coordinación.
```

### off: pass

```text
Los borradores solo pueden compartirse fuera del equipo con permiso escrito de quien los haya creado. Incluso con permiso, deben eliminarse los correos personales. Los recuentos sin nombres pueden enviarse a coordinación.
```

## modes-es-029 · conditions

Source task:

> Reescribe el aviso: “La solicitud debe recibirse antes de las 15:00 UTC del 4 de septiembre de 2030. Enviarla antes no basta si llega después. Los justificantes pueden llegar hasta cuatro días hábiles después de una solicitud recibida a tiempo.”

### baseline: pass

```text
La solicitud debe llegar antes de las 15:00 UTC del 4 de septiembre de 2030. No basta con enviarla antes si llega después del plazo. Si la solicitud llega a tiempo, los justificantes pueden recibirse hasta cuatro días hábiles después de su recepción.
```

### lite: pass

```text
La solicitud debe recibirse antes de las 15:00 UTC del 4 de septiembre de 2030. No basta con enviarla antes si llega después. Los justificantes pueden llegar hasta cuatro días hábiles después de una solicitud recibida a tiempo.
```

### full: pass

```text
La solicitud debe recibirse antes de las 15:00 UTC del 4 de septiembre de 2030. No basta con enviarla antes si llega después. Los justificantes pueden recibirse hasta cuatro días hábiles después de recibir una solicitud a tiempo.
```

### ultra: pass

```text
La solicitud debe recibirse antes de las 15:00 UTC del 4 de septiembre de 2030; no basta con enviarla antes si llega después. Los justificantes pueden llegar hasta cuatro días hábiles después de una solicitud recibida a tiempo.
```

### off: pass

```text
La solicitud debe llegar antes de las 15:00 UTC del 4 de septiembre de 2030. No basta con enviarla antes si se recibe después de ese límite. Si la solicitud se recibe a tiempo, los justificantes pueden llegar hasta cuatro días hábiles después de su recepción.
```

## modes-es-030 · conditions

Source task:

> Responde solo qué acceso está permitido: la puerta del patio se usa si no hay público en la sala. La principal puede usarse salvo durante una grabación. Ahora hay público en la sala y no se está grabando.

### baseline: pass

```text
Solo está permitido el acceso por la puerta principal.
```

### lite: pass

```text
La puerta principal.
```

### full: pass

```text
Solo está permitido el acceso por la puerta principal.
```

### ultra: pass

```text
La puerta principal.
```

### off: pass

```text
La puerta principal.
```

## modes-es-031 · technical

Source task:

> Reescribe la nota de la versión 3.8: `lote revisar --prueba` verifica la configuración sin generar un archivo. Que pase no confirma espacio suficiente en destino. Para generar se usa `lote crear --real`. Conserva los comandos.

### baseline: pass

```text
Versión 3.8: `lote revisar --prueba` verifica la configuración sin generar un archivo. Superar la verificación no garantiza espacio suficiente en destino. Para generar el archivo, usa `lote crear --real`.
```

### lite: pass

```text
Versión 3.8: `lote revisar --prueba` verifica la configuración sin generar un archivo. Superar la prueba no confirma que haya espacio suficiente en destino. Para generar el archivo, usa `lote crear --real`.
```

### full: pass

```text
Versión 3.8: `lote revisar --prueba` verifica la configuración sin generar un archivo. Superar la verificación no confirma que haya espacio suficiente en destino. Para generar el archivo, usa `lote crear --real`.
```

### ultra: pass

```text
Versión 3.8: `lote revisar --prueba` verifica la configuración sin generar un archivo. Superar la prueba no confirma espacio suficiente en destino. Para generar el archivo, usa `lote crear --real`.
```

### off: pass

```text
En la versión 3.8, `lote revisar --prueba` verifica la configuración sin generar un archivo. Que la verificación pase no confirma que haya espacio suficiente en el destino. Para generar el archivo, usa `lote crear --real`.
```

## modes-es-032 · technical

Source task:

> Explica para soporte: el mensaje se confirma después de guardar la transacción. Si el proceso se detiene antes de confirmar, puede recibirse de nuevo. La deduplicación usa evento_id, no el nombre de la persona. Una segunda recepción no demuestra dos registros guardados.

### baseline: pass

```text
El mensaje se confirma después de guardar la transacción. Si el proceso se detiene antes de confirmarlo, el mensaje puede recibirse de nuevo. La deduplicación se basa en evento_id, no en el nombre de la persona. Recibir el mensaje por segunda vez no demuestra que se hayan guardado dos registros.
```

### lite: pass

```text
El mensaje se confirma después de guardar la transacción. Si el proceso se detiene antes de confirmarlo, puede recibirse de nuevo. La deduplicación usa evento_id, no el nombre de la persona. Recibir el mensaje por segunda vez no demuestra que se hayan guardado dos registros.
```

### full: pass

```text
El mensaje se confirma después de guardar la transacción. Si el proceso se detiene antes de confirmarlo, el mensaje puede recibirse de nuevo. La deduplicación usa evento_id, no el nombre de la persona. Recibir el mensaje por segunda vez no demuestra que se hayan guardado dos registros.
```

### ultra: pass

```text
El mensaje se confirma después de guardar la transacción. Si el proceso se detiene antes de confirmar, el mensaje puede recibirse de nuevo. La deduplicación usa evento_id, no el nombre de la persona. Recibirlo dos veces no demuestra que se hayan guardado dos registros.
```

### off: pass

```text
El mensaje se confirma después de guardar la transacción. Si el proceso se detiene antes de confirmarlo, el mensaje puede recibirse de nuevo, aunque la transacción ya se haya guardado. La deduplicación usa evento_id, no el nombre de la persona. Por tanto, recibir el mensaje una segunda vez no demuestra que se hayan guardado dos registros.
```

## modes-es-033 · technical

Source task:

> Acorta: “La copia pasó el checksum, pero no se ha hecho una restauración. Este resultado no demuestra que pueda recuperarse la aplicación. Incluye /srv/proyectos y excluye /srv/logs.”

### baseline: pass

```text
La copia pasó el checksum, pero no se probó la restauración: no demuestra que la aplicación sea recuperable. Incluye /srv/proyectos y excluye /srv/logs.
```

### lite: pass

```text
La copia pasó el checksum, pero no se ha probado la restauración: esto no demuestra que la aplicación pueda recuperarse. Incluye /srv/proyectos y excluye /srv/logs.
```

### full: pass

```text
La copia pasó el checksum, pero no se ha probado la restauración: no demuestra que la aplicación pueda recuperarse. Incluye /srv/proyectos y excluye /srv/logs.
```

### ultra: pass

```text
La copia pasó el checksum, pero no se ha probado la restauración: no demuestra que la aplicación pueda recuperarse. Incluye /srv/proyectos y excluye /srv/logs.
```

### off: pass

```text
La copia pasó el checksum, pero no se ha probado una restauración: el resultado no demuestra que la aplicación pueda recuperarse. Incluye /srv/proyectos y excluye /srv/logs.
```

## modes-es-034 · technical

Source task:

> Calcula la tasa nominal de contenido: el equipo envía una lectura de 12 bits cada 200 ms. No incluyas cabeceras, cuyo tamaño no se ha indicado. Explica brevemente qué mide el resultado.

### baseline: pass

```text
200 ms = 0,2 s; 12 bits ÷ 0,2 s = 60 bits/s. Esta tasa nominal mide los bits de las lecturas enviados por segundo, sin incluir cabeceras.
```

### lite: pass

```text
La tasa nominal de contenido es 12 bits / 0,2 s = 60 bits/s. Mide los bits de las lecturas enviados por segundo, sin incluir cabeceras, cuyo tamaño no se ha indicado.
```

### full: pass

```text
La tasa nominal de contenido es 60 bits/s: 12 bits ÷ 0,2 s = 60 bits/s. Mide los bits de las lecturas enviados por segundo, sin incluir cabeceras, cuyo tamaño no se ha indicado.
```

### ultra: pass

```text
12 bits / 0,2 s = 60 bits/s. Es la tasa nominal de contenido enviado, sin cabeceras: su tamaño no se ha indicado.
```

### off: pass

```text
200 ms = 0,2 s. La tasa nominal de contenido es 12 bits ÷ 0,2 s = 60 bits/s.

El resultado mide los bits de las lecturas enviados por segundo. No incluye cabeceras, cuyo tamaño no se ha indicado.
```

## modes-es-035 · technical

Source task:

> Edita sin proponer remedios: “La latencia subió después de cambiar la tabla de rutas. Ambos eventos ocurrieron entre las 08:00 y las 08:20 UTC. No hay comparación de control. El orden temporal no prueba que el cambio causara la subida. No se decidió revertirlo.”

### baseline: pass

```text
La latencia aumentó después del cambio en la tabla de rutas; ambos eventos ocurrieron entre las 08:00 y las 08:20 UTC. Sin una comparación de control, el orden temporal no demuestra que el cambio causara el aumento. No se decidió revertir el cambio.
```

### lite: pass

```text
La latencia subió después de cambiar la tabla de rutas. Ambos eventos ocurrieron entre las 08:00 y las 08:20 UTC. No hay comparación de control. El orden temporal no prueba que el cambio causara la subida. No se decidió revertir el cambio.
```

### full: pass

```text
La latencia subió después del cambio en la tabla de rutas. Ambos eventos ocurrieron entre las 08:00 y las 08:20 UTC. Sin una comparación de control, el orden temporal no prueba que el cambio causara la subida. No se decidió revertirlo.
```

### ultra: pass

```text
La latencia subió después del cambio de la tabla de rutas; ambos eventos ocurrieron entre las 08:00 y las 08:20 UTC. Sin comparación de control, el orden temporal no prueba que el cambio causara la subida. No se decidió revertirlo.
```

### off: pass

```text
La latencia aumentó después del cambio en la tabla de rutas. Ambos eventos ocurrieron entre las 08:00 y las 08:20 UTC. No hay comparación de control, y el orden temporal no demuestra que el cambio causara el aumento. No se decidió revertir el cambio.
```

## modes-es-036 · technical

Source task:

> Explica el contrato del campo etiqueta: si falta, se mantiene el valor actual; si vale JSON null, se borra; una cadena vacía es un valor válido. No se ha definido esa regla para otros campos.

### baseline: pass

```text
El campo `etiqueta` mantiene su valor actual si se omite, se borra si se envía como `null` de JSON y acepta una cadena vacía como valor válido. Esta regla no se ha definido para otros campos.
```

### lite: pass

```text
Para el campo `etiqueta`, si el campo falta, se mantiene el valor actual. Si su valor es JSON `null`, se borra. Una cadena vacía (`""`) es un valor válido. Esta regla no se ha definido para otros campos.
```

### full: pass

```text
El campo etiqueta tiene estas reglas:
- Si falta, se mantiene el valor actual.
- Si vale JSON null, se borra.
- Una cadena vacía es un valor válido.

Estas reglas no se han definido para otros campos.
```

### ultra: pass

```text
Para el campo `etiqueta`:
- Si falta, se mantiene el valor actual.
- Si vale JSON `null`, se borra.
- Una cadena vacía (`""`) es un valor válido.

Esta regla no se ha definido para otros campos.
```

### off: pass

```text
El campo `etiqueta` distingue tres casos:
- Si no se incluye, se mantiene el valor actual.
- Si se envía como JSON `null`, se borra el valor.
- Si se envía una cadena vacía (`""`), se acepta como un valor válido.

Esta regla no se ha definido para otros campos.
```

## modes-es-037 · technical

Source task:

> Reescribe el resultado: ocho hilos completaron 1.440 tareas en 120 segundos, un total de 12 tareas por segundo. La entrada estaba en caché. No se midió un hilo aislado ni la lectura con caché vacía.

### baseline: pass

```text
Ocho hilos completaron 1.440 tareas en 120 segundos, con un rendimiento total de 12 tareas por segundo y la entrada en caché. No se midió el rendimiento de un hilo aislado ni la lectura con caché vacía.
```

### lite: pass

```text
Ocho hilos completaron 1.440 tareas en 120 segundos: 12 tareas por segundo en total. La entrada estaba en caché. No se midió el rendimiento de un hilo aislado ni la lectura con caché vacía.
```

### full: pass

```text
Ocho hilos completaron 1.440 tareas en 120 segundos: 12 tareas por segundo en total, con la entrada en caché. No se midió el rendimiento de un hilo aislado ni la lectura con caché vacía.
```

### ultra: pass

```text
Ocho hilos completaron 1.440 tareas en 120 segundos: 12 tareas por segundo en total, con la entrada en caché. No se midió un hilo aislado ni la lectura con caché vacía.
```

### off: pass

```text
Ocho hilos completaron 1.440 tareas en 120 segundos, con un rendimiento total de 12 tareas por segundo. La entrada estaba en caché. No se midió el rendimiento de un hilo aislado ni el de la lectura con caché vacía.
```

## modes-es-038 · technical

Source task:

> Resume la configuración: dias_guardado=0 desactiva el borrado automático y no borra todo de inmediato. Los valores positivos cuentan días completos desde la entrada. Sigue siendo posible borrar manualmente. El valor predeterminado es 21 y los cambios afectan solo a registros nuevos.

### baseline: pass

```text
`dias_guardado=0` desactiva el borrado automático; no borra todo de inmediato. Los valores positivos cuentan días completos desde la entrada. El borrado manual sigue disponible. El valor predeterminado es 21 y los cambios solo afectan a registros nuevos.
```

### lite: pass

```text
`dias_guardado=0` desactiva el borrado automático; no borra todo de inmediato. Los valores positivos cuentan días completos desde la entrada. Sigue siendo posible borrar manualmente. El valor predeterminado es 21 y los cambios afectan solo a registros nuevos.
```

### full: pass

```text
dias_guardado=0 desactiva el borrado automático; no borra todo de inmediato. Los valores positivos cuentan días completos desde la entrada. El borrado manual sigue siendo posible. El valor predeterminado es 21 y los cambios solo afectan a registros nuevos.
```

### ultra: pass

```text
`dias_guardado=0` desactiva el borrado automático; no borra todo de inmediato. Los valores positivos cuentan días completos desde la entrada. El borrado manual sigue disponible. El valor predeterminado es 21 y los cambios solo afectan a registros nuevos.
```

### off: pass

```text
`dias_guardado=0` desactiva el borrado automático; no borra todos los registros de inmediato. Los valores positivos indican días completos desde la entrada. El borrado manual sigue siendo posible. El valor predeterminado es 21 y los cambios solo afectan a registros nuevos.
```

## modes-es-039 · technical

Source task:

> Reescribe para dirección: el ensayo autenticó una cuenta de servicio y comprobó que puede conectarse. No autenticó a cada visitante ni verificó su derecho a leer cada expediente. No presentes la conexión como aprobación del sistema de permisos.

### baseline: pass

```text
El ensayo autenticó una cuenta de servicio y confirmó que puede conectarse. No autenticó a cada visitante ni verificó su derecho a leer cada expediente. Por tanto, el resultado confirma la conectividad, no la validez del sistema de permisos.
```

### lite: pass

```text
El ensayo autenticó una cuenta de servicio y comprobó que puede conectarse. No autenticó a cada visitante ni verificó su derecho a leer cada expediente. La conexión no supone la aprobación del sistema de permisos.
```

### full: pass

```text
El ensayo confirmó que una cuenta de servicio autenticada puede conectarse, no que el sistema de permisos esté aprobado. No autenticó a cada visitante ni verificó su derecho a leer cada expediente.
```

### ultra: pass

```text
El ensayo confirmó que una cuenta de servicio autenticada puede conectarse, no que el sistema de permisos sea correcto. No autenticó a cada visitante ni verificó su derecho a leer cada expediente.
```

### off: pass

```text
El ensayo autenticó una cuenta de servicio y confirmó que puede conectarse. No autenticó a cada visitante ni verificó su derecho a leer cada expediente. Por tanto, el resultado demuestra conectividad, pero no constituye una aprobación del sistema de permisos.
```

## modes-es-040 · technical

Source task:

> ¿El aviso “desfase: 75 s” demuestra pérdida? Significa que el último evento aplicado está 75 segundos detrás del último recibido. Los pendientes siguen en la cola. No se aportan recuento de fallos o auditoría de eventos ausentes.

### baseline: pass

```text
No. «Desfase: 75 s» indica que el último evento aplicado está 75 segundos detrás del último recibido; los eventos pendientes siguen en la cola. Sin un recuento de fallos ni una auditoría de eventos ausentes, el aviso no demuestra pérdida.
```

### lite: pass

```text
No. El aviso «desfase: 75 s» significa que el último evento aplicado está 75 segundos detrás del último recibido. Los eventos pendientes siguen en la cola. No se aporta un recuento de fallos ni una auditoría de eventos ausentes, por lo que el aviso no demuestra pérdida.
```

### full: pass

```text
No. «Desfase: 75 s» significa que el último evento aplicado está 75 segundos detrás del último recibido. Los eventos pendientes siguen en la cola. Sin un recuento de fallos ni una auditoría de eventos ausentes, el aviso no demuestra pérdida.
```

### ultra: pass

```text
No. «Desfase: 75 s» indica que el último evento aplicado está 75 segundos detrás del último recibido. Los pendientes siguen en la cola. Sin un recuento de fallos ni una auditoría de eventos ausentes, el aviso no demuestra pérdida.
```

### off: pass

```text
No. El aviso «desfase: 75 s» indica que el último evento aplicado está 75 segundos detrás del último recibido. Los eventos pendientes siguen en la cola. Sin un recuento de fallos ni una auditoría de eventos ausentes, el aviso por sí solo no demuestra pérdida.
```

## modes-es-041 · summary

Source task:

> Resume en tres puntos: el consejo aprobó renovar los baños si el estudio confirma la viabilidad. Rechazó ampliar la cafetería este año. Debatió la rampa sin decidir. Elisa pedirá presupuestos del estudio; no se registró plazo.

### baseline: pass

```text
- El consejo aprobó renovar los baños si el estudio confirma la viabilidad; Elisa pedirá presupuestos del estudio, sin plazo registrado.
- Rechazó ampliar la cafetería este año.
- Debatió la rampa sin tomar una decisión.
```

### lite: pass

```text
- El consejo aprobó renovar los baños si el estudio confirma la viabilidad. Elisa pedirá presupuestos del estudio; no se registró plazo.
- Rechazó ampliar la cafetería este año.
- Debatió la rampa sin tomar una decisión.
```

### full: pass

```text
- El consejo aprobó renovar los baños si el estudio confirma la viabilidad. Elisa pedirá presupuestos del estudio; no se registró plazo.
- Rechazó ampliar la cafetería este año.
- Debatió la rampa sin tomar una decisión.
```

### ultra: pass

```text
- El consejo aprobó renovar los baños si el estudio confirma la viabilidad. Elisa pedirá presupuestos del estudio; no se registró plazo.
- Rechazó ampliar la cafetería este año.
- Debatió la rampa sin decidir.
```

### off: pass

```text
- El consejo aprobó renovar los baños si el estudio confirma la viabilidad. Elisa pedirá presupuestos del estudio; no se registró plazo.
- Rechazó ampliar la cafetería este año.
- Debatió la rampa sin tomar una decisión.
```

## modes-es-042 · summary

Source task:

> Escribe una actualización breve: la pantalla dañada llegó ayer al taller. La sustituta está embalada pero no ha salido. Habrá seguimiento después de la recogida. Se espera recogida el martes, aún sin confirmar por el transportista. No se pidió devolver el cable.

### baseline: pass

```text
La pantalla dañada llegó ayer al taller. La sustituta está embalada, pero aún no ha salido. Se espera la recogida el martes, pendiente de confirmación del transportista; habrá seguimiento después. No se pidió devolver el cable.
```

### lite: pass

```text
La pantalla dañada llegó ayer al taller. La sustituta está embalada, pero aún no ha salido. Se espera la recogida el martes, pendiente de confirmación del transportista. Habrá seguimiento después de la recogida. No se pidió devolver el cable.
```

### full: pass

```text
La pantalla dañada llegó ayer al taller. La sustituta está embalada, pero no ha salido. Se espera la recogida el martes, aún sin confirmación del transportista; habrá seguimiento después. No se pidió devolver el cable.
```

### ultra: pass

```text
La pantalla dañada llegó ayer al taller. La sustituta está embalada, pero no ha salido. Se espera la recogida el martes, pendiente de confirmación del transportista; habrá seguimiento después. No se pidió devolver el cable.
```

### off: pass

```text
La pantalla dañada llegó ayer al taller. La sustituta está embalada, pero aún no ha salido. Se espera la recogida el martes, pendiente de confirmación del transportista; habrá seguimiento después de la recogida. No se pidió devolver el cable.
```

## modes-es-043 · summary

Source task:

> Resume la revisión: se examinaron 80 expedientes elegidos al azar entre los de junio. Doce carecían de fecha de autorización, y cuatro de esos doce también de firma. No se examinaron mayo o julio. Los campos vacíos no prueban que no hubiera autorización.

### baseline: pass

```text
Se revisaron 80 expedientes de junio elegidos al azar: 12 carecían de fecha de autorización y, de esos, cuatro también de firma. No se revisaron expedientes de mayo ni de julio. Los campos vacíos no prueban que faltara autorización.
```

### lite: pass

```text
Se revisaron 80 expedientes elegidos al azar entre los de junio. Doce carecían de fecha de autorización; cuatro de esos doce también carecían de firma. No se revisaron expedientes de mayo ni julio. Los campos vacíos no prueban que no hubiera autorización.
```

### full: pass

```text
Se revisaron 80 expedientes elegidos al azar entre los de junio. Doce carecían de fecha de autorización; cuatro de esos doce también carecían de firma. No se revisaron expedientes de mayo ni de julio. Los campos vacíos no prueban que no hubiera autorización.
```

### ultra: pass

```text
Se revisaron 80 expedientes de junio elegidos al azar: 12 carecían de fecha de autorización y cuatro de esos 12 también de firma. No se revisaron mayo ni julio. Los campos vacíos no prueban que faltara autorización.
```

### off: pass

```text
Se examinaron 80 expedientes elegidos al azar entre los de junio. Doce carecían de fecha de autorización; cuatro de esos doce también carecían de firma. No se examinaron expedientes de mayo ni de julio. Los campos vacíos no prueban que no hubiera autorización.
```

## modes-es-044 · summary

Source task:

> Haz el anuncio más breve que siga completo: el mirador abre el 6 de octubre de 2030 si pasa la revisión de la barandilla. Si no, se anunciará otra fecha, aún sin fijar. La entrada es gratis; los recorridos guiados requieren reserva. El puesto de bebidas estará cerrado el primer día.

### baseline: pass

```text
El mirador abrirá el 6 de octubre de 2030 si supera la revisión de la barandilla; si no, se anunciará otra fecha, aún sin fijar. Entrada gratis; recorridos guiados con reserva. Puesto de bebidas cerrado el primer día.
```

### lite: pass

```text
El mirador abre el 6 de octubre de 2030 si pasa la revisión de la barandilla. Si no, se anunciará otra fecha, aún sin fijar. Entrada gratis; recorridos guiados con reserva. El puesto de bebidas estará cerrado el primer día.
```

### full: pass

```text
El mirador abre el 6 de octubre de 2030 si pasa la revisión de la barandilla. Si no, se anunciará otra fecha, aún sin fijar. Entrada gratis; recorridos guiados con reserva. El puesto de bebidas estará cerrado el primer día.
```

### ultra: pass

```text
El mirador abrirá el 6 de octubre de 2030 si pasa la revisión de la barandilla. Si no, se anunciará otra fecha, aún sin fijar. Entrada gratis; recorridos guiados con reserva. El puesto de bebidas estará cerrado el primer día.
```

### off: pass

```text
El mirador abrirá el 6 de octubre de 2030 si pasa la revisión de la barandilla; si no, se anunciará otra fecha, aún sin fijar. Entrada gratis; recorridos guiados con reserva. El puesto de bebidas estará cerrado el primer día.
```

## modes-es-045 · summary

Source task:

> Resume solo el hallazgo de la auditoría: revisó compras de más de 600 euros del trimestre anterior, excluidas dietas. Cinco de 65 facturas no tenían código de autorización. No se comprobó si hubo permiso verbal. Compras revisará los códigos.

### baseline: flagged

```text
En las compras de más de 600 euros del trimestre anterior, excluidas las dietas, cinco de las 65 facturas revisadas carecían de código de autorización. No se comprobó si hubo permiso verbal.
```

Review notes: Preserves the complete finding. Omitted Purchasing follow-up falls outside the authoritative findings-only scope. / Resume íntegramente el hallazgo. La acción omitida en el invariante 3 queda fuera del alcance autoritativo «solo el hallazgo».

### lite: flagged

```text
En las compras de más de 600 euros del trimestre anterior, excluidas dietas, cinco de las 65 facturas revisadas no tenían código de autorización. No se comprobó si hubo permiso verbal.
```

Review notes: Preserves the complete finding. Omitted Purchasing follow-up falls outside the authoritative findings-only scope. / Resume íntegramente el hallazgo. La acción omitida en el invariante 3 queda fuera del alcance autoritativo «solo el hallazgo».

### full: flagged

```text
En las compras de más de 600 euros del trimestre anterior, excluidas dietas, cinco de las 65 facturas revisadas no tenían código de autorización. No se comprobó si hubo permiso verbal.
```

Review notes: Preserves the complete finding. Omitted Purchasing follow-up falls outside the authoritative findings-only scope. / Resume íntegramente el hallazgo. La acción omitida en el invariante 3 queda fuera del alcance autoritativo «solo el hallazgo».

### ultra: flagged

```text
En las compras de más de 600 euros del trimestre anterior, excluidas dietas, cinco de 65 facturas carecían de código de autorización. No se comprobó si hubo permiso verbal.
```

Review notes: Preserves the complete finding. Omitted Purchasing follow-up falls outside the authoritative findings-only scope. / Resume íntegramente el hallazgo. La acción omitida en el invariante 3 queda fuera del alcance autoritativo «solo el hallazgo».

### off: flagged

```text
En las compras de más de 600 euros del trimestre anterior, excluidas dietas, cinco de las 65 facturas revisadas no tenían código de autorización. No se comprobó si hubo permiso verbal.
```

Review notes: Preserves the complete finding. Omitted Purchasing follow-up falls outside the authoritative findings-only scope. / Resume íntegramente el hallazgo. La acción omitida en el invariante 3 queda fuera del alcance autoritativo «solo el hallazgo».

## modes-es-046 · analysis

Source task:

> Compara únicamente el precio mensual para 14 personas. El plan Río cuesta 19 euros por persona y no tiene mínimo. El plan Pino cuesta 240 euros para hasta 16 personas. Ambos cubren las funciones necesarias. No hay datos de calidad. ¿Cuál cuesta menos aquí?

### baseline: pass

```text
Pino cuesta menos: 240 euros al mes frente a los 266 euros de Río (14 × 19). El ahorro mensual es de 26 euros.
```

### lite: pass

```text
Pino cuesta menos: 240 euros al mes para 14 personas, frente a 266 euros con Río (14 × 19). La diferencia es de 26 euros al mes.
```

### full: pass

```text
Pino cuesta menos: 240 euros al mes para 14 personas, frente a 266 euros de Río (14 × 19). La diferencia es de 26 euros al mes.
```

### ultra: pass

```text
Pino cuesta menos para 14 personas: 240 euros al mes frente a 266 euros de Río (14 × 19). La diferencia es de 26 euros mensuales.
```

### off: pass

```text
El plan Pino cuesta menos: 240 euros al mes para 14 personas, frente a 266 euros del plan Río (14 × 19). La diferencia es de 26 euros al mes.
```

## modes-es-047 · analysis

Source task:

> La directora atribuye a un curso voluntario menos errores: 30 asistentes hicieron 6 y 30 no asistentes hicieron 15. Cada persona eligió participar; no se midió experiencia previa. Explica la diferencia observada y por qué no prueba la causa.

### baseline: pass

```text
Los 30 asistentes cometieron 6 errores y los 30 no asistentes, 15: se observaron 9 errores menos entre los asistentes. Esto no demuestra que el curso causara la diferencia, porque la participación fue voluntaria y no se midió la experiencia previa. Los grupos podrían diferir en factores que influyan en los errores.
```

### lite: pass

```text
Los 30 asistentes hicieron 6 errores y los 30 no asistentes, 15: los asistentes hicieron 9 errores menos. Esta diferencia no demuestra que el curso fuera la causa. La participación fue voluntaria y no se midió la experiencia previa, por lo que los grupos podrían diferir en factores que influyen en los errores.
```

### full: pass

```text
Los 30 asistentes cometieron 6 errores y los 30 no asistentes, 15: se observaron 9 errores menos entre los asistentes. Esto muestra una asociación, no demuestra que el curso causara la diferencia. La participación fue voluntaria y no se midió la experiencia previa, por lo que los grupos podrían diferir en factores que influyen en los errores.
```

### ultra: pass

```text
Los 30 asistentes cometieron 6 errores; los 30 no asistentes, 15: una diferencia de 9 errores. Esto no demuestra que el curso los redujera: la participación fue voluntaria y no se midió la experiencia previa. Los grupos podrían diferir por razones ajenas al curso.
```

### off: pass

```text
Los 30 asistentes cometieron 6 errores y los 30 no asistentes, 15: se observaron 9 errores menos entre quienes asistieron. Esto muestra una asociación, pero no demuestra que el curso causara la diferencia. La participación fue voluntaria y no se midió la experiencia previa, por lo que los grupos podrían haber sido distintos desde el principio.
```

## modes-es-048 · analysis

Source task:

> Los pedidos confirmados necesitan 95 cajas y hay 40 utilizables. Se permite una reserva extra de hasta 12, pero no es obligatoria. No se ha indicado un mínimo del proveedor. ¿Sustenta el texto comprar 120 cajas hoy? Distingue necesidad y reserva.

### baseline: pass

```text
No. Para cubrir los pedidos faltan 55 cajas (95 − 40). La reserva opcional permitiría comprar hasta 12 más, es decir, entre 55 y 67 cajas en total. Comprar 120 excede la necesidad y la reserva permitida; no se ha indicado un mínimo del proveedor que lo justifique.
```

### lite: pass

```text
No. Los pedidos confirmados requieren 95 cajas y hay 40 utilizables: faltan 55. La reserva opcional permite comprar hasta 12 más, es decir, entre 55 y 67 cajas en total. No se ha indicado un mínimo del proveedor que justifique comprar 120 cajas hoy.
```

### full: pass

```text
No. Para cubrir los pedidos confirmados faltan 55 cajas: se necesitan 95 y hay 40 utilizables. La reserva es opcional y permite añadir hasta 12 cajas, de modo que la compra sería de 55 a 67 cajas. No se ha indicado un mínimo del proveedor que justifique comprar 120 hoy.
```

### ultra: pass

```text
No. Para los pedidos confirmados faltan 55 cajas (95 − 40). La reserva opcional permite añadir hasta 12: comprar entre 55 y 67 cajas cubriría la necesidad y la reserva permitida. No se ha indicado un mínimo del proveedor que justifique comprar 120 hoy.
```

### off: pass

```text
No. Para los pedidos confirmados faltan 55 cajas: se necesitan 95 y hay 40 utilizables. La reserva es opcional y permite añadir hasta 12 cajas, por lo que la compra sería de 55 sin reserva o de hasta 67 con ella. No se ha indicado ningún mínimo del proveedor que justifique comprar 120 cajas hoy.
```

## modes-es-049 · analysis

Source task:

> Explica el choque entre notas sin resolverlo: montaje estima 5 semanas si el material llega antes del 2 de abril. Compras estima llegada entre el 7 y el 14 de abril. Son estimaciones, no compromisos. No hay duración revisada para una llegada tardía.

### baseline: pass

```text
La estimación de montaje de 5 semanas depende de que el material llegue antes del 2 de abril, pero Compras estima su llegada entre el 7 y el 14 de abril. Esa ventana no cumple la condición de montaje. Ambas son estimaciones, no compromisos, y no hay una duración revisada para la llegada tardía, por lo que no puede establecerse el plazo resultante.
```

### lite: pass

```text
La estimación de montaje de 5 semanas depende de que el material llegue antes del 2 de abril. Compras estima que llegará entre el 7 y el 14 de abril, fuera de esa condición. Ambas son estimaciones, no compromisos. Sin una duración revisada para una llegada tardía, no puede determinarse cuánto duraría el montaje en ese caso.
```

### full: pass

```text
La estimación de montaje de 5 semanas depende de que el material llegue antes del 2 de abril. Compras estima que llegará entre el 7 y el 14 de abril, fuera de esa condición. Por tanto, las notas no permiten determinar la duración del montaje con esa llegada: no hay una estimación revisada para una llegada tardía. Ambas cifras son estimaciones, no compromisos.
```

### ultra: pass

```text
Las 5 semanas de montaje dependen de que el material llegue antes del 2 de abril. Compras estima la llegada entre el 7 y el 14 de abril, fuera de esa condición. Ambas son estimaciones, no compromisos; no hay una duración revisada para la llegada tardía.
```

### off: pass

```text
La estimación de montaje de 5 semanas depende de que el material llegue antes del 2 de abril. Compras estima que llegará entre el 7 y el 14 de abril, fuera de esa condición. Ambas notas son estimaciones, no compromisos. Como no hay una duración revisada para una llegada tardía, no puede establecerse el plazo de montaje en ese escenario.
```

## modes-es-050 · analysis

Source task:

> ¿Se ha demostrado funcionamiento sin conexión? El probador abrió dos páginas al apagar el Wi-Fi. Ambas ya estaban guardadas en caché. No anotó el estado de los datos móviles, no abrió páginas nuevas y no revisó peticiones de fondo. Responde con estos datos.

### baseline: pass

```text
No se ha demostrado funcionamiento sin conexión. Solo se comprobó que dos páginas ya guardadas en caché se abrían con el Wi-Fi apagado. Como no se anotó el estado de los datos móviles, no se abrieron páginas nuevas ni se revisaron peticiones de fondo, la prueba no demuestra que funcionara sin acceso a la red.
```

### lite: pass

```text
No se ha demostrado funcionamiento sin conexión. Solo se comprobó que dos páginas ya guardadas en caché se abrieron con el Wi-Fi apagado. No se anotó el estado de los datos móviles, no se abrieron páginas nuevas y no se revisaron peticiones de fondo. Por tanto, la prueba no confirma que no hubiera conexión ni que el funcionamiento general fuera posible sin ella.
```

### full: pass

```text
No se ha demostrado el funcionamiento sin conexión. Solo se comprobó que dos páginas ya guardadas en caché se abrieron al apagar el Wi-Fi. No se anotó si los datos móviles estaban activos, no se abrieron páginas nuevas ni se revisaron las peticiones de fondo. La prueba no permite confirmar que no hubiera conexión ni que otras funciones operaran sin ella.
```

### ultra: pass

```text
No se ha demostrado funcionamiento sin conexión. Solo se abrieron dos páginas ya guardadas en caché tras apagar el Wi-Fi. No se anotó el estado de los datos móviles, no se abrieron páginas nuevas ni se revisaron peticiones de fondo. La prueba no confirma que no hubiera conexión ni que otras funciones operaran sin ella.
```

### off: pass

```text
No se ha demostrado el funcionamiento sin conexión. Solo se comprobó que dos páginas ya guardadas en caché se abrían con el Wi-Fi apagado. No se anotó si los datos móviles estaban activos, no se abrieron páginas nuevas ni se revisaron las peticiones de fondo. Por tanto, la prueba no confirma que no hubiera conexión ni demuestra un funcionamiento general sin ella.
```

## modes-es-051 · exact-format

Source task:

> Devuelve exactamente esta frase ya clara, sin título, explicación ni comillas: La piscina cierra a las 19:00.

### baseline: pass

```text
La piscina cierra a las 19:00.
```

### lite: pass

```text
La piscina cierra a las 19:00.
```

### full: pass

```text
La piscina cierra a las 19:00.
```

### ultra: pass

```text
La piscina cierra a las 19:00.
```

### off: pass

```text
La piscina cierra a las 19:00.
```

## modes-es-052 · exact-format

Source task:

> Reescribe en exactamente dos elementos numerados: “1. {huesped}, puede entrar después de las 16:00. 2. Si llega después de las 23:00, llame a {{telefono_noche}} antes de entrar.” Mantén los marcadores sin cambios y no añadas saludo o firma.

### baseline: pass

```text
1. {huesped}, puede entrar después de las 16:00.
2. Si llega después de las 23:00, llame a {{telefono_noche}} antes de entrar.
```

### lite: pass

```text
1. {huesped}, puede entrar después de las 16:00.
2. Si llega después de las 23:00, llame a {{telefono_noche}} antes de entrar.
```

### full: pass

```text
1. {huesped}, puede entrar después de las 16:00.
2. Si llega después de las 23:00, llame a {{telefono_noche}} antes de entrar.
```

### ultra: pass

```text
1. {huesped}, puede entrar después de las 16:00.
2. Si llega después de las 23:00, llame a {{telefono_noche}} antes de entrar.
```

### off: pass

```text
1. {huesped}, puede entrar después de las 16:00.
2. Si llega después de las 23:00, llame a {{telefono_noche}} antes de entrar.
```

## modes-es-053 · exact-format

Source task:

> Devuelve un objeto JSON solo con "case_id", "urgency" y "message". case_id debe ser "E-452" y urgency 4. El mensaje en español debe decir que la revisión empezó, pero no hay fecha de finalización. No uses bloque de código.

### baseline: pass

```text
{"case_id":"E-452","urgency":4,"message":"La revisión empezó, pero no hay fecha de finalización."}
```

### lite: pass

```text
{"case_id":"E-452","urgency":4,"message":"La revisión empezó, pero no hay fecha de finalización."}
```

### full: pass

```text
{"case_id":"E-452","urgency":4,"message":"La revisión empezó, pero no hay fecha de finalización."}
```

### ultra: pass

```text
{"case_id":"E-452","urgency":4,"message":"La revisión empezó, pero no hay fecha de finalización."}
```

### off: pass

```text
{"case_id":"E-452","urgency":4,"message":"La revisión empezó, pero no hay fecha de finalización."}
```

## modes-es-054 · exact-format

Source task:

> Simplifica en una sola frase conservando este enlace Markdown exacto: “Sería recomendable consultar [Guía de entradas](https://example.invalid/entradas?rev=4#formas) antes de mandar el formulario, ya que recoge las opciones disponibles.”

### baseline: flagged

```text
Consulte [Guía de entradas](https://example.invalid/entradas?rev=4#formas) antes de enviar el formulario para conocer las opciones disponibles.
```

Review notes: The imperative materially strengthens the recommendation into an instruction. / Preserves link and sequence but materially strengthens advisory wording into a directive.

### lite: uncertain

```text
Sería recomendable consultar [Guía de entradas](https://example.invalid/entradas?rev=4#formas) antes de enviar el formulario, porque recoge las opciones disponibles.
```

Review notes: Preserves all meaning and the link, but simplifies the original only slightly. / Preserves all meaning and constraints, though simplification is modest. / Review 1 has invalid invariant coverage: missing [], duplicate [3], extra []. Raw checks are retained; this answer cannot pass.

### full: uncertain

```text
Se recomienda consultar [Guía de entradas](https://example.invalid/entradas?rev=4#formas) antes de enviar el formulario porque recoge las opciones disponibles.
```

Review notes: Simplifies while preserving recommendation, sequence, rationale, and exact link. / Simplifies while preserving recommendation, sequence, link, and rationale. / Review 1 has invalid invariant coverage: missing [], duplicate [3], extra []. Raw checks are retained; this answer cannot pass.

### ultra: uncertain

```text
Se recomienda consultar [Guía de entradas](https://example.invalid/entradas?rev=4#formas) antes de enviar el formulario porque recoge las opciones disponibles.
```

Review notes: Simplifies while preserving recommendation, sequence, rationale, and exact link. / Simplifies while preserving recommendation, sequence, link, and rationale. / Review 1 has invalid invariant coverage: missing [], duplicate [3], extra []. Raw checks are retained; this answer cannot pass.

### off: uncertain

```text
Se recomienda consultar [Guía de entradas](https://example.invalid/entradas?rev=4#formas) antes de enviar el formulario porque recoge las opciones disponibles.
```

Review notes: Simplifies while preserving recommendation, sequence, rationale, and exact link. / Simplifies while preserving recommendation, sequence, link, and rationale. / Review 1 has invalid invariant coverage: missing [], duplicate [3], extra []. Raw checks are retained; this answer cannot pass.

## modes-es-055 · exact-format

Source task:

> Produce JSON con exactamente "series", "quantity", "authorized" y "reason". series es "SR/2-C", quantity 0 y authorized false. La razón en español debe indicar que no se liberó ninguna unidad porque la inspección está incompleta. Respeta los tipos JSON.

### baseline: pass

```text
{"series":"SR/2-C","quantity":0,"authorized":false,"reason":"No se liberó ninguna unidad porque la inspección está incompleta."}
```

### lite: pass

```text
{"series":"SR/2-C","quantity":0,"authorized":false,"reason":"No se liberó ninguna unidad porque la inspección está incompleta."}
```

### full: pass

```text
{"series":"SR/2-C","quantity":0,"authorized":false,"reason":"No se liberó ninguna unidad porque la inspección está incompleta."}
```

### ultra: pass

```text
{"series":"SR/2-C","quantity":0,"authorized":false,"reason":"No se liberó ninguna unidad porque la inspección está incompleta."}
```

### off: pass

```text
{"series":"SR/2-C","quantity":0,"authorized":false,"reason":"No se liberó ninguna unidad porque la inspección está incompleta."}
```

## modes-es-056 · exact-format

Source task:

> Edita solo la prosa manteniendo el comando: “Para poder consultar la cola sin alterarla, ejecute `cola ver --solo-lectura`. El comando no elimina entradas.” Conserva expresamente la ausencia de eliminación.

### baseline: pass

```text
Para consultar la cola sin modificarla, ejecute `cola ver --solo-lectura`. El comando no elimina entradas.
```

### lite: pass

```text
Para consultar la cola sin alterarla, ejecute `cola ver --solo-lectura`. El comando no elimina entradas.
```

### full: pass

```text
Para consultar la cola sin alterarla, ejecute `cola ver --solo-lectura`. El comando no elimina entradas.
```

### ultra: pass

```text
Para consultar la cola sin alterarla, ejecute `cola ver --solo-lectura`. El comando no elimina entradas.
```

### off: pass

```text
Para consultar la cola sin alterarla, ejecute `cola ver --solo-lectura`. El comando no elimina entradas.
```

## modes-es-057 · exact-format

Source task:

> Devuelve exactamente tres viñetas, sin título: la ruta A-31 se suspende el 18 de enero; A-32 sigue funcionando; el reembolso se puede solicitar y no se paga automáticamente. Mantén los códigos.

### baseline: pass

```text
- La ruta A-31 se suspende el 18 de enero.
- A-32 sigue funcionando.
- El reembolso se puede solicitar, pero no se paga automáticamente.
```

### lite: pass

```text
- La ruta A-31 se suspende el 18 de enero.
- A-32 sigue funcionando.
- El reembolso se puede solicitar; no se paga automáticamente.
```

### full: pass

```text
- La ruta A-31 se suspende el 18 de enero.
- A-32 sigue funcionando.
- El reembolso se puede solicitar; no se paga automáticamente.
```

### ultra: pass

```text
- La ruta A-31 se suspende el 18 de enero.
- A-32 sigue funcionando.
- El reembolso se puede solicitar; no se paga automáticamente.
```

### off: pass

```text
- La ruta A-31 se suspende el 18 de enero.
- La ruta A-32 sigue funcionando.
- El reembolso se puede solicitar y no se paga automáticamente.
```

## modes-es-058 · exact-format

Source task:

> Devuelve solo esta línea sin cambiar espacios o signos: CTRL-8 | pendiente | 0/18 revisados

### baseline: pass

```text
CTRL-8 | pendiente | 0/18 revisados
```

### lite: pass

```text
CTRL-8 | pendiente | 0/18 revisados
```

### full: pass

```text
CTRL-8 | pendiente | 0/18 revisados
```

### ultra: pass

```text
CTRL-8 | pendiente | 0/18 revisados
```

### off: pass

```text
CTRL-8 | pendiente | 0/18 revisados
```

## modes-es-059 · exact-format

Source task:

> Reescribe en un párrafo, conservando ruta y variable: guarde el borrador en /informes/2030/nota_final.md. Mantenga LISTO=false hasta que lo apruebe la editora. Guardar el archivo no equivale a recibir aprobación.

### baseline: pass

```text
Guarde el borrador en /informes/2030/nota_final.md y mantenga LISTO=false hasta que lo apruebe la editora. Guardar el archivo no equivale a recibir aprobación.
```

### lite: pass

```text
Guarde el borrador en /informes/2030/nota_final.md. Mantenga LISTO=false hasta que lo apruebe la editora. Guardar el archivo no equivale a recibir aprobación.
```

### full: pass

```text
Guarde el borrador en /informes/2030/nota_final.md. Mantenga LISTO=false hasta que lo apruebe la editora. Guardar el archivo no equivale a recibir aprobación.
```

### ultra: pass

```text
Guarde el borrador en /informes/2030/nota_final.md. Mantenga LISTO=false hasta que lo apruebe la editora. Guardar el archivo no equivale a recibir aprobación.
```

### off: pass

```text
Guarde el borrador en /informes/2030/nota_final.md y mantenga LISTO=false hasta que lo apruebe la editora. Guardar el archivo no equivale a recibir aprobación.
```

## modes-es-060 · exact-format

Source task:

> Devuelve únicamente JSON con "code", "delay_seconds" y "description". code es "ESPERA_4" y delay_seconds 30. La descripción en español debe indicar que la espera de 30 segundos es recomendada, no obligatoria.

### baseline: pass

```text
{"code":"ESPERA_4","delay_seconds":30,"description":"La espera de 30 segundos es recomendada, no obligatoria."}
```

### lite: pass

```text
{"code":"ESPERA_4","delay_seconds":30,"description":"La espera de 30 segundos es recomendada, no obligatoria."}
```

### full: pass

```text
{"code":"ESPERA_4","delay_seconds":30,"description":"La espera de 30 segundos es recomendada, no obligatoria."}
```

### ultra: pass

```text
{"code":"ESPERA_4","delay_seconds":30,"description":"La espera de 30 segundos es recomendada, no obligatoria."}
```

### off: pass

```text
{"code":"ESPERA_4","delay_seconds":30,"description":"La espera de 30 segundos es recomendada, no obligatoria."}
```

## modes-es-061 · voice

Source task:

> Mejora esta respuesta amable sin prometer el resultado: “Gracias por avisar del banco inestable, Vera. Hemos pedido al taller que lo examine. Aún no sabemos si puede repararse, pero te comunicaremos el resultado cuando llegue.”

### baseline: pass

```text
Gracias por avisarnos de que el banco está inestable, Vera. Hemos pedido al taller que lo examine. Aún no sabemos si podrá repararse; en cuanto recibamos su valoración, te la comunicaremos.
```

### lite: pass

```text
Gracias por avisarnos del banco inestable, Vera. Hemos pedido al taller que lo examine. Aún no sabemos si puede repararse, pero te comunicaremos el resultado cuando lo recibamos.
```

### full: pass

```text
Gracias por avisarnos del banco inestable, Vera. Hemos pedido al taller que lo examine. Aún no sabemos si puede repararse; te comunicaremos el resultado cuando lo recibamos.
```

### ultra: pass

```text
Gracias por avisarnos del banco inestable, Vera. Hemos pedido al taller que lo examine. Aún no sabemos si puede repararse; te comunicaremos el resultado cuando llegue.
```

### off: pass

```text
Gracias por avisarnos del banco inestable, Vera. Hemos pedido al taller que lo examine. Aún no sabemos si se puede reparar, pero te informaremos en cuanto recibamos el resultado.
```

## modes-es-062 · voice

Source task:

> Acorta conservando la broma: “El romero se ha adueñado de la ventana como un administrador muy aromático. Contamos cinco brotes nuevos esta semana. No es un récord: la semana anterior no contamos. El alquiler sigue pagándose con luz.”

### baseline: pass

```text
El romero administra la ventana con mucho aroma: cinco brotes nuevos esta semana. ¿Récord? La anterior no contamos. El alquiler se paga con luz.
```

### lite: pass

```text
El romero se ha adueñado de la ventana como un administrador aromático. Contamos cinco brotes nuevos esta semana. No es un récord: la anterior no contamos. El alquiler sigue pagándose con luz.
```

### full: pass

```text
El romero manda en la ventana como un administrador muy aromático. Contamos cinco brotes nuevos esta semana. No es un récord: la semana anterior no contamos. El alquiler sigue pagándose con luz.
```

### ultra: pass

```text
El romero manda en la ventana como administrador aromático. Contamos cinco brotes nuevos esta semana. ¿Récord? La anterior no contamos. El alquiler sigue pagándose con luz.
```

### off: pass

```text
El romero manda en la ventana como un administrador aromático: cinco brotes nuevos esta semana. ¿Un récord? La semana pasada no contamos. El alquiler sigue pagándose con luz.
```

## modes-es-063 · voice

Source task:

> Haz directa la disculpa: “Yo indiqué el código postal equivocado. El almacén usó el dato que envié. He preguntado al transportista si puede cambiar el recorrido, pero aún no ha contestado. Siento el retraso.” No culpes al almacén ni garantices el cambio.

### baseline: flagged

```text
Siento el retraso: indiqué mal el código postal. He preguntado al transportista si puede cambiar el recorrido, pero aún no ha respondido.
```

Review notes: La disculpa es directa, pero omite la actuación del almacén con el dato suministrado. / La disculpa es directa, pero omite la explicación material de la actuación del almacén.

### lite: pass

```text
Siento el retraso. Indiqué el código postal equivocado y el almacén usó el dato que envié. He preguntado al transportista si puede cambiar el recorrido, pero aún no ha contestado.
```

### full: pass

```text
Siento el retraso. Yo indiqué el código postal equivocado; el almacén usó el dato que envié. He preguntado al transportista si puede cambiar el recorrido, pero aún no ha contestado.
```

### ultra: pass

```text
Siento el retraso. Indiqué mal el código postal; el almacén usó el dato que envié. He preguntado al transportista si puede cambiar el recorrido, pero aún no ha respondido.
```

### off: pass

```text
Siento el retraso. Indiqué mal el código postal; el almacén usó el dato que envié. He preguntado al transportista si puede cambiar el recorrido, pero aún no ha contestado.
```

## modes-es-064 · voice

Source task:

> Reescribe con tono sereno: “Se encontraron dos cascos junto a la pista después del cierre. No se sabe de quién son. Están en la oficina de mantenimiento. Sus dueños pueden acudir a recepción y describirlos antes de recogerlos. No sabemos si se dejaron allí a propósito.”

### baseline: pass

```text
Después del cierre se encontraron dos cascos junto a la pista. Están en la oficina de mantenimiento y no sabemos a quién pertenecen ni si se dejaron allí a propósito. Sus dueños pueden acudir a recepción y describirlos antes de recogerlos.
```

### lite: pass

```text
Se encontraron dos cascos junto a la pista después del cierre. No se sabe de quién son ni si se dejaron allí a propósito. Están en la oficina de mantenimiento. Sus dueños pueden acudir a recepción y describirlos antes de recogerlos.
```

### full: pass

```text
Se encontraron dos cascos junto a la pista después del cierre. Están en la oficina de mantenimiento. No se sabe de quién son ni si se dejaron allí a propósito. Sus dueños pueden acudir a recepción y describirlos antes de recogerlos.
```

### ultra: pass

```text
Se encontraron dos cascos junto a la pista después del cierre. Están en la oficina de mantenimiento. No se sabe de quién son ni si se dejaron allí a propósito. Sus dueños pueden acudir a recepción y describirlos antes de recogerlos.
```

### off: pass

```text
Después del cierre se encontraron dos cascos junto a la pista. Están en la oficina de mantenimiento. No se sabe de quién son ni si se dejaron allí a propósito. Sus dueños pueden acudir a recepción y describirlos antes de recogerlos.
```

## modes-es-065 · voice

Source task:

> Ajusta este diálogo sin eliminar la vacilación: “Podría ir en el tren temprano”, dijo Alba, “si acaba la visita. Pero no he comprado billete y no quiero que me esperes como si ya estuviera decidido.” No conviertas la posibilidad en plan.

### baseline: pass

```text
—Podría tomar el tren temprano si termina la visita —dijo Alba—. Pero aún no he comprado billete… No quiero que me esperes como si ya lo hubiera decidido.
```

### lite: pass

```text
“Podría ir en el tren temprano”, dijo Alba, “si acaba la visita. Pero no he comprado billete y no quiero que me esperes como si ya estuviera decidido.”
```

### full: pass

```text
«Podría ir en el tren temprano si acaba la visita», dijo Alba. «Pero no he comprado billete y no quiero que me esperes como si ya estuviera decidido».
```

### ultra: pass

```text
“Podría tomar el tren temprano”, dijo Alba, “si acaba la visita. Pero no he comprado billete y no quiero que me esperes como si ya estuviera decidido.”
```

### off: pass

```text
«Podría ir en el tren temprano —dijo Alba—, si acaba la visita. Pero… no he comprado billete y no quiero que me esperes como si ya estuviera decidido».
```

## modes-es-066 · scope

Source task:

> Responde solo quién tiene la próxima acción registrada: la coordinadora redactó el plan; la técnica debe comprobar el esquema antes de que la coordinadora lo envíe al cliente; el cliente podrá comentar después. No hay fecha de comprobación.

### baseline: pass

```text
La técnica.
```

### lite: pass

```text
La técnica.
```

### full: pass

```text
La técnica.
```

### ultra: pass

```text
La técnica.
```

### off: pass

```text
La técnica.
```

## modes-es-067 · scope

Source task:

> Cambia solo la segunda frase y devuelve las tres: “El museo abre a las diez. Es obligatorio que los visitantes conserven la entrada hasta la salida. La tienda cierra a las seis.” Mantén la primera y la tercera literalmente.

### baseline: pass

```text
El museo abre a las diez. Los visitantes deben conservar la entrada hasta la salida. La tienda cierra a las seis.
```

### lite: pass

```text
El museo abre a las diez. Los visitantes deben conservar la entrada hasta la salida. La tienda cierra a las seis.
```

### full: pass

```text
El museo abre a las diez. Los visitantes deben conservar la entrada hasta la salida. La tienda cierra a las seis.
```

### ultra: pass

```text
El museo abre a las diez. Los visitantes deben conservar la entrada hasta la salida. La tienda cierra a las seis.
```

### off: pass

```text
El museo abre a las diez. Los visitantes deben conservar la entrada hasta la salida. La tienda cierra a las seis.
```

## modes-es-068 · scope

Source task:

> Responde solo si hubo decisión sobre la iluminación: el consejo aprobó nuevas mesas, aplazó la decisión de iluminación hasta el estudio y pidió muestras para pintar la puerta. El estudio no tiene fecha.

### baseline: pass

```text
No; la decisión sobre la iluminación se aplazó hasta el estudio.
```

### lite: pass

```text
No. La decisión sobre la iluminación se aplazó hasta el estudio, que no tiene fecha.
```

### full: pass

```text
No. La decisión sobre la iluminación se aplazó hasta el estudio, que no tiene fecha.
```

### ultra: pass

```text
No; se aplazó hasta el estudio, que no tiene fecha.
```

### off: pass

```text
No; la decisión sobre la iluminación se aplazó hasta el estudio, que no tiene fecha.
```

## modes-es-069 · scope

Source task:

> Resume solo el problema que queda: la clienta agradeció cambiar el recipiente. El nuevo encaja, pero la bisagra sustituida todavía se atasca con el frío. El equipo no ha probado esa condición. La clienta no pidió cambiar toda la máquina.

### baseline: pass

```text
La bisagra sustituida todavía se atasca con el frío y el equipo no ha probado esa condición.
```

### lite: pass

```text
La bisagra sustituida todavía se atasca con el frío. El equipo no ha probado esa condición.
```

### full: pass

```text
La bisagra sustituida todavía se atasca con el frío. El equipo no ha probado esa condición.
```

### ultra: pass

```text
La bisagra sustituida todavía se atasca con el frío; el equipo no ha probado esa condición.
```

### off: pass

```text
La bisagra sustituida todavía se atasca con el frío; el equipo no ha probado esa condición.
```

## modes-es-070 · scope

Source task:

> Corrige solo la concordancia, manteniendo orden y datos: “Las dos bolsas fue cerradas antes de imprimir las etiquetas. No se sabe quién las cerró. Omar imprimió las etiquetas.” No atribuyas el cierre a Omar.

### baseline: pass

```text
Las dos bolsas fueron cerradas antes de imprimir las etiquetas. No se sabe quién las cerró. Omar imprimió las etiquetas.
```

### lite: pass

```text
Las dos bolsas fueron cerradas antes de imprimir las etiquetas. No se sabe quién las cerró. Omar imprimió las etiquetas.
```

### full: pass

```text
Las dos bolsas fueron cerradas antes de imprimir las etiquetas. No se sabe quién las cerró. Omar imprimió las etiquetas.
```

### ultra: pass

```text
Las dos bolsas fueron cerradas antes de imprimir las etiquetas. No se sabe quién las cerró. Omar imprimió las etiquetas.
```

### off: pass

```text
Las dos bolsas fueron cerradas antes de imprimir las etiquetas. No se sabe quién las cerró. Omar imprimió las etiquetas.
```

## modes-es-071 · ambiguity

Source task:

> Haz visible la ambigüedad: “Nico dijo a Paz que su permiso había caducado.” No consta a quién se refiere “su”. Reescribe sin elegir titular e indica solo la aclaración necesaria.

### baseline: pass

```text
Nico dijo a Paz que un permiso había caducado. Falta aclarar de quién era el permiso.
```

### lite: flagged

```text
Nico dijo a Paz que un permiso había caducado. Falta aclarar a quién se refiere «su»: ¿a Nico o a Paz?
```

Review notes: Explicita las dos lecturas contextuales sin resolver la ambigüedad. / No asigna titular, pero limita indebidamente las posibilidades de referencia.

### full: pass

```text
Nico dijo a Paz que un permiso había caducado. Falta aclarar de quién era el permiso.
```

### ultra: pass

```text
Nico dijo a Paz que un permiso había caducado. Falta aclarar a quién se refiere «su».
```

### off: pass

```text
Nico dijo a Paz que un permiso había caducado, pero no consta de quién era. Hay que aclarar a quién se refiere «su».
```

## modes-es-072 · ambiguity

Source task:

> Reescribe: “La carpeta se devolvió después de que Eva llamara al conserje. No sabemos quién la devolvió. El conserje registró la recepción a las 16:50.” Separa los actores conocidos de los desconocidos.

### baseline: pass

```text
Eva llamó al conserje. Después, alguien cuya identidad desconocemos devolvió la carpeta. El conserje registró la recepción a las 16:50.
```

### lite: pass

```text
Eva llamó al conserje. Después se devolvió la carpeta; no sabemos quién la devolvió. El conserje registró la recepción a las 16:50.
```

### full: pass

```text
Eva llamó al conserje. Después se devolvió la carpeta, pero no sabemos quién la devolvió. El conserje registró la recepción a las 16:50.
```

### ultra: pass

```text
Eva llamó al conserje. Después se devolvió la carpeta; no sabemos quién la devolvió. El conserje registró la recepción a las 16:50.
```

### off: pass

```text
Eva llamó al conserje. Después se devolvió la carpeta, pero no sabemos quién la devolvió. El conserje registró la recepción a las 16:50.
```

## modes-es-073 · ambiguity

Source task:

> La nota pone “entregar antes del 08/09”, sin año ni convención de fecha. Piden escribir el mes con letras. Explica brevemente qué falta; no elijas una fecha ni uses el año actual.

### baseline: pass

```text
Falta aclarar la convención de fecha: «08/09» puede significar 8 de septiembre o 9 de agosto. También falta el año; no puede fijarse una fecha completa.
```

### lite: pass

```text
Falta confirmar si «08/09» significa 8 de septiembre o 9 de agosto, y de qué año. Sin esa aclaración, no se puede escribir el mes con letras.
```

### full: pass

```text
Falta aclarar si «08/09» significa 8 de septiembre o 9 de agosto y a qué año corresponde. Sin esa información no puede escribirse la fecha completa con el mes en letras.
```

### ultra: pass

```text
Falta aclarar si «08/09» significa 8 de septiembre o 9 de agosto, y de qué año, para escribir el mes con letras.
```

### off: pass

```text
Falta aclarar si «08/09» significa 8 de septiembre o 9 de agosto, y a qué año corresponde. Sin esos datos no puede escribirse la fecha completa con el mes en letras.
```

## modes-es-074 · ambiguity

Source task:

> Redacta una actualización sin decidir entre fuentes: el panel indica “recogido” y el registro del depósito “pendiente de recogida”. Ambos se actualizaron a las 11:00 sin firma. No ha llegado confirmación del transportista.

### baseline: pass

```text
El panel indica «recogido», mientras que el registro del depósito indica «pendiente de recogida». Ambos se actualizaron a las 11:00, sin firma. No ha llegado confirmación del transportista, por lo que el estado de la recogida sigue sin confirmarse.
```

### lite: pass

```text
El panel indica «recogido», pero el registro del depósito indica «pendiente de recogida». Ambos se actualizaron a las 11:00, sin firma. No ha llegado confirmación del transportista, por lo que el estado de la recogida sigue sin confirmarse.
```

### full: pass

```text
Las fuentes discrepan: el panel indica «recogido» y el registro del depósito, «pendiente de recogida». Ambos se actualizaron a las 11:00, sin firma. No ha llegado confirmación del transportista, por lo que la recogida sigue sin confirmarse.
```

### ultra: pass

```text
El panel indica «recogido»; el registro del depósito, «pendiente de recogida». Ambos se actualizaron a las 11:00, sin firma. Los estados son contradictorios y no ha llegado confirmación del transportista.
```

### off: pass

```text
El estado de la recogida sigue sin confirmar: el panel indica «recogido», mientras que el registro del depósito indica «pendiente de recogida». Ambos se actualizaron a las 11:00, sin firma. No ha llegado confirmación del transportista.
```

## modes-es-075 · ambiguity

Source task:

> Aclara sin aumentar la certeza: “La abolladura pudo crecer durante el viaje, pero la imagen anterior está demasiado desenfocada para comparar.” El texto no dice que el viaje originara la abolladura.

### baseline: pass

```text
Es posible que la abolladura aumentara durante el viaje, pero la imagen anterior está demasiado desenfocada para comprobarlo mediante una comparación. Esto no implica que el viaje originara la abolladura.
```

### lite: pass

```text
La abolladura pudo aumentar de tamaño durante el viaje, pero la imagen anterior está demasiado desenfocada para comparar. Esto no significa que el viaje la originara.
```

### full: pass

```text
La abolladura pudo aumentar de tamaño durante el viaje, pero la imagen anterior está demasiado desenfocada para comparar. Esto no significa que el viaje originara la abolladura.
```

### ultra: pass

```text
La abolladura pudo aumentar durante el viaje, pero la imagen anterior está demasiado desenfocada para comparar. Esto no implica que el viaje la originara.
```

### off: pass

```text
La abolladura pudo aumentar durante el viaje, pero la imagen anterior está demasiado desenfocada para comprobarlo mediante una comparación. Esto no implica que el viaje originara la abolladura.
```

## modes-es-076 · evidence

Source task:

> Resume la observación: un voluntario contó 22 pasos de peces junto a una ventana del tanque entre las 12:00 y las 12:20. El mismo pez podía pasar varias veces. No se observaron otras ventanas o periodos. No estimes cuántos peces hay en total.

### baseline: pass

```text
Entre las 12:00 y las 12:20, un voluntario contó 22 pasos de peces junto a una ventana del tanque. Un mismo pez podía pasar varias veces. La observación se limitó a esa ventana y ese periodo; no permite determinar el número total de peces.
```

### lite: pass

```text
Un voluntario contó 22 pasos de peces junto a una ventana del tanque entre las 12:00 y las 12:20. El mismo pez podía pasar varias veces. No se observaron otras ventanas ni periodos; el recuento no permite estimar cuántos peces hay en total.
```

### full: pass

```text
Un voluntario contó 22 pasos de peces junto a una ventana del tanque entre las 12:00 y las 12:20. El mismo pez podía pasar varias veces. No se observaron otras ventanas ni periodos; el recuento no permite estimar el total de peces.
```

### ultra: pass

```text
Un voluntario contó 22 pasos de peces junto a una ventana del tanque entre las 12:00 y las 12:20. Un mismo pez podía pasar varias veces. No se observaron otras ventanas ni periodos; el conteo no permite estimar el total de peces.
```

### off: pass

```text
Entre las 12:00 y las 12:20, un voluntario contó 22 pasos de peces junto a una ventana del tanque. Un mismo pez podía pasar varias veces. No se observaron otras ventanas ni otros periodos, por lo que el recuento no permite determinar cuántos peces hay en total.
```

## modes-es-077 · evidence

Source task:

> Reescribe para la inspección: “No se vio óxido en la cara exterior de la puerta.” No se desmontó la puerta ni se hicieron análisis. No extiendas la observación a las partes ocultas.

### baseline: pass

```text
En la inspección visual no se observó óxido en la cara exterior de la puerta. No se desmontó la puerta ni se realizaron análisis; la observación no abarca las partes ocultas.
```

### lite: pass

```text
No se observó óxido en la cara exterior de la puerta. No se desmontó la puerta ni se hicieron análisis. La observación no abarca las partes ocultas.
```

### full: pass

```text
No se observó óxido en la cara exterior de la puerta. No se desmontó la puerta ni se hicieron análisis. Esta observación no abarca las partes ocultas.
```

### ultra: pass

```text
No se observó óxido en la cara exterior de la puerta. No se desmontó ni se hicieron análisis; la observación no abarca las partes ocultas.
```

### off: pass

```text
No se observó óxido en la cara exterior de la puerta. No se desmontó la puerta ni se realizaron análisis; esta observación no se extiende a las partes ocultas.
```

## modes-es-078 · evidence

Source task:

> Explica al ayuntamiento: el 80% de 75 personas que voluntariamente escanearon un QR pidieron más fuentes. El cartel estaba junto a la entrada de un polideportivo. No hubo selección aleatoria. No lo presentes como opinión del 80% de la ciudad.

### baseline: pass

```text
El 80% de las 75 personas que escanearon voluntariamente un QR pidió más fuentes. El cartel estaba junto a la entrada de un polideportivo y no hubo selección aleatoria. El resultado describe a quienes participaron, no la opinión del 80% de la ciudad.
```

### lite: pass

```text
El 80% de las 75 personas que escanearon voluntariamente un QR pidieron más fuentes. El cartel estaba junto a la entrada de un polideportivo. No hubo selección aleatoria, por lo que el resultado no representa la opinión del 80% de la ciudad.
```

### full: pass

```text
El 80% de las 75 personas que escanearon voluntariamente un QR pidió más fuentes. El cartel estaba junto a la entrada de un polideportivo. No hubo selección aleatoria, por lo que el resultado no representa la opinión del 80% de la ciudad.
```

### ultra: pass

```text
El 80% de las 75 personas que escanearon voluntariamente un QR pidió más fuentes. El cartel estaba junto a la entrada de un polideportivo. No hubo selección aleatoria: el resultado no representa la opinión del 80% de la ciudad.
```

### off: pass

```text
El 80% de las 75 personas que escanearon voluntariamente un QR pidió más fuentes. El cartel estaba junto a la entrada de un polideportivo y no hubo selección aleatoria. El resultado describe las respuestas de quienes participaron, no la opinión del 80% de la ciudad.
```

## modes-es-079 · evidence

Source task:

> Reescribe esta nota de agenda, sin consejo médico: la cita de las 10:15 se canceló porque el profesional no estará disponible. No se indica el motivo. Se contactará con las personas afectadas para acordar otra hora. No se ha fijado sustitución.

### baseline: pass

```text
La cita de las 10:15 se canceló porque el profesional no estará disponible. No se indica el motivo de su indisponibilidad. Se contactará con las personas afectadas para acordar otra hora. No se ha fijado sustitución.
```

### lite: pass

```text
La cita de las 10:15 se canceló porque el profesional no estará disponible. No se indica el motivo de su ausencia. Se contactará con las personas afectadas para acordar otra hora. No se ha fijado una sustitución.
```

### full: pass

```text
La cita de las 10:15 se canceló porque el profesional no estará disponible. No se indica el motivo de su indisponibilidad. Se contactará con las personas afectadas para acordar otra hora. Aún no se ha fijado una cita de sustitución.
```

### ultra: pass

```text
La cita de las 10:15 se canceló porque el profesional no estará disponible; no se indica el motivo. Se contactará con las personas afectadas para acordar otra hora. No se ha fijado sustitución.
```

### off: pass

```text
La cita de las 10:15 se canceló porque el profesional no estará disponible. No se indica el motivo de su indisponibilidad. Se contactará con las personas afectadas para acordar otra hora. No se ha fijado sustitución.
```

## modes-es-080 · evidence

Source task:

> Escribe una nota de calidad: la báscula indicó 1 kg cuatro veces con una pesa certificada de 1 kg hoy. Solo se probó esa carga. No demuestra exactitud con otras cargas ni constituye una calibración completa.

### baseline: pass

```text
Hoy, la báscula indicó 1 kg en cuatro mediciones con una pesa certificada de 1 kg. Solo se probó esa carga; los resultados no demuestran exactitud con otras cargas ni constituyen una calibración completa.
```

### lite: pass

```text
Hoy, la báscula indicó 1 kg en cuatro mediciones con una pesa certificada de 1 kg. Solo se probó esa carga. El resultado no demuestra exactitud con otras cargas ni constituye una calibración completa.
```

### full: pass

```text
Hoy, la báscula indicó 1 kg en cuatro mediciones con una pesa certificada de 1 kg. Solo se probó esa carga. El resultado no demuestra exactitud con otras cargas ni constituye una calibración completa.
```

### ultra: pass

```text
Hoy, la báscula indicó 1 kg en cuatro mediciones con una pesa certificada de 1 kg. Solo se probó esa carga: el resultado no demuestra exactitud con otras cargas ni constituye una calibración completa.
```

### off: pass

```text
Hoy, la báscula indicó 1 kg en cuatro mediciones con una pesa certificada de 1 kg. Solo se probó esa carga. Este resultado no demuestra exactitud con otras cargas ni constituye una calibración completa.
```

## modes-es-081 · translation

Source task:

> Traduce el aviso completo al español, sin resumir: “The archive will close at 13:00 UTC on 24 December 2030. Online requests may still be submitted, but staff will not review them until 3 January 2031. Submission does not reserve an appointment.”

### baseline: pass

```text
El archivo cerrará a las 13:00 UTC del 24 de diciembre de 2030. Se podrán seguir presentando solicitudes en línea, pero el personal no las revisará hasta el 3 de enero de 2031. La presentación de una solicitud no reserva una cita.
```

### lite: pass

```text
El archivo cerrará a las 13:00 UTC del 24 de diciembre de 2030. Se podrán seguir enviando solicitudes en línea, pero el personal no las revisará hasta el 3 de enero de 2031. El envío no reserva una cita.
```

### full: pass

```text
El archivo cerrará a las 13:00 UTC del 24 de diciembre de 2030. Se podrán seguir presentando solicitudes en línea, pero el personal no las revisará hasta el 3 de enero de 2031. Presentar una solicitud no reserva una cita.
```

### ultra: pass

```text
El archivo cerrará a las 13:00 UTC del 24 de diciembre de 2030. Se podrán seguir enviando solicitudes en línea, pero el personal no las revisará hasta el 3 de enero de 2031. Enviar una solicitud no reserva una cita.
```

### off: pass

```text
El archivo cerrará a las 13:00 UTC del 24 de diciembre de 2030. Se podrán seguir presentando solicitudes en línea, pero el personal no las revisará hasta el 3 de enero de 2031. La presentación de una solicitud no reserva una cita.
```

## modes-es-082 · translation

Source task:

> Traduce al español sin convertir moneda: “The invoice is A$760 including tax. Optional training costs A$95 per person and is not included. The invoice does not say whether travel expenses will be charged.”

### baseline: pass

```text
La factura asciende a A$760, impuestos incluidos. La formación opcional cuesta A$95 por persona y no está incluida. La factura no indica si se cobrarán gastos de viaje.
```

### lite: pass

```text
El importe de la factura es de A$760, impuestos incluidos. La formación opcional cuesta A$95 por persona y no está incluida. La factura no indica si se cobrarán los gastos de viaje.
```

### full: pass

```text
El importe de la factura es de A$760, impuestos incluidos. La formación opcional cuesta A$95 por persona y no está incluida. La factura no indica si se cobrarán gastos de viaje.
```

### ultra: pass

```text
La factura es de A$760, impuestos incluidos. La formación opcional cuesta A$95 por persona y no está incluida. La factura no indica si se cobrarán gastos de viaje.
```

### off: pass

```text
El importe de la factura es de A$760, impuestos incluidos. La formación opcional cuesta A$95 por persona y no está incluida. La factura no indica si se cobrarán los gastos de viaje.
```

## modes-es-083 · translation

Source task:

> Traduce todo el texto al español sin deducir el género de Sam: “Sam reviewed the diagram, not the device. The diagram was approved afterward, but the note does not name the approver. Sam has not confirmed when the device will be tested.”

### baseline: pass

```text
Sam revisó el diagrama, no el dispositivo. El diagrama fue aprobado después, pero la nota no indica quién lo aprobó. Sam no ha confirmado cuándo se probará el dispositivo.
```

### lite: pass

```text
Sam revisó el diagrama, no el dispositivo. El diagrama fue aprobado después, pero la nota no indica quién lo aprobó. Sam no ha confirmado cuándo se probará el dispositivo.
```

### full: pass

```text
Sam revisó el diagrama, no el dispositivo. El diagrama se aprobó después, pero la nota no identifica a la persona que lo aprobó. Sam no ha confirmado cuándo se probará el dispositivo.
```

### ultra: pass

```text
Sam revisó el diagrama, no el dispositivo. El diagrama se aprobó después, pero la nota no identifica a quien lo aprobó. Sam no ha confirmado cuándo se probará el dispositivo.
```

### off: pass

```text
Sam revisó el diagrama, no el dispositivo. El diagrama fue aprobado después, pero la nota no identifica a quien lo aprobó. Sam no ha confirmado cuándo se probará el dispositivo.
```

## modes-es-084 · translation

Source task:

> El idioma de destino es español. Traduce manteniendo [12] y su relación con la afirmación: “In the supplied study, 18 of 30 inspected samples had surface marks [12]. The samples came from one supplier-selected batch. The study does not estimate marks across all production.”

### baseline: pass

```text
En el estudio proporcionado, 18 de las 30 muestras inspeccionadas presentaban marcas superficiales [12]. Las muestras procedían de un único lote seleccionado por el proveedor. El estudio no estima la presencia de marcas en toda la producción.
```

### lite: pass

```text
En el estudio proporcionado, 18 de las 30 muestras inspeccionadas tenían marcas superficiales [12]. Las muestras procedían de un único lote seleccionado por el proveedor. El estudio no estima la presencia de marcas en toda la producción.
```

### full: pass

```text
En el estudio proporcionado, 18 de las 30 muestras inspeccionadas tenían marcas superficiales [12]. Las muestras procedían de un único lote seleccionado por el proveedor. El estudio no estima la presencia de marcas en toda la producción.
```

### ultra: pass

```text
En el estudio proporcionado, 18 de las 30 muestras inspeccionadas tenían marcas superficiales [12]. Las muestras procedían de un único lote seleccionado por el proveedor. El estudio no estima la presencia de marcas en toda la producción.
```

### off: pass

```text
En el estudio proporcionado, 18 de las 30 muestras inspeccionadas tenían marcas superficiales [12]. Las muestras procedían de un único lote seleccionado por el proveedor. El estudio no estima la presencia de marcas en el conjunto de la producción.
```

## modes-es-085 · translation

Source task:

> Traduce al español únicamente el valor de "note" y devuelve un objeto JSON con las mismas claves y los demás valores intactos. Fuente: {"job":"Z-91","attempts":2,"finished":false,"note":"Two attempts ended before completion. The cause has not been established."}

### baseline: pass

```text
{"job":"Z-91","attempts":2,"finished":false,"note":"Dos intentos terminaron antes de completarse. La causa no se ha establecido."}
```

### lite: pass

```text
{"job":"Z-91","attempts":2,"finished":false,"note":"Dos intentos terminaron antes de completarse. No se ha establecido la causa."}
```

### full: pass

```text
{"job":"Z-91","attempts":2,"finished":false,"note":"Dos intentos terminaron antes de completarse. No se ha establecido la causa."}
```

### ultra: pass

```text
{"job":"Z-91","attempts":2,"finished":false,"note":"Dos intentos terminaron antes de completarse. La causa no se ha establecido."}
```

### off: pass

```text
{"job":"Z-91","attempts":2,"finished":false,"note":"Dos intentos terminaron antes de completarse. La causa no se ha determinado."}
```

## modes-es-086 · translation

Source task:

> Traduce estos tres elementos al español manteniendo numeración y orden: “1. Open the case only after the power is disconnected. 2. Check whether the indicator is dark; do not assume it is. 3. You may leave the case open while waiting for the technician.”

### baseline: pass

```text
1. Abra la carcasa solo después de desconectar la alimentación eléctrica.
2. Compruebe si el indicador está apagado; no dé por hecho que lo está.
3. Puede dejar la carcasa abierta mientras espera al técnico.
```

### lite: pass

```text
1. Abra la carcasa solo después de desconectar la alimentación eléctrica.
2. Compruebe si el indicador está apagado; no dé por hecho que lo está.
3. Puede dejar la carcasa abierta mientras espera al técnico.
```

### full: pass

```text
1. Abra la carcasa solo después de desconectar la alimentación eléctrica.
2. Compruebe si el indicador está apagado; no dé por hecho que lo está.
3. Puede dejar la carcasa abierta mientras espera al técnico.
```

### ultra: pass

```text
1. Abre la carcasa solo después de desconectar la alimentación eléctrica.
2. Comprueba si el indicador está apagado; no lo des por hecho.
3. Puedes dejar la carcasa abierta mientras esperas al técnico.
```

### off: pass

```text
1. Abra la carcasa solo después de desconectar la alimentación eléctrica.
2. Compruebe si el indicador está apagado; no dé por hecho que lo está.
3. Puede dejar la carcasa abierta mientras espera al técnico.
```

## modes-es-087 · translation

Source task:

> El idioma de destino es español. Traduce todo, sin convertir unidades: “The board is 3.5 ft long and 0.75 in thick. These are nominal dimensions; no individual board was measured. The pack contains six boards, not six square feet of material.”

### baseline: pass

```text
La tabla mide 3,5 pies de largo y 0,75 pulgadas de grosor. Estas son dimensiones nominales; no se midió ninguna tabla individualmente. El paquete contiene seis tablas, no seis pies cuadrados de material.
```

### lite: pass

```text
La tabla mide 3.5 ft de largo y 0.75 in de grosor. Estas son dimensiones nominales; no se midió ninguna tabla individualmente. El paquete contiene seis tablas, no seis pies cuadrados de material.
```

### full: pass

```text
La tabla mide 3,5 ft de largo y 0,75 in de grosor. Estas son dimensiones nominales; no se midió ninguna tabla individualmente. El paquete contiene seis tablas, no seis pies cuadrados de material.
```

### ultra: pass

```text
La tabla mide 3.5 ft de largo y 0.75 in de grosor. Son dimensiones nominales; no se midió ninguna tabla individualmente. El paquete contiene seis tablas, no seis pies cuadrados de material.
```

### off: pass

```text
La tabla mide 3,5 pies de largo y 0,75 pulgadas de grosor. Estas son dimensiones nominales; no se midió ninguna tabla individualmente. El paquete contiene seis tablas, no seis pies cuadrados de material.
```

## modes-es-088 · translation

Source task:

> El idioma de destino es español. Traduce íntegramente: “Of 160 people who voluntarily answered a survey in the museum shop, 104 preferred a later closing time. The survey was not random and did not include people who never visit the shop. A preference is not proof of future evening attendance.”

### baseline: pass

```text
De las 160 personas que respondieron voluntariamente a una encuesta en la tienda del museo, 104 preferían un horario de cierre más tardío. La encuesta no fue aleatoria y no incluyó a las personas que nunca visitan la tienda. Una preferencia no demuestra que vaya a haber asistencia en horario vespertino en el futuro.
```

### lite: pass

```text
De las 160 personas que respondieron voluntariamente a una encuesta en la tienda del museo, 104 preferían un horario de cierre más tardío. La encuesta no fue aleatoria y no incluyó a personas que nunca visitan la tienda. Una preferencia no demuestra que habrá asistencia futura por la tarde o por la noche.
```

### full: pass

```text
De las 160 personas que respondieron voluntariamente a una encuesta en la tienda del museo, 104 preferían un horario de cierre más tardío. La encuesta no fue aleatoria y no incluyó a personas que nunca visitan la tienda. Una preferencia no demuestra que habrá asistencia en horario vespertino en el futuro.
```

### ultra: pass

```text
De las 160 personas que respondieron voluntariamente a una encuesta en la tienda del museo, 104 preferían un horario de cierre más tardío. La encuesta no fue aleatoria y no incluyó a quienes nunca visitan la tienda. Una preferencia no demuestra que vayan a acudir por la tarde o por la noche en el futuro.
```

### off: pass

```text
De las 160 personas que respondieron voluntariamente a una encuesta en la tienda del museo, 104 preferían un horario de cierre más tardío. La encuesta no fue aleatoria y no incluyó a personas que nunca visitan la tienda. Una preferencia no demuestra que vaya a haber visitas futuras por la tarde o por la noche.
```

## modes-es-089 · translation

Source task:

> El idioma de destino es español. Traduce conservando el conflicto: “The planner lists the trial as canceled. The laboratory lists it as postponed. Both records were updated at 09:20, and neither names an author. We have not received a final decision.”

### baseline: pass

```text
El planificador indica que el ensayo está cancelado. El laboratorio indica que está pospuesto. Ambos registros se actualizaron a las 09:20 y ninguno identifica a su autor. No hemos recibido una decisión definitiva.
```

### lite: pass

```text
El planificador indica que el ensayo está cancelado. El laboratorio indica que está pospuesto. Ambos registros se actualizaron a las 09:20 y ninguno identifica a su autor. No hemos recibido una decisión final.
```

### full: pass

```text
El planificador indica que el ensayo está cancelado. El laboratorio indica que está pospuesto. Ambos registros se actualizaron a las 09:20 y ninguno identifica a su autor. No hemos recibido una decisión definitiva.
```

### ultra: pass

```text
El planificador indica que el ensayo está cancelado. El laboratorio indica que está pospuesto. Ambos registros se actualizaron a las 09:20 y ninguno identifica a su autor. No hemos recibido una decisión final.
```

### off: pass

```text
El planificador indica que el ensayo está cancelado. El laboratorio indica que está aplazado. Ambos registros se actualizaron a las 09:20 y ninguno identifica a su autor. No hemos recibido una decisión definitiva.
```

## modes-es-090 · translation

Source task:

> Traduce al español manteniendo la voz de ficción: “The kettle clicked like an impatient uncle. I promised it nothing, because the tea leaves had vanished. Outside, the rain seemed to be rehearsing. I did not know whether the guest would arrive.”

### baseline: pass

```text
La tetera chasqueó como un tío impaciente. No le prometí nada, porque las hojas de té habían desaparecido. Afuera, la lluvia parecía estar ensayando. No sabía si el invitado llegaría.
```

### lite: pass

```text
La tetera hizo clic como un tío impaciente. No le prometí nada, porque las hojas de té habían desaparecido. Afuera, la lluvia parecía estar ensayando. No sabía si llegaría la visita.
```

### full: pass

```text
La tetera hizo clic como un tío impaciente. No le prometí nada, porque las hojas de té habían desaparecido. Afuera, la lluvia parecía estar ensayando. No sabía si llegaría la visita.
```

### ultra: pass

```text
La tetera hizo un chasquido como un tío impaciente. No le prometí nada, porque las hojas de té habían desaparecido. Afuera, la lluvia parecía estar ensayando. No sabía si llegaría la visita.
```

### off: pass

```text
La tetera hizo un clic como un tío impaciente. No le prometí nada, porque las hojas de té habían desaparecido. Afuera, la lluvia parecía estar ensayando. Yo no sabía si llegaría el invitado.
```

## modes-es-091 · translation

Source task:

> El idioma de destino es español. Traduce todo el mensaje: “The warning applies to the north walkway only. It does not close the garden or the south walkway. Repairs have been requested, but no contractor has accepted the job. Do not describe the whole site as closed.”

### baseline: pass

```text
La advertencia se aplica únicamente al sendero norte. No implica el cierre del jardín ni del sendero sur. Se han solicitado reparaciones, pero ningún contratista ha aceptado el trabajo. No describas todo el recinto como cerrado.
```

### lite: pass

```text
La advertencia se aplica únicamente al sendero norte. No implica el cierre del jardín ni del sendero sur. Se han solicitado reparaciones, pero ningún contratista ha aceptado el trabajo. No describas todo el recinto como cerrado.
```

### full: pass

```text
La advertencia se aplica únicamente al sendero norte. No implica el cierre del jardín ni del sendero sur. Se han solicitado reparaciones, pero ningún contratista ha aceptado el trabajo. No describas todo el recinto como cerrado.
```

### ultra: pass

```text
La advertencia se aplica solo al sendero norte. No cierra el jardín ni el sendero sur. Se han solicitado reparaciones, pero ningún contratista ha aceptado el trabajo. No describas todo el recinto como cerrado.
```

### off: pass

```text
La advertencia se aplica únicamente al sendero norte. No implica el cierre del jardín ni del sendero sur. Se han solicitado reparaciones, pero ningún contratista ha aceptado el trabajo. No describas todo el recinto como cerrado.
```

## modes-es-092 · translation

Source task:

> El idioma de destino es español. Traduce sin eliminar la cuenta: “There are 84 seats. Twelve are reserved and six are blocked for repairs, with no overlap. That leaves 66 currently available. The 20 seats on order are not part of the current total.”

### baseline: pass

```text
Hay 84 asientos. Doce están reservados y seis están bloqueados por reparaciones, sin que ningún asiento pertenezca a ambos grupos. Eso deja 66 disponibles actualmente. Los 20 asientos encargados no forman parte del total actual.
```

### lite: pass

```text
Hay 84 asientos. Doce están reservados y seis están bloqueados por reparaciones, sin que ningún asiento pertenezca a ambos grupos. Eso deja 66 disponibles actualmente. Los 20 asientos que se han pedido no forman parte del total actual.
```

### full: pass

```text
Hay 84 asientos. Doce están reservados y seis están bloqueados por reparaciones, sin que ningún asiento pertenezca a ambos grupos. Por tanto, actualmente hay 66 disponibles. Los 20 asientos pedidos no forman parte del total actual.
```

### ultra: pass

```text
Hay 84 asientos. Doce están reservados y seis están bloqueados por reparaciones, sin solapamiento entre ambos grupos. Quedan 66 disponibles actualmente. Los 20 asientos pedidos no forman parte del total actual.
```

### off: pass

```text
Hay 84 asientos. Doce están reservados y seis están bloqueados por reparaciones, sin que ningún asiento pertenezca a ambos grupos. Por lo tanto, quedan 66 disponibles actualmente. Los 20 asientos encargados no forman parte del total actual.
```

## modes-es-093 · translation

Source task:

> Traduce al español el texto completo. Mantén la cita "Hold for review" literalmente en inglés: “The label says ‘Hold for review’. This does not mean the item has failed inspection. Inspection has not started, and no release date is set.”

### baseline: pass

```text
La etiqueta dice «Hold for review». Esto no significa que el artículo no haya superado la inspección. La inspección no ha comenzado y no se ha fijado una fecha de liberación.
```

### lite: pass

```text
La etiqueta dice «Hold for review». Esto no significa que el artículo no haya pasado la inspección. La inspección no ha comenzado y no se ha fijado una fecha de liberación.
```

### full: pass

```text
La etiqueta dice «Hold for review». Esto no significa que el artículo no haya pasado la inspección. La inspección no ha comenzado y no se ha fijado una fecha de liberación.
```

### ultra: pass

```text
La etiqueta dice «Hold for review». Esto no significa que el artículo haya fallado la inspección. La inspección no ha comenzado y no hay una fecha de liberación fijada.
```

### off: pass

```text
La etiqueta dice «Hold for review». Esto no significa que el artículo no haya superado la inspección. La inspección no ha comenzado y no se ha fijado una fecha de autorización para su salida.
```

## modes-es-094 · translation

Source task:

> El idioma de destino es español. Traduce sin resolver la fecha ambigua: “The handwritten note says ‘return by 05/06’. It gives no year or date convention. Please confirm the intended date before replacing it with a month written in words.”

### baseline: flagged

```text
La nota manuscrita dice «devolver antes del 05/06». No indica el año ni el formato de fecha utilizado. Confirma la fecha prevista antes de sustituirla por una fecha con el mes escrito en palabras.
```

Review notes: Preserva los invariantes enumerados, pero adelanta materialmente el límite de devolución. / No resuelve la fecha, pero convierte el plazo inclusivo en exclusivo.

### lite: pass

```text
La nota manuscrita dice «devolver a más tardar el 05/06». No indica el año ni la convención de fecha utilizada. Confirma la fecha prevista antes de sustituirla por una fecha con el mes escrito en palabras.
```

### full: pass

```text
La nota manuscrita dice «devolver a más tardar el 05/06». No indica el año ni el formato de fecha. Confirma la fecha prevista antes de sustituirla por una fecha con el mes escrito en palabras.
```

### ultra: flagged

```text
La nota manuscrita dice «devolver antes del 05/06». No indica el año ni el formato de fecha. Confirma la fecha prevista antes de sustituirla por una fecha con el mes escrito en palabras.
```

Review notes: Preserva la ambigüedad, pero adelanta materialmente el límite de devolución. / Mantiene la ambigüedad, pero adelanta el límite de devolución.

### off: flagged

```text
La nota manuscrita dice «devolver antes del 05/06». No indica el año ni la convención de fecha utilizada. Confirma la fecha prevista antes de sustituirla por una fecha con el mes escrito en palabras.
```

Review notes: No resuelve la fecha, pero cambia el plazo inclusivo por uno anterior. / Cumple los invariantes, pero cambia el límite temporal del original.

## modes-es-095 · translation

Source task:

> El idioma de destino es español. Traduce íntegramente: “You must choose a delivery method. You may also add a note for the driver, but the note is optional. Leaving the note blank does not cancel the order. The button CONFIRM_2 must be pressed after choosing the method.”

### baseline: pass

```text
Debes elegir un método de entrega. También puedes añadir una nota para el conductor, pero la nota es opcional. Dejar la nota en blanco no cancela el pedido. Debes pulsar el botón CONFIRM_2 después de elegir el método.
```

### lite: pass

```text
Debes elegir un método de entrega. También puedes añadir una nota para el conductor, pero la nota es opcional. Dejar la nota en blanco no cancela el pedido. El botón CONFIRM_2 debe pulsarse después de elegir el método.
```

### full: pass

```text
Debes elegir un método de entrega. También puedes añadir una nota para quien realice la entrega, pero es opcional. Dejar la nota en blanco no cancela el pedido. El botón CONFIRM_2 debe pulsarse después de elegir el método.
```

### ultra: pass

```text
Debes elegir un método de entrega. También puedes añadir una nota para quien haga la entrega, pero es opcional. Dejar la nota en blanco no cancela el pedido. El botón CONFIRM_2 debe pulsarse después de elegir el método.
```

### off: pass

```text
Debes elegir un método de entrega. También puedes añadir una nota para el conductor, pero la nota es opcional. Dejar la nota en blanco no cancela el pedido. El botón CONFIRM_2 debe pulsarse después de elegir el método.
```

## modes-es-096 · translation

Source task:

> Traduce al español sin cambiar identificadores: “The timeout is 8 seconds per attempt, not 8 seconds for the whole job. The client makes at most three attempts. A response with HTTP 403 is not retried. The setting max_attempts=3 counts the initial attempt.”

### baseline: pass

```text
El tiempo de espera es de 8 segundos por intento, no de 8 segundos para todo el trabajo. El cliente realiza como máximo tres intentos. Una respuesta con HTTP 403 no se reintenta. La configuración max_attempts=3 cuenta el intento inicial.
```

### lite: pass

```text
El tiempo de espera es de 8 segundos por intento, no de 8 segundos para todo el trabajo. El cliente realiza como máximo tres intentos. No se reintenta una respuesta con HTTP 403. La configuración max_attempts=3 cuenta el intento inicial.
```

### full: pass

```text
El tiempo de espera es de 8 segundos por intento, no de 8 segundos para todo el trabajo. El cliente realiza como máximo tres intentos. No se reintenta una respuesta con HTTP 403. La configuración max_attempts=3 cuenta el intento inicial.
```

### ultra: pass

```text
El tiempo de espera es de 8 segundos por intento, no de 8 segundos para toda la tarea. El cliente realiza como máximo tres intentos. No se reintenta ante una respuesta HTTP 403. La configuración max_attempts=3 incluye el intento inicial.
```

### off: pass

```text
El tiempo de espera es de 8 segundos por intento, no de 8 segundos para todo el trabajo. El cliente realiza como máximo tres intentos. No se vuelve a intentar tras una respuesta con HTTP 403. La configuración max_attempts=3 cuenta el intento inicial.
```

## modes-es-097 · translation

Source task:

> El idioma de destino es español. Traduce todo el párrafo: “The river looked clearer after the rain, according to one observer. No turbidity measurement was taken. The observation does not show that the rain improved water quality or that the water is safe to drink.”

### baseline: pass

```text
El río parecía más claro después de la lluvia, según un observador. No se realizó ninguna medición de turbidez. La observación no demuestra que la lluvia haya mejorado la calidad del agua ni que el agua sea segura para beber.
```

### lite: pass

```text
El río parecía más claro después de la lluvia, según un observador. No se realizó ninguna medición de turbidez. La observación no demuestra que la lluvia haya mejorado la calidad del agua ni que el agua sea segura para beber.
```

### full: pass

```text
Según una persona que lo observó, el río parecía más claro después de la lluvia. No se midió la turbidez. La observación no demuestra que la lluvia haya mejorado la calidad del agua ni que el agua sea segura para beber.
```

### ultra: pass

```text
Según una persona que lo observó, el río parecía más claro después de la lluvia. No se midió la turbidez. La observación no demuestra que la lluvia mejorara la calidad del agua ni que el agua sea potable.
```

### off: pass

```text
El río parecía más claro después de la lluvia, según una persona que lo observó. No se realizó ninguna medición de turbidez. La observación no demuestra que la lluvia haya mejorado la calidad del agua ni que el agua sea segura para beber.
```

## modes-es-098 · translation

Source task:

> Traduce esta nota de agenda ficticia al español, sin añadir consejo médico: “The appointment is for a discussion of the supplied results, not a new test. The results have not been reviewed by the clinician yet. The patient may bring a support person. The note contains no diagnosis.”

### baseline: pass

```text
La cita es para hablar sobre los resultados proporcionados, no para realizar una nueva prueba. El profesional clínico aún no ha revisado los resultados. El paciente puede llevar a una persona de apoyo. La nota no contiene ningún diagnóstico.
```

### lite: pass

```text
La cita es para comentar los resultados proporcionados, no para realizar una nueva prueba. El profesional clínico aún no ha revisado los resultados. El paciente puede llevar a una persona de apoyo. La nota no contiene ningún diagnóstico.
```

### full: pass

```text
La cita es para hablar sobre los resultados proporcionados, no para realizar una nueva prueba. El profesional clínico aún no ha revisado los resultados. El paciente puede traer a una persona de apoyo. La nota no contiene ningún diagnóstico.
```

### ultra: pass

```text
La cita es para comentar los resultados proporcionados, no para realizar una nueva prueba. El profesional clínico aún no ha revisado los resultados. El paciente puede llevar a una persona de apoyo. La nota no contiene ningún diagnóstico.
```

### off: pass

```text
La cita es para hablar sobre los resultados proporcionados, no para realizar una nueva prueba. El profesional clínico aún no ha revisado los resultados. El paciente puede acudir con una persona de apoyo. La nota no contiene ningún diagnóstico.
```

## modes-es-099 · translation

Source task:

> El idioma de destino es español. Traduce esta cláusula ficticia sin interpretarla jurídicamente: “A written extension may change the delivery date only. It does not waive the inspection requirement. Silence from the buyer is not approval. This clause applies to order N-48, not to other orders.”

### baseline: pass

```text
Una prórroga por escrito puede modificar únicamente la fecha de entrega. No exime del requisito de inspección. El silencio del comprador no constituye aprobación. Esta cláusula se aplica al pedido N-48, no a otros pedidos.
```

### lite: pass

```text
Una prórroga por escrito puede cambiar únicamente la fecha de entrega. No exime del requisito de inspección. El silencio del comprador no constituye aprobación. Esta cláusula se aplica al pedido N-48, no a otros pedidos.
```

### full: pass

```text
Una prórroga por escrito puede cambiar únicamente la fecha de entrega. No exime del requisito de inspección. El silencio del comprador no constituye aprobación. Esta cláusula se aplica al pedido N-48, no a otros pedidos.
```

### ultra: pass

```text
Una prórroga por escrito puede cambiar únicamente la fecha de entrega. No exime del requisito de inspección. El silencio del comprador no constituye aprobación. Esta cláusula se aplica al pedido N-48, no a otros pedidos.
```

### off: pass

```text
Una prórroga por escrito puede modificar únicamente la fecha de entrega. No exime del requisito de inspección. El silencio del comprador no constituye aprobación. Esta cláusula se aplica al pedido N-48, no a otros pedidos.
```

## modes-es-100 · translation

Source task:

> El idioma de destino es español. Traduce todo el aviso y conserva el valor técnico OPEN: “The field remains OPEN until the supervisor closes it. OPEN does not mean the investigation has begun. The record was created automatically, and the note does not name an investigator.”

### baseline: pass

```text
El campo permanece en OPEN hasta que el supervisor lo cierre. OPEN no significa que la investigación haya comenzado. El registro se creó automáticamente y la nota no identifica a ningún investigador.
```

### lite: pass

```text
El campo permanece en OPEN hasta que el supervisor lo cierre. OPEN no significa que la investigación haya comenzado. El registro se creó automáticamente y la nota no identifica a ningún investigador.
```

### full: pass

```text
El campo permanece en OPEN hasta que el supervisor lo cierre. OPEN no significa que la investigación haya comenzado. El registro se creó automáticamente y la nota no identifica a ninguna persona encargada de la investigación.
```

### ultra: pass

```text
El campo permanece en OPEN hasta que el supervisor lo cierre. OPEN no significa que la investigación haya comenzado. El registro se creó automáticamente y la nota no identifica a ninguna persona encargada de la investigación.
```

### off: pass

```text
El campo permanece en OPEN hasta que el supervisor lo cierre. OPEN no significa que la investigación haya comenzado. El registro se creó automáticamente y la nota no identifica a ninguna persona encargada de la investigación.
```

