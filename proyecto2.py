from datetime import date
from datetime import datetime

class Empleado:
    def __init__(self, IDEmpleado, nombre, telefono, direccion, correo):
        self.IDEmpleado = IDEmpleado
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
class Categoria:
    def __init__(self, IDCategoria, nombre):
        self.IDCategoria = IDCategoria
        self.nombre = nombre
class Proveedor:
    def __init__(self, IDProveedor, nombre, empresa, telefono, direccion, correo, IDCategoria):
        self.IDProveedor = IDProveedor
        self.nombre = nombre
        self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.IDCategoria = IDCategoria
class Producto:
    def __init__(self, IDProducto, nombre, IDCategoria, precio, totalVentas, totalCompras):
        self.IDProducto = IDProducto
        self.nombre = nombre
        self.IDCategoria = IDCategoria
        self.precio = precio
        self.totalVentas = totalVentas
        self.totalCompras = totalCompras
        self.stock = self.totalCompras - self.totalVentas
class Cliente:
    def __init__(self, NIT, nombre, telefono, direccion, correo):
        self.NIT = NIT
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
class Venta:
    def __init__(self, IDVenta, fecha, NIT, IDEmpleado, total):
        self.IDVenta = IDVenta
        self.fecha = fecha
        self.NIT = NIT
        self.IDEmpleado = IDEmpleado
        self.total = total
class DetallesVenta:
    def __init__(self, IDDetallesVenta, IDVenta, cantidad, IDProducto, precio, subTotal):
        self.IDDetallesVenta = IDDetallesVenta
        self.IDVenta = IDVenta
        self.cantidad = cantidad
        self.IDProducto = IDProducto
        self.precio = precio
        self.subTotal = subTotal
class Compras:
    def __init__(self, IDcompras, fecha, IDproveedor, IDempleado, total):
        self.IDcompras = IDcompras
        self.fecha = fecha
        self.IDproveedor = IDproveedor
        self.IDempleado = IDempleado
        self.total = total
class DetallesCompras:
    def __init__(self, IDDetallesCompras, IDcompras, cantidad, IDproducto, precioCompra, subtotal, fechaCaducidad):
        self.IDDetallesCompras = IDDetallesCompras
        self.IDcompras = IDcompras
        self.cantidad = cantidad
        self.IDproducto = IDproducto
        self.precioCompra = precioCompra
        self.subtotal = subtotal
        self.fechaCaducidad = fechaCaducidad

