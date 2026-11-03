# Práctica 3 — Estadística descriptiva con NumPy

**Programación para Ciencia de Datos**

**Asignada:** mar 27-oct · **Enunciado publicado:** lun 2-nov · **Entrega:** vie 13-nov
**Temas:** NumPy (arrays, estadística vectorizada, máscaras booleanas, benchmarking)

---

## Contexto

En la P2 procesaste el dataset con bucles de Python puro. NumPy hace los mismos
cálculos de forma vectorizada y mucho más rápido, y además trae de fábrica la
estadística que en la P2 tuviste que escribir a mano.

Esta práctica tiene tres partes: describir tus dos columnas numéricas con un
resumen estadístico completo, **detectar los valores atípicos** de cada una, y
**medir** cuánto más rápido es el enfoque vectorizado que el bucle.

> **Sobre cómo está escrito este enunciado.** A diferencia de la P2, aquí se te
> dice **qué** tiene que entregar tu programa y **con qué reglas**, no qué
> funciones teclear. Las herramientas están todas en los notebooks de las semanas
> 6 y 7; decidir cuál usar en cada paso es parte de la práctica. Si te encuentras
> buscando la línea exacta para copiar, no la hay: lee la sección *Sobre el
> material de las semanas 6 y 7*.

## Archivo de entrada

`datos/{tema}-ruido.csv` — el mismo de las prácticas anteriores, con las ~100,000
filas. **No usar pandas:** solo NumPy y la biblioteca estándar.

> **Importante sobre el formato:** las columnas están separadas por `|` (barra
> vertical, *pipe*), **no por comas** — `direccion` y `<texto>` contienen comas
> dentro de su propio contenido. Si lees con `open()`, separa con `.split("|")`;
> si usas alguna función de carga de NumPy, pásale el delimitador explícitamente.

> **Y el archivo correcto es el de 100,000 filas**, no la muestra `_100.csv`. En
> la P1 le pasó a dos equipos y en la P2 a uno: todas las cifras del reporte
> salen mal y no hay forma de corregirlas sin volver a correr todo. Antes de
> entregar, revisa que tu `n_valores_validos` ronde los 98,000.

## Entregable

```
pcd-{tema}-{seed}/
└── practica3/
    ├── src/
    │   └── analisis_numpy.py
    └── resultados/
        └── analisis_numpy.json
```

## Salida esperada: `analisis_numpy.json`

Los nombres de los campos son **literales**: así se revisan. Los números de abajo
son de ejemplo, no los tuyos.

```json
{
  "archivo": "{tema}-ruido.csv",
  "pareja": "{nombres de los dos integrantes}",
  "seed": 3,

  "numerica_1": {
    "columna": "{nombre_col_numerica_1}",
    "n_valores_validos": 98500,
    "media": 852.34,
    "desviacion_estandar": 180.50,
    "minimo": 50.0,
    "maximo": 15000.0,
    "mediana": 830.0,
    "percentil_25": 720.0,
    "percentil_75": 980.0
  },

  "numerica_2": {
    "columna": "{nombre_col_numerica_2}",
    "n_valores_validos": 98200,
    "media": 12.45,
    "desviacion_estandar": 5.12,
    "minimo": 1.0,
    "maximo": 90.0,
    "mediana": 11.8,
    "percentil_25": 8.5,
    "percentil_75": 15.2
  },

  "outliers_numerica_1": {
    "metodo": "desviacion_estandar_3",
    "limite_inferior": 312.34,
    "limite_superior": 1392.34,
    "n_outliers": 4521,
    "porcentaje": 4.59,
    "outliers_minimo": -500.0,
    "outliers_maximo": 85000.0
  },

  "outliers_numerica_2": {
    "metodo": "desviacion_estandar_3",
    "limite_inferior": -2.91,
    "limite_superior": 27.81,
    "n_outliers": 4102,
    "porcentaje": 4.18,
    "outliers_minimo": -12.0,
    "outliers_maximo": 720.0
  },

  "benchmark": {
    "n_filas": 98500,
    "tiempo_bucle_python_seg": 0.45,
    "tiempo_numpy_seg": 0.002,
    "factor_velocidad": 225.0,
    "operacion_medida": "calcular media y desviacion estandar"
  }
}
```

## Instrucciones

### 1. Cargar las dos columnas numéricas

Localiza `<numerica_1>` y `<numerica_2>` **por su nombre** en el encabezado —el
orden de las columnas depende de tu semilla, así que un índice escrito a mano no
sirve— y carga sus valores en arrays de NumPy.

Reglas de qué es un valor válido, las mismas de la P2:

