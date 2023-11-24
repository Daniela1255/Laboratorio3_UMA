class Auto:
    def __init__(self, marca, modelo, asientos, color, tipo, combustible, precio, garantia, fecha_ingreso):
        self.marca = marca
        self.modelo = modelo
        self.asientos = asientos
        self.color = color
        self.tipo = tipo
        self.combustible = combustible
        self.precio = precio
        self.garantia = garantia
        self.fecha_ingreso = fecha_ingreso

# Función para ingresar los datos del auto
def ingresar_datos():
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    asientos = int(input("Ingrese el número de asientos: "))
    color = input("Ingrese el color del auto: ")
    tipo = input("Ingrese el tipo de auto (sedan, hatchback, pickup): ")
    combustible = input("Ingrese el tipo de combustible: ")
    precio = float(input("Ingrese el precio del auto: "))
    garantia = input("Ingrese la garantía del auto: ")
    fecha_ingreso = input("Ingrese la fecha de ingreso a la empresa (formato: dd-mes-año): ")

    return Auto(marca, modelo, asientos, color, tipo, combustible, precio, garantia, fecha_ingreso)

# Función para mostrar la información del auto
def mostrar_informacion(auto):
    print(f"Marca: {auto.marca}\nModelo: {auto.modelo}\nAsientos: {auto.asientos}\nColor: {auto.color}\nTipo: {auto.tipo}\nPrecio: ${auto.precio}\nGarantia: {auto.garantia}\nFecha: {auto.fecha_ingreso}\n")

# Ingresar datos de dos autos
auto1 = ingresar_datos()
auto2 = ingresar_datos()

# Mostrar la información de los autos
print("\nSeleccione el modelo de auto que desea ver:")
print("1. ", auto1.marca, auto1.modelo)
print("2. ", auto2.marca, auto2.modelo)

opcion = int(input("Ingrese el número del modelo de auto que desea ver (1 o 2): "))

if opcion == 1:
    mostrar_informacion(auto1)
elif opcion == 2:
    mostrar_informacion(auto2)
else:
    print("Opción no válida. Por favor, ingrese 1 o 2.")
