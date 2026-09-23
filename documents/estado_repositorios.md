# Estado de los repositorios — Prácticas PCD

**Fecha de revisión:** 22-sep-2026
**Fuente:** `PCD/content/documents/equipos.csv` vs. carpetas clonadas en `PCD/evaluation/teams/` (después de `git pull` en los 14 repos ya existentes, más **Asterix y Tifosis clonados por primera vez hoy** — el usuario los agregó a `equipos.csv`)
**Estructura esperada:** ver "Repositorio del curso" en `PCD/content/documents/PlaneacionPCDAlumnos.md`
(`.gitignore`, `README.md`, `requirements.txt`, `datos/`, `practica1/` a `practica6/` con `src/` y `resultados/`, `proyecto/`)

**Nota sobre `datos/`:** el profesor entrega los archivos `{tema}-ruido.csv` por separado — a los alumnos solo se les exige tener **creada la carpeta** `datos/` en la raíz del repo, no que ya contenga el dataset.

**Leyenda:** ✅ Cumple &nbsp;·&nbsp; ❌ No cumple &nbsp;·&nbsp; ⚠️ Cumple parcialmente (ver observaciones)

---

## Tabla general

| # | Equipo | Tema | .gitignore | README.md | requirements.txt | datos/ | practica1-6 | proyecto/ | **Total cumple** | Observaciones |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 1 | Alergicos_al_10 | Pedidos a domicilio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | ⬆️ **Mejoró — ahora cumple 6/6:** agregó `requirements.txt` y la carpeta `datos/` (con `.gitkeep`). |
| 2 | Asterix | Reservaciones | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | **5/6** | 🆕 **Recién clonado hoy** (`https://github.com/erizo0/PCD_EquipoAsterix2026.git`). Estructura completa salvo `requirements.txt` (no existe). Tiene archivos sueltos sin sentido aparente (`aaa.txt`…`fff.tx` dentro de cada `practicaN/`, y una carpeta `src/` extra en la raíz que no es parte de la estructura esperada) — no afecta el cumplimiento pero vale la pena avisarle al equipo. |
| 3 | Bit_and_Byte | Inspección agrícola | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | ⬆️ **Mejoró mucho — ahora cumple 6/6:** completó toda la estructura (`datos/`, `practica1-6` con `src/`/`resultados/`, `proyecto/`) de una sola vez. |
| 4 | CVA_IXT | Pedidos a domicilio | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | **5/6** | ⬆️ **Mejoró mucho:** corrigió `readme.md` → `README.md`, agregó `requirements.txt`, `datos/` y completó `practica1-6`. `proyecto/` tiene `src/` y `resultados/` pero le falta `datos/`. |
| 5 | Hondurenos | Streaming musical | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios de estructura (sigue 6/6). Hubo commits nuevos (ajustes de README y notas en `practica1`) y se creó una rama `feature/practica1-notas` sin mergear a `main` — no afecta la evaluación. |
| 6 | JR | Boletos deportivos | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/6** | Sigue sin repo registrado en `equipos.csv`. |
| 7 | LUMINA | Citas médicas | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | **4/6** | ⬆️ **Mejoró:** agregó `datos/`. `practica1-6` tienen `src/` pero ninguna tiene `resultados/`. `proyecto/` tiene `resultados/`/`datos/` pero no `src/`. |
| 8 | Mamba | Boletos deportivos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | ⬆️ **Mejoró mucho — ahora cumple 6/6:** abandonó el esquema de `src/`/`resultados/` genéricos en la raíz y adoptó la estructura estándar completa. **Hallazgo de higiene:** agregó un `.DS_Store` versionado en la raíz. |
| 9 | NPC | Streaming musical | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 10 | Noble_6 | Tickets de soporte | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | **5/6** | ⬆️ **Mejoró mucho:** completó `datos/`, `practica1-6` y `proyecto/` en un solo commit. Solo falta `requirements.txt`. |
| 11 | Orugas | Reseñas de cursos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | ⬆️ **Mejoró mucho — ahora cumple 6/6:** completó toda la estructura. **Nota:** además de `requirements.txt` creó por error un archivo `requirements .txt` (con espacio antes del punto) — vale la pena avisarles para que lo borren. |
| 12 | Pastes_Don_Miau | Citas médicas | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | **3/6** | ⬆️ **Mejoró:** agregó `.gitignore` y `requirements.txt` (ambos vacíos, lo cual está bien). Sigue faltando `datos/`, `practica1-6` y `proyecto/`. |
| 13 | Soviets | Tickets de soporte | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | **5/6** | ⬆️ **Mejoró:** completó `src/`/`resultados/` en `practica2-6` (antes solo `practica1` estaba completa). `proyecto/` sigue como carpeta vacía sin subcarpetas. |
| 14 | Tifosis | Ventas online | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | 🆕 **Recién clonado hoy** (`https://github.com/arvicamp/Repositorio_PCD.git`). Estructura completa desde el primer momento, incluyendo el dataset (`ventas_online-ruido.csv`) ya presente en `datos/` — ver nota abajo sobre identificación de este repo. |
| 15 | Yayos | Reservaciones | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | **5/6** | ⬆️ **Mejoró mucho:** completó `datos/` y `practica1-6`. `proyecto/` existe pero sin subcarpetas `src/`/`resultados/`/`datos/`. |
| 16 | los_cazadores_de_bandides | Ventas online | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios de estructura (sigue 6/6); solo un ajuste menor en README. |
| 17 | the_sea_bros | Reportes de tránsito | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | **4/6** | ⬆️ **Mejoró:** agregó `requirements.txt`, reemplazó `codigos/` por `datos/`, y creó las 6 carpetas `practica1-6` más `proyecto/` — pero todas están vacías, sin `src/`/`resultados/` dentro. También eliminó el `.DS_Store` que tenía versionado (higiene resuelta). |

