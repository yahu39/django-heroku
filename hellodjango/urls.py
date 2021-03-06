from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()
from django.conf.urls.defaults import *
from principal.views import index_view, post


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # (r'^index/$',index_view),
    # (r'^post/(\d{1,2})/$', post),
    # (r'^$','principal.views.lista_bebidas'),
    (r'^sobre/$','principal.views.sobre'),
    (r'^inicio/$','principal.views.inicio'),
    (r'^$','principal.views.inicio'),
    (r'^usuarios/$','principal.views.usuarios'),
    (r'^recetas/$','principal.views.lista_recetas'),
    (r'^receta/(?P<id_receta>\d+)$','principal.views.detalle_receta'),
    (r'^contacto/$','principal.views.contacto'),
    (r'^receta/nueva/$','principal.views.nueva_receta'),
    (r'^comenta/$','principal.views.nuevo_comentario'),
    (r'^usuario/nuevo/$','principal.views.nuevo_usuario'),
    (r'^ingresar/$','principal.views.ingresar'),
    (r'^privado/$','principal.views.privado'),
    (r'^cerrar/$','principal.views.cerrar'),
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^hellodjango/', include('hellodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)
