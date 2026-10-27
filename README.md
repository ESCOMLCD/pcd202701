# Programación para Ciencia de Datos

**Instituto Politécnico Nacional**

**Periodo:** agosto — diciembre 2026

**Modalidad:** presencial

**Duración:** 16 semanas (48 sesiones de 90 minutos)

**Horario:** martes, miércoles y viernes

---

## Descripción del curso

Este curso introduce a los estudiantes en las herramientas y técnicas fundamentales de programación aplicadas a la ciencia de datos. A lo largo del semestre, los alumnos aprenden a configurar un entorno de desarrollo profesional, versionar su trabajo con Git, programar en Python, manipular y limpiar datos con NumPy y pandas, y comunicar hallazgos mediante visualizaciones con Matplotlib y Seaborn.

El curso está diseñado para estudiantes con bases de programación pero con poca o ninguna experiencia en Python. El enfoque es práctico: cada tema se introduce a partir de un problema concreto y se aplica inmediatamente sobre datos reales o sintéticos.

## Temas del curso

| Semana | Tema |
|---|---|
| 1 | Terminal, VS Code y entornos virtuales |
| 2 | Git y GitHub |
| 3 | Python I: fundamentos y estructuras de datos |
| 4 | Python II: funciones y manejo de archivos |
| 5 | Python III: clases, programación funcional y JSON |
| 6-7 | NumPy: fundamentos, estadística y filtrado |
| 8 | Expresiones regulares (regex) |
| 9-10 | Pandas: exploración, filtrado, limpieza y transformación |
| 11 | EDA y estadística descriptiva |
| 12 | Matplotlib |
| 13 | Seaborn |
| 14 | Comunicar hallazgos y taller de proyecto |
| 15-16 | Presentaciones de proyectos |

## Evaluación

El curso se evalúa mediante 3 evaluaciones parciales con igual peso (33.3% cada una). Cada evaluación parcial se compone de:

- 2 prácticas (25% cada una)
- 1 examen o presentación (50%)

Las prácticas se realizan en parejas sobre un dataset sintético único por equipo. El proyecto final se presenta en equipos de 3 integrantes usando datos reales elegidos por los alumnos.

## Calificaciones de prácticas

Calificación de cada práctica sobre **100**. Actualizada al 27-oct-2026.

Cuando una celda trae **dos números** (`anterior/vigente`), el primero es la calificación
de la entrega original y el segundo es la que quedó después de que el equipo **corrigió
las observaciones** que se le señalaron en el `README.md` de su repositorio. **La que
cuenta es la segunda.** Se deja la primera a la vista para que quede registro de dónde
salió cada equipo y de cuánto le valió corregir.

| Equipo | P1 | P2 | P3 | P4 | P5 | P6 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Alergicos_al_10 | 95/99 | 100 | — | — | — | — |
| Asterix | 60/90 | 100 | — | — | — | — |
| Bit_and_Byte | 100 | 97 | — | — | — | — |
| CVA_IXT | 100 | 52 | — | — | — | — |
| Hondurenos | 94/99 | 100 | — | — | — | — |
| JR | 100 | 100 | — | — | — | — |
| LUMINA | 81/90 | 90 | — | — | — | — |
| Mamba | 75/90 | 74 | — | — | — | — |
| NPC | 100 | 100 | — | — | — | — |
| Noble_6 | 100 | 100 | — | — | — | — |
| Orugas | 98/99 | 100 | — | — | — | — |
| Pastes_Don_Miau | 66/90 | 84 | — | — | — | — |
| Soviets | 100 | 100 | — | — | — | — |
| Tifosis | 95 | 100 | — | — | — | — |
| Yayos | 100 | 100 | — | — | — | — |
| los_cazadores_de_bandides | 83/90 | 100 | — | — | — | — |
| the_sea_bros | 68/90 | 85 | — | — | — | — |

**Práctica 2** (entrega lun 26-oct): los 17 equipos entregaron dentro del plazo —el
commit más tardío en `practica2/` fue el de JR, el 26-oct a las 23:27— así que ninguna
calificación lleva penalización por retraso. Promedio del grupo: **93.1**.
Máxima: 100 (11 equipos). Mínima: 52. Mediana: 100.

La calificación se asignó con esta rúbrica sobre 100: nombres exactos de los entregables
(10), requisitos de Git (8), requisitos de código —5 funciones, `lambda`, `map`/`filter`,
sin librerías externas, sin `Counter` ni `statistics.median`— (12), encabezado del JSON
(6), `valores_unicos_categorica` (10), `conteo_por_categoria` (10),
`categoria_mas_frecuente` (6), `top_3_categorias` (8), `estadisticas_numerica_1` (12),
`estadisticas_numerica_2` (8), `promedio_por_categoria` (6) y `filtrado` (4). Cada
criterio se verificó campo por campo contra la solución de referencia del tema y la
semilla de cada equipo: exacto en los conteos, con tolerancia de redondeo en los
promedios.

**Lo que salió bien.** Los 17 cumplieron los requisitos de código sin excepción: todos
definen más de 5 funciones (de 7 a 22), todos usan `lambda` y `map`/`filter`, y ninguno
recurrió a `Counter`, a `statistics.median` ni a una librería externa. Tres equipos
(CVA_IXT, NPC y los_cazadores_de_bandides) armaron además la clase `Dataset` opcional, y
the_sea_bros dividió el trabajo en dos clases propias. **Tifosis cumplió el requisito de
rama de trabajo** que traía pendiente desde P1: creó `feature/practica2` y la integró a
`main`.

**Los cinco errores que costaron puntos**, cada uno de un equipo distinto y todos de una
sola causa:

