from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import *
admin.autodiscover()


from django.conf import settings
import settings


urlpatterns = patterns('',
		url(r'^time/$', current_datetime,name="vista_time"),
		
		
		url(r'^time/plus/(\d{1,2})/$', hours_ahead),
        url(r'^material_adm/',material_view,name="material_adm"),
		url(r'^actualizar_material/',actualizar_material_view, name="actualizar_material"),
        url(r'^sobre/$',sobre),
		url(r'^eliminar_material_adm/',eliminar_material_view,name="eliminar_material_adm"),
		url(r'^agregar_proveedor/',proveedor_view,name="agregar_proveedor"),
		url(r'^actualizar_proveedor/',actualizar_proveedor_view, name="actualizar_proveedor"),
		url(r'^eliminar_proveedor/',eliminar_proveedor_view,name="eliminar_proveedor"),
		url(r'^agregar_vendedor/',vendedor_view,name="agregar_vendedor"),
		url(r'^actualizar_vendedor/',actualizar_vendedor_view, name="actualizar_vendedor"),
		url(r'^eliminar_vendedor/',eliminar_vendedor_view,name="eliminar_vendedor"),
		url(r'^bodega_adm/',bodega_view,name="bodega_adm"),
		url(r'^cotizar_adm/',cotizar_view,name="cotizar_adm"),
		url(r'^eliminar_cotizar/',eliminar_cotizar_view,name="eliminar_cotizar"),
		url(r'^carro_cotizar/',carro_cotizar_view,name="carro_cotizar"),
		url(r'^ventas_adm/',ventas_view,name="ventas_adm"),
		url(r'^kits_adm/',kits_view,name="kits_adm"),
		url(r'^carro_kits_adm/',carro_kits_view,name="carro_kits_adm"),
		url(r'^eliminar_kits_adm/',eliminar_kits_view,name="eliminar_kits_adm"),
		url(r'^compatible/',compatible_view,name="compatible"),
		url(r'^eliminar_ventas/',eliminar_ventas_view,name="eliminar_ventas"),
		url(r'^carro_ventas/',carro_ventas_view,name="carro_ventas"),
		
		url(r'^ventas_vendedor/',ventas_vendedor_view,name="ventas_vendedor"),
		url(r'^eliminar_ventas_vendedor/',eliminar_ventas_vendedor_view,name="eliminar_ventas_vendedor"),
		url(r'^carro_ventas_vendedor/',carro_ventas_vendedor_view,name="carro_ventas_vendedor"),
		
		url(r'^cotizar_vendedor/',cotizar_vendedor_view,name="cotizar_vendedor"),
		url(r'^eliminar_cotizar_vendedor/',eliminar_cotizar_vendedor_view,name="eliminar_cotizar_vendedor"),
		url(r'^carro_cotizar_vendedor/',carro_cotizar_vendedor_view,name="carro_cotizar_vendedor"),
		
		url(r'^material_vendedor/',material_vendedor_view,name="material_vendedor"),
		
		url(r'^orden_adm/',orden_view,name="orden_adm"),
		url(r'^carro_orden/',carro_orden_view,name="carro_orden"),
		url(r'^eliminar_orden/',eliminar_orden_view,name="eliminar_orden"),
		url(r'^despacho_adm/',despacho_view,name="despacho_adm"),
		url(r'^carro_despacho/',carro_despacho_view,name="carro_despacho"),
		url(r'^eliminar_despacho/',eliminar_despacho_view,name="eliminar_despacho"),
		url(r'^agregar_bodega/',bodega_view, name="vista_bodega"),
		url(r'^actualizar_bodega/',actualizar_bodega_view, name="actualizar_bodega"),
		url(r'^eliminar_bodega/',eliminar_bodega_view,name="eliminar_bodega"),
		url(r'^agregar_area/',area_view, name="vista_area"),
		url(r'^actualizar_area/',actualizar_area_view, name="actualizar_area"),
		url(r'^eliminar_area/',eliminar_area_view,name="eliminar_area"),
		url(r'^agregar_grupo/',grupo_view, name="vista_grupo"),
		url(r'^actualizar_grupo/',actualizar_grupo_view, name="actualizar_grupo"),
		url(r'^eliminar_grupo/',eliminar_grupo_view,name="eliminar_grupo"),
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(admin.site.urls)),
		url(r'^login/',Login_view, name="vista_login"),
		url(r'^templates/(?P<path>.*)','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
		
		(r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 
            'django.views.static.serve',
           {'document_root' : settings.STATIC_ROOT }),
		

		
		
)


