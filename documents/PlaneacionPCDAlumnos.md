# Programación para Ciencia de Datos — Planeación del Curso

**Periodo:** martes 25 de agosto — viernes 11 de diciembre de 2026

**Horario:** martes, miércoles y viernes, 90 minutos por sesión

**Duración:** 16 semanas (48 sesiones)

**Día no laboral:** miércoles 16 de septiembre (se repone en otra fecha)

---

## 1. Calendario del curso

| Semana | Tema | Sesiones | Entregas y exámenes |
|---|---|---|---|
| 1 | Terminal + VS Code + Entornos virtuales | 25, 26, 28-ago | Formación de parejas (vie 28) |
| 2 | Git + GitHub (intensivo) | 1, 2, 4-sep | Parejas formadas (vie 4) · Elección de tema de prácticas (vie 4) |
| 3 | Python I: fundamentos y estructuras de datos | 8, 9, 11-sep | |
| 4 | Python II: funciones y manejo de archivos | 15, ~~16 (feriado)~~, 18-sep | **Se asigna P1** (vie 18) |
| 5 | Python III: clases y programación funcional | 22, 23, 25-sep | **Entrega P1** (vie 25) |
| 6 | NumPy I: fundamentos | 29, 30-sep, 2-oct | **Se asigna P2** (mar 29) · **Examen 1** (vie 2) |
| 7 | NumPy II: estadística y filtrado | 6, 7, 9-oct | **Entrega P2** (vie 9) |
| 8 | Regex ligera | 13, 14, 16-oct | **Se asigna P3** (mar 13) |
| 9 | Pandas I: exploración y filtrado | 20, 21, 23-oct | **Entrega P3** (vie 23) |
| 10 | Pandas II: limpieza y transformación | 27, 28, 30-oct | **Se asigna P4** (mar 27) |
| 11 | EDA y estadística descriptiva | 3, 4, 6-nov | **Entrega P4** (vie 6) · **Examen 2** (vie 6) |
| 12 | Matplotlib | 10, 11, 13-nov | **Se asigna P5** (mar 10) · Formación de equipos de proyecto (mar 10) · Elección de dataset del proyecto (vie 13) |
| 13 | Seaborn | 17, 18, 20-nov | **Entrega P5** (vie 20) |
| 14 | Comunicar hallazgos + taller de proyecto | 24, 25, 27-nov | **Se asigna P6** (mar 24) |
| 15 | Presentaciones | 1, 2, 4-dic | **Entrega P6** (vie 4) |
| 16 | Presentaciones | 8, 9, 11-dic | |

---

## 2. Evaluación y calificación

### Composición de cada evaluación parcial (escala 0-10)

| Componente | Peso |
|---|---|
| Práctica A | 25% |
| Práctica B | 25% |
| Examen / Presentación | 50% |

### Agrupación

| Evaluación | Componentes |
|---|---|
| **Evaluación 1** | Práctica 1 + Práctica 2 + Examen 1 |
| **Evaluación 2** | Práctica 3 + Práctica 4 + Examen 2 |
| **Evaluación 3** | Práctica 5 + Práctica 6 + Presentación |

### Calificación final

| Evaluación | Peso |
|---|---|
| Evaluación 1 | 33.3% |
| Evaluación 2 | 33.3% |
| Evaluación 3 | 33.4% |

Tope de calificación final: **10**.

La presentación del proyecto es **obligatoria** y sustituye al tercer examen parcial. No presentar equivale a obtener **0** en el componente de examen de la Evaluación 3.

---

## 3. Políticas del curso

### Entregas tardías
- **-1 punto por cada día natural de retraso** sobre la calificación de la práctica.
- Máximo 5 días de retraso. Después de 5 días la práctica vale **0**.

### Asistencia
- No hay requisito formal de asistencia.