- **Bit_and_Byte (97)** — usó el **percentil 0.75** en vez del 0.90 en el filtrado. Es el
  valor que traía el notebook de la semana 5, copiado sin cambiar; el enunciado advertía
  justo de esto. Todo lo demás está perfecto.
- **LUMINA (90)** — el cálculo es correcto, pero dentro de `estadisticas_numerica_*`
  nombró los campos `n_validos`, `min` y `max` en vez de `n_valores_validos`, `minimo` y
  `maximo`, y su script se llama `analisis2.py` en vez de `analisis_python.py`. Los
  valores coinciden con la referencia, así que esos campos se contaron a mitad de punto:
  lo que falló es el formato, no la cuenta.
- **the_sea_bros (85)** y **Pastes_Don_Miau (84)** — los dos **descartaron los valores
  negativos** de las columnas numéricas. El enunciado pide excluir solo lo vacío y lo no
  convertible; los negativos son parte del ruido del dataset y cuentan. Por eso su
  `minimo` sale en 3.0 y 2.0 en vez de −600.0 y −900.0, y con ~1,300 valores menos se
  mueven el promedio, la mediana y el `promedio_por_categoria`.
- **Mamba (74)** — normalizó la columna categórica con `.strip().upper()`. El enunciado de
  esta práctica pide aplicar **únicamente** `.strip()` y advierte en negrita que no se
  unifiquen las variantes de escritura, porque el punto es ver el ruido antes de
  limpiarlo. Con el `.upper()` reportan 8 categorías en lugar de 24, lo que arrastra el
  conteo, el top 3 y el promedio por categoría.
- **CVA_IXT (52)** — corrió el script sobre `pedidos_domicilio-ruido_100.csv`, la **muestra
  de 100 filas**, en vez del archivo completo. Su código es de los más completos del grupo
  (20 funciones y la clase `Dataset`), pero todas las cifras del reporte son de 99
  registros en lugar de 98,881. Es un cambio de una línea.

**La observación del paso 6** (describir en el `README.md` que las variantes de escritura
aparecen como categorías separadas) la documentaron **7 de 17**: Bit_and_Byte, Hondurenos,
NPC, Noble_6, Orugas, Pastes_Don_Miau y Soviets. No se descontó por omitirla, pero es la
observación que conecta directo con lo que van a limpiar en P4 y P5.

**Práctica 1** (entrega mar 6-oct): los 17 equipos entregaron dentro del plazo, así que
ninguna calificación lleva penalización por retraso. Con la ronda de correcciones ya
aplicada, el promedio del grupo es **96.0** (era 89.1 con las calificaciones de la
entrega original). Máxima: 100 (siete equipos). Mínima: 90. Mediana: 99.

**Cómo se aplicó la ronda de correcciones.** Nueve de los diez equipos que tenían
observaciones las atendieron y subieron sus correcciones entre el 8 y el 12 de octubre.
A cada uno se le reconoció así:

- Si su calificación original era de **90 o más**, su práctica quedó en **99**.
- Si era **menor a 90**, quedó en **90**.
- Los siete equipos que ya tenían **100** se quedan en 100: no tenían nada que corregir.
- **Tifosis** conserva su **95** original. Su observación era el requisito de crear una
  rama de trabajo y mergearla a `main`, y a la fecha de corte su repositorio seguía con
  solo `main` y cero merges.

Corregir no sube a nadie a 100: ese lugar se reserva para quien entregó bien la primera
vez. Pero sí reconoce el trabajo de leer la retroalimentación y actuar sobre ella, que es
lo que más va a servirles en las prácticas que siguen.

La calificación se asignó con esta rúbrica sobre 100: estructura del monorepo (8),
nombres exactos de los entregables (10), requisitos de Git (10), Python puro (8),
formato del `resumen.txt` (9), encabezado con archivo/pareja/semilla (10), dimensiones
(10), primeras 5 filas (5), columna categórica (12), columna numérica_1 (13) y calidad
de datos (5). Las observaciones de cada equipo están en el `README.md` de su propio
repositorio; el detalle de la revisión está en `documents/estado_repositorios.md`.

> **Política de retraso** (del enunciado de cada práctica): −10 puntos sobre 100 por
> cada día natural de retraso, hasta un máximo de 5 días; a partir del sexto día la
> práctica vale 0. Una práctica no entregada cuenta como **0** hasta que se entregue.

## Estructura del repositorio

```
content/
├── README.md             # Este archivo
├── documents/
│   └── PlaneacionPCDAlumnos.md   # Planeación completa del curso
├── labs/
│   ├── P1_setup_reconocimiento.md
│   ├── P2_procesamiento_python.md
│   ├── P3_estadistica_numpy.md
│   ├── P4_exploracion_pandas_regex.md
│   ├── P5_limpieza_datos.md
│   └── P6_eda_matplotlib.md
├── presentations/
│   ├── week01/           # Terminal, VS Code, entornos virtuales
│   ├── week02/           # Git y GitHub
│   ├── week03/           # Python I: fundamentos y estructuras de datos
│   ├── week04/           # Python II: funciones y manejo de archivos
│   ├── week05/           # Python III: clases, programación funcional y JSON
│   ├── week06/           # NumPy I: fundamentos
│   ├── week07/           # NumPy II: estadística y filtrado
│   ├── week08/           # Regex
│   ├── week09/           # Pandas I: exploración y filtrado
│   ├── week10/           # Pandas II: limpieza y transformación
│   ├── week11/           # EDA y estadística descriptiva
│   ├── week12/           # Matplotlib
│   ├── week13/           # Seaborn
│   └── week14/           # Comunicar hallazgos y taller de proyecto
└── tools/
    └── nb_clean.py   # Filtro de Git: limpia la metadata de los notebooks
```

## Contacto

**Profesor:** Mario Augusto Ramírez

**GitHub:** [augustoramirez](https://github.com/augustoramirez)
