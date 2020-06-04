from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models



class Tipousuario(models.Model):
    idtipousuario = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=70)

    class Meta:
        db_table = 'tipousuario'


class ManejadorUsuario(BaseUserManager):

    def create_user(self, usuario, password = None):
        if not usuario:
            raise ValueError('Usuarios deben tener un usuario valido.')
        
        usuario = self.model(usuario = usuario, )
        usuario.set_password(password)
        usuario.tipousuario = Tipousuario.objects.get(pk=1)
        usuario.save(using = self._db)
        return usuario
    
    def create_superuser(self, usuario, password, nombre, apellido_paterno, apellido_materno, correo):
        usuario = self.create_user(usuario, password=password)
        usuario.nombre = nombre
        usuario.apellido_paterno = apellido_paterno
        usuario.apellido_materno = apellido_materno
        usuario.correo = correo
        usuario.save(using = self._db)
        admin = Administrador(usuario=usuario)
        admin.save()
        return usuario


class Usuario(AbstractBaseUser):
    idusuario = models.AutoField(primary_key=True)
    tipousuario = models.ForeignKey(Tipousuario, models.DO_NOTHING, db_column='tipousuario')
    usuario = models.CharField(max_length=70, unique=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    correo = models.CharField(max_length=200)

    class Meta:
        db_table = 'usuario'

    objects = ManejadorUsuario()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['nombre','apellido_paterno','apellido_materno','correo']

    def get_full_name(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno
    
    def get_short_name(self):
        return self.nombre
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno

        


class Administrador(models.Model):
    idadministrador = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario')

    class Meta:
        db_table = 'administrador'


class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    rubro = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario')

    class Meta:
        db_table = 'cliente'


class Detallefactura(models.Model):
    iddetalle = models.AutoField(primary_key=True)
    total = models.BigIntegerField()
    factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='factura')
    serviciocomedor = models.ForeignKey('Serviciocomedor', models.DO_NOTHING, db_column='serviciocomedor', blank=True, null=True)
    huesped = models.ForeignKey('Huesped', models.DO_NOTHING, db_column='huesped', blank=True, null=True)

    class Meta:
        db_table = 'detallefactura'


class Detallepedido(models.Model):
    idedetalle = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor')
    pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='pedido')
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto')
    cantidad = models.IntegerField()
    total = models.BigIntegerField()

    class Meta:
        db_table = 'detallepedido'


class Empleado(models.Model):
    idempleado = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario')

    class Meta:
        db_table = 'empleado'


class Estadofactura(models.Model):
    idestado = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        db_table = 'estadofactura'


class Estadohabitacion(models.Model):
    idestado = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        db_table = 'estadohabitacion'


class Estadopedido(models.Model):
    idestado = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=90)

    class Meta:
        db_table = 'estadopedido'


class Factura(models.Model):
    idfactura = models.AutoField(primary_key=True)
    giro = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')
    estadofactura = models.ForeignKey(Estadofactura, models.DO_NOTHING, db_column='estadofactura')

    class Meta:
        db_table = 'factura'


class Habitacion(models.Model):
    idhabitacion = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    tipocama = models.CharField(max_length=70)
    accesorios = models.CharField(max_length=255)
    precio = models.IntegerField()
    administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador')
    estadohabitacion = models.ForeignKey(Estadohabitacion, models.DO_NOTHING, db_column='estadohabitacion')

    class Meta:
        db_table = 'habitacion'


class Huesped(models.Model):
    idhuesped = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidopaterno = models.CharField(max_length=100)
    apellidomaterno = models.CharField(max_length=100)
    rut = models.CharField(max_length=11)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')
    habitacion = models.ForeignKey(Habitacion, models.DO_NOTHING, db_column='habitacion', blank=True, null=True)
    fechadesde = models.DateField()
    fechahasta = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'huesped'


class Pedido(models.Model):
    idpedido = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado')
    observaciones = models.CharField(max_length=255)
    estadopedido = models.ForeignKey(Estadopedido, models.DO_NOTHING, db_column='estadopedido')
    fechapedido = models.DateField()

    class Meta:
        db_table = 'pedido'


class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=70)
    stock = models.BigIntegerField()
    administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador')
    tipoproducto = models.ForeignKey('Tipoproducto', models.DO_NOTHING, db_column='tipoproducto')
    precio = models.IntegerField()

    class Meta:
        db_table = 'producto'


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    rubro = models.CharField(max_length=100)
    telefono = models.IntegerField()
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    sitioweb = models.CharField(max_length=150, blank=True, null=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario')

    class Meta:
        db_table = 'proveedor'


class Recepcionproducto(models.Model):
    codigo = models.BigIntegerField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado')
    detallepedido = models.ForeignKey(Detallepedido, models.DO_NOTHING, db_column='detallepedido')
    fecharecepcion = models.DateField()

    class Meta:
        db_table = 'recepcionproducto'


class Serviciocomedor(models.Model):
    idservicio = models.AutoField(primary_key=True)
    plato = models.CharField(max_length=100)
    precio = models.IntegerField()
    tiposervicio = models.ForeignKey('Tiposervicio', models.DO_NOTHING, db_column='tiposervicio')
    administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador')

    class Meta:
        db_table = 'serviciocomedor'


class Tipoproducto(models.Model):
    idtipo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=90)

    class Meta:
        db_table = 'tipoproducto'


class Tiposervicio(models.Model):
    idtipo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80)

    class Meta:
        db_table = 'tiposervicio'


