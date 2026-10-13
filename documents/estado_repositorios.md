# Estado de los repositorios — Prácticas PCD

**Fecha de revisión:** 12-oct-2026 — **seguimiento de correcciones a la Práctica 1**
**Fuente:** `PCD/content/documents/equipos.csv` vs. carpetas clonadas en `PCD/evaluation/teams/` (después de `git pull` en los 17 repos registrados)
**Estructura esperada:** ver "Repositorio del curso" en `PCD/content/documents/PlaneacionPCDAlumnos.md`
(`.gitignore`, `README.md`, `requirements.txt`, `datos/`, `practica1/` a `practica6/` con `src/` y `resultados/`, `proyecto/`)

**Nota sobre `datos/`:** el profesor entrega los archivos `{tema}-ruido.csv` por separado — a los alumnos solo se les exige tener **creada la carpeta** `datos/` en la raíz del repo, no que ya contenga el dataset.

**Enfoque de este reporte:** la estructura dejó de ser el tema (los 17 siguen en 6/6 por cuarto reporte consecutivo). Lo que se revisa aquí es si cada equipo **atendió las observaciones numeradas** que se les escribieron en su propio `README.md` el 8-oct-2026 a las 00:51 h, junto con la calificación de P1.

**Leyenda:** ✅ Cumple &nbsp;·&nbsp; ❌ No cumple &nbsp;·&nbsp; ⚠️ Cumple parcialmente (ver observaciones)

---

## Tabla general

