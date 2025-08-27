from datetime import date

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
    def __init__(self, IDProducto, nombre, IDCategoria, precio, totalVentas, totalCompras, stock):
        self.IDProducto = IDProducto
        self.nombre = nombre
        self.IDCategoria = IDCategoria
        self.precio = precio
        self.totalVentas = totalVentas
        self.totalCompras = totalCompras
        self.stock = stock
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
                            while True:
                                try:
                                    totalCompras = int(input("Ingrese los productos comprados: "))
                                    break
                                except ValueError:
                                    print("Ingrese numeros enteros")
                            totalVentas = 0
                            stock = totalCompras - totalVentas
                            self.Productos[idP] = Producto(idP,nombre, idCat,precio,totalCompras,totalVentas,stock)
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
                                    break
                        except ValueError:
                            input("Ingrese una cantidad correcta")
                    precio = producto.precio
                    subTotal = precio * cantidad
                    self.Detalles_Venta[idDet]: DetallesVenta(idDet,idVenta,cantidad,idProd,precio, subTotal)
                    input("Detalle venta agregada correcta")

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
                    while True:
                        try:
                            Mod_DetallesVenta.AgregarDetallesVenta(idVenta)
                        except ValueError:
                            input("Ingrese un ID correcto")
                    self.Ventas[idVenta] = Venta(idVenta,fecha_str,NIT,idEm,total)
                    input("Venta ingresada correctamente")
                else:
                    input("El ID de la venta ya existe")
            except ValueError:
                input("Ingrese un ID correcto")




Mod_Empleado = Mod_Empleado()
Mod_Categoria = Mod_Categoria()
Mod_Producto = Mod_Producto()
Mod_Proveedor = Mod_Proveedor()
Mod_Clientes = Mod_Clientes()
Mod_Venta = Mod_Venta()
Mod_DetallesVenta = Mod_DetallesVenta()
Mod_Venta.AgregarVenta()
Mod_Producto.AgregarProducto()
Mod_Empleado.AgregarEmpleado()
Mod_Producto.AgregarProducto()
Mod_Proveedor.AgregarProveedor()
