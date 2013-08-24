from django import *

from django.core.exceptions import ValidationError


# Support for HTML5 "required" attritbute
old_build_attrs = forms.Widget.build_attrs
def build_attrs(self, extra_attrs=None, **kwargs):
    attrs = old_build_attrs(self, extra_attrs, **kwargs)
    if self.is_required:
        attrs["required"] = "required"
    return attrs
 
forms.Widget.build_attrs = build_attrs

class loginform(forms.Form):
		TITLE_CHOICES = (
		('a', 'Administrador'),
		('v', 'Vendedor'),
		)
		nombre = forms.RegexField(regex= "^[a-zA-Z ]*$",error_messages={'required': 'Por favor ingresar nombre', 'invalid': 'Ingresar un nombre correcto'},max_length='100')
		contrasena= forms.CharField(widget=forms.PasswordInput(render_value=False),error_messages={'required': 'Por favor ingresar contrasena'})
		opcion = forms.ChoiceField(widget = forms.Select(), choices = ([('admin','Administrador'), ('vendedor','Vendedor') ]))
	
		
		def clean(self):
				
				return self.cleaned_data
				
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
		marca_material=forms.RegexField(regex= "^[a-zA-Z ]*$",error_messages={'required': 'Por favor ingresar una marca', 'invalid': 'Ingresar una marca correcta'},max_length='100')#CharField(widget=forms.TextInput())
		modelo_material=forms.CharField(widget=forms.TextInput(),error_messages={'required': 'Por favor ingresar un modelo'})
		
		nombre_material=forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={'required': 'Por favor ingresar un nombre'})
		precio_material=forms.IntegerField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={'required': 'Por favor ingresar precio', 'invalid': 'Ingresar un precio valido'})	
		cantidad_material=forms.IntegerField(widget=forms.TextInput(attrs={ 'required': 'true' }),error_messages={'required': 'Por favor ingresar cantidad', 'invalid': 'Ingresar una cantidad valida'})
		
		def clean(self):
				
				return self.cleaned_data
		

class proveedorform(forms.Form):
		rut_proveedor=forms.CharField(widget=forms.TextInput(),error_messages={'required': 'Por favor ingresar rut'})
		nombre_proveedor=forms.RegexField(regex= "^[a-zA-Z ]*$",error_messages={'required': 'Por favor ingresar nombre', 'invalid': 'Ingresar un nombre valido'},max_length='40')
		direc_proveedor=forms.CharField(widget=forms.TextInput(),error_messages={'required': 'Por favor ingresar una direccion'})
		fono_proveedor=forms.IntegerField(error_messages={'required': 'Por favor ingresar un telefono', 'invalid': 'Ingresar un telefono valido'})
		movil_proveedor=forms.IntegerField(error_messages={'required': 'Por favor ingresar nro de celular', 'invalid': 'Ingresar un nro de celular valido'})
		correo_proveedor=forms.EmailField(widget=forms.TextInput(),error_messages={'required': 'Por favor ingresar email', 'invalid': 'Ingresar un email valido'})
		
		def clean(self):
				
				return self.cleaned_data

		def clean_rut_proveedor(self):
			a=self.cleaned_data
			rut=a.get('rut_proveedor')
			lista=rut.split('-')
			c=['1','2','3','4','5','6','7','8','9','0','k']
			if len(lista[0])<7 or lista[1] not in c:
				raise ValidationError('Rut invalido')
			return rut
			
				
				
				
class vendedorform(forms.Form):
	
	rut_vendedor=forms.CharField(widget=forms.TextInput(),error_messages={'required': 'Por favor ingresar rut'})
	nombre_vendedor=forms.RegexField(regex= "^[a-zA-Z ]*$",error_messages={'required': 'Por favor ingresar nombre', 'invalid': 'Ingresar un nombre valido'},max_length='40')
	direccion_vendedor=forms.CharField(widget=forms.TextInput(),error_messages={'required': 'Por favor ingresar una direccion'})
	contrasena_vendedor=forms.CharField(widget=forms.TextInput(),error_messages={'required': 'Por favor ingresar contrasena'})
	telefono_vendedor=forms.IntegerField(error_messages={'required': 'Por favor ingresar un telefono', 'invalid': 'Ingresar un telefono valido'})
	edad_vendedor=forms.IntegerField(error_messages={'required': 'Por favor ingresar una edad', 'invalid': 'Ingresar una edad valida'})
	opcion = forms.ChoiceField(widget = forms.Select(), choices = ([('admin','Administrador'), ('vendedor','Vendedor') ]))

	def clean(self):

		return self.cleaned_data

	def clean_rut_vendedor(self):
		a=self.cleaned_data
		rut=a.get('rut_vendedor')
		lista=rut.split('-')
		c=['1','2','3','4','5','6','7','8','9','0','k']
		d=['1','2','3','4','5','6','7','8','9','0']
		if len(lista[0])<7 :
			raise ValidationError('Rut invalido')
		for b in d:

			if lista[0]!=d[b] and b<len(d):
				raise ValidationError('Rut invalido')
		for i in c:	
			if lista[1]!=c[i] and i<len(c):
				raise ValidationError('Rut invalido')

		return rut

class bodegaform(forms.Form):
		
		direccion=forms.CharField(widget=forms.TextInput())
		
		def clean(self):
				
				return self.cleaned_data
				
				
class areaform(forms.Form):
		
		cod_bodega=forms.CharField(widget=forms.TextInput())
		pasillo=forms.CharField(widget=forms.TextInput())
		estante=forms.CharField(widget=forms.TextInput())
		gaveta=forms.CharField(widget=forms.TextInput())
		
		def clean(self):
				
				return self.cleaned_data
				
				
class grupoform(forms.Form):


	nombre_tipo_material=forms.CharField(widget=forms.TextInput())
	cod_bodega=forms.CharField(widget=forms.TextInput())
	cod_area=forms.CharField(widget=forms.TextInput())

	def clean(self):

		return self.cleaned_data
				
				

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
	
	
	
	direc_emision=forms.CharField(widget=forms.TextInput())
	condicion_pago=forms.ChoiceField(widget = forms.Select(), choices = ([('Cuotas','Cuotas'), ('Contado','Contado') ]))
	
	def clean(self):
				
		return self.cleaned_data
		
		
class despachoform(forms.Form):
	
	
	
	
	def clean(self):
				
		return self.cleaned_data
		
		
		
		
class kitsform(forms.Form):
	
	nombre_kits=forms.CharField(widget=forms.TextInput())
	precio_kits=forms.CharField(widget=forms.TextInput())

	def clean(self):

		return self.cleaned_data