| # | Equipo | Tema | .gitignore | README.md | requirements.txt | datos/ | practica1-6 | proyecto/ | **Total cumple** | Observaciones |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 1 | Alergicos_al_10 | Pedidos a domicilio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **Corrigieron su única observación:** la semilla pasó de `100000` a **144** (commits del 11-oct 16:59 y 17:04). Su `resumen.txt` ahora coincide con la referencia en todos los campos. |
| 2 | Asterix | Reservaciones | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **Atendieron 6 de sus 7 observaciones** (9-oct 08:54 y 08:59): corrieron el dataset `_100000` (ya reportan 103000 filas), renombraron `p1.py` → `resumen.py` y `resumen_ejemplo.txt` → `resumen.txt`, agregaron `--- Dimensiones ---`, y el mín/máx de `precio_noche` ya cuadra (−26954.3 / 325370.4). **Requisito de rama ya cumplido:** crearon `feauture/resumen` (con el typo), trabajaron ahí las dos correcciones y quedó integrada en `main` por fast-forward. Lo único que queda de la obs. 6 es la cuenta de la categórica (27 únicos / `Merida` 13482 vs. 20 / 13761): es exactamente la lectura **sin `.strip()`**, el mismo criterio que se dio por válido a CVA_IXT, NPC, Noble_6 y Yayos. **Pendiente de higiene (el más viejo del grupo):** siguen los 19 archivos basura en `practica2/` a `practica6/` y `proyecto/`. |
| 3 | Bit_and_Byte | Inspección agrícola | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). Sin commits nuevos — **no tenían nada que corregir** (100/100, sin observaciones). `LICENSE` en la raíz; no estorba. |
| 4 | CVA_IXT | Pedidos a domicilio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). Sin commits nuevos — **no tenían nada que corregir** (100/100; su única nota era la del `.strip()`, sin efecto en la calificación). |
| 5 | Hondurenos | Streaming musical | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **Corrigieron sus 2 observaciones calificables** (9-oct 21:14): agregaron la línea `Pareja:` (con los tres integrantes) y el mín/máx de `reproducciones` ya cuadra (−115110.0 / 1253040.0). Mantienen la normalización a minúsculas de la categórica, que ya se les había dado por válida. Detalle nuevo: en la línea del conteo escribieron texto de más — `Valores únicos: 8 corresponen a los generos musicales` (además con el typo "corresponen"); el campo debe traer solo el número. |
| 6 | JR | Boletos deportivos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). Sin commits nuevos — **no tenían nada que corregir** (100/100, sin observaciones). |
| 7 | LUMINA | Citas médicas | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **Corrigieron sus 3 observaciones calificables y además la nota opcional** (12-oct 23:40, la corrección más reciente del grupo): agregaron `=== RESUMEN DEL DATASET ===`, los cinco encabezados de sección (`--- Dimensiones ---`, `--- Primeras 5 filas ---`, etc.), la semilla **21**, y aplicaron el `.strip()` que se les sugirió — ahora reportan 21 únicos y `Pediatria` (13724), idéntico a la referencia. Su `resumen.txt` quedó alineado con la solución en todos los campos. Único extra: una línea `Errores numéricos: 0` que no está en el formato pedido. |
| 8 | Mamba | Boletos deportivos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **Corrigieron sus 2 observaciones** (8-oct 08:50, los primeros en responder — unas horas después de recibir la retroalimentación): la categórica ya es **`equipo`** (24 únicos, `Toros` 12031) y la numérica **`precio_boleto`** (98883 válidos, −7813.6 / 106722.0). Ambos valores coinciden exacto con la referencia. Su commit explica la causa: habían dejado los índices de columna de la prueba con el archivo de 100 registros. Pendiente menor (no estaba en las observaciones calificadas): en `Pareja:` sigue "MAMBA" en vez de los nombres, y la sangría de "Celdas vacías por columna" va a 4 espacios en vez de 2. |
| 9 | NPC | Streaming musical | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). Sin commits nuevos — **no tenían nada que corregir** (100/100). ⬆️ Ya limpiaron el `test_setup.py` y el `notas.md` de la semana 1 que arrastraban en `practica1/`; esa carpeta ahora solo tiene `src/` y `resultados/`. |
| 10 | Noble_6 | Tickets de soporte | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). Sin commits nuevos — **no tenían nada que corregir** (100/100). |
| 11 | Orugas | Reseñas de cursos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **Corrigieron su única observación** (11-oct 16:51): agregaron la línea `=== RESUMEN DEL DATASET ===`. Su `resumen.txt` ahora coincide con la referencia en todos los campos. Sin pendientes de higiene. |
| 12 | Pastes_Don_Miau | Citas médicas | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **Corrigieron sus 5 observaciones** (9-oct 14:45) — la recuperación más grande del grupo: corrieron el dataset `_100000` (103000 filas), renombraron `resultados.txt` → `resumen.txt`, llenaron la semilla **34**, y la categórica (21 únicos / `Pediatria` 13712) y el mín/máx de `tiempo_espera_min` (−900.0 / 8520.0) ya cuadran con la referencia. Siguen dos cosas que **no** estaban en las observaciones calificadas: el campo vacío de más al inicio de cada una de las primeras 5 filas (`&#124; email &#124; id &#124; ...`), y desviaciones de formato (títulos con comillas `--- Columna categórica 'especialidad' ---`, `(13712 veces)` en vez de `apariciones`, sufijo `vacíos` en cada conteo). |
| 13 | Soviets | Tickets de soporte | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). No tenían nada que corregir (100/100). Aun así subieron un commit el 10-oct 18:31 reordenando su `README.md`. Pendientes menores de higiene, sin cambio: `Hola-Mundo.py` en la raíz, y su `.gitignore` sigue siendo el único **sin** `__pycache__/`. |
| 14 | Tifosis | Ventas online | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ❌ **El único equipo con una observación pendiente y sin responder:** se les pidió crear una rama de trabajo, trabajarla y mergearla a `main`; el repositorio **sigue teniendo solo `main` y 0 merges**. Sin commits nuevos desde la retroalimentación. Sigue el `ventas_online-ruido.csv` extra en `datos/` además del par `_100`/`_100000`. |
| 15 | Yayos | Reservaciones | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). Sin commits nuevos — **no tenían nada que corregir** (100/100; su única nota era la del `.strip()`, sin efecto en la calificación). ⬆️ Ya quitaron de la raíz el `week03_python_fundamentos.ipynb` del material del curso. |
| 16 | los_cazadores_de_bandides | Ventas online | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **Corrigieron sus 2 observaciones** (9-oct 08:50): arreglaron el doble descuento de la cabecera (ya reportan 103000 filas) y cambiaron la numérica a **`monto_venta`** (98866 válidos, −14634.3 / 200325.6). Ambos coinciden exacto con la referencia. Pendiente menor (no estaba en las observaciones calificadas): en `Pareja:` sigue el nombre del equipo en vez de los nombres. |
| 17 | the_sea_bros | Reportes de tránsito | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **Atendieron sus 4 observaciones** (8-oct 15:57, el mismo día de la retroalimentación): llenaron la semilla **55**, pusieron el separador con espacios a los lados de la barra, la categórica ya es **`zona`** —y de hecho ahora la toman por nombre en el código (`columnas.index("zona")`), que era el fondo de la observación— y la numérica es **`duracion_incidente_min`** (98877 válidos, −600.0 / 6360.0, exacto). La cuenta de la categórica sí sigue distinta (14 únicos / `Periferico` 14127 vs. 21 / 13831) porque en `resumen.py:51` hacen `.lower().title()` sin `.strip()`; es el mismo tipo de normalización que se dio por válida a Hondurenos. De paso quitaron los acentos de los títulos, con lo que el formato quedó igual al de la referencia. |

