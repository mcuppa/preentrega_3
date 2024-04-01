from django.urls import path
from. import views


urlpatterns = [
    path('',views.index, name='home'),
    path('pinturas/', views.pinturas, name='pinturas'),
    path('cargar_pintura/', views.cargar_pintura, name='cargar_pintura'),
    path('mostrar_pinturas/', views.mostrar_pinturas, name='mostrar_pinturas'),
    path('buscar_pinturas/', views.buscar_pinturas, name='buscar_pinturas'),
    path('accesorios/', views.accesorios, name='accesorios'),
    path('cargar_accesorios/', views.cargar_accesorios, name='cargar_accesorios'),
    path('mostrar_accesorios/', views.mostrar_accesorios, name='mostrar_accesorios'),
    path('clientes/', views.clientes, name='clientes'),
    path('cargar_clientes/', views.cargar_clientes, name='cargar_clientes'),

    path('mostrar_clientes/', views.mostrar_clientes, name='mostrar_clientes'),

]