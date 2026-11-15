
# Video explicativo: https://youtu.be/VmErNzsSjL0

"""
Actividad Integradora Final 2026 - "Generador de planes turísticos"
Elementos de Programación - UNSL

Archivo principal del programa. Lee las opciones turísticas desde
datos_turismo.txt, genera un plan aleatorio y lo guarda en formato
de texto y CSV (Pandas).
"""

import random
import pandas as pd

# Nombres de los archivos que utiliza el programa.
ARCHIVO_DATOS = "datos_turismo.txt"
ARCHIVO_TXT = "plan_turistico.txt"
ARCHIVO_CSV = "plan_turistico.csv"

# El archivo de entrada tiene 10 opciones por categoría, en este orden.
CATEGORIAS = ("Lugares para visitar", "Actividades recreativas", "Comidas típicas")
COLUMNAS = ("Día", "Lugar", "Actividad", "Comida")
OPCIONES_POR_CATEGORIA = 10


def leer_datos(nombre_archivo):
    """Lee datos_turismo.txt y devuelve un diccionario con las 3 categorías.

    Las primeras 10 líneas son los lugares para visitar, las 10 siguientes
    son las actividades recreativas y las últimas 10 son las comidas típicas.
    """
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    # Guardamos solamente las líneas con contenido, sin espacios ni saltos de línea.
    opciones = []
    for linea in lineas:
        opcion = linea.strip()
        if opcion != "":
            opciones.append(opcion)

    cantidad_necesaria = len(CATEGORIAS) * OPCIONES_POR_CATEGORIA
    if len(opciones) < cantidad_necesaria:
        print("Error: el archivo", nombre_archivo, "debe tener al menos",
              cantidad_necesaria, "opciones.")
        return {}

    # Organizamos las opciones en un diccionario: categoría -> lista de opciones.
    datos = {}
    for i in range(len(CATEGORIAS)):
        inicio = i * OPCIONES_POR_CATEGORIA
        fin = inicio + OPCIONES_POR_CATEGORIA
        datos[CATEGORIAS[i]] = opciones[inicio:fin]

    return datos


def elegir_sin_repetir(opciones, cantidad):
    """Devuelve 'cantidad' opciones al azar, sin repetirlas."""
    # Copiamos la lista para no modificar los datos originales.
    disponibles = opciones[:]
    seleccion = []

    while len(seleccion) < cantidad and len(disponibles) > 0:
        elegida = random.choice(disponibles)
        seleccion.append(elegida)
        disponibles.remove(elegida)

    return seleccion


def generar_plan(datos, cantidad_dias):
    """Genera el plan turístico con una opción de cada categoría por día."""
    lugares = elegir_sin_repetir(datos[CATEGORIAS[0]], cantidad_dias)
    actividades = elegir_sin_repetir(datos[CATEGORIAS[1]], cantidad_dias)
    comidas = elegir_sin_repetir(datos[CATEGORIAS[2]], cantidad_dias)

    # Cada día se guarda como un diccionario dentro de una lista.
    plan = []
    for i in range(cantidad_dias):
        registro = {
            "Día": i + 1,
            "Lugar": lugares[i],
            "Actividad": actividades[i],
            "Comida": comidas[i],
        }
        plan.append(registro)

    return plan


def guardar_y_mostrar(plan, nombre_persona):
    """Guarda el plan en TXT y CSV, y lo muestra en pantalla como tabla."""
    # 1) Guardamos el plan en un archivo de texto.
    archivo = open(ARCHIVO_TXT, "w", encoding="utf-8")
    archivo.write("Plan turístico de " + nombre_persona + "\n")
    archivo.write("=" * 50 + "\n")

    for registro in plan:
        archivo.write("Día " + str(registro["Día"]) + "\n")
        archivo.write("  Lugar para visitar: " + registro["Lugar"] + "\n")
        archivo.write("  Actividad recreativa: " + registro["Actividad"] + "\n")
        archivo.write("  Comida típica: " + registro["Comida"] + "\n")
        archivo.write("-" * 50 + "\n")

    archivo.close()

    # 2) Creamos un DataFrame de Pandas a partir de la lista de diccionarios.
    tabla = pd.DataFrame(plan, columns=COLUMNAS)

    # 3) Guardamos el DataFrame en un archivo CSV.
    #    utf-8-sig permite abrir el archivo con Excel conservando los acentos.
    tabla.to_csv(ARCHIVO_CSV, index=False, encoding="utf-8-sig")

    # 4) Mostramos el DataFrame en pantalla.
    print()
    print("¡Plan turístico generado con éxito!")
    print("Plan turístico de " + nombre_persona)
    print(tabla)
    print()
    print("Archivos generados:")
    print("- " + ARCHIVO_TXT)
    print("- " + ARCHIVO_CSV)

    return tabla


def pedir_nombre():
    """Pide el nombre de la persona hasta que ingrese un valor no vacío."""
    nombre = input("Ingrese su nombre: ").strip()

    while nombre == "":
        print("Error: el nombre no puede estar vacío.")
        nombre = input("Ingrese su nombre: ").strip()

    return nombre


def pedir_cantidad_dias():
    """Pide la cantidad de días y valida que sea un entero entre 1 y 5."""
    entrada = input("Ingrese la cantidad de días que desea planificar (1 a 5): ").strip()

    # isdigit() permite comprobar que se haya escrito un número entero.
    # Si no es un número, la condición se cumple y no se ejecuta int(entrada).
    while not entrada.isdigit() or int(entrada) < 1 or int(entrada) > 5:
        print("Error: la cantidad de días debe ser un número entero entre 1 y 5.")
        entrada = input("Ingrese la cantidad de días que desea planificar (1 a 5): ").strip()

    return int(entrada)


def main():
    """Función principal: coordina la lectura, la generación y el guardado."""
    print("¡Bienvenido al generador de planes turísticos!")

    nombre = pedir_nombre()
    cantidad_dias = pedir_cantidad_dias()

    datos = leer_datos(ARCHIVO_DATOS)
    if len(datos) == 0:
        print("No se pudo generar el plan porque faltan datos en", ARCHIVO_DATOS)
        return

    plan = generar_plan(datos, cantidad_dias)
    guardar_y_mostrar(plan, nombre)


# Inicio del programa.
main()
