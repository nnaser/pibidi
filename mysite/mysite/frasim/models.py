from django.db import models

				
class Vendedor(models.Model):
	
	rut_vendedor=models.CharField(max_length=15, primary_key=True)
	nombre_vendedor=models.CharField(max_length=40)
	edad_vendedor=models.CharField(max_length=12)
	direccion_vendedor=models.CharField(max_length=40)
	telefono_vendedor=models.CharField(max_length=12)
	contrasena_vendedor=models.CharField(max_length=16)
	rol=models.CharField(max_length=16)

	def __unicode__(self):
		return self.nombre_vendedor
	   
	   
	   

class Material(models.Model):

	cod_material=models.AutoField( primary_key=True)
	id_marca=models.CharField(max_length=20)#ForeignKey(MARCA, related_name='MODELO')
	id_modelo=models.CharField(max_length=20)#ForeignKey(MODELO, related_name='MODELO')
	cod_tipo_mat=models.CharField(max_length=20)#ForeignKey(TIPO_MATERIAL, related_name='TIPO_MATERIAL')
	nombre_material=models.CharField(max_length=40)
	precio_material=models.DecimalField(max_digits=10,decimal_places=2)
	cantidad_material=models.PositiveSmallIntegerField()

	def __unicode__(self):
		return self.nombre_material
		
		
class Compatibilidad(models.Model):

	cod_mat=models.CharField(max_length=20)
	cod_mat_2=models.CharField(max_length=20)
	id_marca=models.CharField(max_length=20)
	id_modelo=models.CharField(max_length=20)
	cod_tipo_mat=models.CharField(max_length=20)
	nombre_material=models.CharField(max_length=40)
	
	def __unicode__(self):
		return self.cod_mat_2	
		

class Productos(models.Model):

	codigo_material=models.AutoField( primary_key=True)
	marca=models.CharField(max_length=20)#ForeignKey(MARCA, related_name='MODELO')
	modelo=models.CharField(max_length=20)#ForeignKey(MODELO, related_name='MODELO')
	codigo_tipo_mat=models.CharField(max_length=20)#ForeignKey(TIPO_MATERIAL, related_name='TIPO_MATERIAL')
	nombre=models.CharField(max_length=40)
	precio=models.DecimalField(max_digits=6,decimal_places=2)
	cantidad=models.PositiveSmallIntegerField()

	def __unicode__(self):
		return self.nombre
			


class Proveedor(models.Model):
	rut_proveedor=models.CharField(max_length=15, primary_key=True)
	nombre_proveedor=models.CharField(max_length=40)
	direc_proveedor=models.CharField(max_length=40)
	fono_proveedor=models.CharField(max_length=12)
	movil_proveedor=models.CharField(max_length=12)
	correo_proveedor=models.CharField(max_length=30)

	def __unicode__(self):
		return self.nombre_proveedor
		
		
		
class Area(models.Model):

	cod_area=models.AutoField('COD_AREA', primary_key=True)
	cod_bodega=models.CharField(max_length=20)#ForeignKey('BODEGA')
	pasillo=models.CharField(max_length=5)
	estante=models.CharField(max_length=5)
	gaveta=models.CharField(max_length=5)

	def __unicode__(self):
		return str(self.cod_area)

class Bodega(models.Model):

	cod_bodega=models.AutoField('COD_BODEGA', primary_key=True)
	direccion=models.CharField(max_length=40)

	def __unicode__(self):
		return self.direccion
		
		

		
class Cotizacion(models.Model):

	nro_cotizacion=models.AutoField('NRO_COTIZACION', primary_key=True)
	rut_vendedor=models.CharField(max_length=10)
	fecha_cotizacion=models.CharField(max_length=10)
	hora_cotizacion=models.CharField(max_length=10)

	def __unicode__(self):
		return str(self.nro_cotizacion)
		

class Detalle_cotizacion(models.Model):	

	nro_cotizacion=models.CharField(max_length=20)
	cod_mat=models.CharField(max_length=20)
	id_marca=models.CharField(max_length=20)#ForeignKey(MARCA, related_name='MODELO')
	id_modelo=models.CharField(max_length=20)#ForeignKey(MODELO, related_name='MODELO')
	cod_tipo_mat=models.CharField(max_length=20)#ForeignKey(TIPO_MATERIAL, related_name='TIPO_MATERIAL')
	nombre_material=models.CharField(max_length=40)
	precio_material=models.DecimalField(max_digits=10,decimal_places=2)
	cantidad_material=models.PositiveSmallIntegerField()
	def __unicode__(self):
		return str(self.nro_cotizacion)
		
		
class Detalle_cot(models.Model):

	cod_material=models.CharField(max_length=20)
	nro_cotizacion=models.ForeignKey('COTIZACION')
	cant_mat_cotizado=models.PositiveSmallIntegerField()

