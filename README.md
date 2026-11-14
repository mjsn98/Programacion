# Generador de planes turísticos

**Actividad Integradora Final 2026 — Elementos de Programación (UNSL)**

Programa desarrollado en Python que genera un plan turístico personalizado. El
usuario ingresa su nombre y la cantidad de días que desea planificar (entre 1 y
5); el programa selecciona al azar un lugar para visitar, una actividad
recreativa y una comida típica para cada día, y guarda el resultado en un
archivo de texto y en un archivo CSV creado con Pandas.

## Integrantes

- Santillan, Mara
- Suarez Bonahora, Flavia

## Video explicativo

- Enlace: **PENDIENTE**

> La primera línea de `generador.py` debe contener el enlace al video alojado en
> YouTube o Google Drive, configurado como público o con acceso por enlace. Se
> debe reemplazar el texto `PENDIENTE` antes de la entrega. El video no debe
> incluirse dentro del archivo ZIP.

## Requisitos

- Python 3.10 o superior.
- Pandas.

Instalación de Pandas (si no está instalado):

```bash
python -m pip install pandas
```

## Archivos del proyecto

| Archivo | Descripción |
| --- | --- |
| `generador.py` | Programa principal. Contiene todas las funciones y la ejecución. |
| `datos_turismo.txt` | Archivo de entrada con las opciones turísticas. |
| `plan_turistico.txt` | Salida generada automáticamente en formato de texto. |
| `plan_turistico.csv` | Salida generada automáticamente en formato CSV (Pandas). |
| `README.md` | Documentación del programa. |
| `.gitignore` | Archivos que no se versionan (PDF de la cátedra, temporales, ZIP). |

Para la entrega en el Aula Virtual, el archivo comprimido debe llamarse
`AI_Santillan_SuarezBonahora.zip` y contener **únicamente** `generador.py` y
`datos_turismo.txt`.

## Formato del archivo de entrada

`datos_turismo.txt` contiene **30 líneas con contenido**, una opción por línea,
organizadas en tres bloques de 10:

| Líneas | Categoría |
| --- | --- |
| 1 a 10 | Lugares para visitar |
| 11 a 20 | Actividades recreativas |
| 21 a 30 | Comidas típicas |

El programa identifica la categoría de cada opción por su **posición** en el
archivo, no por un encabezado. Las líneas vacías se ignoran. Si el archivo tiene
menos de 30 opciones, el programa muestra un mensaje de error y no genera el
plan. Las opciones están inspiradas en destinos y comidas de la provincia de San
Luis.

## Ejecución

Desde la carpeta del proyecto:

```bash
python generador.py
```

El programa solicita los datos por teclado:

```text
¡Bienvenido al generador de planes turísticos!
Ingrese su nombre: Ana
Ingrese la cantidad de días que desea planificar (1 a 5): 3
```

Luego genera y muestra la tabla, y crea los dos archivos de salida:

```text
¡Plan turístico generado con éxito!
Plan turístico de Ana
   Día                     Lugar            Actividad             Comida
0    1  Museo Histórico Regional  Kayak en el embalse  Guiso de lentejas
1    2          Dique La Florida     Avistaje de aves  Membrillo y queso
2    3       Capilla del Rosario   Trepada al mirador  Chivito al asador

Archivos generados:
- plan_turistico.txt
- plan_turistico.csv
```

> La tabla puede verse con columnas ocultas si la consola es angosta; el
> DataFrame completo se imprime y se guarda en el CSV. Los valores concretos
> cambian en cada ejecución porque la selección es aleatoria.

## Funciones implementadas

El programa está dividido en funciones con parámetros y valores de retorno:

### `leer_datos(nombre_archivo)`

- **Parámetro:** nombre del archivo de texto.
- **Devuelve:** un diccionario `{categoría: [opciones]}` con las tres
  categorías.
- **Tarea:** abre el archivo, lee todas las líneas, elimina espacios y líneas
  vacías, valida que haya al menos 30 opciones y divide la lista en bloques de
  10 mediante rebanadas (*slicing*). Si faltan datos, devuelve un diccionario
  vacío.

### `elegir_sin_repetir(opciones, cantidad)`

- **Parámetros:** lista de opciones y cantidad de elementos a elegir.
- **Devuelve:** una lista con `cantidad` opciones al azar.
- **Tarea:** copia la lista de opciones y, mientras falten elementos, elige uno
  con `random.choice()` y lo quita de la copia con `remove()`. Así se evita
  repetir el mismo lugar, actividad o comida en los distintos días.

### `generar_plan(datos, cantidad_dias)`

- **Parámetros:** diccionario de datos y cantidad de días.
- **Devuelve:** una lista de diccionarios, uno por día, con las claves `Día`,
  `Lugar`, `Actividad` y `Comida`.
- **Tarea:** elige las opciones de las tres categorías y arma el plan día por
  día.

### `guardar_y_mostrar(plan, nombre_persona)`

- **Parámetros:** lista de diccionarios con el plan y nombre del turista.
- **Devuelve:** el DataFrame creado.
- **Tarea:**
  1. Escribe `plan_turistico.txt` con `open()`, `write()` y `close()`.
  2. Crea el DataFrame con `pd.DataFrame(plan, columns=COLUMNAS)`.
  3. Guarda el DataFrame con `tabla.to_csv(...)`.
  4. Muestra la tabla en pantalla con `print(tabla)`.

