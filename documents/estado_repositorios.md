# Estado de los repositorios — Prácticas PCD

**Fecha de revisión:** 29-sep-2026
**Fuente:** `PCD/content/documents/equipos.csv` vs. carpetas clonadas en `PCD/evaluation/teams/` (después de `git pull` en los 17 repos registrados)
**Estructura esperada:** ver "Repositorio del curso" en `PCD/content/documents/PlaneacionPCDAlumnos.md`
(`.gitignore`, `README.md`, `requirements.txt`, `datos/`, `practica1/` a `practica6/` con `src/` y `resultados/`, `proyecto/`)

**Nota sobre `datos/`:** el profesor entrega los archivos `{tema}-ruido.csv` por separado — a los alumnos solo se les exige tener **creada la carpeta** `datos/` en la raíz del repo, no que ya contenga el dataset.

**Leyenda:** ✅ Cumple &nbsp;·&nbsp; ❌ No cumple &nbsp;·&nbsp; ⚠️ Cumple parcialmente (ver observaciones)

---

## Tabla general

| # | Equipo | Tema | .gitignore | README.md | requirements.txt | datos/ | practica1-6 | proyecto/ | **Total cumple** | Observaciones |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 1 | Alergicos_al_10 | Pedidos a domicilio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 2 | Asterix | Reservaciones | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios de estructura (sigue 6/6). Siguen los archivos sueltos sin sentido dentro de cada `practicaN/` (`aaa.txt`…`fff.tx`) y `ggg.txt` en `proyecto/` — pendiente que los limpien. Nota aparte: el equipo movió/renombró su repo a `erizo0/pcd-reservaciones-6765`; ya se actualizó en `equipos.csv` y en el remote local. |
| 3 | Bit_and_Byte | Inspección agrícola | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 4 | CVA_IXT | Pedidos a domicilio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 5 | Hondurenos | Streaming musical | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 6 | JR | Boletos deportivos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | ⬆️ Corrigieron el `README.md`: ya llenaron el tema y el seed reales (antes tenían el placeholder del template sin editar). Sigue 6/6. |
| 7 | LUMINA | Citas médicas | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 8 | Mamba | Boletos deportivos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 9 | NPC | Streaming musical | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 10 | Noble_6 | Tickets de soporte | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | **5/6** | Sin cambios. Sigue faltando `requirements.txt`. |
| 11 | Orugas | Reseñas de cursos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). Sigue sin borrar el archivo duplicado `requirements .txt` (con espacio antes del punto). |
| 12 | Pastes_Don_Miau | Citas médicas | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 13 | Soviets | Tickets de soporte | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 14 | Tifosis | Ventas online | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 15 | Yayos | Reservaciones | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 16 | los_cazadores_de_bandides | Ventas online | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 17 | the_sea_bros | Reportes de tránsito | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | **5/6** | Sin cambios. `proyecto/` sigue solo con `datos/`, le falta `src/` y `resultados/`. Sigue la carpeta extra `mi_primer_proyecto/` en la raíz. |

---

## Cambios desde el 26-sep

- **JR**: corrigió el `README.md` (ya no tiene placeholders sin llenar) — sigue 6/6, sin cambio de puntaje.
- **Resto de los 16 equipos**: sin cambios de estructura ni de contenido relevante desde el 26-sep.

## Resumen

- **Repositorios clonados y evaluados:** 17 de 17
- **Cumplen 6/6 (estructura completa):** Alergicos_al_10, Asterix, Bit_and_Byte, CVA_IXT, Hondurenos, JR, LUMINA, Mamba, NPC, Orugas, Pastes_Don_Miau, Soviets, Tifosis, Yayos, los_cazadores_de_bandides — **15 equipos**
- **Cumplen 5/6:** Noble_6 (falta `requirements.txt`) y the_sea_bros (falta terminar `proyecto/`)
- **Problema más común:** `requirements.txt` faltante (solo Noble_6) y `proyecto/` incompleto (solo the_sea_bros) — sin cambios respecto al reporte anterior.
- **Hallazgos de higiene de repositorio:** sin novedades. Sigue pendiente que Orugas borre `requirements .txt` duplicado, que Asterix limpie los archivos sueltos dentro de cada práctica, y que the_sea_bros aclare/borre `mi_primer_proyecto/`.

## Nota — repo movido (Asterix)

Al hacer `git push` el 26-sep, GitHub avisó que el repo de Asterix se movió a `https://github.com/erizo0/pcd-reservaciones-6765.git` (antes `PCD_EquipoAsterix2026`). Se actualizó `repo_url` en `equipos.csv` y el `remote origin` del clon local a la URL nueva; el `git pull` de hoy ya se hizo contra la URL correcta sin problema.
