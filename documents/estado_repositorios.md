# Estado de los repositorios — Prácticas PCD

**Fecha de revisión:** 6-oct-2026 — **día de entrega de la Práctica 1**
**Fuente:** `PCD/content/documents/equipos.csv` vs. carpetas clonadas en `PCD/evaluation/teams/` (después de `git pull` en los 17 repos registrados)
**Estructura esperada:** ver "Repositorio del curso" en `PCD/content/documents/PlaneacionPCDAlumnos.md`
(`.gitignore`, `README.md`, `requirements.txt`, `datos/`, `practica1/` a `practica6/` con `src/` y `resultados/`, `proyecto/`)

**Nota sobre `datos/`:** el profesor entrega los archivos `{tema}-ruido.csv` por separado — a los alumnos solo se les exige tener **creada la carpeta** `datos/` en la raíz del repo, no que ya contenga el dataset.

**Leyenda:** ✅ Cumple &nbsp;·&nbsp; ❌ No cumple &nbsp;·&nbsp; ⚠️ Cumple parcialmente (ver observaciones)

---

## Tabla general

| # | Equipo | Tema | .gitignore | README.md | requirements.txt | datos/ | practica1-6 | proyecto/ | **Total cumple** | Observaciones |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 1 | Alergicos_al_10 | Pedidos a domicilio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). P1 entregada con los nombres correctos y ya con contenido real (`resumen.py` 4.2 KB, `resumen.txt` 4.0 KB) — antes estaban en 0 bytes. **Error en el encabezado:** `Seed: 100000`; su semilla es **144** (100000 es el tamaño del dataset, no la semilla). Rama `feature/resumen` creada y mergeada ✅. |
| 2 | Asterix | Reservaciones | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ Por fin limpiaron la basura de `practica1/`, pero **solo de ahí**: `bbb.txt`…`fff.tx` siguen en `practica2/` a `practica6/`, y `ggg.txt`, `nummm.txt`, `kkdkjdsjsdlsdk.txt`, `rreange.txt` en `proyecto/`. **Nombres de entregable mal:** `src/p1.py` (debe ser `resumen.py`) y `resultados/resumen_ejemplo.txt` (debe ser `resumen.txt`). **Corrieron el script sobre la muestra chica:** reportan `Filas: 103`, cuando el dataset completo tiene 103,000. Falta la sección `--- Dimensiones ---`. **No cumplen el requisito de rama:** el repo solo tiene `main`; el único merge es un merge de `pull`, no de una rama de trabajo. |
| 3 | Bit_and_Byte | Inspección agrícola | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). **P1 correcta:** nombres, semilla (2584), columnas (`cultivo` / `puntaje_calidad`) y dataset completo (103,000 filas) — todo bien. Documentaron la práctica en el README. Detalle cosmético: los títulos de sección llevan comillas (`--- Columna categórica: 'cultivo' ---`) y el formato pide sin ellas. Ramas `feature/*` mergeadas ✅. `LICENSE` en la raíz; no estorba. |
| 4 | CVA_IXT | Pedidos a domicilio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **Corrigieron el nombre** que se les señaló el 2-oct: `resume.py` → `resumen.py`, y agregaron `resultados/resumen.txt`. **P1 correcta:** semilla (233), columnas (`tipo_comida` / `monto_pedido`) y 103,000 filas. Único detalle: en `Pareja:` pusieron el nombre del equipo en vez de los nombres de los integrantes. |
| 5 | Hondurenos | Streaming musical | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ Completaron P1: ya está `resultados/resumen.txt` (antes solo tenían `notas.md`) y limpiaron el `test_setup.py` de `practica1/src/`. Semilla (377), columnas (`genero_musical` / `reproducciones`) y 103,000 filas correctas. **Falta la línea `Pareja:`** en el encabezado del `resumen.txt` — es parte del formato pedido. `generar_estructuras.sh` sigue en la raíz; inofensivo. |
| 6 | JR | Boletos deportivos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ Entregaron P1 con los nombres correctos, columnas correctas (`equipo` / `precio_boleto`) y 103,000 filas. **Error en el encabezado:** `Seed: 100000`; su semilla es **13**. Mergearon `feature/resumen` vía Pull Request ✅ — buen uso de Git. Último commit 4-oct. |
| 7 | LUMINA | Citas médicas | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ Entregaron P1 con nombres correctos, columnas correctas (`especialidad` / `tiempo_espera_min`) y 103,000 filas. Dos observaciones: **(1) `Seed: 100000`**, su semilla es **21**; **(2) el formato del `resumen.txt` no es el pedido** — el encabezado dice `RESUMEN DE LA PRACTICA` en vez de `=== RESUMEN DEL DATASET ===` y los títulos de sección van sin los delimitadores `---`. `feature/resumen` sí quedó mergeada en `main` (fast-forward, por eso no aparece commit de merge) ✅. |
| 8 | Mamba | Boletos deportivos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ Borraron el duplicado `ResumenP1.py` que se les señaló ✅. Semilla (8) y 103,000 filas correctas. **Error de fondo: eligieron mal las dos columnas.** Reportan categórica = `telefono` (96,000 valores únicos — señal de que la detectan automáticamente en vez de usar la tabla del enunciado; debe ser **`equipo`**) y numérica = `asistencia_partido`, que es la `numerica_2`; la que pide P1 es **`precio_boleto`**. En `Pareja:` pusieron "MAMBA" en vez de los nombres. |
| 9 | NPC | Streaming musical | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **De no haber empezado a P1 completa y correcta:** nombres, semilla (610), columnas (`genero_musical` / `reproducciones`) y 103,000 filas, todo bien. Pendiente de limpieza: en `practica1/` siguen el `test_setup.py` y el `notas.md` de la semana 1, que no son entregables de P1. |
| 10 | Noble_6 | Tickets de soporte | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **P1 completa y correcta:** nombres, semilla (1597), columnas (`categoria_problema` / `tiempo_resolucion_hrs`) y 103,000 filas. `feature/estadisticas` quedó mergeada en `main` (fast-forward) ✅. |
| 11 | Orugas | Reseñas de cursos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **P1 completa y correcta:** nombres, semilla (3), columnas (`curso` / `calificacion`) y 103,000 filas. Rama `desarrollo` mergeada ✅. Sin pendientes de higiene. |
| 12 | Pastes_Don_Miau | Citas médicas | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ Empezaron P1, pero con **cuatro problemas**: (1) la salida se llama **`resultados.txt`**, debe ser `resumen.txt`; (2) **`Seed: ??`** — dejaron el placeholder sin llenar (su semilla es **34**); (3) **corrieron el script sobre la muestra chica**, reportan `Filas: 103` en vez de 103,000; (4) **hay un campo vacío de más al inicio de cada fila** (`| email | direccion | ...`) — es un desajuste en el `split`/formato de salida. Columnas sí correctas (`especialidad` / `tiempo_espera_min`). Rama mergeada ✅. |
| 13 | Soviets | Tickets de soporte | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ **P1 completa y correcta:** nombres, semilla (987), nombres de los dos integrantes, columnas (`categoria_problema` / `tiempo_resolucion_hrs`) y 103,000 filas. Es el `resumen.py` más extenso del grupo (5.6 KB). Pendientes menores: `Hola-Mundo.py` sigue en la raíz, y su `.gitignore` es el único que **no** incluye `__pycache__/`. |
| 14 | Tifosis | Ventas online | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ Entregaron P1 con nombres correctos, semilla (2), columnas correctas (`producto` / `monto_venta`) y 103,000 filas — **el contenido está bien**. **Pero no cumplen el requisito de Git:** el repo solo tiene la rama `main`, sin ninguna rama de trabajo creada ni mergeada (0 merges). Sigue el `ventas_online-ruido.csv` extra en `datos/` además del par `_100`/`_100000`. Último commit 3-oct. |
| 15 | Yayos | Reservaciones | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ Entregaron P1 con nombres correctos, semilla (10946), columnas (`destino` / `precio_noche`) y 103,000 filas. Dos detalles: en `Pareja:` solo aparece "Regina" (falta el otro integrante), y los títulos de sección van sin acentos. `week03_python_fundamentos.ipynb` (material del curso) sigue copiado en la raíz. `feature/resumen` mergeada ✅. |
| 16 | los_cazadores_de_bandides | Ventas online | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ Entregaron P1 con los nombres correctos y semilla correcta (1). **Dos errores de fondo:** (1) la columna numérica reportada es `minutos_en_sitio`, que es la `numerica_2`; P1 pide **`monto_venta`**; (2) **el conteo de filas está desfasado en 1** — reportan `Filas: 102999` y son 103,000: en `resumen.py:19` hacen `n_filas = len(filas) - 1` cuando en la línea 17 ya habían quitado la cabecera con `lineas[1:]`, así que restan dos veces. Categórica (`producto`) correcta. Ramas `isis` y `ulises` mergeadas ✅. |
| 17 | the_sea_bros | Reportes de tránsito | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Estructura sin cambios (sigue 6/6). ⬆️ Entregaron P1 con los nombres correctos y 103,000 filas, pero con **tres errores**: (1) **`Seed: ?`** — dejaron el placeholder sin llenar (su semilla es **55**); (2) **columnas mal elegidas**: categórica = `telefono` (96,000 únicos; debe ser **`zona`**) y numérica = `descripcion_incidente`, que es texto — su propia salida lo delata con `Valores validos: 0` y `Minimo: N/A (Es puro texto)`, y aun así lo dejaron así; debe ser **`duracion_incidente_min`**; (3) las primeras 5 filas van separadas con `|` pegado, y el formato pide ` | ` con espacios. 55 commits, el repo más activo del grupo. |

