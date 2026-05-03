# Lista donde se guardan los empleados
empleados = []

def registrar_empleado():
    print("\n--- REGISTRAR EMPLEADO ---")
    nombre = input("Ingrese el nombre: ")
    salario_base = float(input("Ingrese el salario base: "))
    dias_trabajados = int(input("Ingrese los días trabajados: "))

    empleado = {
        "nombre": nombre,
        "salario_base": salario_base,
        "dias_trabajados": dias_trabajados
    }

    empleados.append(empleado)
    print("✅ Empleado registrado correctamente.\n")


def calcular_nomina():
    print("\n--- NÓMINA ---")

    if len(empleados) == 0:
        print("⚠️ No hay empleados registrados.\n")
        return

    SALARIO_MINIMO = 1300000
    AUXILIO_TRANSPORTE = 160000

    for emp in empleados:
        salario_base = emp["salario_base"]
        dias = emp["dias_trabajados"]

        # Pago proporcional por días trabajados
        salario = (salario_base / 30) * dias

        # Auxilio de transporte
        if salario_base < (2 * SALARIO_MINIMO):
            salario += AUXILIO_TRANSPORTE

        # Descuento 8%
        descuento = salario * 0.08
        salario_final = salario - descuento

        print(f"\nEmpleado: {emp['nombre']}")
        print(f"Salario base: ${salario_base}")
        print(f"Días trabajados: {dias}")
        print(f"Pago total: ${round(salario_final, 2)}")


def menu():
    while True:
        print("\n====== SISTEMA DE NÓMINA ======")
        print("1. Registrar empleado")
        print("2. Calcular nómina")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            calcular_nomina()
        elif opcion == "3":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida")


# Ejecutar programa
menu()