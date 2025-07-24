def registrar_cliente(cliente):
    try:
        cantidad=int(input("Cuantos clientes desea ingresar?: "))
    except ValueError:
        print("El valor ingresado no es valido")
        return

    for i in range(cantidad):
        codigo_cliente=input(f"Ingrese codigo de cliente #{i+1}: ")
        if codigo_cliente in cliente:
            print("El codigo ingresado ya existe. Intente nuevamente")
            continue
        nombre=input("Ingrese nombre del cliente: ")
        try:
            cantidad_destinos=int(input("Cuantos destinos desea ingresar?: "))
        except ValueError:
            print("El valor ingresado no es valido")
            return
        destinos={}
        for i in range(cantidad_destinos):
            nombre_destinos=input(f"Ingrese nombre del destino#{i+1}: ")
            destinos[nombre_destinos]={
                "destino":nombre_destinos
            }
        cliente[codigo_cliente]={
            "nombre":nombre,
            "destino":destinos
        }
def mostrar_cliente(cliente):
    if not cliente:
        print("No hay clientes registrados")
        return
    print("*** Listado de Clientes y Destinos Visitados ***")
    for codigo_cliente,datos in cliente:
        print(f"{codigo_cliente}: {cliente[codigo_cliente]}")
        destinos=datos.get["destino",{}]
        if destinos:
            for cosa, in destinos.items():
                print(f"Destino: {destino}")