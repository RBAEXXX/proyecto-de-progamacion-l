nombre_de_usuario = "usuario1"
contraseña = "123"

while True:
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña_ingresada = input("Ingrese su contraseña: ")
    if usuario == nombre_de_usuario and contraseña_ingresada == contraseña:
        print("Ingreso exitoso!")
        break
    else:
        print("Error de datos. Por favor ingrese nuevamente su nombre de usuario y contraseña.")
    
tecnicos = ['Roger', 'Didier', 'Carlos', 'Cristian']

dispositivos = {}

def asignar_dispositivo():    
    print("Tecnicos:")
    print('1. Roger')
    print('2. Didier')
    print('3. Carlos')
    print('4. Cristian')
    tecnico = input('Ingrese el nombre del técnico: ')
    if tecnico not in tecnicos:
        print('Error: Técnico no válido')
        return
    dispositivo = input('Ingrese el nombre del dispositivo: ')
    hora_entrada = input('Ingrese la hora de entrada: ')
    hora_salida = input('Ingrese la hora de salida: ')
    fecha_entrada= input('Ingrese la fecha de entrada:')
    fecha_salida= input('Ingrese la fecha de salida:')
    motivo_de_daño=input('Ingrese el daño del dispositivo:')

    reparado = input('¿Está reparado? (S/N): ')
    dispositivos[dispositivo] = {
        'tecnico': tecnico,
        'hora_entrada': hora_entrada,
        'hora_salida': hora_salida,
        'fecha_entrada': fecha_entrada,
        'fecha_salida': fecha_salida,
        'motivo_de_daño': motivo_de_daño,
        'reparado': reparado
    }
    print('Dispositivo asignado con éxito')

def ver_datos_dispositivo():
    dispositivo = input('Ingrese el nombre del dispositivo: ')
    if dispositivo not in dispositivos:
        print('Error: Dispositivo no encontrado')
        return
    print(f'Técnico: {dispositivos[dispositivo]["tecnico"]}')
    print(f'Hora de entrada: {dispositivos[dispositivo]["hora_entrada"]}')
    print(f'Hora de salida: {dispositivos[dispositivo]["hora_salida"]}')
    print(f'fecha de entrada: {dispositivos[dispositivo]["fecha_entrada"]}')
    print(f'fecha de salida: {dispositivos[dispositivo]["fecha_salida"]}')
    print(f'motivo de daño: {dispositivos[dispositivo]["motivo_de_daño"]}')
    print(f'Reparado: {"Sí" if dispositivos[dispositivo]["reparado"].lower() == "s" else "No"}')

def generar_factura():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    productos = []
    precios = []
    continuar = "si"
    while continuar == "si":
        producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        productos.append(producto)
        precios.append(precio)
        continuar = input("¿Desea ingresar otro producto? (si/no): ").lower()
        if continuar == "no":
            break  

    print("FACTURA\n")
    print(f"Cliente: {nombre_cliente}\n")
    print("Productos:\n")
    for i in range(len(productos)):
        print(f"  - {productos[i]}: ${precios[i]}")
    print("\nTotal: $" + str(sum(precios)))

    opcion_salida = input("Presione 's' para salir o cualquier otra tecla para generar otra factura: ")
    if opcion_salida.lower() == "s":
        return 
    else:
        generar_factura()  



precios = {'xiaomi mi 11 lite 5g ': 150000000, 'Apple macbook': 472500000, 'iphone 11': 170000000, 'camara go pro':5000000}

def registrar_venta():
    producto = input('Ingrese el nombre del producto (xiaomi mi 11 lite 5g,Apple macbook,iphone 11,camara go pro ): ')
    if producto.lower() not in precios:
        print('Error: Producto no válido')
        return
    cantidad = int(input('Ingrese la cantidad vendida: '))
    precio_unitario = precios[producto.lower()]
    total = precio_unitario * cantidad
    print(f'Se han vendido {cantidad} {producto}s por un total de {total} pesos')
    
while True:
    print(" BIENVENIDO A COMPUCEL")
    print('Seleccione una opción:')
    print('1. Asignar dispositivo a técnico')
    print('2. Ver datos de dispositivo')
    print('3. Hacer factura del trabajo')
    print('4. Registrar venta de celular o computador')
    print('5. Salir')
    opcion = input()
    if opcion == '1':
        asignar_dispositivo()
    elif opcion == '2':
        ver_datos_dispositivo()
    elif opcion == '3':
        generar_factura()
    elif opcion == '4':
        registrar_venta()
    elif opcion == '5': 
        registrar_venta:(5)
        break