### `pedir_nombre()`

- **Devuelve:** el nombre ingresado por teclado.
- **Tarea:** solicita el nombre con `input()` y vuelve a pedirlo si está vacío.

### `pedir_cantidad_dias()`

- **Devuelve:** un número entero entre 1 y 5.
- **Tarea:** solicita la cantidad de días y valida con un ciclo `while` que sea
  un número entero dentro del rango permitido. Si el dato es incorrecto,
  muestra un mensaje de error y lo solicita nuevamente.

### `main()`

- **Tarea:** función principal que coordina la ejecución: muestra el mensaje de
  bienvenida, pide los datos, lee el archivo, genera el plan y llama a la función
  que guarda y muestra los resultados.

## Colecciones y estructuras de datos utilizadas

- **Tuplas:** `CATEGORIAS` y `COLUMNAS` guardan valores fijos que no deben
  modificarse.
- **Diccionario:** `datos` relaciona cada categoría con su lista de opciones;
  cada registro del plan también es un diccionario con las claves de las
  columnas.
- **Listas:** almacenan las líneas del archivo, las opciones de cada categoría,
  las opciones seleccionadas y el plan completo. Se usan operaciones como
  `append()`, `remove()` y rebanadas.
- **Cadenas:** se usan `strip()`, `isdigit()`, concatenación y repetición de
  separadores (`"=" * 50`).

## Selección aleatoria

La elección se realiza con `random.choice()` sobre las opciones disponibles de
cada categoría. Para que un mismo lugar, actividad o comida no se repita entre
los días de un mismo plan, la opción elegida se elimina de una copia de la lista
y se continúa eligiendo hasta completar la cantidad de días solicitada. Como
consecuencia, cada ejecución produce un plan diferente.

## Uso de Pandas

Se utilizan las instrucciones pedidas en el enunciado:

```python
import pandas as pd

tabla = pd.DataFrame(plan, columns=COLUMNAS)
print(tabla)
tabla.to_csv(ARCHIVO_CSV, index=False, encoding="utf-8-sig")
```

- `pd.DataFrame()` arma la tabla a partir de la lista de diccionarios.
- `print()` muestra la tabla en pantalla.
- `to_csv()` guarda el archivo CSV sin el índice de filas.
- `encoding="utf-8-sig"` agrega la marca de orden de bytes para que Excel abra
  correctamente los acentos y la letra ñ.

## Archivos de salida

### `plan_turistico.txt`

Se escribe con las operaciones básicas de archivos vistas en el curso. Tiene un
encabezado con el nombre de la persona y, para cada día, el lugar, la actividad
y la comida seleccionados.

### `plan_turistico.csv`

Tiene cuatro columnas: `Día`, `Lugar`, `Actividad` y `Comida`. Se puede abrir con
Excel, LibreOffice Calc o cualquier editor de texto.

## Validaciones y manejo de errores

- El nombre no puede quedar vacío.
- La cantidad de días debe ser un número entero entre 1 y 5. Se rechazan letras,
  números negativos, cero y valores mayores que 5, solicitando el dato otra vez.
- Si `datos_turismo.txt` no tiene al menos 30 opciones, se informa el problema y
  no se genera el plan.
- Si el archivo de entrada no existe, Python muestra el error de archivo no
  encontrado; por eso debe ejecutarse el programa desde la carpeta que contiene
  `datos_turismo.txt`.

## Contenidos del cronograma aplicados

La solución utiliza únicamente contenidos desarrollados en la materia:

- **Unidad 2:** `input()`, ejecución de scripts y comentarios.
- **Unidad 3:** tipos de datos, operadores, expresiones y conversión de tipos.
- **Unidad 4:** condicionales `if`, ciclos `while` y `for`.
- **Unidad 5:** listas, tuplas, cadenas y diccionarios; operaciones comunes.
- **Unidad 6:** funciones (`def`, parámetros y `return`), archivos y biblioteca
  (`random` y `pandas`).

No se utilizan clases, funciones lambda, comprensiones de listas ni manejo de
excepciones con `try`/`except`, ya que no forman parte de los contenidos del
cronograma.

## Git

El proyecto está versionado con Git. Para consultar el estado y el historial:

```bash
git status
git log --oneline
```

Para registrar cambios después de una modificación:

```bash
git add .
git commit -m "Descripción del cambio"
```

El archivo `.gitignore` excluye los PDF de la cátedra, los archivos temporales de
Python, los entornos virtuales y los ZIP de entrega.

## Entrega

1. Reemplazar los datos de los integrantes y el enlace del video en este README
   y en la primera línea de `generador.py`.
2. Verificar que el programa funcione con `datos_turismo.txt`.
3. Crear el archivo `AI_Apellido1_Apellido2.zip` con **solo** `generador.py` y
   `datos_turismo.txt`.
4. Subirlo al Aula Virtual antes del **16/11 a las 23 hs**.
5. Asegurarse de que el enlace del video sea accesible sin solicitar permisos.
