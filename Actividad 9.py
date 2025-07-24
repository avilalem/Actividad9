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
            "destinos":destinos
        }
def contar_destinos(cliente):
    total=0
    for datos in cliente.values():
        total += len(datos["nobre_destino"])
    return total

def cliente_mas_destinos(cliente):
    max_destinos=0
    nombre_cliente=""
    for datos in cliente.values():
        cantidad=len(datos["destinos"])
        if cantidad>max_destinos:
            max_destinos=cantidad
            nombre_cliente=datos["nombre"]
        return nombre_cliente, max_destinos


def mostrar_cliente(cliente):
    if not cliente:
        print("No hay estudiantes registrados")
        return
    print("Lista de clientes:")
    for codigo,datos in cliente.items():
        print(f"{codigo}: - Nombre: {datos['nombre']}")
        destinos=datos["destinos"]
        if destinos:
            print(f"Destinos: {destinos['nobre_destino']}")
        else:
            print("No hay destinos")

