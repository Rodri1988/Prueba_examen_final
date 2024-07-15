import json
import random

def asignacion_de_sueldo(trabajadores, sueldos):
    for persona in trabajadores:
        sueldo_aleatorio = random.randrange(300000, 2500000, step=200000)
        trabajador = {   
            "Nombre": persona,
            "Sueldo": sueldo_aleatorio,
            "Descuento salud": f"{sueldo_aleatorio * 0.07:.0f}",
            "Descuento AFP": f"{sueldo_aleatorio * 0.12:.0f}",
            "Sueldo Líquido": f"{sueldo_aleatorio * 0.81:.0f}"} 
        sueldos.append(trabajador)
    print("Sueldos aleatorios asignados exitósamente")
    
    
def clasificar_sueldos(sueldos):
    menor_de_800 = []
    entre_800_y_2Mill = []
    mas_de_2Mill = []
    total = 0
    for trabajador in sueldos:
        if trabajador["Sueldo"] < 800000:
            menor_de_800.append(trabajador)
        elif 800000 <= trabajador["Sueldo"] < 2000000:
            entre_800_y_2Mill.append(trabajador)
        elif 2000000 <= trabajador["Sueldo"]:
            mas_de_2Mill.append(trabajador)
    print(f"\nSueldos menores a $800.000\tTOTAL = {len(menor_de_800)}\nNombre empleado\t\tSueldo")
    for trabajador in menor_de_800:
        print(f"{trabajador["Nombre"]}\t\t$ {trabajador["Sueldo"]}")
    print(f"\nSueldos entre $800.000 y $2.000.000\tTOTAL = {len(entre_800_y_2Mill)}\nNombre empleado\t\tSueldo")
    for trabajador in entre_800_y_2Mill:
        print(f"{trabajador["Nombre"]}\t\t$ {trabajador["Sueldo"]}")
    print(f"\nSueldos superiores a $2.000.000\tTOTAL = {len(mas_de_2Mill)}\nNombre empleado\t\tSueldo")
    for trabajador in mas_de_2Mill:
        print(f"{trabajador["Nombre"]}\t\t$ {trabajador["Sueldo"]}")
    for trabajador in sueldos:
        total += trabajador["Sueldo"]
    print(f"\nTOTAL SUELDOS: $ {total}\n")
def ver_estadisticas(sueldos):
    dinero = []
    sueldo_máximo = []
    sueldo_mínimo = []
    total = 0
    for trabajador in sueldos:
        dinero.append(trabajador["Sueldo"])
    for trabajador in sueldos:
        if trabajador["Sueldo"] == max(dinero):
            sueldo_máximo.append(trabajador["Nombre"])
        elif trabajador["Sueldo"] == min(dinero):
            sueldo_mínimo.append(trabajador["Nombre"])
    print(f"Sueldo más alto:")
    for trabajador in sueldo_máximo:
        print(f"{trabajador}\t$ {max(dinero)}")
    print(f"\nSueldo más bajo:")
    for trabajador in sueldo_mínimo:
        print(f"{trabajador}\t$ {min(dinero)}")
    for trabajador in dinero:
        total += trabajador
    print(f"\nPromedio de sueldos: $ {total//10}")
    dinero.sort()
    print(f"Media geométrica: $ {(dinero[4]+dinero[5])//2}\n")
def reporte_de_sueldos(nombre_archivo, sueldos):
    print("Nombre empleado\t\tSueldo Base\tDescuento Salud\tDescuento AFP\tSueldo Líquido")
    for trabajador in sueldos:
        print(f"{trabajador["Nombre"]}\t\t{trabajador["Sueldo"]}\t\t{trabajador["Descuento salud"]}\t\t{trabajador["Descuento AFP"]}\t\t{trabajador["Sueldo Líquido"]}")
    print("\nDatos guardados exitósamente en formato JSON\n")
    with open(f"{nombre_archivo}.json", "w") as archivo:
        json.dump(sueldos, archivo, indent=1)
    
sueldos = []
trabajadores = ["Juan Pérez", "María García" ,"Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
while True:
    try:
        menu = input("\n=== Aplicación de sueldos ===\n------------------------------\n1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadísticas\n4. Reporte de sueldos\n5. Salir del programa\nELIGE UNA DE LAS OPCIONES (1-5)\n")
        if menu == "1":
            if sueldos == []:
                asignacion_de_sueldo(trabajadores, sueldos)
            else:
                sueldos = []
                asignacion_de_sueldo(trabajadores, sueldos)
        elif menu == "2":
            if sueldos == []:
                print("No existen sueldos asignados")
            else:
                clasificar_sueldos(sueldos)
        elif menu == "3":
            if sueldos == []:
                print("No existen sueldos asignados")
            else:
                ver_estadisticas(sueldos)
        elif menu == "4":
            if sueldos == []:
                print("No existen sueldos asignados")
            else:
                nombre_archivo = input("Ingrese el nombre de archivo para guardar los datos: ")
                reporte_de_sueldos(nombre_archivo, sueldos)
        elif menu == "5":
            print("Finalizando programa.........\nDesarrollado por Rodrigo Candia\n16.787.945-4")
            break
        else:
            raise ValueError
    except ValueError:
        print("Elija una opción válida")
