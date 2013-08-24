from django import *

from django.core.exceptions import ValidationError


class loginform(forms.Form):
		TITLE_CHOICES = (
		('a', 'Administrador'),
		('v', 'Vendedor'),
		)
		nombre = forms.RegexField(regex= "^[a-zA-Z ]*$",error_messages={'required': 'Por favor ingresar nombre', 'invalid': 'Ingresar un nombre correcto'},max_length='100')
		contrasena= forms.CharField(widget=forms.PasswordInput(render_value=False))
		opcion = forms.ChoiceField(widget = forms.Select(), choices = ([('admin','Administrador'), ('vendedor','Vendedor') ]))
	
		
		def clean(self):
				
				return self.cleaned_data
				
		#def clean_contrasena(self):
		#	a=self.cleaned_data
		#	pas=a.get('contrasena')
		#	if len(pas)<4:
#				raise ValidationError('shiiiiit')

#			return pas
			
			
				
				

				
				
class materialform(forms.Form):
		TITLE_CHOICES = (
		('a', 'Administrador'),
		('v', 'Vendedor'),
		)
		marca_material=forms.CharField(widget=forms.TextInput())
		modelo_material=forms.CharField(widget=forms.TextInput())
		
		nombre_material=forms.CharField(widget=forms.TextInput())
		precio_material=forms.CharField(widget=forms.TextInput())
		
		cantidad_material=forms.CharField(widget=forms.TextInput())
		
		def clean(self):
				
				return self.cleaned_data
				

class proveedorform(forms.Form):
		rut_proveedor=forms.CharField(widget=forms.TextInput())
		nombre_proveedor=forms.CharField(widget=forms.TextInput())
		direc_proveedor=forms.CharField(widget=forms.TextInput())
		fono_proveedor=forms.CharField(widget=forms.TextInput())
		movil_proveedor=forms.CharField(widget=forms.TextInput())
		correo_proveedor=forms.CharField(widget=forms.TextInput())
		
		def clean(self):
				
				return self.cleaned_data
				
				
				
class vendedorform(forms.Form):
	
	rut_vendedor=forms.CharField(widget=forms.TextInput())
	nombre_vendedor=forms.CharField(widget=forms.TextInput())
	direccion_vendedor=forms.CharField(widget=forms.TextInput())
	contrasena_vendedor=forms.CharField(widget=forms.TextInput())
	telefono_vendedor=forms.CharField(widget=forms.TextInput())
	edad_vendedor=forms.CharField(widget=forms.TextInput())
	opcion = forms.ChoiceField(widget = forms.Select(), choices = ([('admin','Administrador'), ('vendedor','Vendedor') ]))

	def clean(self):

		return self.cleaned_data
				

class bodegaform(forms.Form):
		
		direccion=forms.CharField(widget=forms.TextInput())
		
		def clean(self):
				
				return self.cleaned_data
				
				
class areaform(forms.Form):
		
		
		pasillo=forms.CharField(widget=forms.TextInput())
		estante=forms.CharField(widget=forms.TextInput())
		gaveta=forms.CharField(widget=forms.TextInput())
		
		def clean(self):
				
				return self.cleaned_data
				
				
class grupoform(forms.Form):


	nombre_tipo_material=forms.CharField(widget=forms.TextInput())
	

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