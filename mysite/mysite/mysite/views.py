from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from frasim.models import *
import datetime
from frasim.forms import *

from django.contrib.auth import *
from django.http import *

from django.contrib import messages

def current_datetime(request):
	now = datetime.datetime.now()
	ctx={"current_date":now}
	return render_to_response('current_datetime.html',ctx,context_instance=RequestContext(request))


def hours_ahead(request, offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def lista_bebidas(request):
        bebidas = Bebida.objects.all()
        return render_to_response('lista_bebidas.html',{'lista':bebidas})

def sobre(request):

        
        return render_to_response('frasim.html')
		
def material_adm(request):

        
        return render_to_response('material-adm.html')
		

		
def Login_view(request):


		
		if request.method == "POST":
			form=loginform(request.POST)
			
			
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				contrasena = form.cleaned_data['contrasena']
				opcion=form.cleaned_data['opcion']
				
				if Vendedor.objects.filter(nombre_vendedor=nombre,contrasena_vendedor=contrasena):
					
					if opcion=='admin' and Vendedor.objects.filter(nombre_vendedor=nombre,contrasena_vendedor=contrasena,rol="admin"):
						return HttpResponseRedirect('/agregar_bodega/')
					else:
						if opcion=='vendedor' and Vendedor.objects.filter(nombre_vendedor=nombre,contrasena_vendedor=contrasena,rol="vendedor"):
							return HttpResponseRedirect('/ventas_vendedor/')
					
				
			
				form = loginform()
				ctx={'form':form}
				return render_to_response('login.html',ctx,context_instance=RequestContext(request))
			else:
				ctx={'form':form}
				return render_to_response('login.html',ctx,context_instance=RequestContext(request))				
		else: #GET
			form = loginform()
			ctx={'form':form}
			return render_to_response('login.html',ctx,context_instance=RequestContext(request))
			
			
			
			
			
def material_view(request):

		if request.method == "POST":
			form=materialform(request.POST)
			lala=request.POST.keys()
		
			for clave in lala:
					if clave=="opcion":
		
						if form.is_valid():
							marca_material=form.cleaned_data['marca_material']
							modelo_material=form.cleaned_data['modelo_material']
						
							codigo_tipo_material=request.POST["opcion"]
							nombre_material=form.cleaned_data['nombre_material']
							precio_material=form.cleaned_data['precio_material']
						
						
							cantidad_material=form.cleaned_data['cantidad_material']
							q=Tipo_material.objects.all()
							
							for i in q:
								
								if i.nombre_tipo_material==codigo_tipo_material:
									p=Material()
									p.id_marca=marca_material
									p.id_modelo=modelo_material
									
									p.cod_tipo_mat=codigo_tipo_material
									p.nombre_material=nombre_material
									p.precio_material=precio_material
									
								
									p.cantidad_material=cantidad_material
									p.save()
									
							lolo=Material.objects.all()
							largo=len(lolo)
							lol=lolo[largo-1]
							
							
							
							for clave in lala:
								if clave==request.POST[clave]:
								
									w=Material.objects.get(cod_material=lol.cod_material)
									p=Material.objects.filter(cod_material=clave)
									for i in p:
										
										q=Compatibilidad()
										q.cod_mat=lol.cod_material
										q.cod_mat_2=i.cod_material
										q.id_marca=i.id_marca
										q.id_modelo=i.id_modelo
										q.cod_tipo_mat=i.cod_tipo_mat
										q.nombre_material=i.nombre_material
										q.save()
										
										q=Compatibilidad()
										q.cod_mat=i.cod_material
										q.cod_mat_2=w.cod_material
										q.id_marca=w.id_marca
										q.id_modelo=w.id_modelo
										q.cod_tipo_mat=w.cod_tipo_mat
										q.nombre_material=w.nombre_material
										q.save()	
							grupos=Tipo_material.objects.all()
							materiales=Material.objects.all()
							form = materialform()
							ctx={'form':form,"grupos":grupos,"materiales":materiales}
							messages.success(request,'Registro exitoso')
							return render_to_response('material-adm.html',ctx,context_instance=RequestContext(request))
						else:	
							materiales=Material.objects.all()		
							grupos=Tipo_material.objects.all()
							ctx={'form':form,"grupos":grupos,"materiales":materiales}
							return render_to_response('material-adm.html',ctx,context_instance=RequestContext(request))
		else: #GET
			grupos=Tipo_material.objects.all()
			materiales=Material.objects.all()
			form = materialform()
			ctx={'form':form,"grupos":grupos,"materiales":materiales}
			return render_to_response('material-adm.html',ctx,context_instance=RequestContext(request))
			
			
			
def actualizar_material_view(request):


			if request.method == "POST":
				lala=request.POST.keys()
			
				aa=False
				
				
				
				for clave in lala:
					if clave=="codigo":
						aa=True
					if clave=="lala":
						p=Material.objects.get(cod_material=request.POST["lala"])
						
					
						ctx={"material":p}
						return render_to_response('act-material.html',ctx,context_instance=RequestContext(request))
				if aa==True:		
					p=Material.objects.get(cod_material=request.POST["codigo"])
					p.id_marca=request.POST["marca"]
					p.id_modelo=request.POST["modelo"]
					
					p.cod_tipo_mat=request.POST["cod_grupo"]
					p.nombre_material=request.POST["nombre"]
					p.precio_material=request.POST["precio"]
					
				
					p.cantidad_material=request.POST["cantidad"]
					p.save()
					materiales=Material.objects.all()
					ctx={'materiales':materiales}
					return render_to_response('actualizar-material.html',ctx,context_instance=RequestContext(request))
				else:
					materiales=Material.objects.all()
					ctx={'materiales':materiales}
					return render_to_response('actualizar-material.html',ctx,context_instance=RequestContext(request))
			else:
				materiales=Material.objects.all()
				
				ctx={'materiales':materiales}
				return render_to_response('actualizar-material.html',ctx,context_instance=RequestContext(request))

			
			
def eliminar_material_view(request):


		if request.method == "POST":
			lala=request.POST.keys()
			lolo=request.POST.values()
			
			print lala
			print lolo
			
			for clave in lala:
				if "Eliminar"==request.POST[clave]:
					p=Material.objects.filter(cod_material=clave)
					p.delete()
					
					q=Compatibilidad.objects.filter(cod_mat=clave)
					q.delete()
					w=Compatibilidad.objects.filter(cod_mat_2=clave)
					w.delete()
					
					
				
				
			
			
			materiales=Material.objects.all()
			ctx={'materiales':materiales}
			return render_to_response('eliminar-material-adm.html',ctx,context_instance=RequestContext(request))
		else: #GET
			materiales=Material.objects.all()
			ctx={'materiales':materiales}
			return render_to_response('eliminar-material-adm.html',ctx,context_instance=RequestContext(request))
			
			
			
def compatible_view(request):


			if request.method == "POST":
				lala=request.POST.keys()
			
				aa=False
				
				
				
				for clave in lala:
					
					if clave=="codigo":
						aa=True
					if "Ver"==request.POST[clave]:
						p=Compatibilidad.objects.filter(cod_mat=clave)
						
						ctx={"material":p}
						return render_to_response('detalle_comp.html',ctx,context_instance=RequestContext(request))
				if aa==True:		
					p=Material.objects.get(cod_material=request.POST["codigo"])
					p.id_marca=request.POST["marca"]
					p.id_modelo=request.POST["modelo"]
					
					p.cod_tipo_mat=request.POST["cod_grupo"]
					p.nombre_material=request.POST["nombre"]
					p.precio_material=request.POST["precio"]
					
				
					p.cantidad_material=request.POST["cantidad"]
					p.save()
					materiales=Material.objects.all()
					ctx={'materiales':materiales}
					return render_to_response('compatible.html',ctx,context_instance=RequestContext(request))
				else:
					materiales=Material.objects.all()
					ctx={'materiales':materiales}
					return render_to_response('compatible.html',ctx,context_instance=RequestContext(request))
			else:
				materiales=Material.objects.all()
				
				ctx={'materiales':materiales}
				return render_to_response('compatible.html',ctx,context_instance=RequestContext(request))
			
			

def proveedor_view(request):

		if request.method == "POST":
			form=proveedorform(request.POST)
			
			if form.is_valid():
				rut_proveedor=form.cleaned_data['rut_proveedor']
				nombre_proveedor=form.cleaned_data['nombre_proveedor']
				direc_proveedor=form.cleaned_data['direc_proveedor']
				fono_proveedor=form.cleaned_data['fono_proveedor']
				movil_proveedor=form.cleaned_data['movil_proveedor']
				correo_proveedor=form.cleaned_data['correo_proveedor']
				
				
				p=Proveedor()
				p.rut_proveedor=rut_proveedor
				p.nombre_proveedor=nombre_proveedor
				p.direc_proveedor=direc_proveedor
				p.fono_proveedor=fono_proveedor
				p.movil_proveedor=movil_proveedor
				p.correo_proveedor=correo_proveedor
				p.save()
				form = proveedorform()
				ctx={'form':form}
				messages.success(request,'Registro exitoso')
				return render_to_response('proveedor-adm.html',ctx,context_instance=RequestContext(request))
			else:
				ctx={'form':form}
				return render_to_response('proveedor-adm.html',ctx,context_instance=RequestContext(request))
		else: #GET
			form = proveedorform()
			ctx={'form':form}
			return render_to_response('proveedor-adm.html',ctx,context_instance=RequestContext(request))
			
			
			
def actualizar_proveedor_view(request):


			if request.method == "POST":
				lala=request.POST.keys()
				aa=False
			
			
				for clave in lala:
					if clave=="rut":
						aa=True
					if clave=="lala":
						p=Proveedor.objects.get(rut_proveedor=request.POST["lala"])
						
						
						ctx={"proveedor":p}
						return render_to_response('act-proveedor.html',ctx,context_instance=RequestContext(request))
					
				
				if aa==True:
					p=Proveedor.objects.get(rut_proveedor=request.POST["rut"])
					p.nombre_proveedor=request.POST["nombre"]
					p.direc_proveedor=request.POST["direccion"]
					p.fono_proveedor=request.POST["fono"]
					p.movil_proveedor=request.POST["movil"]
					p.correo_proveedor=request.POST["correo"]
					p.save()
					proveedores=Proveedor.objects.all()
					ctx={'proveedores':proveedores}
					return render_to_response('actualizar-prov.html',ctx,context_instance=RequestContext(request))
					
				else:
					proveedores=Proveedor.objects.all()
					ctx={'proveedores':proveedores}
					return render_to_response('actualizar-prov.html',ctx,context_instance=RequestContext(request))
					
			else:
				proveedores=Proveedor.objects.all()
				
				ctx={'proveedores':proveedores}
				return render_to_response('actualizar-prov.html',ctx,context_instance=RequestContext(request))
			
			
def eliminar_proveedor_view(request):


			if request.method == "POST":
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Proveedor.objects.filter(rut_proveedor=clave)
						p.delete()
						
						
				
				proveedores=Proveedor.objects.all()
				ctx={'proveedores':proveedores}
				return render_to_response('eliminar-proveedor-adm.html',ctx,context_instance=RequestContext(request))
			else:
					
				proveedores=Proveedor.objects.all()
				ctx={'proveedores':proveedores}
				return render_to_response('eliminar-proveedor-adm.html',ctx,context_instance=RequestContext(request))
			
			
			
def vendedor_view(request):

		if request.method == "POST":
			form=vendedorform(request.POST)
		
			if form.is_valid():
				rut_vendedor=form.cleaned_data['rut_vendedor']
				nombre_vendedor=form.cleaned_data['nombre_vendedor']
				direccion_vendedor=form.cleaned_data['direccion_vendedor']
				contrasena_vendedor=form.cleaned_data['contrasena_vendedor']
				telefono_vendedor=form.cleaned_data['telefono_vendedor']
				edad_vendedor=form.cleaned_data['edad_vendedor']
				rol=form.cleaned_data['opcion']
				
				
				p=Vendedor()
				p.rut_vendedor=rut_vendedor
				p.nombre_vendedor=nombre_vendedor
				p.direccion_vendedor=direccion_vendedor
				p.contrasena_vendedor=contrasena_vendedor
				p.telefono_vendedor=telefono_vendedor
				p.edad_vendedor=edad_vendedor
				p.rol=rol
				p.save()
				form = vendedorform()
				ctx={'form':form}
				messages.success(request,'Registro exitoso')
				return render_to_response('vendedor-adm.html',ctx,context_instance=RequestContext(request))
			else:
				ctx={'form':form}

				return render_to_response('vendedor-adm.html',ctx,context_instance=RequestContext(request))
		else: #GET
			form = vendedorform()
			ctx={'form':form}
			return render_to_response('vendedor-adm.html',ctx,context_instance=RequestContext(request))
			
			
			
def actualizar_vendedor_view(request):


			if request.method == "POST":
				lala=request.POST.keys()
				
				aa=False
			
				for clave in lala:
					if clave=="rut" or clave=="nombre" or clave=="edad" or clave=="direccion" or clave=="fono" or clave=="contrasena":
						if request.POST[clave]==None:
							aa=False
						else:
							aa=True
					if clave=="lala":
						p=Vendedor.objects.get(rut_vendedor=request.POST["lala"])
						
						
						ctx={"vendedor":p}
						return render_to_response('act-vendedor.html',ctx,context_instance=RequestContext(request))
					
	
				
				if aa==True:
					p=Vendedor.objects.get(rut_vendedor=request.POST["rut"])
					p.nombre_vendedor=request.POST["nombre"]
					p.edad_vendedor=request.POST["edad"]
					p.direccion_vendedor=request.POST["direccion"]
					p.telefono_vendedor=request.POST["fono"]
					p.contrasena_vendedor=request.POST["contrasena"]
					p.rol=request.POST["opcion"]
					p.save()
					vendedores=Vendedor.objects.all()
					ctx={'vendedores':vendedores}
					return render_to_response('actualizar-vendedor.html',ctx,context_instance=RequestContext(request))
				else:
					vendedores=Vendedor.objects.all()
					ctx={'vendedores':vendedores}
					return render_to_response('actualizar-vendedor.html',ctx,context_instance=RequestContext(request))
			else:
				vendedores=Vendedor.objects.all()
				
				ctx={'vendedores':vendedores}
				return render_to_response('actualizar-vendedor.html',ctx,context_instance=RequestContext(request))
			
			
def eliminar_vendedor_view(request):


			if request.method == "POST":
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Vendedor.objects.filter(rut_vendedor=clave)
						p.delete()
						
						
				
				vendedor=Vendedor.objects.all()
				ctx={'vendedores':vendedor}
				return render_to_response('eliminar-vendedor-adm.html',ctx,context_instance=RequestContext(request))
			else:
				vendedor=Vendedor.objects.all()
				ctx={'vendedores':vendedor}
				return render_to_response('eliminar-vendedor-adm.html',ctx,context_instance=RequestContext(request))
				
				
				
			
			
def bodega_view(request):


		if request.method == "POST":
			form=bodegaform(request.POST)
		
			
			if form.is_valid() :
				
				direccion = form.cleaned_data['direccion']
				p=Bodega()
			
				p.direccion=direccion
				p.save()
				form = bodegaform()
				ctx={'form':form}

				messages.success(request,'Registro exitoso')
				return render_to_response('adm.html',ctx,context_instance=RequestContext(request))
			else:
				ctx={'form':form}
				return render_to_response('adm.html',ctx,context_instance=RequestContext(request))

		else: #GET
			form = bodegaform()
			ctx={'form':form}
			return render_to_response('adm.html',ctx,context_instance=RequestContext(request))
			
			
def actualizar_bodega_view(request):


			if request.method == "POST":
				lala=request.POST.keys()
				for clave in lala:
					if clave=="lala":
						p=Bodega.objects.get(cod_bodega=request.POST["lala"])
						ctx={"bodega":p}
						return render_to_response('act-bodega.html',ctx,context_instance=RequestContext(request))
						
				p=Bodega.objects.get(cod_bodega=request.POST["codigo"])
				p.direccion=request.POST["direccion"]
				p.save()
				bodegas=Bodega.objects.all()
				ctx={'bodegas':bodegas}
				return render_to_response('actualizar_bodega.html',ctx,context_instance=RequestContext(request))
			else:
				bodegas=Bodega.objects.all()
				
				ctx={'bodegas':bodegas}
				return render_to_response('actualizar_bodega.html',ctx,context_instance=RequestContext(request))
				
				

				
	
			
			

def eliminar_bodega_view(request):


			if request.method == "POST":
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Bodega.objects.filter(cod_bodega=clave)
						p.delete()
						
						
				
				bodegas=Bodega.objects.all()
				ctx={'bodegas':bodegas}
				return render_to_response('eliminar-bodega.html',ctx,context_instance=RequestContext(request))
			else:
				bodegas=Bodega.objects.all()
				
				ctx={'bodegas':bodegas}
				return render_to_response('eliminar-bodega.html',ctx,context_instance=RequestContext(request))			
			
			
def area_view(request):

		if request.method == "POST":
			form=areaform(request.POST)
			
			
			if form.is_valid() :
				print "lala"
				q=Bodega.objects.get(direccion=request.POST["opcion"])
				cod_bodega=q.cod_bodega
				pasillo=form.cleaned_data['pasillo']
				estante=form.cleaned_data['estante']
				gaveta=form.cleaned_data['gaveta']

				p=Area()
				
				p.cod_bodega=cod_bodega
				p.pasillo=pasillo
				p.estante=estante
				p.gaveta=gaveta
				p.save()
				
				bodegas=Bodega.objects.all()
				form = areaform()
				ctx={'form':form,"bodegas":bodegas}

				messages.success(request,'Registro exitoso')
				return render_to_response('adm-area.html',ctx,context_instance=RequestContext(request))
			else:
				bodegas=Bodega.objects.all()
				ctx={'form':form,"bodegas":bodegas}
				return render_to_response('adm-area.html',ctx,context_instance=RequestContext(request))

		else: #GET
			bodegas=Bodega.objects.all()
			form = areaform()
			print "GET"
			ctx={'form':form,"bodegas":bodegas}
			return render_to_response('adm-area.html',ctx,context_instance=RequestContext(request))
			
			
			
def actualizar_area_view(request):


			if request.method == "POST":
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if clave=="lala":
						p=Area.objects.get(cod_area=request.POST["lala"])
						
						
						ctx={"area":p}
						return render_to_response('act-area.html',ctx,context_instance=RequestContext(request))
						
				p=Area.objects.get(cod_area=request.POST["codigo"])
				p.cod_bodega=request.POST["codigo1"]
				p.pasillo=request.POST["pasillo"]
				p.estante=request.POST["estante"]
				p.gaveta=request.POST["gaveta"]
				p.save()
				areas=Area.objects.all()
				ctx={'areas':areas}
				return render_to_response('actualizar_area.html',ctx,context_instance=RequestContext(request))
			else:
				areas=Area.objects.all()
				
				ctx={'areas':areas}
				return render_to_response('actualizar_area.html',ctx,context_instance=RequestContext(request))
			
			
	

def eliminar_area_view(request):

			if request.method == "POST":
				lala=request.POST.keys()
			
			
			
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Area.objects.filter(cod_area=clave)
						p.delete()
						
						
				
				areas=Area.objects.all()
				ctx={'areas':areas}
				return render_to_response('eliminar-area.html',ctx,context_instance=RequestContext(request))
			else:
				areas=Area.objects.all()
				ctx={'areas':areas}
				return render_to_response('eliminar-area.html',ctx,context_instance=RequestContext(request))
			
def grupo_view(request):

		if request.method == "POST":
			form=grupoform(request.POST)
			aa=True
			
			if form.is_valid() :
				
				nombre_tipo_material=form.cleaned_data['nombre_tipo_material']
				cod_bodega=request.POST["opcion"]
				cod_area=request.POST["opcion2"]
				q=Tipo_material.objects.all()
				for i in q:
					if i.nombre_tipo_material==nombre_tipo_material:
						aa=False

				if aa==True:
					p=Tipo_material()
				
					p.nombre_tipo_material=nombre_tipo_material
					p.cod_bodega=cod_bodega
					p.cod_area=cod_area
					p.save()
			
				form = grupoform()
				ctx={'form':form}

				messages.success(request,'Registro exitoso')
				return render_to_response('adm-grupo.html',ctx,context_instance=RequestContext(request))
			else:

				bodegas=Bodega.objects.all()
				areas=Area.objects.all()
				ctx={'form':form,'bodegas':bodegas,'areas':areas}
				return render_to_response('adm-grupo.html',ctx,context_instance=RequestContext(request))
		else: #GET
			bodegas=Bodega.objects.all()
			areas=Area.objects.all()
			form = grupoform()
			ctx={'form':form,'bodegas':bodegas,'areas':areas}
			return render_to_response('adm-grupo.html',ctx,context_instance=RequestContext(request))
			
			
			
def actualizar_grupo_view(request):


			if request.method == "POST":
				lala=request.POST.keys()
			
			
			
				for clave in lala:
					if clave=="lala":
						p=Tipo_material.objects.get(codigo_tipo_material=request.POST["lala"])
						
						
						ctx={"grupo":p}
						return render_to_response('act-grupo.html',ctx,context_instance=RequestContext(request))
						
				p=Tipo_material.objects.get(codigo_tipo_material=request.POST["codigo"])
				
				p.nombre_tipo_material=request.POST["nombre"]
				p.cod_bodega=request.POST["bodega"]
				p.cod_area=request.POST["area"]
				p.save()
				grupos=Tipo_material.objects.all()
				ctx={'grupos':grupos}
				return render_to_response('actualizar_grupo.html',ctx,context_instance=RequestContext(request))
			else:
				grupos=Tipo_material.objects.all()
				
				ctx={'grupos':grupos}
				return render_to_response('actualizar_grupo.html',ctx,context_instance=RequestContext(request))
			
def eliminar_grupo_view(request):
			
			if request.method == "POST":
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Tipo_material.objects.filter(codigo_tipo_material=clave)
						p.delete()
						
						
				
				grupos=Tipo_material.objects.all()
				ctx={'grupos':grupos}
				return render_to_response('eliminar-grupo.html',ctx,context_instance=RequestContext(request))
			else:
				grupos=Tipo_material.objects.all()
				ctx={'grupos':grupos}
				return render_to_response('eliminar-grupo.html',ctx,context_instance=RequestContext(request))
			
def cotizar_view(request):
		
		
		if request.method == "POST":
			
			form2=buscaform(request.POST)
			
			
			if request.POST["busca"]=='agregar':
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if clave==request.POST[clave]:
						p=Material.objects.get(cod_material=clave)
						q=Productos()
						
						q.codigo_material=p.cod_material
						q.marca=p.id_marca
						q.modelo=p.id_modelo
						q.codigo_tipo_mat=p.cod_tipo_mat
						q.nombre=p.nombre_material
						q.precio=p.precio_material
						q.cantidad=p.cantidad_material
						q.save()
						
				
				
				grupos=Tipo_material.objects.all()
				form2 = buscaform()
				ctx={'form2':form2,"grupos":grupos}
				return render_to_response('cotizar-adm.html',ctx,context_instance=RequestContext(request))
				
			else:
				lala=request.POST.keys()
				
				for clave in lala:
					if clave=="opcion":	
					
						materiales=Material.objects.filter(cod_tipo_mat=request.POST["opcion"]) 
						grupos=Tipo_material.objects.all()
						form = cotizarform()
						form2 = buscaform()
						ctx={'form':form,'form2':form2,"materiales":materiales,"grupos":grupos}
						return render_to_response('cotizar-adm.html',ctx,context_instance=RequestContext(request))
						
					else:
						grupos=Tipo_material.objects.all()
						form2=buscaform()
						ctx={'form2':form2,"grupos":grupos}
						return render_to_response('cotizar-adm.html',ctx,context_instance=RequestContext(request))
			
		else: #GET
			grupos=Tipo_material.objects.all()
			form2=buscaform()
			ctx={'form2':form2,"grupos":grupos}
			return render_to_response('cotizar-adm.html',ctx,context_instance=RequestContext(request))
			
			
			
def eliminar_cotizar_view(request):
			
			if request.method == "POST":
				lala=request.POST.keys()
			
			
				
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Cotizacion.objects.filter(nro_cotizacion=clave)
						p.delete()
						q=Detalle_cotizacion.objects.filter(nro_cotizacion=clave)
						q.delete()
				
					if "Ver"==request.POST[clave]:
						detalles=Detalle_cotizacion.objects.filter(nro_cotizacion=clave)
						ctx={'detalles':detalles}
						return render_to_response('detalle_cotizacion.html',ctx,context_instance=RequestContext(request))
						
					if "Vender"==request.POST[clave]:
						p=Cotizacion.objects.get(nro_cotizacion=clave)
						w=Venta()
						w.rut_vendedor=p.rut_vendedor
						w.fecha_venta=p.fecha_cotizacion
						w.hora_venta=p.hora_cotizacion
						w.save()
						
						p=Cotizacion.objects.filter(nro_cotizacion=clave)
						p.delete()
						
						q=Detalle_cotizacion.objects.filter(nro_cotizacion=clave)
						
						lala=Venta.objects.all()
						largo=len(lala)
						lol=lala[largo-1]
					
						
						
						
						
						
						for i in q:
							z=Detalle_venta()
							z.nro_venta=lol
							z.cod_mat=i.cod_mat
							z.id_marca=i.id_marca
							z.id_modelo=i.id_modelo
							z.cod_tipo_mat=i.cod_tipo_mat
							z.nombre_material=i.nombre_material
							z.precio_material=i.precio_material
							z.cantidad_material=i.cantidad_material
							z.save()
							
							w=Material.objects.get(id_marca=i.id_marca,id_modelo=i.id_modelo)
							aa=i.cantidad_material
							descuento=int(w.cantidad_material)-int(aa)
							w.cantidad_material=str(descuento)
							w.save()
						
						
						
						q=Detalle_cotizacion.objects.filter(nro_cotizacion=clave)
						q.delete()	
							
				
				cotizaciones=Cotizacion.objects.all()
				ctx={'cotizaciones':cotizaciones}
				return render_to_response('eliminar-cotizar-adm.html',ctx,context_instance=RequestContext(request))
			else:
				cotizaciones=Cotizacion.objects.all()
				ctx={'cotizaciones':cotizaciones}
				return render_to_response('eliminar-cotizar-adm.html',ctx,context_instance=RequestContext(request))
				
				
				
def carro_cotizar_view(request):
			
			valor=0
			
			if request.method == "POST":
				form=cotizarform(request.POST)
				lala=request.POST.keys()
				ahora = datetime.datetime.now()
				
			
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Productos.objects.filter(codigo_material=clave)
						p.delete()
							
							
					if "generar cotizacion"==request.POST[clave]:
						p=Productos.objects.all()
						for clave in p:
							w=Material.objects.get(id_marca=clave.marca,id_modelo=clave.modelo,nombre_material=clave.nombre)
							aa=request.POST[str(clave.marca)+str(clave.modelo)+str(clave.nombre)]
							if aa=="":
								valor=1
						
						if valor==0:
							for clave in p:
								w=Material.objects.get(id_marca=clave.marca,id_modelo=clave.modelo,nombre_material=clave.nombre)
								aa=request.POST[str(clave.marca)+str(clave.modelo)+str(clave.nombre)]
								descuento=int(w.cantidad_material)-int(aa)
								w.cantidad_material=str(descuento)
								
								w=Productos.objects.get(marca=clave.marca,modelo=clave.modelo,nombre=clave.nombre)
								w.cantidad=int(aa)
								w.save()
								
							
						if form.is_valid() and valor==0:
						
							rut_vendedor=form.cleaned_data['rut_vendedor']
							
							q=Cotizacion()
							
							q.rut_vendedor=rut_vendedor
							q.fecha_cotizacion=str(ahora.day)+"/"+str(ahora.month)+"/"+ str(ahora.year)
							q.hora_cotizacion=str(ahora.hour)+":"+str(ahora.minute)+":"+str(ahora.second)
							q.save()
							p=Productos.objects.all()
							
							lala=Cotizacion.objects.all()
							largo=len(lala)
							lol=lala[largo-1]
							
							
							for i in p:
								z=Detalle_cotizacion()
								z.nro_cotizacion=lol
								z.cod_mat=i.codigo_material
								z.id_marca=i.marca
								z.id_modelo=i.modelo
								z.cod_tipo_mat=i.codigo_tipo_mat
								z.nombre_material=i.nombre
								z.precio_material=i.precio
								z.cantidad_material=i.cantidad
								z.save()
							
							p.delete()
						
				form = cotizarform()
				
				productos=Productos.objects.all()
				ctx={'productos':productos,'form':form}

				messages.success(request,'Cotizacion registrada')
				return render_to_response('carro_cotizar.html',ctx,context_instance=RequestContext(request))
			else:
				form = cotizarform()
				
				productos=Productos.objects.all()
				ctx={'productos':productos,'form':form}
				return render_to_response('carro_cotizar.html',ctx,context_instance=RequestContext(request))
				
				
				
def ventas_view(request):
		
		
		if request.method == "POST":
			
			form2=buscaform(request.POST)
		
			
			if request.POST["busca"]=='agregar':
				lala=request.POST.keys()
			
			
			
				for clave in lala:
					if clave==request.POST[clave]:
						p=Material.objects.get(cod_material=clave)
						q=Productos()
						
						q.codigo_material=p.cod_material
						q.marca=p.id_marca
						q.modelo=p.id_modelo
						q.codigo_tipo_mat=p.cod_tipo_mat
						q.nombre=p.nombre_material
						q.precio=p.precio_material
						q.cantidad=p.cantidad_material
						q.save()
						
				
			
				grupos=Tipo_material.objects.all()
				form2 = buscaform()
				ctx={'form2':form2,"grupos":grupos}
				return render_to_response('ventas-adm.html',ctx,context_instance=RequestContext(request))
				
			else:
				lala=request.POST.keys()
				
				
				for clave in lala:
					if clave=="opcion":
				
						materiales=Material.objects.filter(cod_tipo_mat=request.POST["opcion"]) 
							
						form2 = buscaform()
						grupos=Tipo_material.objects.all()
						ctx={'form2':form2,"materiales":materiales,"grupos":grupos}
						return render_to_response('ventas-adm.html',ctx,context_instance=RequestContext(request))
					else:
						grupos=Tipo_material.objects.all()
						form2=buscaform()
						ctx={'form2':form2,"grupos":grupos}
						return render_to_response('ventas-adm.html',ctx,context_instance=RequestContext(request))
		else: #GET
			grupos=Tipo_material.objects.all()
			form2=buscaform()
			ctx={'form2':form2,"grupos":grupos}
			return render_to_response('ventas-adm.html',ctx,context_instance=RequestContext(request))
			
			
def eliminar_ventas_view(request):
			
			if request.method == "POST":
				lala=request.POST.keys()
				
				
				
			
				
					
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Venta.objects.filter(nro_venta=clave)
						p.delete()
						q=Detalle_venta.objects.filter(nro_venta=clave)
						q.delete()
						
					if "Ver"==request.POST[clave]:
					
						detalles=Detalle_venta.objects.filter(nro_venta=clave)
						ctx={'detalles':detalles}
						return render_to_response('detalle_venta.html',ctx,context_instance=RequestContext(request))
							
							
							
						
				
				ventas=Venta.objects.all()
				ctx={'ventas':ventas}
				return render_to_response('eliminar-ventas-adm.html',ctx,context_instance=RequestContext(request))
			else:
				ventas=Venta.objects.all()
				ctx={'ventas':ventas}
				return render_to_response('eliminar-ventas-adm.html',ctx,context_instance=RequestContext(request))
				
				
				
				
				
		
def carro_ventas_view(request):
			
			valor=0
			
			
			if request.method == "POST":
				form=ventasform(request.POST)
				lala=request.POST.keys()
				mm=""
				ahora = datetime.datetime.now()
				if request.POST["elige"]=='eliminar':
			
					for clave in lala:
						if clave==request.POST[clave]:
							p=Productos.objects.filter(codigo_material=clave)
							p.delete()
						
							
				else:
					p=Productos.objects.all()
					
					for clave in p:
						w=Material.objects.get(id_marca=clave.marca,id_modelo=clave.modelo,nombre_material=clave.nombre)
						aa=request.POST[str(clave.marca)+str(clave.modelo)+str(clave.nombre)]
						if aa=="":
							valor=1
							
					if valor==0:		
						for clave in p:
							w=Material.objects.get(id_marca=clave.marca,id_modelo=clave.modelo,nombre_material=clave.nombre)
							aa=request.POST[str(clave.marca)+str(clave.modelo)+str(clave.nombre)]
							descuento=int(w.cantidad_material)-int(aa)
							w.cantidad_material=str(descuento)
							w.save()
							
							w=Productos.objects.get(marca=clave.marca,modelo=clave.modelo,nombre=clave.nombre)
							w.cantidad=int(aa)
							w.save()
						
					if form.is_valid() and valor==0 :
						
						rut_vendedor=form.cleaned_data['rut_vendedor']
						
						q=Venta()
						
						q.rut_vendedor=rut_vendedor
						q.fecha_venta=str(ahora.day)+"/"+str(ahora.month)+"/"+ str(ahora.year)
						q.hora_venta=str(ahora.hour)+":"+str(ahora.minute)+":"+str(ahora.second)
						q.save()
						lala=Venta.objects.all()
						largo=len(lala)
						lol=lala[largo-1]
					
						
						
						
						p=Productos.objects.all()
						
						for i in p:
							z=Detalle_venta()
							z.nro_venta=lol
							z.cod_mat=i.codigo_material
							z.id_marca=i.marca
							z.id_modelo=i.modelo
							z.cod_tipo_mat=i.codigo_tipo_mat
							z.nombre_material=i.nombre
							z.precio_material=i.precio
							z.cantidad_material=i.cantidad
							z.save()
						p.delete()
						
						
						
					
						
						
				form = ventasform()
			
				productos=Productos.objects.all()
				ctx={'productos':productos,'form':form}

				messages.success(request,'Venta registrada')
				return render_to_response('carro_ventas.html',ctx,context_instance=RequestContext(request))
			else:
				form = ventasform()
				now = datetime.datetime.now()
				productos=Productos.objects.all()
				ctx={'productos':productos,'form':form,"tiempo":now}
				return render_to_response('carro_ventas.html',ctx,context_instance=RequestContext(request))
				
				
				

def orden_view(request):
		
		
		if request.method == "POST":
			
			form2=buscaform(request.POST)
			
			
			if request.POST["busca"]=='agregar':
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if clave==request.POST[clave]:
						p=Material.objects.get(cod_material=clave)
						q=Productos()
						
						q.codigo_material=p.cod_material
						q.marca=p.id_marca
						q.modelo=p.id_modelo
						q.codigo_tipo_mat=p.cod_tipo_mat
						q.nombre=p.nombre_material
						q.precio=p.precio_material
						q.cantidad=p.cantidad_material
						q.save()
						
				
			
				grupos=Tipo_material.objects.all()
				form2 = buscaform()
				ctx={'form2':form2,"grupos":grupos}
				return render_to_response('orden-adm.html',ctx,context_instance=RequestContext(request))
				
			else:
				lala=request.POST.keys()
					
				for clave in lala:
					if clave=="opcion":
						materiales=Material.objects.filter(cod_tipo_mat=request.POST["opcion"]) 
						grupos=Tipo_material.objects.all()
						form = cotizarform()
						form2 = buscaform()
						ctx={'form':form,'form2':form2,"materiales":materiales,"grupos":grupos}
						return render_to_response('orden-adm.html',ctx,context_instance=RequestContext(request))
					else:
						grupos=Tipo_material.objects.all()
						form2=buscaform()
						ctx={'form2':form2,"grupos":grupos}
						return render_to_response('orden-adm.html',ctx,context_instance=RequestContext(request))
					
					
			
			
		else: #GET
			grupos=Tipo_material.objects.all()
			form2=buscaform()
			ctx={'form2':form2,"grupos":grupos}
			return render_to_response('orden-adm.html',ctx,context_instance=RequestContext(request))
			
			
			
			
def carro_orden_view(request):
			valor=0
			
			
			if request.method == "POST":
				form=ordenform(request.POST)
				lala=request.POST.keys()
				ahora = datetime.datetime.now()
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Productos.objects.filter(codigo_material=clave)
						p.delete()							
					if "generar orden"==request.POST[clave]:									
						#########################################
						p=Productos.objects.all()
						for clave in p:
							w=Material.objects.get(id_marca=clave.marca,id_modelo=clave.modelo,nombre_material=clave.nombre)
							aa=request.POST[str(clave.marca)+str(clave.modelo)+str(clave.nombre)]
							if aa=="":
								valor=1
						if valor==0:		
							for clave in p:
								w=Productos.objects.get(marca=clave.marca,modelo=clave.modelo,nombre=clave.nombre)
								w.cantidad=int(aa)
								w.save()
						if form.is_valid() and valor==0 :
							direc_emision=form.cleaned_data['direc_emision']
							condicion_pago=form.cleaned_data['condicion_pago']
							q=Orden_de_compra()
							q.rut_proveedor=request.POST["opcion"]
							q.fecha_oc=str(ahora.day)+"/"+str(ahora.month)+"/"+ str(ahora.year)
							q.hora_oc=str(ahora.hour)+":"+str(ahora.minute)+":"+str(ahora.second)
							q.direc_emision=direc_emision
							q.condicion_pago=condicion_pago
							q.save()
							lala=Orden_de_compra.objects.all()
							largo=len(lala)
							lol=lala[largo-1]
							p=Productos.objects.all()
							for i in p:
								z=Detalle_oc()
								z.nro_oc=lol
								z.cod_mat=i.codigo_material
								z.id_marca=i.marca
								z.id_modelo=i.modelo
								z.cod_tipo_mat=i.codigo_tipo_mat
								z.nombre_material=i.nombre
								z.precio_material=i.precio
								z.cantidad_material=i.cantidad
								z.save()
							p.delete()
							form = ordenform()
						else:
							if form.is_valid()!=True:
								proveedores=Proveedor.objects.all()
								ctx={'form':form,"proveedores":proveedores}
								return render_to_response('carro_orden.html',ctx,context_instance=RequestContext(request))
							if valor!=0:
								proveedores=Proveedor.objects.all()
								ctx={'form':form,"proveedores":proveedores}

								messages.success(request,'Orden de compra registrada')
								return render_to_response('carro_orden.html',ctx,context_instance=RequestContext(request))
					
						
				form = ordenform()
				proveedores=Proveedor.objects.all()
				productos=Productos.objects.all()
				ctx={'productos':productos,'form':form,"proveedores":proveedores}

				messages.success(request,'Orden de compra registrada')
				return render_to_response('carro_orden.html',ctx,context_instance=RequestContext(request))
			else:
				form = ordenform()
				proveedores=Proveedor.objects.all()
				productos=Productos.objects.all()
				ctx={'productos':productos,'form':form,"proveedores":proveedores}
				return render_to_response('carro_orden.html',ctx,context_instance=RequestContext(request))
				
				
				
def eliminar_orden_view(request):
			
			if request.method == "POST":
				lala=request.POST.keys()
			
			
			
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Orden_de_compra.objects.filter(num_oc=clave)
						p.delete()
					if "Ver"==request.POST[clave]:
					
						detalles=Detalle_oc.objects.filter(nro_oc=clave)
						ctx={'detalles':detalles}
						return render_to_response('detalle_oc.html',ctx,context_instance=RequestContext(request))		
						
						
				
				ordenes=Orden_de_compra.objects.all()
				ctx={'ordenes':ordenes}
				return render_to_response('eliminar-orden-adm.html',ctx,context_instance=RequestContext(request))
			else:
				ordenes=Orden_de_compra.objects.all()
				ctx={'ordenes':ordenes}
				return render_to_response('eliminar-orden-adm.html',ctx,context_instance=RequestContext(request))
				
				
				
				
				
def despacho_view(request):
		
		
		if request.method == "POST":
			
			form2=buscaform(request.POST)
		
			
			if request.POST["busca"]=='agregar':
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if clave==request.POST[clave]:
						p=Material.objects.get(cod_material=clave)
						q=Productos()
						
						q.codigo_material=p.cod_material
						q.marca=p.id_marca
						q.modelo=p.id_modelo
						q.codigo_tipo_mat=p.cod_tipo_mat
						q.nombre=p.nombre_material
						q.precio=p.precio_material
						q.cantidad=p.cantidad_material
						q.save()
						
				
				
				grupos=Tipo_material.objects.all()
				form2 = buscaform()
				ctx={'form2':form2,"grupos":grupos}
				return render_to_response('despacho-adm.html',ctx,context_instance=RequestContext(request))
				
			else:
				
					
					
					
					materiales=Material.objects.filter(cod_tipo_mat=request.POST["opcion"]) 
					grupos=Tipo_material.objects.all()
					form = cotizarform()
					form2 = buscaform()
					ctx={'form':form,'form2':form2,"materiales":materiales,"grupos":grupos}
					return render_to_response('despacho-adm.html',ctx,context_instance=RequestContext(request))
						
					
					
				
			
		else: #GET
			grupos=Tipo_material.objects.all()
			form2=buscaform()
			ctx={'form2':form2,"grupos":grupos}
			return render_to_response('despacho-adm.html',ctx,context_instance=RequestContext(request))
			
			
			
def carro_despacho_view(request):
			
			
			valor=0
			
			if request.method == "POST":
				form=despachoform(request.POST)
				lala=request.POST.keys()
				ahora = datetime.datetime.now()
				
			
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Productos.objects.filter(codigo_material=clave)
						p.delete()
							
							
					if "generar despacho"==request.POST[clave]:
						
							
							
							
						#######################################
						
						p=Productos.objects.all()
					
						for clave in p:
							w=Material.objects.get(id_marca=clave.marca,id_modelo=clave.modelo,nombre_material=clave.nombre)
							aa=request.POST[str(clave.marca)+str(clave.modelo)+str(clave.nombre)]
							if aa=="":
								valor=1
								
						if valor==0:		
							for clave in p:
								w=Material.objects.get(id_marca=clave.marca,id_modelo=clave.modelo,nombre_material=clave.nombre)
								aa=request.POST[str(clave.marca)+str(clave.modelo)+str(clave.nombre)]
								aumento=int(w.cantidad_material)+int(aa)
								w.cantidad_material=str(aumento)
								w.save()
								
								w=Productos.objects.get(marca=clave.marca,modelo=clave.modelo,nombre=clave.nombre)
								w.cantidad=int(aa)
								w.save()
							
						if form.is_valid() and valor==0 :
							
							rut_proveedor=request.POST["opcion"]
							
							q=Despacho_material()
							
							q.rut_proveedor=rut_proveedor
							print str(ahora.day)+"/"+str(ahora.month)+"/"+ str(ahora.year)
							q.fecha_despacho=str(ahora.day)+"/"+str(ahora.month)+"/"+ str(ahora.year)
							q.hora_despacho=str(ahora.hour)+":"+str(ahora.minute)+":"+str(ahora.second)
							q.save()
							lala=Despacho_material.objects.all()
							largo=len(lala)
							lol=lala[largo-1]
						
							
							
							
							p=Productos.objects.all()
							
							for i in p:
								z=Detalle_despacho()
								z.nro_despacho=lol
								z.cod_mat=i.codigo_material
								z.id_marca=i.marca
								z.id_modelo=i.modelo
								z.cod_tipo_mat=i.codigo_tipo_mat
								z.nombre_material=i.nombre
								z.precio_material=i.precio
								z.cantidad_material=i.cantidad
								z.save()
							p.delete()		
					
					
					
						
				form = despachoform()
				
				productos=Productos.objects.all()
				proveedores=Proveedor.objects.all()
				ctx={'productos':productos,'form':form,"proveedores":proveedores}
				return render_to_response('carro_despacho.html',ctx,context_instance=RequestContext(request))
			else:
				form = despachoform()
				productos=Productos.objects.all()
				proveedores=Proveedor.objects.all()
				ctx={'productos':productos,'form':form,"proveedores":proveedores}
				return render_to_response('carro_despacho.html',ctx,context_instance=RequestContext(request))
				
				
				
def eliminar_despacho_view(request):
			
			if request.method == "POST":
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Despacho_material.objects.filter(cod_despacho=clave)
						p.delete()
						
					if "Ver"==request.POST[clave]:
					
						detalles=Detalle_despacho.objects.filter(nro_despacho=clave)
						ctx={'detalles':detalles}
						return render_to_response('detalle_despacho.html',ctx,context_instance=RequestContext(request))	
						
						
				
				despachos=Despacho_material.objects.all()
				ctx={'despachos':despachos}
				return render_to_response('eliminar-despacho-adm.html',ctx,context_instance=RequestContext(request))
			else:
				despachos=Despacho_material.objects.all()
				ctx={'despachos':despachos}
				return render_to_response('eliminar-despacho-adm.html',ctx,context_instance=RequestContext(request))
				
				
				
				
				
				
				
				
def ventas_vendedor_view(request):
		
		
		if request.method == "POST":
			
			form2=buscaform(request.POST)
			
			
			if request.POST["busca"]=='agregar':
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if clave==request.POST[clave]:
						p=Material.objects.get(cod_material=clave)
						q=Productos()
						
						q.codigo_material=p.cod_material
						q.marca=p.id_marca
						q.modelo=p.id_modelo
						q.codigo_tipo_mat=p.cod_tipo_mat
						q.nombre=p.nombre_material
						q.precio=p.precio_material
						q.cantidad=p.cantidad_material
						q.save()
						
				
				
				grupos=Tipo_material.objects.all()
				form2 = buscaform()
				ctx={'form2':form2,"grupos":grupos}
				return render_to_response('ventas-vendedor.html',ctx,context_instance=RequestContext(request))
				
			else:
				
					
					
					
					materiales=Material.objects.filter(cod_tipo_mat=request.POST["opcion"]) 
					
					grupos=Tipo_material.objects.all()
					form2 = buscaform()
					ctx={'form2':form2,"materiales":materiales,"grupos":grupos}
					return render_to_response('ventas-vendedor.html',ctx,context_instance=RequestContext(request))
						
					
					
				
			
		else: #GET
			grupos=Tipo_material.objects.all()
			form2=buscaform()
			ctx={'form2':form2,"grupos":grupos}
			return render_to_response('ventas-vendedor.html',ctx,context_instance=RequestContext(request))
			
			
def eliminar_ventas_vendedor_view(request):
			
			if request.method == "POST":
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if clave==request.POST[clave]:
						p=Venta.objects.filter(nro_venta=clave)
						p.delete()
						
						
				
				ventas=Venta.objects.all()
				ctx={'ventas':ventas}
				return render_to_response('eliminar-ventas-vendedor.html',ctx,context_instance=RequestContext(request))
			else:
				ventas=Venta.objects.all()
				ctx={'ventas':ventas}
				return render_to_response('eliminar-ventas-vendedor.html',ctx,context_instance=RequestContext(request))
				
				
				
				
				
		
def carro_ventas_vendedor_view(request):
			
			
			
			if request.method == "POST":
				form=ventasform(request.POST)
				lala=request.POST.keys()
			
				if request.POST["elige"]=='eliminar':
			
					for clave in lala:
						if clave==request.POST[clave]:
							p=Productos.objects.filter(codigo_material=clave)
							p.delete()
							
							
				else:
					if form.is_valid() :
				
						rut_vendedor=form.cleaned_data['rut_vendedor']
						fecha_venta=form.cleaned_data['fecha_venta']
						hora_venta=form.cleaned_data['hora_venta']
						q=Venta()
					
						q.rut_vendedor=rut_vendedor
						q.fecha_venta=fecha_venta
						q.hora_venta=hora_venta
						q.save()
						p=Productos.objects.all()
						p.delete()
						
				
						
						
				form = ventasform()
				
				productos=Productos.objects.all()
				ctx={'productos':productos,'form':form}
				return render_to_response('carro-ventas-vendedor.html',ctx,context_instance=RequestContext(request))
			else:
				form = ventasform()
				
				productos=Productos.objects.all()
				ctx={'productos':productos,'form':form}
				return render_to_response('carro-ventas-vendedor.html',ctx,context_instance=RequestContext(request))
				
				
				
				
				
def cotizar_vendedor_view(request):
		
		
		if request.method == "POST":
			
			form2=buscaform(request.POST)
		
			
			if request.POST["busca"]=='agregar':
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if clave==request.POST[clave]:
						p=Material.objects.get(cod_material=clave)
						q=Productos()
						
						q.codigo_material=p.cod_material
						q.marca=p.id_marca
						q.modelo=p.id_modelo
						q.codigo_tipo_mat=p.cod_tipo_mat
						q.nombre=p.nombre_material
						q.precio=p.precio_material
						q.cantidad=p.cantidad_material
						q.save()
						
				
				
				grupos=Tipo_material.objects.all()
				form2 = buscaform()
				ctx={'form2':form2,"grupos":grupos}
				return render_to_response('cotizar-vendedor.html',ctx,context_instance=RequestContext(request))
				
			else:
			
					
					
					
					materiales=Material.objects.filter(cod_tipo_mat=request.POST["opcion"]) 
					grupos=Tipo_material.objects.all()
					form = cotizarform()
					form2 = buscaform()
					ctx={'form':form,'form2':form2,"materiales":materiales,"grupos":grupos}
					return render_to_response('cotizar-vendedor.html',ctx,context_instance=RequestContext(request))
						
					
					
				
			
		else: #GET
			grupos=Tipo_material.objects.all()
			form2=buscaform()
			ctx={'form2':form2,"grupos":grupos}
			return render_to_response('cotizar-vendedor.html',ctx,context_instance=RequestContext(request))
			
			
			
def eliminar_cotizar_vendedor_view(request):
			
			if request.method == "POST":
				lala=request.POST.keys()
				
			
			
				for clave in lala:
					if clave==request.POST[clave]:
						p=Cotizacion.objects.filter(nro_cotizacion=clave)
						p.delete()
						
						
				
				cotizaciones=Cotizacion.objects.all()
				ctx={'cotizaciones':cotizaciones}
				return render_to_response('eliminar-cotizar-vendedor.html',ctx,context_instance=RequestContext(request))
			else:
				cotizaciones=Cotizacion.objects.all()
				ctx={'cotizaciones':cotizaciones}
				return render_to_response('eliminar-cotizar-vendedor.html',ctx,context_instance=RequestContext(request))
				
				
				
def carro_cotizar_vendedor_view(request):
			
			
			
			if request.method == "POST":
				form=cotizarform(request.POST)
				lala=request.POST.keys()
				
				if request.POST["elige"]=='eliminar':
			
					for clave in lala:
						if clave==request.POST[clave]:
							p=Productos.objects.filter(codigo_material=clave)
							p.delete()
							
							
				else:
					if form.is_valid() :
					
						rut_vendedor=form.cleaned_data['rut_vendedor']
						fecha_cotizacion=form.cleaned_data['fecha_cotizacion']
						hora_cotizacion=form.cleaned_data['hora_cotizacion']
						q=Cotizacion()
					
						q.rut_vendedor=rut_vendedor
						q.fecha_cotizacion=fecha_cotizacion
						q.hora_cotizacion=hora_cotizacion
						q.save()
						p=Productos.objects.all()
						p.delete()
					
					
						
						
				form = cotizarform()
				
				productos=Productos.objects.all()
				ctx={'productos':productos,'form':form}
				return render_to_response('carro-cotizar-vendedor.html',ctx,context_instance=RequestContext(request))
			else:
				form = cotizarform()
				
				productos=Productos.objects.all()
				ctx={'productos':productos,'form':form}
				return render_to_response('carro-cotizar-vendedor.html',ctx,context_instance=RequestContext(request))
				
				
				
				
def material_vendedor_view(request):


		if request.method == "POST":
			lala=request.POST.keys()
		
			
			
			for clave in lala:
				if clave==request.POST[clave]:
					p=Material.objects.filter(cod_material=clave)
					p.delete()
				
					
			materiales=Material.objects.all()
			ctx={'materiales':materiales}
			return render_to_response('material-vendedor.html',ctx,context_instance=RequestContext(request))
		else: #GET
			materiales=Material.objects.all()
			ctx={'materiales':materiales}
			return render_to_response('material-vendedor.html',ctx,context_instance=RequestContext(request))
			
			
			
			
def kits_view(request):
		
		
		if request.method == "POST":
			
			form2=buscaform(request.POST)
		
			
			if request.POST["busca"]=='agregar':
				lala=request.POST.keys()
			
			
			
				for clave in lala:
					if clave==request.POST[clave]:
						p=Material.objects.get(cod_material=clave)
						q=Productos()
						
						q.codigo_material=p.cod_material
						q.marca=p.id_marca
						q.modelo=p.id_modelo
						q.codigo_tipo_mat=p.cod_tipo_mat
						q.nombre=p.nombre_material
						q.precio=p.precio_material
						q.cantidad=p.cantidad_material
						q.save()
						
				
			
				grupos=Tipo_material.objects.all()
				form2 = buscaform()
				ctx={'form2':form2,"grupos":grupos}
				return render_to_response('kits-adm.html',ctx,context_instance=RequestContext(request))
				
			else:
				lala=request.POST.keys()
				
				for clave in lala:
					if clave=="opcion":	
						materiales=Material.objects.filter(cod_tipo_mat=request.POST["opcion"]) 
						
						form2 = buscaform()
						grupos=Tipo_material.objects.all()
						ctx={'form2':form2,"materiales":materiales,"grupos":grupos}
						return render_to_response('kits-adm.html',ctx,context_instance=RequestContext(request))
					else:
						grupos=Tipo_material.objects.all()
						form2=buscaform()
						ctx={'form2':form2,"grupos":grupos}
						return render_to_response('kits-adm.html',ctx,context_instance=RequestContext(request))		
			
		else: #GET
			grupos=Tipo_material.objects.all()
			form2=buscaform()
			ctx={'form2':form2,"grupos":grupos}
			return render_to_response('kits-adm.html',ctx,context_instance=RequestContext(request))			


			
			
			
def carro_kits_view(request):
			
			valor=0
			
			if request.method == "POST":
				form=kitsform(request.POST)
				lala=request.POST.keys()
				
				if request.POST["elige"]=='eliminar':
			
					for clave in lala:
						if clave==request.POST[clave]:
							p=Productos.objects.filter(codigo_material=clave)
							p.delete()
						
							
				else:
					p=Productos.objects.all()
					
					for clave in p:
						aa=request.POST[str(clave.marca)+str(clave.modelo)+str(clave.nombre)]
						if aa=="":
							valor=1
						
					
					if valor==0:
						for clave in p:
							aa=request.POST[str(clave.marca)+str(clave.modelo)+str(clave.nombre)]
							w=Productos.objects.get(marca=clave.marca,modelo=clave.modelo,nombre=clave.nombre)
							w.cantidad=int(aa)
							w.save()
						
						
					if form.is_valid() and valor==0 :
						
						nombre=form.cleaned_data['nombre_kits']
						precio=form.cleaned_data['precio_kits']
						
						q=Kits()
						
						q.nombre_kits=nombre
						q.precio_kits=precio
						q.save()
						lala=Kits.objects.all()
						largo=len(lala)
						lol=lala[largo-1]					
						p=Productos.objects.all()
						
						for i in p:
							z=Detalle_kits()
							z.cod_kits=lol
							z.cod_mat=i.codigo_material
							z.id_marca=i.marca
							z.id_modelo=i.modelo
							z.cod_tipo_mat=i.codigo_tipo_mat
							z.nombre_material=i.nombre
							z.precio_material=i.precio
							z.cantidad_material=i.cantidad
							z.save()
						p.delete()
						form = kitsform()
					else:
						if form.is_valid!=True:
							productos=Productos.objects.all()
							ctx={'productos':productos,'form':form}
							return render_to_response('carro_kits.html',ctx,context_instance=RequestContext(request))
				
				form =kitsform()
				#productos=Productos.objects.all()
				ctx={'form':form}
				return render_to_response('carro_kits.html',ctx,context_instance=RequestContext(request))
			else:
				form = kitsform()
				
				productos=Productos.objects.all()
				ctx={'productos':productos,'form':form}
				return render_to_response('carro_kits.html',ctx,context_instance=RequestContext(request))		




def eliminar_kits_view(request):
			
			if request.method == "POST":
				lala=request.POST.keys()
				
				
			
			
				for clave in lala:
					if "Eliminar"==request.POST[clave]:
						p=Kits.objects.filter(cod_kits=clave)
						p.delete()
						
					if "Ver"==request.POST[clave]:	
							
						detalles=Detalle_kits.objects.filter(cod_kits=clave)
						ctx={'detalles':detalles}
						return render_to_response('detalle_kits.html',ctx,context_instance=RequestContext(request))
							
							
							
						
				
				kits=Kits.objects.all()
				ctx={'kits':kits}
				return render_to_response('eliminar-kits-adm.html',ctx,context_instance=RequestContext(request))
			else:
				kits=Kits.objects.all()
				ctx={'kits':kits}
				return render_to_response('eliminar-kits-adm.html',ctx,context_instance=RequestContext(request))				