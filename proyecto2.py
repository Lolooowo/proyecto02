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
    def __init__(self, IDCliente, nombre, telefono, direccion, correo):
        self.IDCliente = IDCliente
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
                idE= int(input("Ingrese el ID del empleado: ")).strip()
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
                    self.Empleados[idP] = Empleado(idP, nombre, telefono, direccion, correo)
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
                        idCat = int(input("Ingrese el ID del categoria: ")).strip()
                        if idCat not in Mod_Categoria.Categorias:
                            input("Error: La categoría no existe. Agrega primero la categoría.")
                            break
                        else:
                            self.Proveedores[idProv] = Proveedor(idProv, empresa, telefono, direccion, correo, idCat)
                            input("Proveedor ingresado correctamente")
                            break
                else:
                    input("El ID del proveedor ya existe")
            except ValueError:
                input("Ingrese numeros enteros")



class Mod_Producto:
    def __init__(self):
        self.Productos = {}
    def AgregarProducto(self):
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
                            self.Productos[idP] = Producto(nombre, idCat, precio, totalCompras, totalVentas, stock)
                            input("Producto ingresado correctamente")
                            break
                else:
                    input("El ID del producto ya existe")
            except ValueError:
                input("Ingrese un ID correcto")






Mod_Empleado = Mod_Empleado()
Mod_Empleado.AgregarEmpleado()
