# Estado de los repositorios — Prácticas PCD

**Fecha de revisión:** 23-sep-2026
**Fuente:** `PCD/content/documents/equipos.csv` vs. carpetas clonadas en `PCD/evaluation/teams/` (después de `git pull` en los 16 repos registrados)
**Estructura esperada:** ver "Repositorio del curso" en `PCD/content/documents/PlaneacionPCDAlumnos.md`
(`.gitignore`, `README.md`, `requirements.txt`, `datos/`, `practica1/` a `practica6/` con `src/` y `resultados/`, `proyecto/`)

**Nota sobre `datos/`:** el profesor entrega los archivos `{tema}-ruido.csv` por separado — a los alumnos solo se les exige tener **creada la carpeta** `datos/` en la raíz del repo, no que ya contenga el dataset.

**Leyenda:** ✅ Cumple &nbsp;·&nbsp; ❌ No cumple &nbsp;·&nbsp; ⚠️ Cumple parcialmente (ver observaciones)

---

## Tabla general

| # | Equipo | Tema | .gitignore | README.md | requirements.txt | datos/ | practica1-6 | proyecto/ | **Total cumple** | Observaciones |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 1 | Alergicos_al_10 | Pedidos a domicilio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 2 | Asterix | Reservaciones | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | **5/6** | Sin cambios. Sigue faltando `requirements.txt`; siguen los archivos sueltos sin sentido (`aaa.txt`…`fff.tx` en cada `practicaN/`) y la carpeta `src/` extra en la raíz. |
| 3 | Bit_and_Byte | Inspección agrícola | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 4 | CVA_IXT | Pedidos a domicilio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | ⬆️ **Mejoró — ahora cumple 6/6:** movió la carpeta `datos/` de la raíz a `proyecto/datos/` (renombrado, fast-forward) y simplificó el `README.md`. `proyecto/` ya tiene `src/`, `resultados/` y `datos/`. |
| 5 | Hondurenos | Streaming musical | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 6 | JR | Boletos deportivos | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/6** | Sigue sin repo registrado en `equipos.csv`. |
| 7 | LUMINA | Citas médicas | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | ⬆️ **Mejoró — ahora cumple 6/6:** completó `resultados/` en `practica3` a `practica6` (antes solo tenían `src/`) y agregó `src/` a `proyecto/`. |
| 8 | Mamba | Boletos deportivos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 9 | NPC | Streaming musical | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 10 | Noble_6 | Tickets de soporte | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | **5/6** | Sin cambios. Sigue faltando `requirements.txt`. |
| 11 | Orugas | Reseñas de cursos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). Sigue sin borrar el archivo duplicado `requirements .txt` (con espacio antes del punto). |
| 12 | Pastes_Don_Miau | Citas médicas | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | ⬆️ **Mejoró mucho — ahora cumple 6/6:** completó `src/`/`resultados/` en `practica6` (última que faltaba) y toda la estructura de `proyecto/` (`src/`, `resultados/`, `datos/`). |
| 13 | Soviets | Tickets de soporte | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | ⬆️ **Mejoró — ahora cumple 6/6:** completó `proyecto/` con `datos/`, `resultados/` y `src/` (antes estaba vacío). |
| 14 | Tifosis | Ventas online | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 15 | Yayos | Reservaciones | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | **5/6** | Sin cambios. `proyecto/` sigue vacío (solo `.gitkeep`, sin `src/`/`resultados/`/`datos/`). |
| 16 | los_cazadores_de_bandides | Ventas online | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 17 | the_sea_bros | Reportes de tránsito | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | **4/6** | Sin cambios. `practica1-6` y `proyecto/` siguen vacías (solo `.gitkeep`, sin `src/`/`resultados/`/`datos/` dentro). Tiene una carpeta extra `mi_primer_proyecto/` en la raíz que no es parte de la estructura esperada. |

---

## Cambios desde el 22-sep

- **CVA_IXT**: 5/6 → **6/6**. Movió `datos/` de la raíz a `proyecto/datos/`, completando la estructura de `proyecto/`.
- **LUMINA**: 4/6 → **6/6**. Terminó `resultados/` en `practica3-6` y `src/` en `proyecto/`.
- **Pastes_Don_Miau**: sigue mejorando de forma acelerada, ahora 6/6 — completó `practica6` y toda la carpeta `proyecto/` en un solo pull.
- **Soviets**: 5/6 → **6/6**. Completó `proyecto/` (le faltaba desde hacía varios reportes).
- **Alergicos_al_10, Asterix, Bit_and_Byte, Hondurenos, Mamba, NPC, Noble_6, Orugas, Tifosis, Yayos, los_cazadores_de_bandides, the_sea_bros**: sin cambios de estructura.
- **JR**: sigue sin repo registrado.

## Resumen

- **Repositorios clonados y evaluados:** 16 de 17
- **Repositorios vacíos (sin clonar):** 1 de 17 — JR (sin `repo_url` en `equipos.csv`)
- **Cumplen 6/6 (estructura completa):** Alergicos_al_10, Bit_and_Byte, CVA_IXT, Hondurenos, LUMINA, Mamba, NPC, Orugas, Pastes_Don_Miau, Soviets, Tifosis, los_cazadores_de_bandides — **12 equipos** (subió de 8 a 12 respecto al 22-sep)
- **Cumplen 5/6:** Asterix y Noble_6 (a ambos les falta solo `requirements.txt`); Yayos (le falta `proyecto/`)
- **Cumplen 4/6 o menos:** the_sea_bros (4/6) y JR (0/6, sin repo)
- **Problema más común:** `requirements.txt` faltante (Asterix, Noble_6) y `proyecto/`/`practica1-6` totalmente vacíos en the_sea_bros.
- **Hallazgos de higiene de repositorio:** sin novedades hoy. Sigue pendiente que Orugas borre el archivo duplicado `requirements .txt` y que Asterix limpie sus archivos sueltos (`aaa.txt`…`fff.tx`) y la carpeta `src/` extra en la raíz.

## Nota — repo duplicado (EQUIPO_SIN_NOMBRE1)

La carpeta `PCD/evaluation/teams/EQUIPO_SIN_NOMBRE1/Repositorio_PCD/` sigue siendo un segundo clon del mismo repo de **Tifosis** (`https://github.com/arvicamp/Repositorio_PCD.git`, mismo `HEAD` `5dcda7e`). Hoy el `git pull` en esa carpeta trajo los commits que Tifosis ya tenía desde el 22-sep (no es información nueva, solo estaba desactualizada). Sigue pendiente que el usuario confirme si se borra esta carpeta redundante (no se tocó — fuera de alcance de este reporte).
