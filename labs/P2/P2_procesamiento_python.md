# Práctica 2 — Procesamiento de datos con Python puro

**Programación para Ciencia de Datos**

**Asignada:** mié 14-oct · **Entrega:** lun 26-oct
**Temas:** Funciones, programación funcional (`lambda`, `map`, `filter`), clases (opcional)

---

## Contexto

Ya conoces las estructuras de datos de Python y la programación funcional. Ahora vas a procesar el mismo dataset de forma más organizada: usando funciones reutilizables y herramientas como `map`, `filter` y `lambda`. El objetivo es producir un análisis más completo que en P1, pero aún sin usar librerías externas.

## Archivo de entrada

`{tema}-ruido.csv` (el mismo de P1), que ya está en la carpeta `datos/` de la raíz de su repositorio. Recuerda: las columnas están separadas por `|`, no por comas (ver nota en P1 sobre por qué).

> **Usa el archivo completo, no la muestra.** En `datos/` hay dos archivos: `{tema}-ruido_100.csv` (100 filas, para probar tu código mientras lo escribes) y `{tema}-ruido_100000.csv` (el dataset completo, ~103,000 filas). **La entrega se califica contra el archivo completo.** Si tu `analisis_python.json` reporta cifras del orden de 100 registros en lugar de 103,000, procesaste el archivo equivocado. En P1 esto le pasó a dos equipos y arrastró casi todos los números del reporte.

## Entregable

```
pcd-{tema}-{seed}/
└── practica2/
    ├── src/
    │   └── analisis_python.py
    └── resultados/
        └── analisis_python.json
```

## Salida esperada: `analisis_python.json`

```json
{
  "archivo": "{tema}-ruido.csv",
  "pareja": "{nombre_pareja}",
  "seed": 3,

  "valores_unicos_categorica": {
    "columna": "{nombre_col_categorica}",
    "n_valores_unicos": 8,
    "valores": ["valor1", "valor2", "..."]
  },

  "conteo_por_categoria": {
    "valor1": 12543,
    "valor2": 13021
  },

  "categoria_mas_frecuente": {
    "valor": "valor2",
    "conteo": 13021
  },

  "top_3_categorias": [
    {"valor": "valor2", "conteo": 13021},
    {"valor": "valor1", "conteo": 12543},
    {"valor": "valor7", "conteo": 12190}
  ],

  "estadisticas_numerica_1": {
    "columna": "{nombre_col_numerica_1}",
    "n_valores_validos": 98500,
    "minimo": 50.0,
    "maximo": 15000.0,
    "promedio": 852.34,
    "mediana": 780.5
  },

  "estadisticas_numerica_2": {
    "columna": "{nombre_col_numerica_2}",
    "n_valores_validos": 98200,
    "minimo": 1.0,
    "maximo": 90.0,
    "promedio": 12.45,
    "mediana": 11.0
  },

  "promedio_por_categoria": {
    "valor1": 845.12,
    "valor2": 902.77
  },

  "filtrado": {
    "condicion": "{nombre_col_numerica_1} > 5000.0",
    "umbral_usado": 5000.0,
    "n_registros_que_cumplen": 2341,
    "porcentaje": 2.38
  }
}
```

## Instrucciones

1. **Leer el archivo** usando `open()` y organizar los datos en una **lista de diccionarios** — cada fila es un `dict` donde las llaves son los nombres de las columnas. Separa cada línea con `.split("|")` (el separador es `|`, no coma).
2. **Función `valores_unicos(datos, columna)`:** recibe la lista de dicts y un nombre de columna. Aplica `.strip()` a cada valor, descarta los que queden vacíos, y usa un `set` para obtener los valores únicos. Retorna el set.
3. **Función `conteo_por_categoria(datos, columna)`:** construye un diccionario `{valor: conteo}` para la columna categórica, aplicando también `.strip()` y sin contar las celdas vacías. Determina cuál es el valor más frecuente.

   > **Importante — cómo normalizar los valores de texto.** En los dos puntos anteriores aplica **únicamente** `.strip()`, que quita los espacios del inicio y del final, y descarta los valores que queden vacíos. **No** pases a minúsculas ni unifiques variantes de escritura.
   >
   > El dataset trae el mismo valor escrito de varias formas a propósito (`Pizza`, `PIZZA`, `pizza `, ` Pizza`). En esta práctica esas variantes se cuentan como **valores distintos**: la idea es justamente que veas el ruido real que traen los datos antes de limpiarlo. La limpieza de esas variantes la vas a hacer más adelante, en P4 y P5, con pandas.
   >
   > Si normalizas a minúsculas aquí, obtendrás menos valores únicos de los esperados y tus conteos no van a coincidir. Lo mismo al revés: si no aplicas `.strip()`, `Pizza` y `Pizza ` te van a salir como dos categorías diferentes.
4. **Las 3 categorías más frecuentes (`top_3_categorias`):** a partir del diccionario de conteos, obtén las **tres** categorías con más apariciones, ordenadas de mayor a menor, como una lista de objetos `{"valor": ..., "conteo": ...}`. Úsalo con `sorted()` y su parámetro `key`. Si hay empate en el conteo, desempata por el nombre de la categoría en orden alfabético, para que el resultado sea siempre el mismo.
5. **Función `estadisticas(datos, columna)`:** calcula min, max, promedio **y mediana** de una columna numérica. Debe usar primero `filter()` para excluir valores vacíos o no convertibles, y luego `map()` sobre el resultado ya filtrado para convertir esos strings a floats (en ese orden: si conviertes antes de filtrar, `float("")` lanza un error). Retorna un diccionario.

   > **La mediana no es el promedio.** Es el valor que queda justo a la mitad de los datos **ordenados**. Con un número impar de valores es el del centro; con un número **par** son dos los que quedan al centro, y la mediana es el promedio de esos dos. Tu función tiene que resolver bien los dos casos: no asumas que siempre vas a tener un número impar de valores válidos, porque eso cambia de una columna a otra.
   >
   > Repórtala redondeada a 2 decimales, igual que el promedio.
