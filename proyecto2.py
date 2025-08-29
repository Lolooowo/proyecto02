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
        self.Empleados = {}
        self.cargar_empleados()

    def cargar_empleados(self):
        try:
            with open("Empleados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        idEmp,Nombre,telefono,direccion,correo = linea.split(":")
                        self.Empleados[idEmp]={
                            Empleado(idEmp,Nombre, telefono,direccion,correo)
                        }
                print(f"Empleados importados correctamente desde el archivo {archivo.name}")
        except FileNotFoundError:
            print(f"No existe el archivo a importar, se creará uno al guardar")

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
                    self.Empleados[idE] = Empleado(idE, nombre, telefono, direccion, correo)
                    print(f"Empleado Ingresado correctamente")
                    break
                else:
                    print("El ID de empleado ya existe")
            except ValueError:
                input("Ingresa un ID correctamente, únicamente numeros")
class Mod_Categoria:
    def __init__(self):
        self.Categorias = {}
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
                    self.Categorias[idC] = Categoria(idC, nombre)
                    input("Categoria ingresada correctamente")
                    break
                else:
                    print("El ID de categoria ya existe")
            except ValueError:
                input("Ingrese unicamente números")
class Mod_Proveedor:
    def __init__(self):
        self.Proveedores = {}
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
                            self.Proveedores[idProv] = Proveedor(idProv, nombre, empresa, telefono, direccion, correo, idCat)
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
        while True:
            try:
                idP = int(input("Ingrese el ID del producto: "))
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
                fecha_str = input("Ingrese la fecha de caduccio del producto (dd/mm/yyyy): ")
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