---

## Cambios desde el 2-oct

El cambio es masivo: **el 2-oct había 11 equipos con `practica1/` completamente vacía; hoy los 17 tienen entregable de P1 subido.**

**Entregaron P1 por primera vez (11 equipos):** Bit_and_Byte, JR, LUMINA, Noble_6, Orugas, Pastes_Don_Miau, Soviets, Tifosis, Yayos, los_cazadores_de_bandides, the_sea_bros.

**Completaron o corrigieron lo que les faltaba (5 equipos):**

- **Alergicos_al_10**: sus `resumen.py` / `resumen.txt` pasaron de 0 bytes a contenido real.
- **CVA_IXT**: renombraron `resume.py` → `resumen.py` y agregaron el `resumen.txt` que faltaba.
- **Hondurenos**: agregaron el `resumen.txt` que faltaba y quitaron el `test_setup.py` de `practica1/src/`.
- **Mamba**: borraron el duplicado `ResumenP1.py`.
- **NPC**: pasaron de solo tener el `test_setup.py` de la semana 1 a entregar P1 completa.

**Higiene resuelta (1 equipo):**

- **Asterix**: borraron los archivos basura de `practica1/` (`aaa.txt`, `a1a1.txt`, `a2a2a2.txt`). Siguen pendientes los de `practica2/` a `practica6/` y `proyecto/`.