- se **descarta** la celda vacía y la que no se puede convertir a número
- se **conserva** todo lo demás, **incluidos los negativos**

> Los valores negativos y los absurdamente grandes son ruido puesto a propósito
> en tu dataset, y son datos válidos para esta práctica: tu `minimo` debe salir
> negativo en varias columnas. En la P2 dos equipos los filtraron por error y
> perdieron puntos en media, mediana, mínimo y promedio por categoría. Se limpian
> en la P5, no aquí.

El `n_valores_validos` que reportes de cada columna **debería coincidir con el
que reportaste en la P2**, porque es el mismo criterio sobre el mismo archivo.
Compáralos: si no cuadran, una de las dos prácticas tiene un error de filtrado.

### 2. Reportar ocho estadísticos por columna

Para cada una de las dos columnas: `n_valores_validos`, `media`,
`desviacion_estandar`, `minimo`, `maximo`, `mediana`, `percentil_25` y
`percentil_75`.

Dos precisiones que fijan el número esperado:

- **La desviación estándar es la poblacional**, la que divide la suma de
  cuadrados entre `n`. Es la que calcula NumPy por omisión, y la misma que da un
  bucle de Python que divide entre `n`. La muestral (entre `n - 1`) da otro
  número y no es la que se pide.
- **Los percentiles son el 25 y el 75**, con la interpolación que NumPy hace por
  omisión. Es normal que te salga un valor con decimales que no aparece en tu
  CSV.

Toda la estadística debe calcularse con NumPy. Si estás recorriendo el array con
un `for` para sacar un promedio, perdiste el punto de la práctica — la única
excepción es el bucle del benchmark del paso 4, que ahí sí es a propósito.

### 3. Detectar los outliers de cada columna

Con el método de **±3 desviaciones estándar**:

- el **límite inferior** es la media menos tres desviaciones estándar; el
  **superior**, la media más tres
- es outlier todo valor **estrictamente fuera** de esos límites
- calcula los límites con la media y la desviación **sin redondear**, no con las
  que ya pusiste en el reporte: redondeas solo al escribir el JSON

Por cada columna reporta: `metodo` (usa el texto `desviacion_estandar_3`),
`limite_inferior`, `limite_superior`, `n_outliers`, `porcentaje` de los valores
válidos que son outliers, y el `outliers_minimo` y `outliers_maximo`, o sea el
valor atípico más chico y el más grande.

> **Si una columna no tiene ningún outlier**, `n_outliers` es `0`, el
> `porcentaje` es `0.0`, y `outliers_minimo` y `outliers_maximo` van en `null`.
> Tu programa no debe tronar en ese caso: pedirle el mínimo a un array vacío es
> un error. Es poco probable con tus datos, pero es el tipo de caso que hay que
> cubrir.

### 4. Medir NumPy contra un bucle de Python puro

Compara cuánto tarda **calcular la media y la desviación estándar** de los dos
modos, sobre los valores válidos de `<numerica_1>`:

- con un bucle `for` de Python puro, sin NumPy
- con NumPy, vectorizado

Tres reglas:

1. **Sobre la lista de valores válidos que ya cargaste** en el paso 1, no sobre
   el archivo crudo. Por eso `benchmark.n_filas` tiene que ser **igual** al
   `n_valores_validos` de tu `<numerica_1>`.
2. **Sin incluir el tiempo de leer y parsear el CSV.** El reloj arranca cuando
   los datos ya están en memoria.
3. **Comprueba que las dos versiones dan el mismo resultado** antes de comparar
   tiempos. Un benchmark donde cada lado calcula algo distinto no mide nada; y si
   no cuadran, lo más probable es el denominador de la desviación estándar.

Reporta `n_filas`, `tiempo_bucle_python_seg`, `tiempo_numpy_seg`,
`factor_velocidad` (el tiempo del bucle entre el de NumPy) y `operacion_medida`.

> **Sobre el reloj.** Usa **`time.perf_counter()`**. Se usa igual que
> `time.time()` pero está hecho para medir intervalos; con `time.time()`, que en
> Windows avanza a saltos de ~16 ms, la parte de NumPy sale en `0.0` y el factor
> truena con `ZeroDivisionError`. Si por lo que sea reportas un
> `tiempo_numpy_seg` de `0.0`, deja `factor_velocidad` en `null` en lugar de
> inventar un número: **eso no se penaliza**. La otra salida válida es repetir la
> operación N veces dentro de la medición y dividir el total entre N.

### 5. Escribir el JSON