class Mod_Empleado:
    def __init__(self):
        self.Empleados ={}
        self.cargar_empleados()

    def cargar_empleados(self):
        try:
            with open("Empleados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        idEmp,Nombre,telefono,direccion,correo = linea.split(":")
                        self.Empleados[idEmp]={
                            "nombre": Nombre,
                            "telefono": telefono,
                            "direccion": direccion,
                            "correo": correo,
                        }
                print(f"Empleados importados correctamente desde el archivo {archivo.name}")
        except FileNotFoundError:
            print(f"No existe el archivo a importar, se creará uno al guardar")
    def guardar_Empleados(self):
        with open(f"Empleados.txt", "w", encoding="utf-8") as archivo:
            for clave, valor in self.Empleados.items():
                archivo.write(f"{clave}:{valor["nombre"]}:{valor["telefono"]}:{valor["direccion"]}:{valor["correo"]}\n")

    def AgregarEmpleado(self):
        while True:
            try:
                idE= int(input("Ingrese el ID del empleado: "))
                if idE not in self.Empleados:
                    while True:
                        nombre = input("Ingrese el nombre del empleado: ").strip()
                        if not nombre:
                            input("No se puede dejar el nombre vacío")
                        else:
                            break
                    while True:
                        telefono = input("Ingrese el telefono del empleado: ").strip()
                        if not telefono:
                            input("No se puede ingresar un telefono vacío")
                        else:
                            break
                    while True:
                        direccion = input("Ingrese la direccion del empleado: ").strip()
                        if not direccion:
                            input("No se puede dejar la direccion vacía")
                        else:
                            break
                    while True:
                        correo = input("Ingrese la correo del empleado: ").strip()
                        if not correo:
                            input("No se puede dejar el correo vacío")
                        else:
                            break
                    nuevoEmpleado = Empleado(idE, nombre, telefono, direccion, correo)
                    self.Empleados[nuevoEmpleado.IDEmpleado] = {
                        "nombre": nuevoEmpleado.nombre,
                        "telefono": nuevoEmpleado.telefono,
                        "direccion": nuevoEmpleado.direccion,
                        "correo": nuevoEmpleado.correo
                    }
                    Mod_Empleado.guardar_Empleados()
                    print(f"Empleado Ingresado correctamente")
                    break
                else:
                    print("El ID de empleado ya existe")
            except ValueError:
                input("Ingresa un ID correctamente, únicamente numeros")
    def MostrarDatos(self):
        for id,valor in self.Empleados.items():
            print(f"\tID: {id}")
            print(f"Nombre: {valor["nombre"]}, Telefono: {valor["telefono"]}, Direccion: {valor["direccion"]}, Correo: {valor["correo"]}")
class Mod_Categoria:
    def __init__(self):
        self.Categorias = {}
        self.cargar_Categorias()
    def cargar_Categorias(self):
        try:
            with open(f"Categorias.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        idCat,nombre=linea.split(":")
                        self.Categorias[idCat]={
                            "nombre": nombre,
                        }
                print(f"Categorias Importadas correctamente desde el archivo {archivo.name}.")
        except FileNotFoundError:
            print(f"No existe el archivoa importar, se creará uno nuevo al guardar")
    def guardar_Categorias(self):
        with open(f"Categorias.txt", "w", encoding="utf-8") as archivo:
            for clave, valor in self.Categorias.items():
                archivo.write(f"{clave}:{valor.nombre}\n")
    def AgregarCategoria(self):
        while True:
            try:
                idC= int(input("Ingrese el ID del categoria: "))
                if idC not in self.Categorias:
                    while True:
                        nombre = input("Ingrese el nombre de la categoria: ").strip()
                        if not nombre:
                            input("No se puede dejar el nombre de la categoria vacía")
                        else:
                            break
                    nuevaCategoria = Categoria(idC, nombre)
                    self.Categorias[nuevaCategoria.IDCategoria] = {
                        "nombre": nuevaCategoria.nombre,
                    }
                    self.guardar_Categorias()
                    print("Categoria ingresada correctamente")
                    break
                else:
                    print("El ID de categoria ya existe")
            except ValueError:
                input("Ingrese unicamente números")
    def MostrarDatos(self):
        for id,cat in self.Categorias.items():
            print(f"\tID:{id} Nombre:{cat.nombre}")
class Mod_Proveedor:
    def __init__(self):
        self.Proveedores = {}
        self.cargarProveedor()
    def cargarProveedores(self):
        try:
            with open(f"Proveedores.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        idProv,nombre,empresa,telefono,direccion,correo,idCat=linea.split(":")
                        self.Proveedores[idProv]={
                            "nombre": nombre,
                            "empresa": empresa,
                            "telefono": telefono,
                            "direccion": direccion,
                            "correo": correo,
                            "idCat": idCat
                        }
                print(f"Proveedores importados correctamente desde el archivo {archivo.name}.")
        except FileNotFoundError:
            print(f"No existe el archivo a importar, se creará uno nuevo al guardar")
    def guardarProveedor(self):
        with open(f"Proveedores.txt", "w", encoding="utf-8") as archivo:
            for id,prov in self.Proveedores.items():
                archivo.write(f"{id}:{prov['nombre']}:{prov["empresa"]}:{prov["telefono"]}:{prov["direccion"]}:{prov["correo"]}:{prov["idCat"]}\n")
    def AgregarProveedor(self):
        while True:
            try:
                idProv = int(input("Ingrese el ID del proveedor: "))
                if idProv not in self.Proveedores:
                    while True:
                        nombre = input("Ingrese el nombre del proveedor: ").strip()
                        if not nombre:
                            input("No se puede dejar el nombre vacío")
                        else:
                            break
                    while True:
                        empresa = input("Ingrese la empresa: ").strip()
                        if not empresa:
                            input("No se puede dejar la empresa vacía")
                        else:
                            break
                    while True:
                        telefono = input("Ingrese el telefono del proveedor: ").strip()
                        if not telefono:
                            input("No se puede dejar el telefono vacío")
                        else:
                            break
                    while True:
                        direccion = input("Ingrese la direccion del proveedor: ").strip()
                        if not direccion:
                            input("No se puede dejar la direccion vacía")
                        else:
                            break
                    while True:
                        correo = input("Ingrese el correo del proveedor: ").strip()
                        if not correo:
                            input("No se puede dejar el correo vacío")
                        else:
                            break
                    while True:
                        idCat= int(input("Ingrese el ID del categoria: "))
                        if idCat not in Mod_Categoria.Categorias:
                            input("Error: La categoría no existe. Agrega primero la categoría.")
                            break
                        else:
                            nuevoProveedor = Proveedor(idProv, nombre, empresa, telefono, direccion, correo, idCat)
                            self.Proveedores[nuevoProveedor.IDProveedor]={
                                "nombre": nuevoProveedor.nombre,
                                "empresa": nuevoProveedor.empresa,
                                "telefono": nuevoProveedor.telefono,
                                "direccion": nuevoProveedor.direccion,
                                "correo": nuevoProveedor.correo,
                                "idCat": nuevoProveedor.idCat
                            }
                            input("Proveedor ingresado correctamente")
                            break
                else:
                    input("El ID del proveedor ya existe")
            except ValueError:
                input("Ingrese numeros enteros")



class Mod_Producto:
    def __init__(self):
        self.Productos = {}
    def AgregarProducto(self,):
        salir=0
        while salir!=1972:
            while True:
                try:
                    idP = int(input("Ingrese el ID del producto: "))
                    if idP == 1972:
                        salir= idP
                        break
                    else:
                        if idP not in self.Productos:
                            while True:
                                nombre = input("Ingrese el nombre del producto: ").strip()
                                if not nombre:
                                    input("No se puede dejar el nombre del producto vacío")
                                else:
                                    break
                            while True:
                                idCat = int(input("Ingrese el ID del categoria: "))
                                if idCat not in Mod_Categoria.Categorias:
                                    input("Error: La categoría no existe. Agrega primero la categoría.")
                                    break
                                else:
                                    while True:
                                        try:
                                            precio = float(input("Ingrese el precio del producto: Q."))
                                            break
                                        except ValueError:
                                            input("Ingrese el precio correcto.")
                                    totalCompras = 0
                                    totalVentas = 0
                                    self.Productos[idP] = Producto(idP,nombre, idCat,precio,totalCompras,totalVentas)
                                    input("Producto ingresado correctamente")
                                    break
                        else:
                            input("El ID del producto ya existe")

                except ValueError:
                    input("Ingrese un ID correcto")
class Mod_Clientes:
    def __init__(self):
        self.Clientes ={}

    def AgregarCliente(self):
        while True:
            try:
                NIT = int(input("Ingrese el NIT del cliente: "))
                if NIT not in self.Clientes:
                    while True:
                        nombre = input("Ingrese el nombre del cliente: ").strip()
                        if not nombre:
                            input("No se puede dejar el nombre del cliente")
                        else:
                            break
                    while True:
                        telefono = input("Ingrese el nombre del cliente: ").strip()
                        if not telefono:
                            input("No se puede dejar el telefono vacío")
                        else:
                            break
                    while True:
                        direccion = input("Ingrese la direccion del cliente: ").strip()
                        if not direccion:
                            input("No se puede dejar la direccion vacía")
                        else:
                            break
                    while True:
                        correo = input("Ingrese el correo del cliente: ").strip()
                        if not correo:
                            input("No se puede dejar el correo vacío")
                        else:
                            break
                    self.Clientes[NIT] = Cliente(NIT,nombre,telefono,direccion,correo)
                    input("Cliente ingresado correctamente")
                    break
                else:
                    input("El ID del cliente ya existe")
            except ValueError:
                input("Ingrese un ID correcto")


class Mod_DetallesVenta:
    def __init__(self):
        self.Detalles_Venta = {}
    def AgregarDetallesVenta(self, idVenta):
        idProd = 0
        while idProd!=1972:
            while True:
                try:
                    if len(self.Detalles_Venta) == 0:
                        idDet= 1
                        break
                    else:
                        mayor = len(self.Detalles_Venta)
                        idDet = mayor + 1
                        break
                except ValueError:
                    input("Ingrese un ID correcto")
            while True:
                try:
                    idProd = int(input("Ingrese el ID del producto: "))
                    if idProd == 1972:
                        break
                    else:
                        if idProd not in Mod_Producto.Productos:
                            input("No existe el producto con el ID ingresado...")
                        else:
                            while True:
                                try:
                                    producto = Mod_Producto.Productos[idProd]
                                    cantidad = int(input(f"Ingrese la cantidad de producto {producto.nombre}:"))
                                    if cantidad<0:
                                        input("No se puede ingresar una cantidad negativa")
                                    else:
                                        if cantidad>producto.stock:
                                            input("No existe stock para ese producto")
                                        else:
                                            Mod_Producto.Productos[idProd].totalVentas = cantidad
                                            break
                                except ValueError:
                                    input("Ingrese una cantidad correcta")
                            precio = producto.precio
                            subTotal = precio * cantidad
                            self.Detalles_Venta[idDet]: DetallesVenta(idDet,idVenta,cantidad,idProd,precio, subTotal)
                            input("Detalle venta agregada correcta")
                            break
                except ValueError:
                    input("Ingrese un ID correcto")



class Mod_Venta:
    def __init__(self):
        self.Ventas = {}
    def AgregarVenta(self):
        while True:
            try:
                idVenta = int(input("Ingrese el ID del venta: "))
                if idVenta not in self.Ventas:
                    fecha = date.today()
                    fecha_str = fecha.strftime("%d/%m/%Y %H:%M:%S")
                    while True:
                        try:
                            NIT = int(input("Ingrese el NIT del cliente: "))
                            if NIT not in Mod_Clientes.Clientes:
                                input("No existe el cliente con ese NIT")
                            else:
                                break
                        except ValueError:
                            input("Ingrese un NIT correcto")
                    while True:
                        try:
                            idEm = int(input("Ingrese el ID del empleado: "))
                            if idEm not in Mod_Empleado.Empleados:
                                input("No existe el empleado con ese ID")
                            else:
                                break
                        except ValueError:
                            input("Ingrese un ID correcto")
                    total= 0
                    Mod_DetallesVenta.AgregarDetallesVenta(idVenta)
                    for clave, valor in Mod_DetallesVenta.Detalles_Venta.items():
                        if valor.idVenta == idVenta:
                            total += valor.subTotal
                    self.Ventas[idVenta] = Venta(idVenta,fecha_str,NIT,idEm,total)
                    input("Venta ingresada correctamente")
                else:
                    input("El ID de la venta ya existe")
            except ValueError:
                input("Ingrese un ID correcto")
class Mod_DetallesCompras:
    def __init__(self):
        self.Detalles_Compras = {}
    def AgregarCompras(self, idCompras):
        cantidad= 0
        while cantidad!=1972:
            if len(self.Detalles_Compras) == 0:
                idDetCom = 1
                break
            else:
                mayor = len(self.Detalles_Compras)
                idDetCom = mayor + 1
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del productos para ingresarlos al sistema: "))
                    if cantidad == 1972:
                        break
                    if cantidad<0:
                        input("Ingrese la cantidad en numeros enteros positivos.")
                    else:
                        break
                except ValueError:
                    input("Ingrese una cantidad correcta")
            while True:
                try:
                    idProd = int(input("Ingrese el ID del producto: "))
                    if idProd not in Mod_Producto.Productos:
                        input("No existe el producto con ese ID, por favor ingrese el producto antes")
                    else:
                        Mod_Producto.Productos[idProd].totalCompras = cantidad
                        while True:
                            try:
                                precioCompra = float(input("Ingrese el precio de compra del producto: "))
                                if precioCompra<0:
                                    input("Por favor ingresa un precio positivo")
                                else:
                                    break
                            except ValueError:
                                input("Ingrese un precio correcto")
                        break
                except ValueError:
                    input("Ingrese un ID correcto")
            subtotal = cantidad * precioCompra
            while True:
                fecha_str = input("Ingrese la fecha de caducidad del producto (dd/mm/yyyy): ")
                try:
                    fechaCaducidad = datetime.strptime(fecha_str, "%d/%m/%Y").date()
                    break
                except ValueError:
                    input("Formato de fecha inválido. Debe ser dd/mm/yy.")
            self.Detalles_Compras[idDetCom]= DetallesCompras(idDetCom,idCompras,cantidad,idProd,precioCompra,subtotal,fechaCaducidad)
            input("Venta agregada correctamente")

class Mod_Compras:
    def __init__(self):
        self.Compras = {}
    def agregarCompras(self):
        while True:
            try:
                idCom= int(input("Ingrese el ID de la compra: "))
                if idCom in self.Compras:
                    input("El ID de la compra ya existe")
                else:
                    break
            except ValueError:
                input("Ingrese un ID correcto")
        fechaCompra = date.today()
        fechaCompra_str = fechaCompra.strftime("%d/%m/%Y %H:%M:%S")
        cont = 0
        while True:
            try:
                if cont == 3:
                    break
                else:
                    idProv = int(input("Ingrese el ID del proveedor: "))
                    if idProv not in Mod_Proveedor.Proveedores:
                        input("No existe un proveedor con ese ID")
                        cont +=1
                    else:
                        cont = 0
                        while True:
                            try:
                                if cont == 3:
                                    break
                                idEmp = int(input("Ingrese el ID de la empresa: "))
                                if idEmp not in Mod_Empleado.Empleados:
                                    input("No existe un empleado con ese ID")
                                    cont += 1
                                else:
                                    total=0
                                    Mod_DetallesCompras.AgregarCompras(idCom)
                                    for clave, valor in Mod_DetallesCompras.Detalles_Compras.items():
                                        if valor.idCompra == idCom:
                                            total += valor.subtotal
                                    self.Compras[idCom] = Compras(idCom, fechaCompra_str, idProv, idEmp, total)
                                    input("Venta agregada correctamente")
                            except ValueError:
                                input("Ingrese un ID correcto")
                        break
            except ValueError:
                input("Ingrese un ID correcto")

Mod_Empleado = Mod_Empleado()
Mod_Categoria = Mod_Categoria()
Mod_Producto = Mod_Producto()
Mod_Proveedor = Mod_Proveedor()
Mod_Clientes = Mod_Clientes()
Mod_Venta = Mod_Venta()
Mod_DetallesVenta = Mod_DetallesVenta()
Mod_Compras = Mod_Compras()
Mod_DetallesCompras = Mod_DetallesCompras()

while True:
    print("MENU")
    print("1. Agregar Producto/Categoria/Cliente/Empleado/Proveedor")
    print("2. Realizar una Venta")
    print("3.Realizar una Compra")
    print("4. Mostrar Datos")
    print("5. SALIR")
    try:
        opcion = int(input("Selecciona una opcion: "))
        match opcion:
            case 1:
                while True:
                    print("\n1. Agregar Producto")
                    print("2. Agregar una Categoria")
                    print("3. Agregar Cliente")
                    print("4. Agregar Empleado")
                    print("5. Agregar Proveedor")
                    print("6. Regresar al menú principal")
                    try:
                        opcion1=int(input("Selecciona una opcion: "))
                        match opcion1:
                            case 1:
                                if len(Mod_Categoria.Categorias) == 0:
                                    input("No existen categorias, por favor agregue una categoria antes.")
                                else:
                                    print("\nAgregando un Producto")
                                    Mod_Producto.AgregarProducto()
                            case 2:
                                print("\nAgregando una Categoría.")
                                Mod_Categoria.AgregarCategoria()
                            case 3:
                                print("\nAgregando un Cliente")
                                Mod_Clientes.AgregarCliente()
                            case 4:
                                print("\nAgregando un Empleado")
                                Mod_Empleado.AgregarEmpleado()
                            case 5:
                                if len(Mod_Categoria.Categorias) == 0:
                                    input("No existen categorias, por favor agregue una categoria antes.")
                                else:
                                    print("\nAgregando un Proveedor")
                                    Mod_Proveedor.AgregarProveedor()
                            case 6:
                                input("Saliendo al menú principal...")
                                break
                            case _:
                                input("Ingrese una opcion correcta")
                    except ValueError:
                        input("Ingrese una opcion correcta")

            case 2:
                if len(Mod_Empleado.Empleados) == 0:
                    input("No hay empleados ingresados, por favor registre un empleado antes.")
                elif len(Mod_Clientes.Clientes) == 0:
                    input("No hay clientes ingresado, registre al cliente antes.")
                elif len(Mod_Producto.Productos) == 0:
                    input("No hay productos ingresados, registre al producto antes.")
                else:
                    print("\nAgregando una Venta:")
                    Mod_Venta.AgregarVenta()
            case 3:
                if len(Mod_Empleado.Empleados) == 0:
                    input("No hay empleados ingresados, por favor registre un empleado antes.")
                elif len(Mod_Proveedor.Proveedores) == 0:
                    input("No hay Proveedores ingresados, por favor registre al proveedor antes.")
                elif len(Mod_Producto.Productos) == 0:
                    input("No hay productos ingresados, por favor registre al producto antes.")
                else:
                    print("\nAgregando una Compra:")
                    Mod_Compras.agregarCompras()
            case 4:
                while True:
                    print("1. Mostrar Empleados.")
                    print("2. Mostrar Productos")
                    print("3. Mostrar Venta")
                    print("4. Mostrar Compra")
                    print("5. Mostrar Proveedor")
                    print("6. Mostrar Clientes")
                    print("7. Mostrar Categorias")
                    print("8. Saliendo al menú principal")
                    try:
                        opcion4=int(input("Selecciona una opcion: "))
                        match opcion4:
                            case 1:
                                Mod_Empleado.MostrarDatos()
                                input("")
                            case 2:
                                Mod_Producto.MostrarDatos()
                                input("")
                            case 3:
                                Mod_Venta.MostrarDatos()
                                input("")
                            case 4:
                                Mod_Compras.MostrarDatos()
                                input("")
                            case 5:
                                Mod_Proveedor.MostrarDatos()
                                input("")
                            case 6:
                                Mod_Clientes.MostrarDatos()
                            case 7:
                                Mod_Categorias.MostrarDatos()
                            case 8:
                                input("Saliendo al menú principal...")
                                break
                            case _:
                                pass
                    except ValueError:
                        input("Ingrese una opcion correcta")
            case 5:
                break
            case _:
                print("Selecciona una opcion válida")
    except ValueError:
        input("Ingrese una opcion correcta")