**Estructura:** sin cambios — los 17 equipos siguen en 6/6.

---

## Evaluación de la Práctica 1 (entrega hoy, 6-oct)

Los 17 equipos entregaron. La estructura del monorepo ya no es el problema; lo que diferencia las entregas es la **corrección del contenido**.

### Resultado por equipo

| Estado | Equipos | Total |
|---|---|:---:|
| **Correcta** — nombres, semilla, columnas y dataset completo bien | **Bit_and_Byte, CVA_IXT, Noble_6, NPC, Orugas, Soviets, Tifosis**\* | 7 |
| **Correcta con detalles menores de formato** | **Hondurenos** (falta la línea `Pareja:`), **Yayos** (`Pareja:` incompleta, sin acentos) | 2 |
| **Con errores de fondo** | **Alergicos_al_10, JR, LUMINA** (semilla), **Mamba, the_sea_bros** (columnas), **los_cazadores_de_bandides** (columna numérica + conteo de filas), **Asterix, Pastes_Don_Miau** (nombres + muestra chica + formato) | 8 |

\* Tifosis tiene el contenido correcto pero **no cumple el requisito de rama de trabajo** (ver abajo).

### Errores agrupados por tipo

**1. Semilla mal reportada (5 equipos) — el error más común**

| Equipo | Reportó | Debía ser |
|---|---|---|
| Alergicos_al_10 | `Seed: 100000` | 144 |
| JR | `Seed: 100000` | 13 |
| LUMINA | `Seed: 100000` | 21 |
| the_sea_bros | `Seed: ?` | 55 |
| Pastes_Don_Miau | `Seed: ??` | 34 |