---

## Seguimiento de correcciones a la Práctica 1

Diez equipos tenían observaciones que afectaban la calificación. **Nueve de los diez corrigieron; el único que no respondió es Tifosis.**

| Equipo | Calif. 8-oct | Obs. calificables | Corregidas | Fecha de la corrección | Estado |
|---|:---:|:---:|:---:|---|---|
| Mamba | 75 | 2 | **2** | 8-oct 08:50 | ✅ Completo |
| the_sea_bros | 68 | 4 | **4** | 8-oct 15:57 | ✅ Completo |
| Asterix | 60 | 7 | **6** + 1 parcial | 9-oct 08:59 | ⚠️ Queda solo la cuenta de la categórica (lectura sin `.strip()`) |
| los_cazadores_de_bandides | 83 | 2 | **2** | 9-oct 08:50 | ✅ Completo |
| Pastes_Don_Miau | 66 | 5 | **5** | 9-oct 14:45 | ✅ Completo |
| Hondurenos | 94 | 2 | **2** | 9-oct 21:14 | ✅ Completo |
| Orugas | 98 | 1 | **1** | 11-oct 16:51 | ✅ Completo |
| Alergicos_al_10 | 95 | 1 | **1** | 11-oct 17:04 | ✅ Completo |
| LUMINA | 81 | 3 | **3** + la nota opcional | 12-oct 23:40 | ✅ Completo (el único que atendió también lo opcional) |
| **Tifosis** | **95** | **1** | **0** | — | ❌ **Sin responder** (sigue sin rama de trabajo) |

Los otros siete equipos —**Bit_and_Byte, CVA_IXT, JR, NPC, Noble_6, Soviets y Yayos**— no tenían observaciones calificables (100/100), así que no había nada que corregir. Soviets subió un commit de reordenamiento de su `README.md` el 10-oct.

### Qué tipo de error se corrigió mejor

| Tipo de error | Equipos que lo tenían | Lo corrigieron |
|---|---|:---:|
| Semilla mal reportada o sin llenar | Alergicos_al_10, LUMINA, Pastes_Don_Miau, the_sea_bros | **4 de 4** |
| Columna categórica o numérica equivocada | Mamba, the_sea_bros, los_cazadores_de_bandides | **3 de 3** |
| Script corrido sobre la muestra de 100 filas | Asterix, Pastes_Don_Miau | **2 de 2** |
| Nombres de entregable incorrectos | Asterix, Pastes_Don_Miau | **2 de 2** |
| Formato del `resumen.txt` (encabezado/secciones) | Asterix, LUMINA, Orugas | **3 de 3** |
| Bugs de conteo o separador | los_cazadores_de_bandides, the_sea_bros | **2 de 2** |
| Mín/máx de la numérica fuera de rango | Asterix, Hondurenos, Pastes_Don_Miau | **3 de 3** |
| **Requisito de rama de trabajo** | **Asterix, Tifosis** | **1 de 2** |

El patrón es claro: **todo lo que era un error de contenido o de formato se corrigió al 100%.** Lo único que quedó sin atender es el requisito de Git de Tifosis — justo el tipo de observación que no se arregla editando el script.

### Lo que queda abierto

1. **Tifosis** — sin rama de trabajo. Es la única observación calificable viva del grupo.
2. **Asterix** — los 19 archivos basura en `practica2/` a `practica6/` y `proyecto/` (`bbb.txt`, `cccc.txt`, `ddd.txt`, `eeee.txt`, `fff.tx`, `ggg.txt`, `nummm.txt`, `kkdkjdsjsdlsdk.txt`, `rreange.txt` y los que están dentro de cada `src/` y `resultados/`). Viene arrastrándose desde septiembre y nunca ha sido una observación calificable, pero ya es el pendiente más viejo del curso.
3. **`Pareja:` con el nombre del equipo en vez de los nombres** — Mamba y los_cazadores_de_bandides. No se les descontó, pero conviene corregirlo antes de P2.
4. **Soviets** — `.gitignore` sin `__pycache__/` (el único del grupo) y `Hola-Mundo.py` en la raíz.
5. **Decisión pendiente del profesor:** si estas correcciones afectan la calificación de P1. El criterio que ya se comunicó a LUMINA en su README el 8-oct fue que **se califica la entrega que estaba dentro del plazo**, y que tomar la versión corregida implicaría contarla como entrega tardía. Si ese criterio se mantiene, las nueve correcciones no mueven la calificación de P1 — pero sí vale reconocerlas, porque son evidencia de que la retroalimentación en el README se está leyendo y atendiendo.

