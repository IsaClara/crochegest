from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_encomendas, name='listar_encomendas'),
    path('cliente/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('encomenda/cadastrar/', views.cadastrar_encomenda, name='cadastrar_encomenda'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('encomenda/<int:id>/editar/', views.editar_encomenda, name='editar_encomenda'),
    path('encomenda/<int:id>/excluir/', views.excluir_encomenda, name='excluir_encomenda'),
    path('cliente/<int:id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('cliente/<int:id>/excluir/', views.excluir_cliente, name='excluir_cliente'),

]