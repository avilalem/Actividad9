def registrar_destinos(cantidad_destinos):
        if cantidad_destinos ==0:
            return {}
        else:
            destinos=registrar_destinos(cantidad_destinos-1)
            nombre_destino=input("Ingrese el nombre del destino: ")
            destinos[nombre_destino]={"nobre_destino":nombre_destino}
            return destinos

def registrar_cliente():
    cliente={}
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
        destinos=registrar_destinos(cantidad_destinos)
        cliente[codigo_cliente]={
            "nombre":nombre,
            "destino":destinos
        }
def mostrar_cliente(cliente, codigos=None, indice=0):
    if not cliente:
        print("No hay clientes registrados")
        return
    if codigos is None:
        codigos=list(cliente.keys())
        print("*** Listado de Clientes y Destinos Visitados ***")
