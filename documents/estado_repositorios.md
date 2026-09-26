# Estado de los repositorios — Prácticas PCD

**Fecha de revisión:** 26-sep-2026
**Fuente:** `PCD/content/documents/equipos.csv` vs. carpetas clonadas en `PCD/evaluation/teams/` (después de `git pull` en los 16 repos ya existentes, más **JR clonado por primera vez hoy** — el usuario agregó su `repo_url` a `equipos.csv`)
**Estructura esperada:** ver "Repositorio del curso" en `PCD/content/documents/PlaneacionPCDAlumnos.md`
(`.gitignore`, `README.md`, `requirements.txt`, `datos/`, `practica1/` a `practica6/` con `src/` y `resultados/`, `proyecto/`)

**Nota sobre `datos/`:** el profesor entrega los archivos `{tema}-ruido.csv` por separado — a los alumnos solo se les exige tener **creada la carpeta** `datos/` en la raíz del repo, no que ya contenga el dataset.

**Leyenda:** ✅ Cumple &nbsp;·&nbsp; ❌ No cumple &nbsp;·&nbsp; ⚠️ Cumple parcialmente (ver observaciones)

---

## Tabla general

| # | Equipo | Tema | .gitignore | README.md | requirements.txt | datos/ | practica1-6 | proyecto/ | **Total cumple** | Observaciones |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 1 | Alergicos_al_10 | Pedidos a domicilio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 2 | Asterix | Reservaciones | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | ⬆️ **Mejoró — ahora cumple 6/6:** agregaron `requirements.txt` (ya lo tienen, con dependencias listadas) y borraron la carpeta `src/` extra en la raíz. Siguen los archivos sueltos sin sentido dentro de cada `practicaN/` (`aaa.txt`…`fff.tx`) y `ggg.txt` en `proyecto/` — no afecta el cumplimiento pero vale la pena que los limpien. |
| 3 | Bit_and_Byte | Inspección agrícola | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 4 | CVA_IXT | Pedidos a domicilio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 5 | Hondurenos | Streaming musical | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 6 | JR | Boletos deportivos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | 🆕 **Recién clonado hoy** (`https://github.com/julioyaelgarciaceron-sys/JR--PRACTICASPCD-2027-1`). Estructura completa desde el primer momento. **Detalle menor:** el `README.md` sigue con el placeholder del template sin llenar (`{boletos deportivos}` y `{seed}` literales en vez del tema y el seed reales) — no afecta el cumplimiento estructural pero conviene que lo corrijan. |
| 7 | LUMINA | Citas médicas | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 8 | Mamba | Boletos deportivos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios de estructura (sigue 6/6). Ya empezaron a trabajar la P1 de verdad: subieron `practica1/src/ResumenP1.py` y `practica1/resultados/Resumenp1.txt` (antes solo tenían el `test_setup.py` de prueba). |
| 9 | NPC | Streaming musical | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 10 | Noble_6 | Tickets de soporte | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | **5/6** | Sin cambios. Sigue faltando `requirements.txt`. |
| 11 | Orugas | Reseñas de cursos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). Sigue sin borrar el archivo duplicado `requirements .txt` (con espacio antes del punto). |
| 12 | Pastes_Don_Miau | Citas médicas | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 13 | Soviets | Tickets de soporte | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 14 | Tifosis | Ventas online | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 15 | Yayos | Reservaciones | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | ⬆️ **Mejoró — ahora cumple 6/6:** completaron `proyecto/` con `src/`, `resultados/` y `datos/` (este último ya con su dataset, `reservaciones-ruido_100.csv` y `_100000.csv`, adentro). |
| 16 | los_cazadores_de_bandides | Ventas online | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **6/6** | Sin cambios (sigue 6/6). |
| 17 | the_sea_bros | Reportes de tránsito | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | **5/6** | ⬆️ **Mejoró:** completaron `src/` y `resultados/` en las 6 `practicaN/` (antes estaban vacías). Sigue faltando `proyecto/`: solo tiene `datos/`, le falta `src/` y `resultados/`. Sigue la carpeta extra `mi_primer_proyecto/` en la raíz (con su propio `src/`/`resultados/`, no forma parte de la estructura esperada). |

---

## Cambios desde el 23-sep

- **JR**: 🆕 se dio de alta en `equipos.csv` y se clonó por primera vez hoy. Entra directo con **6/6** — estructura completa desde el inicio.
- **Asterix**: 5/6 → **6/6**. Agregó `requirements.txt` y borró la carpeta `src/` extra en la raíz (quedan los archivos sueltos dentro de cada práctica, pendientes de limpiar).
- **Yayos**: 5/6 → **6/6**. Completó `proyecto/` con `src/`, `resultados/` y `datos/` (ya con el dataset dentro).
- **the_sea_bros**: 4/6 → **5/6**. Completó `src/`/`resultados/` en las 6 prácticas; solo le falta terminar `proyecto/`.
- **Mamba**: sigue 6/6, pero ya empezó a trabajar contenido real de la P1 (script y resultado de `practica1`).
- **Alergicos_al_10, Bit_and_Byte, CVA_IXT, Hondurenos, LUMINA, NPC, Noble_6, Orugas, Pastes_Don_Miau, Soviets, Tifosis, los_cazadores_de_bandides**: sin cambios de estructura.

## Resumen

- **Repositorios clonados y evaluados:** 17 de 17 (por primera vez todos los equipos tienen repo)
- **Cumplen 6/6 (estructura completa):** Alergicos_al_10, Asterix, Bit_and_Byte, CVA_IXT, Hondurenos, JR, LUMINA, Mamba, NPC, Orugas, Pastes_Don_Miau, Soviets, Tifosis, Yayos, los_cazadores_de_bandides — **15 equipos** (subió de 12 a 15 respecto al 23-sep)
- **Cumplen 5/6:** Noble_6 (falta `requirements.txt`) y the_sea_bros (falta terminar `proyecto/`)
- **Cumplen menos de 5/6 o sin repo:** ninguno — es la primera revisión con los 17 equipos activos
- **Problema más común:** `requirements.txt` faltante (solo Noble_6) y `proyecto/` incompleto (solo the_sea_bros).
- **Hallazgos de higiene de repositorio:** sin novedades nuevas. Sigue pendiente que Orugas borre `requirements .txt` duplicado, que Asterix limpie los archivos sueltos dentro de cada práctica (`aaa.txt`…`fff.tx`, `ggg.txt`), y que the_sea_bros aclare/borre la carpeta extra `mi_primer_proyecto/`.
