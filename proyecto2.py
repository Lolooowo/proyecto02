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