### Uso de herramientas de IA
- **Prácticas y proyecto:** el uso de herramientas de IA (ChatGPT, Copilot, Claude, etc.) **no está restringido**. Pueden usarlas como apoyo.
- **Exámenes:** son **presenciales** y **no se permite** el uso de ninguna herramienta externa (computadoras, celulares, IA, internet). Únicamente se permite una calculadora básica si el profesor lo indica.

---

## 4. Prácticas (6 en total)

### Parejas y asignación de temas

- Las prácticas se hacen **en parejas**.
- **Viernes 28 de agosto (semana 1):** se presentan los 10 temas disponibles y se discuten preferencias. Cada pareja elige un tema; máximo 2 parejas por tema.
- **Parejas formadas a más tardar el viernes 4 de septiembre (semana 2).**

### Tu dataset

Cada pareja recibe un dataset sintético único que usará durante todo el semestre. El archivo que recibirás se llama `{tema}-ruido.csv` y contiene **~103,000 filas** y **9 columnas** (en orden aleatorio). Tu dataset contiene diversos problemas de calidad (valores faltantes, formatos inconsistentes, outliers, duplicados, entre otros) que deberás identificar y corregir a lo largo de las prácticas.

Las 9 columnas son:

| Columna | Descripción |
|---|---|
| `id` | Identificador único del registro |
| `<categorica>` | Variable categórica del dominio (depende de tu tema) |
| `<numerica_1>` | Variable numérica principal |
| `<numerica_2>` | Variable numérica secundaria |
| `timestamp` | Fecha y hora del registro |
| `<texto>` | Texto libre (comentario, descripción, nota) |
| `email` | Correo electrónico |
| `telefono` | Teléfono |
| `direccion` | Dirección postal |

### Referencia de columnas por tema

Consulta esta tabla para saber cuáles son los nombres reales de las columnas en tu dataset:

| Tema | `<categorica>` | `<numerica_1>` | `<numerica_2>` | `<texto>` |
|---|---|---|---|---|
| `ventas_online` | `producto` | `monto_venta` | `minutos_en_sitio` | `comentario_cliente` |
| `resenas_cursos` | `curso` | `calificacion` | `horas_dedicadas` | `observacion_curso` |
| `boletos_deportivos` | `equipo` | `precio_boleto` | `asistencia_partido` | `resumen_partido` |
| `citas_medicas` | `especialidad` | `tiempo_espera_min` | `edad_paciente` | `diagnostico_breve` |
| `reportes_transito` | `zona` | `duracion_incidente_min` | `vehiculos_afectados` | `descripcion_incidente` |
| `pedidos_domicilio` | `tipo_comida` | `monto_pedido` | `distancia_km` | `comentario_pedido` |
| `streaming_musical` | `genero_musical` | `reproducciones` | `calificacion_promedio` | `resena_cancion` |
| `tickets_soporte` | `categoria_problema` | `tiempo_resolucion_hrs` | `nivel_prioridad` | `descripcion_ticket` |
| `inspeccion_agricola` | `cultivo` | `puntaje_calidad` | `porcentaje_humedad` | `nota_calidad` |
| `reservaciones` | `destino` | `precio_noche` | `dias_anticipacion` | `comentario_hospedaje` |

### Repositorio del curso (monorepo)

Todas las prácticas y el proyecto se entregan en un **único repositorio de GitHub** con la siguiente estructura:

```
pcd-{tema}-{seed}/
├── .gitignore
├── README.md
├── requirements.txt
├── datos/
│   └── {tema}-ruido.csv
├── practica1/
│   ├── src/
│   └── resultados/
├── practica2/
│   ├── src/
│   └── resultados/
├── practica3/
│   ├── src/
│   └── resultados/
├── practica4/
│   ├── src/
│   └── resultados/
├── practica5/
│   ├── src/
│   └── resultados/
├── practica6/
│   ├── src/
│   └── resultados/
└── proyecto/
    ├── src/
    ├── resultados/
    └── datos/
```

