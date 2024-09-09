import json
import os

#Funcion para crear un archivo json
def crear_archivo(archivo):
    if not os.path.exists(archivo):
        with open(archivo, 'w') as file:
            json.dump([], file)
        print(f"Archivo {archivo} creado")
    else:
        print(f"Archivo {archivo} ya existe")

#Funcion para cargar datos desde un archivo json
def cargar_datos(archivo):
    if os.path.exists(archivo):
        with open(archivo, 'r') as file:
            return json.load(file)
        return []
    
#Funcion para guardar datos en un archivo json
def guardar_datos(archivo, datos):
    with open(archivo, 'w') as file:
        json.dump(datos, file, indent=4)

#Funcion para agregar un nuevo medicamento
def agregar_medicamento():
    medicamentos = cargar_datos('medicamentos.json')
    nuevo_medicamento = {
        "id": len(medicamentos) + 1,
        "nombre": input("Nombre del medicamento: "),
        "laboratorio": input("Laboratorio: "),
        "precio": float(input("Precio: ")),
    }
    medicamentos.append(nuevo_medicamento)
    guardar_datos('medicamentos.json', medicamentos)
    print("Medicamento agregado")

#Funcion para mostrar todos los medicamentos
def mostrar_medicamentos():
    medicamentos = cargar_datos('medicamentos.json')
    if medicamentos:
        for medicamento in medicamentos:
            print(medicamento)
    else:
        print("No hay medicamentos")

#Funcion para agregar un nuevo laboratorio
def agregar_laboratorio():
    laboratorios = cargar_datos('laboratorios.json')
    nuevo_laboratorio = {
        "id": len(laboratorios) + 1,
        "nombre": input("Nombre del laboratorio: "),
        "direccion": input("Direccion: "),
        "telefono": input("Telefono: "),
    }
    laboratorios.append(nuevo_laboratorio)
    guardar_datos('laboratorios.json', laboratorios)
    print("Laboratorio agregado")

#Funcion para mostrar todos los laboratorios
def mostrar_laboratorios():
    laboratorios = cargar_datos('laboratorios.json')
    if laboratorios:
        for laboratorio in laboratorios:
            print(laboratorio)
    else:
        print("No hay laboratorios")

#Menu principal
def menu():
    while True:
        print("\Gestion de medicamentos y laboratorios")
        print("1. Crear archivo de medicamentos")
        print("2. Crear archivo de laboratorios")
        print("3. Agregar medicamento")
        print("4. Mostrar medicamentos")
        print("5. Agregar laboratorio")
        print("6. Mostrar laboratorios")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            crear_archivo('medicamentos.json')
        elif opcion == '2':
            crear_archivo('laboratorios.json')
        elif opcion == '3':
            agregar_medicamento()
        elif opcion == '4':
            mostrar_medicamentos()
        elif opcion == '5':
            agregar_laboratorio()
        elif opcion == '6':
            mostrar_laboratorios()
        elif opcion == '7':
            break
        else:
            print("Opcion invalida")

menu()