Tres equipos confundieron la **semilla del equipo** con el **100000 del nombre del archivo** (que es el tamaño del dataset), y dos dejaron el placeholder del formato sin llenar.

**2. Columnas mal elegidas (3 equipos)**

| Equipo | Categórica reportada / correcta | Numérica reportada / correcta |
|---|---|---|
| Mamba | `telefono` / **`equipo`** | `asistencia_partido` / **`precio_boleto`** |
| the_sea_bros | `telefono` / **`zona`** | `descripcion_incidente` / **`duracion_incidente_min`** |
| los_cazadores_de_bandides | `producto` ✅ | `minutos_en_sitio` / **`monto_venta`** |

Mamba y the_sea_bros eligieron `telefono` como columna categórica, con 96,000 valores únicos cada uno: síntoma claro de que la están **detectando automáticamente** (la columna con más valores distintos) en vez de leer la tabla de referencia del enunciado. Mamba y los_cazadores confundieron `numerica_2` con `numerica_1`.

**3. Corrieron el script sobre la muestra de 100 filas (2 equipos)**

**Asterix** y **Pastes_Don_Miau** reportan `Filas: 103` en vez de 103,000: usaron el archivo `{tema}-ruido_100.csv` en lugar del `_100000.csv`. El enunciado pide procesar el archivo completo.

**4. Nombres de entregable incorrectos (2 equipos)**

- **Asterix**: `src/p1.py` y `resultados/resumen_ejemplo.txt` → deben ser `resumen.py` y `resumen.txt`.
- **Pastes_Don_Miau**: `resultados/resultados.txt` → debe ser `resumen.txt`.

**5. Bugs de conteo / formato (2 equipos)**

- **los_cazadores_de_bandides**: `resumen.py:19` hace `n_filas = len(filas) - 1` después de haber quitado la cabecera con `lineas[1:]` en la línea 17 → resta dos veces y reporta 102,999.
- **Pastes_Don_Miau**: cada fila de la salida empieza con un campo vacío de más (`| email | direccion | ...`).

**6. Requisito de rama de trabajo no cumplido (2 equipos)**

El enunciado pide al menos una rama (ej. `feature/resumen`) creada, trabajada y mergeada a `main`.

- **Tifosis**: el repo solo tiene `main`, 0 merges, ninguna rama de trabajo.
- **Asterix**: solo tiene `main`; su único merge es un merge de `pull`, no de una rama de trabajo.

Los otros 15 sí cumplen. Nota: **LUMINA** y **Noble_6** no tienen commit de merge, pero sus ramas `feature/resumen` y `feature/estadisticas` **sí** quedaron integradas en `main` por fast-forward — cuentan como cumplido.

### Requisitos que cumple todo el grupo

- **≥3 commits con mensajes descriptivos:** ✅ los 17. El mínimo es 17 commits (Alergicos_al_10) y el máximo 55 (the_sea_bros).
- **Solo Python puro:** ✅ los 17. Nadie usó `pandas` ni la librería `csv`. Los únicos imports son `os` (Hondurenos, JR, Tifosis) y `pathlib` (Alergicos_al_10), ambos de la biblioteca estándar y aceptables.
- **CSV en `datos/` de la raíz, no dentro de `practica1/`:** ✅ los 17.