**Notas sobre la estructura:**
- El archivo `{tema}-ruido.csv` va en la carpeta `datos/` de la raíz, porque es compartido por las 6 prácticas. No lo dupliquen en cada carpeta de práctica.
- El `requirements.txt` es uno solo en la raíz y se va actualizando conforme avanzan: vacío en P1-P2, se agrega `numpy` en P3, `pandas` en P4, `matplotlib` en P6, `seaborn` en el proyecto.
- El `README.md` debe incluir: nombres de los integrantes, tema asignado, seed, y una breve descripción de cada práctica.
- La carpeta `proyecto/datos/` es para el dataset real del proyecto (distinto al sintético de las prácticas).
- `.gitignore` debe incluir al menos: `__pycache__/`, `.venv/`, `*.pyc`, `*.egg-info/`

### Calendario de entregas

| Práctica | Asignada | Entrega | Temas cubiertos |
|---|---|---|---|
| **P1** | vie 18-sep (semana 4) | vie 25-sep (semana 5) | Terminal + Entornos virtuales + Git + Python I-II |
| **P2** | mar 29-sep (semana 6) | vie 9-oct (semana 7) | Python III (funciones, lambda, map, filter) |
| **P3** | mar 13-oct (semana 8) | vie 23-oct (semana 9) | NumPy I y II |
| **P4** | mar 27-oct (semana 10) | vie 6-nov (semana 11) | Pandas I y II + Regex |
| **P5** | mar 10-nov (semana 12) | vie 20-nov (semana 13) | Limpieza de datos (pandas + regex) |
| **P6** | mar 24-nov (semana 14) | vie 4-dic (semana 15) | EDA + estadística descriptiva + Matplotlib |

### Pipeline de las prácticas

Las prácticas forman un pipeline progresivo. La salida de cada una alimenta la siguiente:

```
P1 (leer CSV crudo) → P2 (organizar con Python puro) → P3 (estadística con NumPy)
    → P4 (explorar con pandas + validar con regex) → P5 (producir CSV limpio)
        → P6 (analizar y visualizar datos limpios)
```

---

### Práctica 1 — Setup del proyecto + primer reconocimiento del dataset

**Asignada:** vie 18-sep · **Entrega:** vie 25-sep

**Temas:** Terminal, VS Code, Entornos virtuales, Git, GitHub, Python I-II

Configurar el monorepo del curso, leer el CSV con Python puro (sin librerías) y generar un resumen del dataset. Especificación completa en el documento de la práctica.

---

### Práctica 2 — Procesamiento de datos con Python puro

**Asignada:** mar 29-sep · **Entrega:** vie 9-oct

**Temas:** Funciones, programación funcional (`lambda`, `map`, `filter`), clases (opcional)

Organizar y procesar el dataset usando funciones reutilizables y programación funcional, sin librerías externas. Salida en JSON. Especificación completa en el documento de la práctica.

---

### Práctica 3 — Estadística descriptiva con NumPy

**Asignada:** mar 13-oct · **Entrega:** vie 23-oct

**Temas:** NumPy (arrays, vectorización, máscaras booleanas, benchmarking)

Repetir el análisis de P2 con NumPy, agregar detección de outliers y medir velocidad NumPy vs bucle puro. Especificación completa en el documento de la práctica.

---

### Práctica 4 — Exploración y validación con pandas + regex

**Asignada:** mar 27-oct · **Entrega:** vie 6-nov

**Temas:** Pandas I y II (lectura, filtrado, groupby, limpieza), Regex (validación con `.str`)

Exploración seria del dataset con pandas: agrupación, validación de emails y teléfonos con regex, diagnóstico de calidad de datos. Especificación completa en el documento de la práctica.

---

### Práctica 5 — Limpieza integral del dataset

**Asignada:** mar 10-nov · **Entrega:** vie 20-nov

**Temas:** Pandas (limpieza, transformación), Regex (corrección de formatos)

Limpiar el dataset de forma integral: corregir formatos, estandarizar categórica, tratar faltantes, eliminar duplicados y outliers. Producir `{tema}-limpio.csv`. Especificación completa en el documento de la práctica.

---

