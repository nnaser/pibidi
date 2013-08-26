from django import *

from django.core.exceptions import ValidationError


class loginform(forms.Form):
		TITLE_CHOICES = (
		('a', 'Administrador'),
		('v', 'Vendedor'),
		)
		nombre = forms.RegexField(widget=forms.TextInput(attrs={ 'required': 'true' }),regex= "^[a-zA-Z ]*$",error_messages={'required': 'Por favor ingresar nombre', 'invalid': 'Ingresar un nombre correcto'},max_length='16')
		contrasena= forms.CharField(widget=forms.PasswordInput(render_value=False,attrs={ 'required': 'true' }),error_messages={'required': 'Por favor ingresar contrasena'})
		opcion = forms.ChoiceField(widget = forms.Select(), choices = ([('admin','Administrador'), ('vendedor','Vendedor') ]))
	
		
		def clean(self):
				
				return self.cleaned_data
		def clean_nombre(self):
			a=self.cleaned_data
			rut=a.get('nombre')
			if len(rut)<4 or len(rut)>16:
				raise ValidationError('Por favor ingrese un nombre de mas de 4 caracteres')
			return rut		
		def clean_contrasena(self):
			a=self.cleaned_data
			pas=a.get('contrasena')
			if len(pas)<4 or len(pas)>16:
				raise ValidationError('Por favor ingrese una contrasena valida')

			return pas
			
				
				

				
				
class materialform(forms.Form):
		TITLE_CHOICES = (
		('a', 'Administrador'),
		('v', 'Vendedor'),
		)
		marca_material=forms.RegexField(widget=forms.TextInput(attrs={ 'required': 'true' }),regex= "^[a-zA-Z ]*$",error_messages={'required': 'Por favor ingresar una marca', 'invalid': 'Ingresar una marca correcta'},max_length='20')#CharField(widget=forms.TextInput())
		modelo_material=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
		
		nombre_material=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
		precio_material=forms.IntegerField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={ 'invalid': 'Ingresar un precio valido'})	
		cantidad_material=forms.IntegerField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={ 'invalid': 'Ingresar una cantidad valida'})
		
		def clean(self):
				
				return self.cleaned_data
		def clean_marca_material(self):
			a=self.cleaned_data
			marca=a.get('marca_material')
			if len(marca)<4:
				raise ValidationError('Por favor ingrese una marca de mas de 4 caracteres')
			return marca
		def clean_modelo_material(self):
			a=self.cleaned_data
			marca=a.get('modelo_material')
			if len(marca)<2:
				raise ValidationError('Por favor ingrese un modelo de mas de 2 caracteres')
			return marca
		def clean_precio_material(self):
			a=self.cleaned_data
			b=a.get('precio_material')
			if b<1:
				raise ValidationError('Precio negativo, por favor ingrese un valor positivo')
			return b
		def clean_cantidad_material(self):
			a=self.cleaned_data
			b=a.get('cantidad_material')
			if b<1:
				raise ValidationError('Cantidad negativa, por favor ingrese un valor positivo')
			return b
				

