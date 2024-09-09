from modulos.empleados import empleados_dict, AgregarEmpleado, Calcular_antiguedad

if __name__ == '__main__':
    while True:
        Nombre = input("Ingrese nombre del empleado: ")
        salario = float(input("Ingrese el salario del empleado:"))
        fecha_ingreso = input("Ingrese la fecha de ingreso del empleado: ")

        AgregarEmpleado(Nombre, salario, fecha_ingreso)

        continuar = input("¿Desea agregar otro empleado? (s/n): ")
        if continuar.lower() != 's':
            break

    print("Empleados agregados: ")

    for Nombre in empleados_dict:
        antiguedad = Calcular_antiguedad(Nombre)
        info = empleados_dict[Nombre]
        print(f"Nombre: {Nombre}, Salario: {info['Salario']}, Fecha de ingreso: {info['Fecha de ingreso']}, Antigüedad: {antiguedad} años.")

