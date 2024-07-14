from django.contrib.auth.models import User # Importo para extender cliente con user
from django.db import models

# Create your models here.

class CondicionIva(models.Model):
    id_condicion_iva = models.AutoField(primary_key=True, verbose_name='ID de Condición')
    condicion_iva = models.CharField(max_length=100, verbose_name='Condición de IVA')
    
    class Meta:
        db_table = 'condicion_iva'
    
    def __str__(self):
        return self.condicion_iva


class Clientes(User):
    telefono = models.CharField(max_length=15, verbose_name='Teléfono') # Telefono del cliente de tabla propia de clientes
    direccion = models.CharField(max_length=255, blank=True, verbose_name='Dirección') # Direccion del cliente (no obligatoria)
    id_condicion_iva = models.ForeignKey(CondicionIva, on_delete=models.PROTECT, related_name='clientes', verbose_name='ID de Condicion de IVA', default=1)
    #foto_cliente = models.ImageField(upload_to='static/img/imagenes_clientes/', default='static/img/imagenes_clientes/default.png', verbose_name='Foto del Cliente') # Si esta vacia se cargara con un emoji
    foto_cliente = models.ImageField(upload_to='imagenes_clientes/', default='imagenes_clientes/default.png', verbose_name='Foto del Cliente') # Si esta vacia se cargara con un emoji
    
    class Meta:
        db_table = 'clientes'
    
    def __str__(self):
        return self.username

class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True, verbose_name='ID del Producto', default=1)
    producto = models.CharField(max_length=100, verbose_name='Producto') # Nombre del producto
    descripcion = models.CharField(max_length=250, verbose_name='Descripción') # Descripcion del producto
    vegano = models.BooleanField(verbose_name='Producto Vegano', default=False)
    stock = models.PositiveBigIntegerField(verbose_name='Stock disponible', default=0)
    precio = models.FloatField(verbose_name='Precio') # Precio del producto
    imagen = models.ImageField(upload_to='imagenes_productos/', default='imagenes_productos/default.jpg', verbose_name='Imagen del Producto') # imagen del producto
    
    class Meta:
        db_table = 'productos'

class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True, verbose_name='ID de Pedido', default=1)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT, verbose_name='ID del Cliente')
    fecha_pedido = models.DateTimeField(verbose_name='Fecha Pedido') # Fecha del pedido
    fecha_despacho = models.DateTimeField(verbose_name='Fecha Despacho', null=True, blank=True) # Fecha de despachado el pedido
    estado_pedido = models.CharField(max_length=50, verbose_name='Estado de Pedido') # Estado del pedido "En Proceso" o "Entregado"
    costo_total = models.FloatField(verbose_name='Costo total del Pedido') # Costo total del pedido
    
    class Meta:
        db_table = 'pedidos'

class DetallePedido(models.Model):
    id_detalle_pedido = models.AutoField(primary_key=True, verbose_name='ID del Detalle del Pedido', default=1)
    id_pedido = models.ForeignKey(Pedidos, on_delete=models.PROTECT, verbose_name='ID del Pedido') # Id relacionda con Pedidos
    id_producto = models.ForeignKey(Productos, on_delete=models.PROTECT, verbose_name='ID del Producto') # Id relacionada con Productos
    cantidad = models.PositiveBigIntegerField(verbose_name='Cantidad') # Cantidad del producto
    precio_unitario = models.FloatField(verbose_name='Precio Unitario') # Precio uni del producto
    
    class Meta:
        db_table = 'detalle_pedido'

class FormularioContacto(models.Model):
    id_contacto = models.AutoField(primary_key=True, verbose_name='ID de Contacto')
    nombre = models.CharField(max_length=50, verbose_name='Nombre') # Nombre de quien usa el formulario
    email = models.EmailField(max_length=254, verbose_name='Email') # email de quien usa el formulario
    mensaje = models.TextField(verbose_name='Mensaje') # Mensaje enviado en el formulario
    fecha = models.DateTimeField(verbose_name='Fecha del mensaje') # Fecha que se envio el mensaje
    
    class Meta:
        db_table = 'formulario_contacto'


class Helado (models.Model):
    sabor = models.CharField(max_length=50)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.sabor