6. **Función `promedio_por_categoria(datos, categorica, numerica)`:** devuelve un diccionario `{categoria: promedio de <numerica_1> en esa categoría}`. Es la primera función de la práctica que **cruza las dos columnas**: para cada fila necesitas su categoría *y* su valor numérico. Descarta las filas donde falte cualquiera de los dos. Redondea cada promedio a 2 decimales.

   > **Esto te va a mostrar algo.** Como las categorías se cuentan sin unificar variantes de escritura, en el resultado van a aparecer `Pizza` y `PIZZA` como entradas separadas, cada una con su propio promedio. **No lo arregles**: obsérvalo y descríbelo en una o dos líneas en el `README.md` de tu repositorio. Ese es exactamente el problema que vas a resolver en P4 y P5 con pandas, y conviene que lo veas ahora con tus propios datos.
7. **Filtrado con `filter` + `lambda`:** filtrar los registros donde `<numerica_1>` supere un umbral (usar el valor del percentil 90, calculable como la posición `int(0.9 * n)` de la lista ordenada de valores válidos). Contar cuántos registros cumplen la condición y calcular el porcentaje **sobre el total de valores válidos de `<numerica_1>`** (no sobre el total de filas del archivo). En `condicion` escribe el umbral ya sustituido, por ejemplo `"monto_venta > 5000.0"`, no la plantilla.

   > **El porcentaje no va a dar exactamente 10%.** Si muchos valores están empatados justo en el umbral, el filtro `> umbral` los deja fuera a todos. Es normal obtener un número bastante por debajo de 10; no es un error.
8. **Guardar el resultado** como JSON con `json.dump(resultado, f, indent=2, ensure_ascii=False)`.

## Requisitos de código

- Definir al menos **5 funciones** con nombres descriptivos
- Usar al menos **1 `lambda`** y al menos **1 `filter()` o `map()`**
- Uso de clases es **opcional**: si lo desean, pueden definir una clase `Dataset` con métodos `resumen()`, `filtrar()`, `agrupar_por()`, etc.
- No usar `import csv`, `import pandas`, ni ninguna librería que no sea de la biblioteca estándar (sí se puede usar `json`)
- **No usar `collections.Counter` ni `statistics.median`.** El punto de esta práctica es que construyan el conteo y la mediana con estructuras de datos básicas; en P3 y P4 ya usarán las herramientas que lo hacen por ustedes

## Sobre el material de la semana 5

El notebook de la semana 5 (`presentations/week05/`) les sirve de base: ahí están el `leer_csv`, la conversión segura a número, y las funciones de valores únicos, conteo y estadísticas. **Úsenlo, para eso está.**

Pero ojo: ese notebook **no resuelve la práctica completa**. Tres cosas que pide esta entrega no están ahí y las tienen que escribir ustedes:

- la **mediana** dentro de `estadisticas()` (es el ejercicio 12 del notebook, que quedó como `# Tu codigo aqui`)
- la función **`promedio_por_categoria()`** (ejercicio 13, también sin resolver)
- el **`top_3_categorias`**, que requiere `sorted()` con `key`

Además, el notebook trabaja sobre un CSV de ejemplo de 12 filas y usa el percentil **0.75**; su práctica va sobre el dataset completo con el percentil **0.90**. Copiar y pegar sin leer les va a dar números que no cuadran.

## Requisitos de Git

Los mismos que en P1, y **se califican igual**:

- Al menos **3 commits** con mensajes descriptivos (no "update", no "asdf")
- Al menos **1 rama de trabajo** (ej. `feature/analisis`) creada, trabajada y **mergeada a `main`**

> **Este requisito no es un adorno.** En P1 dos equipos trabajaron todo directo en `main` y perdieron la mitad de los puntos de este criterio. Si su rama queda integrada por *fast-forward* (sin commit de merge) cuenta como cumplido; lo que no cuenta es no haber creado ninguna rama.

## Nombres de los entregables

Los nombres son **literales**: `analisis_python.py` y `analisis_python.json`, en `practica2/src/` y `practica2/resultados/` respectivamente. No `p2.py`, no `analisis.py`, no `resultados.json`. En P1 dos equipos perdieron puntos por esto.

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
- Se califica el estado del repositorio **al cierre de la entrega**. Si corrigen algo
  después, cuenta como entrega tardía y aplica la penalización; solo se toma en cuenta
  si, ya con el descuento, el resultado les sigue conviniendo.

---

## Estructura del monorepo del curso

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

**Notas:**
- El archivo `{tema}-ruido.csv` va en la carpeta `datos/` de la raíz, porque es compartido por las 6 prácticas. No lo dupliquen en cada carpeta de práctica.
- El `requirements.txt` es uno solo en la raíz y se va actualizando conforme avanzan.
- El `README.md` debe incluir: nombres de los integrantes, tema asignado, seed, y una breve descripción de cada práctica.
- `.gitignore` debe incluir al menos: `__pycache__/`, `.venv/`, `*.pyc`, `*.egg-info/`