---

## Cambios desde el 20-sep

- **6 equipos ahora cumplen 6/6** (antes solo 3): Alergicos_al_10, Bit_and_Byte, Mamba, Orugas se sumaron a Hondurenos, NPC y los_cazadores_de_bandides — todos completaron su estructura de golpe hoy.
- **Asterix y Tifosis**: 🆕 clonados por primera vez (el usuario los dio de alta en `equipos.csv`). Asterix entra con 5/6 (falta `requirements.txt`); Tifosis entra con 6/6.
- **CVA_IXT**: 2/6 → **5/6**. Corrigió el `readme.md` en minúsculas, agregó `requirements.txt` y `datos/`, completó `practica1-6`; solo falta `datos/` dentro de `proyecto/`.
- **Noble_6**: 0/6 → **5/6**. Completó casi toda la estructura en un solo commit; solo falta `requirements.txt`.
- **Soviets**: 4/6 → **5/6**. Terminó `src/`/`resultados/` en las prácticas 2 a 6 (antes solo la 1 estaba completa).
- **Yayos**: 3/6 → **5/6**. Completó `datos/` y `practica1-6`; falta terminar `proyecto/`.
- **the_sea_bros**: 2/6 → **4/6**. Agregó `requirements.txt` y creó `datos/` y las carpetas `practica1-6`/`proyecto/`, aunque siguen vacías por dentro. Resolvió el hallazgo de higiene (`.DS_Store`).
- **LUMINA**: 3/6 → **4/6**. Agregó `datos/`.
- **Pastes_Don_Miau**: 1/6 → **3/6**. Agregó `.gitignore` y `requirements.txt`.
- **Hondurenos, NPC, los_cazadores_de_bandides**: sin cambios de estructura (siguen 6/6), solo commits menores.
- **JR**: sigue sin repo registrado.

## Resumen

- **Repositorios clonados y evaluados:** 16 de 17
- **Repositorios vacíos (sin clonar):** 1 de 17 — JR (sin `repo_url` en `equipos.csv`)
- **Cumplen 6/6 (estructura completa):** Alergicos_al_10, Bit_and_Byte, Hondurenos, Mamba, NPC, Orugas, Tifosis, los_cazadores_de_bandides — **8 equipos**
- **Cumplen 3/6 o menos:** Pastes_Don_Miau (3/6) y JR (0/6, sin repo)
- **Problema más común:** `requirements.txt` faltante (Asterix, Noble_6) y `proyecto/` incompleto o vacío (Soviets, Yayos, the_sea_bros parcialmente, CVA_IXT le falta `datos/`).
- **Hallazgos de higiene de repositorio:** Mamba agregó un `.DS_Store` versionado hoy; Orugas dejó un archivo duplicado `requirements .txt` (con espacio); Asterix tiene varios archivos de prueba sin sentido (`aaa.txt`…`fff.tx`) y una carpeta `src/` extra en la raíz. the_sea_bros resolvió su `.DS_Store`.

## Equipos nuevos: Asterix y Tifosis

- **Asterix** (seed 6765, tema reservaciones): repo `https://github.com/erizo0/PCD_EquipoAsterix2026.git` clonado en `PCD/evaluation/teams/Asterix/PCD_EquipoAsterix2026/`. Estructura completa (5/6), solo falta `requirements.txt` en la raíz.
- **Tifosis** (seed 2, tema ventas online): repo `https://github.com/arvicamp/Repositorio_PCD.git` clonado en `PCD/evaluation/teams/Tifosis/Repositorio_PCD/`. Estructura completa (6/6) y ya trae su dataset (`ventas_online-ruido.csv`) dentro de `datos/`.

**Nota importante — repo duplicado:** el repo de Tifosis (`arvicamp/Repositorio_PCD`) es el mismo que en el reporte del 20-sep se había clonado como **repo suelto no identificado**, en `PCD/evaluation/teams/EQUIPO_SIN_NOMBRE1/Repositorio_PCD/` (mismo remoto, mismo historial). Ahora que el equipo quedó identificado como Tifosis en `equipos.csv`, la carpeta `EQUIPO_SIN_NOMBRE1/` quedó **redundante** — es un segundo clon del mismo repo. No se borró en esta pasada (fuera de alcance de este reporte); queda pendiente que el usuario confirme si se elimina.

## Entrega de datasets (resumen)

| Equipo | Tema | Seed | Archivos entregados |
|---|---|---|---|
| Hondurenos | streaming_musical | 377 | `streaming_musical-ruido_100.csv` / `_100000.csv` |
| NPC | streaming_musical | 610 | `streaming_musical-ruido_100.csv` / `_100000.csv` |
| los_cazadores_de_bandides | ventas_online | 1 | `ventas_online-ruido_100.csv` / `_100000.csv` |
| Soviets | tickets_soporte | 987 | `tickets_soporte-ruido_100.csv` / `_100000.csv` |

Tifosis ya tiene un archivo `ventas_online-ruido.csv` en su `datos/`, pero no coincide con la convención de nombre de las entregas anteriores (`{tema}-ruido_100.csv` / `_100000.csv`) — parece que el equipo lo puso por su cuenta, no que se lo hayan entregado por este flujo. El resto de equipos con repo clonado (11 de 16) aún no tienen listo o completo su `datos/` para recibir el dataset oficial (ver columna `datos/` en la tabla general — Pastes_Don_Miau ni siquiera tiene la carpeta).
