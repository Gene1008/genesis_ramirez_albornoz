empleados_dict = {}

def AgregarEmpleado(Nombre, salario, fecha_ingreso):
    empleados_dict[Nombre] = {
        "Salario": salario,
        "Fecha de ingreso": fecha_ingreso
    }
import datetime

def Calcular_antiguedad(Nombre):
    if Nombre in empleados_dict:
        fecha_ingreso_str = empleados_dict[Nombre]["Fecha de ingreso"]
        fecha_ingreso = datetime.datetime.strptime(fecha_ingreso_str, "%d,%m,%Y").date()
        fecha_actual = datetime.date.today()
        antiguedad = fecha_actual.year - fecha_ingreso.year - ((fecha_actual.month, fecha_actual.day) < (fecha_ingreso.month, fecha_ingreso.day))
        return antiguedad
    else:
        return "Empleado no encontrado."