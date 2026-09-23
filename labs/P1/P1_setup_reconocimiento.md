# Práctica 1 — Setup del proyecto + primer reconocimiento del dataset

**Programación para Ciencia de Datos**

**Asignada:** mié 23-sep · **Entrega:** mar 6-oct
**Temas:** Terminal, VS Code, Entornos virtuales, Git, GitHub, Python I-II

---

## Contexto

Esta es tu primera práctica. Tu pareja ha recibido un dataset sintético (`{tema}-ruido.csv`) que usarán durante todo el semestre. En esta práctica vas a configurar tu entorno de trabajo completo y hacer un primer reconocimiento del dataset usando solo Python puro (sin librerías externas).

## Archivo de entrada

`{tema}-ruido.csv` — proporcionado por el profesor. ~103,000 filas y 9 columnas (el orden de las columnas es aleatorio). Consulta la tabla de referencia de columnas para saber cuáles corresponden a tu tema.

> **Importante sobre el formato:** aunque el archivo termina en `.csv`, las columnas están separadas por `|` (barra vertical / *pipe*), **no por comas**. Esto es intencional: las columnas `direccion` y de texto libre contienen comas dentro de su propio contenido (ej. `"Calle Reforma #123, Col. Centro, CDMX"`), así que si el archivo usara comas como separador, un `.split(",")` simple cortaría esas columnas en pedazos incorrectos y descuadraría toda la fila. Con `|` como separador, tu `.split("|")` funciona sin problema porque ese carácter nunca aparece dentro de los datos.

## Entregable

En esta práctica se crea el **monorepo** del curso (ver estructura al final). Los archivos de P1 van en:

```
pcd-{tema}-{seed}/
├── .gitignore
├── README.md
├── requirements.txt
├── datos/
│   └── {tema}-ruido.csv
└── practica1/
    ├── src/
    │   └── resumen.py
    └── resultados/
        └── resumen.txt
```

## Requisitos de Git y entorno

- Crear el repositorio en GitHub (público o con acceso para el profesor)
- Al menos **3 commits** con mensajes descriptivos (no "update", no "asdf")
- Al menos **1 rama de trabajo** (ej. `feature/resumen`) creada, trabajada y mergeada a `main`
- El CSV de datos debe estar en `datos/` (raíz del repo, no dentro de `practica1/`)

## Salida esperada: `resumen.txt`

El script `resumen.py` debe leer `{tema}-ruido.csv` y generar `resultados/resumen.txt` con el siguiente formato:

```
=== RESUMEN DEL DATASET ===
Archivo: {tema}-ruido.csv
Pareja: {nombre_pareja}
Seed: {seed}

--- Dimensiones ---
Filas: {n_filas}
Columnas: {n_columnas}
Nombres de columnas: {col1}, {col2}, {col3}, ...

--- Primeras 5 filas ---
{col1} | {col2} | {col3} | ...
{val}  | {val}  | {val}  | ...
{val}  | {val}  | {val}  | ...
{val}  | {val}  | {val}  | ...
{val}  | {val}  | {val}  | ...
{val}  | {val}  | {val}  | ...

--- Columna categórica: {nombre_columna} ---
Valores únicos: {n}
Valor más frecuente: {valor} ({conteo} apariciones)

--- Columna numérica: {nombre_columna_numerica_1} ---
Valores válidos (no vacíos): {n}
Mínimo: {valor}
Máximo: {valor}

--- Calidad de datos ---
Celdas vacías totales: {n}
Celdas vacías por columna:
  {columna_1}: {n}
  {columna_2}: {n}
  ...
```

## Instrucciones

1. **Leer el archivo línea por línea** usando `open()`. No usar la librería `csv`, ni `pandas`, ni ninguna librería externa. La primera línea contiene los encabezados; las siguientes son datos. Separar cada línea con `.split("|")` (recuerda: el separador es `|`, no coma — ver nota en "Archivo de entrada").
2. **Contar filas y columnas.** Las filas se cuentan excluyendo la cabecera. Las columnas se cuentan a partir de la cabecera.
3. **Imprimir las primeras 5 filas de datos** separando los valores con ` | `.
4. **Identificar la columna categórica** de tu tema (ver tabla de referencia). Recorrer todas las filas, contar cuántas veces aparece cada valor (ignorando celdas vacías) y reportar el valor más frecuente con su conteo.
5. **Identificar `<numerica_1>`** de tu tema. Recorrer los valores, convertir a `float` (ignorando celdas vacías que no se pueden convertir), y calcular el mínimo y máximo.
6. **Contar celdas vacías** por columna. Una celda se considera vacía si `valor.strip() == ""` después de leer la línea.

> **Nota sobre rendimiento:** el archivo tiene ~103,000 filas. Python puro puede tardar varios segundos en procesarlo — es normal. El script debe procesar el archivo completo.

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

- **-1 punto por cada día natural de retraso** sobre la calificación de la práctica.
- Máximo 5 días de retraso. Después de 5 días la práctica vale **0**.

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