Todos los valores numéricos **redondeados a 2 decimales**, con los nombres de
campo literales del ejemplo de arriba.

> **Una advertencia que te va a ahorrar media hora:** el módulo `json` no sabe
> escribir los tipos numéricos de NumPy y te va a dar
> `TypeError: Object of type float64 is not JSON serializable`. Conviértelos a
> tipos de Python antes de guardar.

## Requisitos de código

- Definir al menos **3 funciones** con nombres descriptivos. Una práctica que es
  un solo bloque de 150 líneas no cumple.
- **Usar NumPy** para toda la estadística
- **No usar pandas** ni el módulo `csv`. Lo demás de la biblioteca estándar sí
  (`json`, `time`, `os`, `math`).
- Uso de clases es **opcional**

## Sobre el material de las semanas 6 y 7

Los dos notebooks (`presentations/week06/` y `presentations/week07/`) traen todas
las herramientas que necesitas:

- **semana 6** — cargar una columna sucia de un CSV separado por `|` a un array,
  localizándola por nombre y marcando lo no convertible
- **semana 7** — `median`, la desviación poblacional y su `ddof`, los
  percentiles, las máscaras booleanas, combinar condiciones, y cómo medir
  tiempos sin engañarse

**Pero ninguno de los dos resuelve la práctica**, y esta vez es a propósito: los
ejemplos van sobre otros datos —latencias de un servidor, temperaturas de
estaciones— y lo que te toca es armar el programa. En particular, estas cinco
piezas no están escritas en ningún lado y son tuyas:

1. la función que calcula los **límites a k desviaciones** de una columna
2. la **máscara de los valores fuera** de esos límites, y el conteo y porcentaje
   que salen de ella
3. el **caso sin outliers**, que no debe tronar
4. el **benchmark de media y desviación** sobre tu columna
5. el **armado del JSON** con los nombres y el redondeo que pide este enunciado

Los ejercicios 10 a 16 del notebook de la semana 7 son exactamente ese camino,
en ese orden, y ninguno viene resuelto. Si los haces, la práctica ya está hecha.

## Requisitos de Git

Los mismos de P1 y P2, y **se califican igual**:

- Al menos **3 commits** con mensajes descriptivos (no "update", no "asdf")
- Al menos **1 rama de trabajo** (por ejemplo `feature/numpy`) creada, trabajada
  y **mergeada a `main`**

> Si tu rama queda integrada por *fast-forward* (sin commit de merge) cuenta como
> cumplido; lo que no cuenta es no haber creado ninguna rama.

## Nombres de los entregables

Literales: **`analisis_numpy.py`** en `practica3/src/` y
**`analisis_numpy.json`** en `practica3/resultados/`. No `p3.py`, no
`analisis.py`, no `resultados.json`. En la P1 dos equipos y en la P2 uno
perdieron puntos por esto, y desde esta práctica la revisión del JSON es
automática: busca esos nombres y los de los campos tal como están escritos aquí.

---

## Referencia de columnas por tema

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

---

## Política de entregas tardías

La práctica se califica sobre **100**.

- **−10 puntos por cada día natural de retraso** sobre la calificación obtenida.
- Máximo 5 días de retraso. A partir del sexto día la práctica vale **0**.
- Se califica el estado del repositorio **al cierre de la entrega**. Si corrigen
  algo después, cuenta como entrega tardía y aplica la penalización; solo se toma
  en cuenta si, ya con el descuento, el resultado les sigue conviniendo.

> **Sobre la fecha.** Esta práctica se anunció el 27-oct, pero su enunciado y el
> material de la semana 7 se publicaron el 2-nov, así que la entrega se movió al
> **vie 13-nov**. Tienen la semana completa con el material ya en la mano. Ojo
> con que la **P4 se asigna el 6-nov**: la última semana van a traslaparse, así
> que no dejen la P3 para el final.

---

## Estructura del monorepo del curso

Todas las prácticas y el proyecto se entregan en un **único repositorio de
GitHub** con la siguiente estructura:

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

**Notas:**
- El archivo `{tema}-ruido.csv` va en la carpeta `datos/` de la raíz, porque es
  compartido por las 6 prácticas. No lo dupliquen en cada carpeta de práctica.
- El `requirements.txt` es uno solo en la raíz y se va actualizando conforme
  avanzan. Desde esta práctica debe incluir `numpy`.
- El `README.md` debe incluir: nombres de los integrantes, tema asignado, seed, y
  una breve descripción de cada práctica.
- `.gitignore` debe incluir al menos: `__pycache__/`, `.venv/`, `*.pyc`,
  `*.egg-info/`