### Puntos a recalcar en clase

1. **La semilla es la del equipo, no el `100000` del nombre del archivo.** Cinco equipos lo reportaron mal; es el error más repetido de la entrega.
2. **Las columnas categórica y numérica se toman de la tabla de referencia del enunciado, no se detectan automáticamente.** Elegir "la columna con más valores únicos" lleva directo a `telefono`, que no es categórica de ningún tema.
3. **`numerica_1` es la que pide P1**, no `numerica_2` (Mamba usó `asistencia_partido` en vez de `precio_boleto`; los_cazadores `minutos_en_sitio` en vez de `monto_venta`).
4. **Correr el script sobre el archivo `_100000.csv`**, no sobre la muestra `_100.csv`. Si el reporte dice `Filas: 103`, se procesó el archivo equivocado.
5. **Los nombres de los entregables son literales:** `resumen.py` y `resumen.txt`. No `p1.py`, no `resumen_ejemplo.txt`, no `resultados.txt`.
6. **Si el formato trae un placeholder (`{seed}`, `{nombre_pareja}`), hay que llenarlo.** Dos equipos entregaron con `Seed: ?` y `Seed: ??`.
7. **La rama de trabajo es un requisito calificable**, no un adorno: dos equipos trabajaron todo directo en `main`.

---

## Resumen

- **Repositorios clonados y evaluados:** 17 de 17 (todos los `git pull` corrieron sin errores, sin conflictos ni symlinks rotos)
- **Cumplen 6/6 (estructura completa):** **los 17 equipos**, por tercer reporte consecutivo
- **Cumplen menos de 6/6:** ninguno
- **Entregaron P1:** **17 de 17**, contra 6 de 17 que tenían algo el 2-oct
- **P1 con contenido correcto:** 7 equipos sin observaciones de fondo, 2 con detalles menores de formato, 8 con errores de fondo
- **Problema más común:** la **semilla mal reportada** en `resumen.txt` (5 equipos), seguido de la **elección automática de columnas** en vez de usar la tabla del enunciado (3 equipos)
- **Hallazgos de higiene de repositorio:**
  - **Asterix** — limpiaron `practica1/` pero siguen los archivos basura en `practica2/` a `practica6/` (`bbb.txt`…`fff.tx`) y en `proyecto/` (`ggg.txt`, `nummm.txt`, `kkdkjdsjsdlsdk.txt`, `rreange.txt`). Es el pendiente más viejo del grupo.
  - **NPC** — `test_setup.py` y `notas.md` de la semana 1 todavía en `practica1/`.
  - **Soviets** — `Hola-Mundo.py` en la raíz; y su `.gitignore` es el único sin `__pycache__/`.
  - **Yayos** — `week03_python_fundamentos.ipynb` (material del curso) copiado a la raíz.
  - **Hondurenos** — `generar_estructuras.sh` en la raíz; inofensivo.
  - **Tifosis** — `ventas_online-ruido.csv` extra en `datos/`, además del par `_100`/`_100000`.
  - **Bit_and_Byte** — `LICENSE` en la raíz; no estorba.
  - **`*.pyc` ausente en 16 de 17 `.gitignore`** — es un patrón del template que se repartió en clase, no un descuido individual; en la práctica `__pycache__/` ya cubre el caso. Vale la pena corregir el template para los próximos cursos.
  - **Sin novedades malas:** ningún equipo tiene `.venv/`, `venv/` ni `__pycache__/` versionado, ni archivos de sistema (`.DS_Store`, `Thumbs.db`).

## Nota — nombre de la carpeta local de Asterix

La carpeta del clon local sigue siendo `PCD/evaluation/teams/Asterix/PCD_EquipoAsterix2026/`, aunque el repo se renombró a `pcd-reservaciones-6765`. El `remote origin` ya apunta a la URL nueva y el `git pull` corre bien, así que es solo cosmético; se puede renombrar la carpeta local cuando convenga.