class proveedorform(forms.Form):
		rut_proveedor=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
		nombre_proveedor=forms.RegexField(widget=forms.TextInput(attrs={ 'required': 'true' }),regex= "^[a-zA-Z ]*$",error_messages={ 'invalid': 'Ingresar un nombre valido'},max_length='40')
		direc_proveedor=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
		fono_proveedor=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={'invalid': 'Ingresar un telefono valido'})
		movil_proveedor=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={'invalid': 'Ingresar un nro de celular valido'})
		correo_proveedor=forms.EmailField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={ 'invalid': 'Ingresar un email valido'})
		
		def clean(self):
				
				return self.cleaned_data

		def clean_rut_proveedor(self):
			a=self.cleaned_data
			rut=a.get('rut_proveedor')
			c=['1','2','3','4','5','6','7','8','9','0','k']
			if '-' in rut:
				lista=rut.split('-')	
				if len(lista[0])<7 or lista[1] not in c or len(lista[0])>8:
					raise ValidationError('Rut invalido')
				try:
					h=int(lista[0])
				except:
					raise ValidationError('Rut invalido')
			else:
				if len(rut)>9 or len(rut)<8:
					raise ValidationError('Rut invalido')
				if rut[-1]!='k':
					try:
						int (rut)
					except:
						raise ValidationError('Rut invalido')
			return rut
			
		def clean_nombre_proveedor(self):
			a=self.cleaned_data
			rut=a.get('nombre_proveedor')
			if len(rut)<4 or len(rut)>30:
				raise ValidationError('Nombre invalido, por favor ingrese un nombre entre 4 a 30 caracteres')
			return rut		
		def clean_direc_proveedor(self):
			a=self.cleaned_data
			rut=a.get('direc_proveedor')
			if len(rut)<4 or len(rut)>30:
				raise ValidationError('Direccion invalida, por favor ingrese una direccion entre 4 a 30 caracteres')
			return rut	
		def clean_fono_proveedor(self):
			a=self.cleaned_data
			b=a.get('fono_proveedor')
			if '-' in b:
				lista=b.split('-')
				if len(lista[1])<7:
					raise ValidationError('telefono invalido, por favor ingrese un telefono entre 7 a 8 caracteres')
				try:
					int(lista[0])
					int(lista[1])
				except:
					raise ValidationError('telefono invalido')
			else:
				try:
					int(b)
				except:
					raise ValidationError('telefono invalido')
			return b

		def clean_movil_proveedor(self):
			a=self.cleaned_data
			b=a.get('movil_proveedor')
			if '-' in b:
				lista=b.split('-')
				if len(lista[1])<8:
					raise ValidationError('telefono invalido, por favor ingrese un telefono entre 8 a 9 caracteres')
				try:
					int(lista[0])
					int(lista[1])
				except:
					raise ValidationError('telefono invalido')
			else:
				try:
					int(b)
				except:
					raise ValidationError('telefono invalido, por favor ingrese solo numeros')
			return b
				
				
				
class vendedorform(forms.Form):
	rut_vendedor=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
	nombre_vendedor=forms.RegexField(widget=forms.TextInput(attrs={ 'required': 'true' }),regex= "^[a-zA-Z ]*$",error_messages={'required': 'Por favor ingresar nombre', 'invalid': 'Ingresar un nombre valido'},max_length='40')
	direccion_vendedor=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={'required': 'Por favor ingresar una direccion'})
	contrasena_vendedor=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={'required': 'Por favor ingresar contrasena'})
	telefono_vendedor=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={'required': 'Por favor ingresar un telefono', 'invalid': 'Ingresar un telefono valido'})
	edad_vendedor=forms.IntegerField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={ 'invalid': 'Ingresar una edad valida'})
	opcion = forms.ChoiceField(widget = forms.Select(), choices = ([('admin','Administrador'), ('vendedor','Vendedor') ]))

	def clean(self):

		return self.cleaned_data

	def clean_rut_vendedor(self):
		a=self.cleaned_data
		rut=a.get('rut_vendedor')
		c=['1','2','3','4','5','6','7','8','9','0','k']
		if '-' in rut:
			lista=rut.split('-')	
			if len(lista[0])<7 or lista[1] not in c or len(lista[0])>8:
				raise ValidationError('Rut invalido')
			try:
				h=int(lista[0])
			except:
				raise ValidationError('Rut invalido')
		else:
			if len(rut)>9 or len(rut)<8:
				raise ValidationError('Rut invalido')
			if rut[-1]!='k':
				try:
					int (rut)
				except:
					raise ValidationError('Rut invalido')
		return rut

	def clean_nombre_vendedor(self):
		a=self.cleaned_data
		rut=a.get('nombre_vendedor')
		if len(rut)<4 or len(rut)>20:
			raise ValidationError('Nombre invalido, por favor ingrese un nombre entre 4 a 20 caracteres')
		return rut
	def clean_direccion_vendedor(self):
		a=self.cleaned_data
		rut=a.get('direccion_vendedor')
		if len(rut)<4 or len(rut)>30:
			raise ValidationError('Direccion invalida, por favor ingrese una direccion entre 4 a 30 caracteres')
		return rut	
	def clean_contrasena_vendedor(self):
		a=self.cleaned_data
		pas=a.get('contrasena_vendedor')
		if len(pas)<4 or len(pas)>16:
			raise ValidationError('Contrasena invalida, por favor ingrese una contrasena entre 4 a 16 caracteres')

		return pas
	def clean_telefono_vendedor(self):
		a=self.cleaned_data
		b=a.get('telefono_vendedor')
		if '-' in b:
			lista=b.split('-')
			if len(lista[1])<7:
				raise ValidationError('telefono invalido, por favor ingrese un telefono entre 7 a 8 caracteres')
			try:
				int(lista[0])
				int(lista[1])
			except:
				raise ValidationError('telefono invalido')
		else:
			try:
				int(b)
			except:
				raise ValidationError('telefono invalido')
		return b
	def clean_edad_vendedor(self):
		a=self.cleaned_data
		b=a.get('edad_vendedor')
		if b<1:
			raise ValidationError('Cantidad negativa, por favor ingrese un valor positivo')
		return b	
				