### Práctica 6 — Análisis exploratorio y visualización con Matplotlib

**Asignada:** mar 24-nov · **Entrega:** vie 4-dic

**Temas:** EDA, estadística descriptiva, Matplotlib

Análisis exploratorio completo del dataset limpio: estadísticas, outliers con IQR, correlaciones, tendencias temporales, y 4 gráficas con Matplotlib. Especificación completa en el documento de la práctica.

---

## 5. Exámenes

| Examen | Fecha | Temas | Formato |
|---|---|---|---|
| **Examen 1** | vie 2-oct (semana 6) | Terminal, Entornos virtuales, Git/GitHub, Python I, II y III | Mitad teoría corta, mitad lectura/depuración de código |
| **Examen 2** | vie 6-nov (semana 11) | NumPy I y II, Regex, Pandas I y II | Dataset nuevo (no visto), preguntas de negocio a responder con código |

Los exámenes son **presenciales** y sin herramientas externas (ver políticas).

---

## 6. Proyecto y presentación

El proyecto es un trabajo con **datos reales** elegidos por ustedes. A diferencia de las prácticas (que usan datos sintéticos), aquí trabajan con un dataset que les interese.

### Equipos

- Equipos de **3 integrantes** (12 equipos en total).
- Pueden mantener las mismas parejas de las prácticas e incorporar un tercer integrante, o formar equipos completamente nuevos.
- **Formación de equipos: martes 10 de noviembre (semana 12).** Ese día los equipos deben estar definidos.

### Dataset

- Eligen **libremente** el dataset real que quieran analizar — puede ser de Kaggle, de otro repositorio público, o cualquier fuente abierta.
- El dataset debe ser público, accesible y tener al menos 1,000 registros con variables numéricas y categóricas.
- **Fecha límite de elección: viernes 13 de noviembre (semana 12).** Cada equipo debe comunicar al profesor qué dataset usará.
- **Cada tema se asigna a exactamente 2 equipos.** Habrá 6 temas y 12 equipos. Los dos equipos que comparten tema no colaboran entre sí — cada uno realiza su propio análisis, genera sus propias gráficas y prepara su propia presentación.

#### Ejemplos de datasets en Kaggle

La siguiente lista es solo para dar ideas — pueden elegir cualquiera de estos u otro dataset que les interese:

| Dataset | Descripción | Link |
|---|---|---|
| Spotify Tracks | +100,000 canciones con características de audio: energía, bailabilidad, tempo, popularidad | [Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) |
| FIFA 22 Complete Players | Atributos de +19,000 jugadores de fútbol: habilidades, posición, valor de mercado | [Kaggle](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset) |
| Netflix Movies and TV Shows | Catálogo completo de Netflix con género, país, duración y clasificación | [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) |
| Video Game Sales | Ventas globales de +16,000 videojuegos con plataforma, género y ventas por región | [Kaggle](https://www.kaggle.com/datasets/gregorut/videogamesales) |
| 120 Years of Olympic History | Registro histórico de atletas y medallistas olímpicos desde 1896 hasta 2016 | [Kaggle](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results) |
| World Happiness Report | Indicadores de felicidad por país: PIB, esperanza de vida, percepción de corrupción | [Kaggle](https://www.kaggle.com/datasets/unsdsn/world-happiness) |
| Supermarket Sales | Registro de ventas de supermercado con datos de productos, clientes y métodos de pago | [Kaggle](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales) |
| Students Performance in Exams | Calificaciones de estudiantes en matemáticas, lectura y escritura con variables sociodemográficas | [Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) |
| Avocado Prices | Precios históricos y volumen de ventas de aguacates en diferentes regiones de EE.UU. | [Kaggle](https://www.kaggle.com/datasets/neuromusic/avocado-prices) |
| Heart Disease Dataset | Datos clínicos de pacientes con variables como colesterol, presión arterial y frecuencia cardíaca | [Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset) |
| Titanic | Datos de los pasajeros del Titanic con variables demográficas y de viaje | [Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset) |
| Stroke Prediction | Información médica y demográfica de pacientes para analizar riesgo de accidente cerebrovascular | [Kaggle](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) |

### Hitos

| Hito | Cuándo |
|---|---|
| Formación de equipos | mar 10-nov (semana 12) |
| Elección de dataset | vie 13-nov (semana 12) |
| Taller + revisión con el profesor | semana 14 |
| Presentaciones | semanas 15-16 |

### Qué debe incluir el proyecto

El reporte final debe incluir hallazgos respaldados por cifra + gráfica (incluyendo visualizaciones con Seaborn: heatmaps, pairplots, catplots). La comunicación de hallazgos se evalúa como parte de la presentación.

### Reglas de las presentaciones

#### Estructura de cada sesión (90 minutos)

1. **Presentación del equipo A (20 min).** Incluye el tiempo para conectar su equipo de cómputo, organizarse y exponer. El orden entre los dos equipos se decide con un **volado** al inicio de la sesión.
2. **Presentación del equipo B (20 min).** Mismo formato.
3. **Preguntas y discusión (20 min).** Los equipos del público formulan sus preguntas, críticas u observaciones. Los equipos que presentaron responden.
4. **Deliberación y cierre (20 min).** El profesor y los alumnos completan sus evaluaciones; retroalimentación general.

#### Temas compartidos

- Los dos equipos que comparten un mismo tema presentan en la misma sesión.
- Cada equipo trabaja por separado: su propio análisis, sus propias gráficas, su propio storytelling. No hay colaboración entre los dos equipos del mismo tema.

#### Participación obligatoria del público

Si tu equipo **no presenta** en una sesión, tienes estas obligaciones:

1. **Formular al menos una intervención** para cada equipo que presenta: puede ser una pregunta, una crítica constructiva o una observación sobre el análisis, las gráficas o los hallazgos. El equipo que presenta debe responder.
2. **Calificar cada presentación** con una nota del 1 al 10, que se entrega al profesor al final de la sesión.

**Penalización por inasistencia:** si tu equipo no envía **ningún representante** a una sesión de presentaciones (ninguno de los 3 integrantes asiste), se le descuenta **-2 puntos sobre la calificación de su propia presentación** por cada sesión a la que faltó. Esta penalización se acumula. **Si un equipo falta a 3 o más sesiones de presentaciones, su calificación de la presentación será automáticamente 0.**

#### Mejor presentación por tema

De los dos equipos que presentan el mismo tema, se determinará cuál tuvo el **mejor desempeño** tomando en cuenta:
- La calificación del profesor
- Las calificaciones asignadas por los demás equipos del grupo

El equipo ganador de cada tema recibe **+1 punto extra en la calificación final de la materia**. Este punto extra puede llevar la calificación por encima de 10, con tope en **10**.

#### Calendario de presentaciones

| Sesión | Fecha | Tema | Equipos |
|---|---|---|---|
| 1 | mar 1-dic | Tema 1 | Equipo A vs Equipo B |
| 2 | mié 2-dic | Tema 2 | Equipo C vs Equipo D |
| 3 | vie 4-dic | Tema 3 | Equipo E vs Equipo F |
| 4 | mar 8-dic | Tema 4 | Equipo G vs Equipo H |
| 5 | mié 9-dic | Tema 5 | Equipo I vs Equipo J |
| 6 | vie 11-dic | Tema 6 | Equipo K vs Equipo L |

La asignación de qué tema se presenta en qué fecha se define después de la elección de datasets (13 de noviembre).

### Rúbrica de la presentación (escala 0-10)

5 criterios, cada uno con peso de 2 puntos:

| Criterio | 2.0 (Excelente) | 1.5 (Notable) | 1.0 (Suficiente) | 0.5 (Insuficiente) |
|---|---|---|---|---|
| **Análisis de datos** | Pipeline completo y correcto: limpieza, agrupaciones, estadística descriptiva, correlaciones. Demuestra dominio de pandas/NumPy. | Pipeline completo con errores menores. | Pipeline incompleto pero funcional. Faltan pasos. | Análisis superficial: solo `describe()` o conteos básicos. |
| **Visualizaciones** | 4+ gráficas bien elegidas (Matplotlib y Seaborn), correctamente etiquetadas, que responden preguntas concretas. Incluye al menos un heatmap o pairplot. | 3-4 gráficas correctas y relevantes. | 2-3 gráficas básicas. Algunas sin etiquetas o con tipo inadecuado. | 1 gráfica o gráficas irrelevantes/mal construidas. |
| **Hallazgos y narrativa** | 2-3 hallazgos claros, cada uno respaldado por cifra + gráfica. Hilo narrativo: problema → análisis → conclusión → recomendación. | 2 hallazgos bien respaldados. Narrativa clara pero sin recomendación. | 1 hallazgo respaldado. Más descripción de pasos que historia. | No hay hallazgos claros o no están respaldados. |
| **Reproducibilidad y código** | Repo organizado, código ejecutable, `requirements.txt` funcional, `.gitignore` correcto. Otro compañero podría replicar el análisis. | Repo organizado y ejecutable con ajustes mínimos. | Código funciona pero repo desorganizado o falta `requirements.txt`. | Código no ejecutable o no está en un repositorio. |
| **Respuesta a preguntas** | Responde con seguridad y precisión. Demuestra que entiende qué hizo y por qué. | Responde correctamente la mayoría. Alguna duda menor. | Responde de forma vaga o imprecisa. | No puede explicar su propio código o decisiones. |

**Calificación** = suma de los 5 criterios (máximo 10).

Se evalúa a **todos los integrantes**: si solo uno puede responder las preguntas, los demás reciben menor puntaje en el criterio de respuesta a preguntas.

---

## 7. Temas por semana (índice detallado)

### Semana 1 — Terminal + VS Code + Entornos virtuales
- **Sesión 1 (mar 25):** Navegación en terminal — `cd`, `ls`, `pwd`, `mkdir`, `cp`, `mv`, `rm`; rutas absolutas vs relativas.
- **Sesión 2 (mié 26):** VS Code — interfaz, terminal integrada, extensiones esenciales (Python, GitLens); crear y ejecutar un primer script `.py`. Entornos virtuales — crear y activar `venv`; `pip install`.
- **Sesión 3 (vie 28):** `pip freeze > requirements.txt` y `pip install -r requirements.txt`; ejercicio integrador. Formación de parejas.

### Semana 2 — Git + GitHub (intensivo)
- **Sesión 1 (mar 1):** Flujo local — `init`, `add`, `commit`, `status`, `log`, `diff`; staging area; `.gitignore`.
- **Sesión 2 (mié 2):** GitHub + ramas — `remote`, `push`, `pull`, `clone`; `branch`, `checkout`/`switch`, `merge`; resolución de conflictos.
- **Sesión 3 (vie 4):** Trabajo colaborativo en parejas — fork/clone, push/pull entre repos. Elección de dataset del proyecto.

### Semana 3 — Python I: fundamentos y estructuras de datos
- **Sesión 1 (mar 8):** Tipos básicos, variables, operadores, conversiones de tipo, `input()` / `print()`, f-strings.
- **Sesión 2 (mié 9):** Control de flujo — `if`/`elif`/`else`; `for` y `while`; `break`/`continue`; `range()`.
- **Sesión 3 (vie 11):** Estructuras de datos — listas, tuplas, sets, diccionarios.

### Semana 4 — Python II: funciones y manejo de archivos
- **Sesión 1 (mar 15):** Funciones — `def`, parámetros, `return`, scope.
- ~~**Sesión 2 (mié 16, feriado)**~~ — se repone.
- **Sesión 3 (vie 18):** Lectura/escritura de archivos (`open`, `with`); parseo de CSV sin librerías.

### Semana 5 — Python III: clases y programación funcional
- **Sesión 1 (mar 22):** Clases y objetos — `class`, `__init__`, atributos, métodos, `self`.
- **Sesión 2 (mié 23):** Programación funcional — `lambda`, `map()`, `filter()`, `reduce()`.
- **Sesión 3 (vie 25):** Ejercicio integrador de Python.

### Semana 6 — NumPy I: fundamentos
- **Sesión 1 (mar 29):** Arrays — creación, `shape`, `ndim`, `dtype`, indexación y slicing.
- **Sesión 2 (mié 30):** Operaciones vectorizadas, broadcasting, funciones universales.
- **Sesión 3 (vie 2):** **Examen 1.**

### Semana 7 — NumPy II: estadística y filtrado
- **Sesión 1 (mar 6):** Estadística descriptiva vectorizada — `mean`, `std`, `min`, `max`, `median`, `percentile`.
- **Sesión 2 (mié 7):** Máscaras booleanas, `np.where`, benchmarking NumPy vs bucle puro.
- **Sesión 3 (vie 9):** Ejercicio integrador NumPy.

### Semana 8 — Regex ligera
- **Sesión 1 (mar 13):** Sintaxis básica — metacaracteres, anclas, clases de caracteres.
- **Sesión 2 (mié 14):** Grupos de captura, `re.search`, `re.findall`, `re.sub`.
- **Sesión 3 (vie 16):** Ejercicios aplicados — validar correos, extraer teléfonos, normalizar fechas.

### Semana 9 — Pandas I: exploración y filtrado
- **Sesión 1 (mar 20):** `DataFrame` y `Series`, `read_csv`, `head`, `tail`, `info`, `describe`.
- **Sesión 2 (mié 21):** Selección y filtrado — `loc`, `iloc`, filtros booleanos, `.query()`, `sort_values`.
- **Sesión 3 (vie 23):** Agrupación — `groupby` + funciones de agregación.

### Semana 10 — Pandas II: limpieza y transformación
- **Sesión 1 (mar 27):** Valores faltantes, conversiones de tipo, duplicados.
- **Sesión 2 (mié 28):** `apply`, `map`, `replace`; `.str` accessor con regex.
- **Sesión 3 (vie 30):** `merge` y `concat`.

### Semana 11 — EDA y estadística descriptiva
- **Sesión 1 (mar 3):** Proceso de EDA — distribuciones, outliers (IQR, z-score), correlaciones.
- **Sesión 2 (mié 4):** Práctica de EDA guiada — histogramas con pandas, formular hipótesis.
- **Sesión 3 (vie 6):** **Examen 2.**

### Semana 12 — Matplotlib
- **Sesión 1 (mar 10):** Anatomía de una figura — `figure`, `axes`, `subplots`; gráficas básicas.
- **Sesión 2 (mié 11):** Personalización — títulos, etiquetas, colores, leyenda, `savefig`.
- **Sesión 3 (vie 13):** Taller — elegir el tipo de gráfica correcto; crear visualizaciones.

### Semana 13 — Seaborn
- **Sesión 1 (mar 17):** Gráficas estadísticas — `histplot`, `boxplot`, `violinplot`, `scatterplot`; paletas y estilos.
- **Sesión 2 (mié 18):** Relaciones — `heatmap`, `pairplot`, `catplot`, `FacetGrid`.
- **Sesión 3 (vie 20):** Taller de Seaborn — replicar y mejorar gráficas con Seaborn.

### Semana 14 — Comunicar hallazgos + taller de proyecto
- **Sesión 1 (mar 24):** Estructura de un reporte de datos — hallazgo + evidencia + limitaciones.
- **Sesión 2 (mié 25):** Revisión del proyecto por equipo — retroalimentación del profesor.
- **Sesión 3 (vie 27):** Ensayo de presentación; feedback de pares.

### Semanas 15-16 — Presentaciones
- **Semana 15** (1, 2, 4-dic): Primera ronda de presentaciones.
- **Semana 16** (8, 9, 11-dic): Segunda ronda de presentaciones y cierre del curso.