---

## Cambios desde el 6-oct

El reporte del 6-oct cerró con los 17 equipos en 6/6 y P1 entregada por todos. Entre el 6-oct y hoy pasaron tres cosas:

- **8-oct 00:51** — se escribió en el `README.md` de cada equipo su calificación de P1, el desglose por criterio y las observaciones numeradas, y se pusheó a los 17 repos.
- **8-oct a 12-oct** — nueve de los diez equipos con observaciones calificables subieron correcciones (detalle en la sección anterior). Los 17 clones quedaron limpios tras el `git pull`, sin conflictos ni symlinks rotos.
- **Higiene resuelta sin que se pidiera:** NPC limpió `practica1/` (ya no están el `test_setup.py` ni el `notas.md` de la semana 1) y Yayos quitó el `week03_python_fundamentos.ipynb` de la raíz.

**Estructura:** sin cambios — los 17 equipos siguen en 6/6, por cuarto reporte consecutivo.

---

## Resumen

- **Repositorios clonados y evaluados:** 17 de 17 (todos los `git pull` corrieron sin errores, sin conflictos ni symlinks rotos)
- **Cumplen 6/6 (estructura completa):** **los 17 equipos**, por cuarto reporte consecutivo
- **Cumplen menos de 6/6:** ninguno
- **Equipos con commits nuevos desde la retroalimentación del 8-oct:** 10 (Mamba, the_sea_bros, Asterix, los_cazadores_de_bandides, Pastes_Don_Miau, Hondurenos, Soviets, Orugas, Alergicos_al_10, LUMINA)
- **Equipos que corrigieron sus observaciones:** **9 de 10** — 8 al 100%, Asterix con 6 de 7 (lo que queda es la lectura sin `.strip()`, criterio ya dado por válido a otros equipos)
- **Equipos con observación pendiente:** **1 — Tifosis** (requisito de rama de trabajo)
- **Más rápidos en responder:** Mamba (8-oct 08:50, unas horas después de recibir la retroalimentación) y the_sea_bros (8-oct 15:57, el mismo día)
- **Corrección más completa:** LUMINA, que además de sus 3 observaciones calificables aplicó el `.strip()` que era solo una sugerencia sin efecto en la calificación
- **Recuperación más grande:** Pastes_Don_Miau, que corrigió las 5 observaciones que tenía (había sacado 66/100)
- **Problema más común antes de las correcciones:** la semilla mal reportada (4 equipos) y la elección equivocada de columnas (3 equipos). Hoy ninguno de los dos queda abierto.
- **Hallazgos de higiene de repositorio:**
  - **Asterix** — 19 archivos basura en `practica2/` a `practica6/` y `proyecto/`. El pendiente más viejo del grupo.
  - **Soviets** — `Hola-Mundo.py` en la raíz; su `.gitignore` es el único **sin** `__pycache__/`.
  - **Hondurenos** — `generar_estructuras.sh` en la raíz; inofensivo.
  - **Tifosis** — `ventas_online-ruido.csv` extra en `datos/`, además del par `_100`/`_100000`.
  - **Bit_and_Byte** — `LICENSE` en la raíz; no estorba.
  - **Resuelto desde el 6-oct:** NPC (`practica1/` limpia) y Yayos (ipynb fuera de la raíz).
  - **Sin novedades malas:** ningún equipo tiene `.venv/`, `venv/` ni `__pycache__/` versionado, ni archivos de sistema (`.DS_Store`, `Thumbs.db`).

## Nota — nombre de la carpeta local de Asterix

La carpeta del clon local sigue siendo `PCD/evaluation/teams/Asterix/PCD_EquipoAsterix2026/`, aunque el repo se renombró a `pcd-reservaciones-6765`. El `remote origin` ya apunta a la URL nueva y el `git pull` corre bien, así que es solo cosmético; se puede renombrar la carpeta local cuando convenga.

## Nota — carpeta duplicada en el área de evaluación

Existe `PCD/evaluation/PCD/evaluation/solutions/P1/resultados/` (vacía), que parece un artefacto de una copia con ruta anidada por error. No afecta nada, pero conviene borrarla para que no se confunda con `PCD/evaluation/solutions/`.