class Tipo_material(models.Model):

	codigo_tipo_material=models.AutoField('COD_TIPO_MAT', primary_key=True)
	nombre_tipo_material=models.CharField(max_length=20)
	cod_bodega=models.CharField(max_length=20)#ForeignKey('BODEGA')
	cod_area=models.CharField(max_length=20)#ForeignKey('AREA')

	def __unicode__(self):
		return str(self.cod_tipo_mat)
		
		
		
class Venta(models.Model):

	nro_venta=models.AutoField('NRO_VENTA', primary_key=True)
	rut_vendedor=models.CharField(max_length=20)
	fecha_venta=models.CharField(max_length=20)
	hora_venta=models.CharField(max_length=100)

	def __unicode__(self):
		return str(self.nro_venta)
		
		
class Detalle_venta(models.Model):	

	nro_venta=models.CharField(max_length=20)
	cod_mat=models.CharField(max_length=20)
	id_marca=models.CharField(max_length=20)#ForeignKey(MARCA, related_name='MODELO')
	id_modelo=models.CharField(max_length=20)#ForeignKey(MODELO, related_name='MODELO')
	cod_tipo_mat=models.CharField(max_length=20)#ForeignKey(TIPO_MATERIAL, related_name='TIPO_MATERIAL')
	nombre_material=models.CharField(max_length=40)
	precio_material=models.DecimalField(max_digits=10,decimal_places=2)
	cantidad_material=models.PositiveSmallIntegerField()
	def __unicode__(self):
		return str(self.nro_venta)
		
		
class Detalle_despacho(models.Model):	

	nro_despacho=models.CharField(max_length=20)
	cod_mat=models.CharField(max_length=20)
	id_marca=models.CharField(max_length=20)#ForeignKey(MARCA, related_name='MODELO')
	id_modelo=models.CharField(max_length=20)#ForeignKey(MODELO, related_name='MODELO')
	cod_tipo_mat=models.CharField(max_length=20)#ForeignKey(TIPO_MATERIAL, related_name='TIPO_MATERIAL')
	nombre_material=models.CharField(max_length=40)
	precio_material=models.DecimalField(max_digits=10,decimal_places=2)
	cantidad_material=models.PositiveSmallIntegerField()
	def __unicode__(self):
		return str(self.nro_despacho)		
		
			
		
		
class Orden_de_compra(models.Model):

	num_oc=models.AutoField('NUM_OC', primary_key=True)
	rut_proveedor=models.CharField(max_length=10)
	fecha_oc=models.CharField(max_length=10)
	hora_oc=models.CharField(max_length=10)
	direc_emision=models.CharField(max_length=40)
	condicion_pago=models.CharField(max_length=25)

	def __unicode__(self):
		return str(self.num_oc)
		
		
class Detalle_oc(models.Model):	

	nro_oc=models.CharField(max_length=20)
	cod_mat=models.CharField(max_length=20)
	id_marca=models.CharField(max_length=20)#ForeignKey(MARCA, related_name='MODELO')
	id_modelo=models.CharField(max_length=20)#ForeignKey(MODELO, related_name='MODELO')
	cod_tipo_mat=models.CharField(max_length=20)#ForeignKey(TIPO_MATERIAL, related_name='TIPO_MATERIAL')
	nombre_material=models.CharField(max_length=40)
	precio_material=models.DecimalField(max_digits=10,decimal_places=2)
	cantidad_material=models.PositiveSmallIntegerField()
	def __unicode__(self):
		return str(self.nro_oc)			
		
		
		
class Despacho_material(models.Model):

	rut_proveedor=models.CharField(max_length=10)
	cod_despacho=models.AutoField('COD_DESPACHO', primary_key=True)
	fecha_despacho=models.CharField(max_length=10)
	hora_despacho=models.CharField(max_length=10)

	def __unicode__(self):
		return str(self.cod_despacho)
		
		
		
class Kits(models.Model):
	
	cod_kits=models.AutoField( primary_key=True)	
	nombre_kits=models.CharField(max_length=20)
	precio_kits=models.DecimalField(max_digits=10,decimal_places=2)
	

	def __unicode__(self):
		return str(self.cod_kits)	



class Detalle_kits(models.Model):	

	cod_kits=models.CharField(max_length=20)
	cod_mat=models.CharField(max_length=20)
	id_marca=models.CharField(max_length=20)#ForeignKey(MARCA, related_name='MODELO')
	id_modelo=models.CharField(max_length=20)#ForeignKey(MODELO, related_name='MODELO')
	cod_tipo_mat=models.CharField(max_length=20)#ForeignKey(TIPO_MATERIAL, related_name='TIPO_MATERIAL')
	nombre_material=models.CharField(max_length=40)
	precio_material=models.DecimalField(max_digits=10,decimal_places=2)
	cantidad_material=models.PositiveSmallIntegerField()
	def __unicode__(self):
		return str(self.cod_kits)		