class bodegaform(forms.Form):
		
		
		direccion=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
		
		def clean(self):
				
				return self.cleaned_data
		def clean_direccion(self):
			a=self.cleaned_data
			rut=a.get('direccion')
			if len(rut)<8 or len(rut)>40:
				raise ValidationError('direccion invalida, por favor ingrese una direccion entre 8 a 40 caracteres')
			return rut
				
				
class areaform(forms.Form):
		
		
		pasillo=forms.IntegerField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={ 'invalid': 'Ingresar un numero entero positivo para el pasillo'})
		estante=forms.IntegerField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={ 'invalid': 'Ingresar un numero entero positivo para el estante'})
		gaveta=forms.IntegerField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={ 'invalid': 'Ingresar un numero entero positivo para la gaveta'})
		
		def clean(self):
				
				return self.cleaned_data
		def clean_pasillo(self):
			a=self.cleaned_data
			b=a.get('pasillo')
			if b<1:
				raise ValidationError('Cantidad negativa, por favor ingrese un valor positivo')
			return b	
		def clean_estante(self):
			a=self.cleaned_data
			b=a.get('estante')
			if b<1:
				raise ValidationError('Cantidad negativa, por favor ingrese un valor positivo')
			return b
		def clean_gaveta(self):
			a=self.cleaned_data
			b=a.get('gaveta')
			if b<1:
				raise ValidationError('Cantidad negativa, por favor ingrese un valor positivo')
			return b		
				
				
class grupoform(forms.Form):


	nombre_tipo_material=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={ 'invalid': 'Ingresar un numero entero positivo para la gaveta'})
	

	def clean(self):

		return self.cleaned_data
	def clean_nombre_tipo_material(self):
		a=self.cleaned_data
		rut=a.get('nombre_tipo_material')
		if len(rut)<4 or len(rut)>16:
			raise ValidationError('nombre invalido, por favor ingrese un nombre entre 4 a 16 caracteres')
		return rut
				
				

class cotizarform(forms.Form):
	

	rut_vendedor=forms.CharField(widget=forms.TextInput())
	
	
	def clean(self):
				
		return self.cleaned_data
				
				
class buscaform(forms.Form):
		
		nombre=forms.CharField(widget=forms.TextInput())
		
		def clean(self):
				
				return self.cleaned_data
				
				
class ventasform(forms.Form):
	

	rut_vendedor=forms.CharField(widget=forms.TextInput())
	

	
	def clean(self):
				
		return self.cleaned_data
		
		
		
class ordenform(forms.Form):
	
	direc_emision=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
	condicion_pago=forms.ChoiceField(widget = forms.Select(), choices = ([('Cuotas','Cuotas'), ('Contado','Contado') ]))
	
	def clean(self):
				
		return self.cleaned_data
	def clean_direc_emision(self):
		a=self.cleaned_data
		rut=a.get('direc_emision')
		if len(rut)<8 or len(rut)>40:
			raise ValidationError('direccion invalida, por favor ingrese una direccion entre 8 a 40 caracteres')
		return rut	
		
		
class despachoform(forms.Form):
	
	
	
	
	def clean(self):
				
		return self.cleaned_data
		
		
		
		
class kitsform(forms.Form):
	
	nombre_kits=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
	precio_kits=forms.IntegerField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={ 'invalid': 'Ingresar un precio valido'})

	def clean(self):

		return self.cleaned_data

	def clean_nombre_kits(self):
		a=self.cleaned_data
		marca=a.get('nombre_kits')
		if len(marca)<8:
			raise ValidationError('Por favor ingrese un modelo de mas de 8 caracteres')
		return marca
	def clean_precio_kits(self):
		a=self.cleaned_data
		b=a.get('precio_kits')
		if b<1:
			raise ValidationError('Precio negativo, por favor ingrese un valor positivo')
		return b