from django.conf.urls import url
from . views import *

urlpatterns = [
    url(r'^marca/cadastrar', marca_new, name='marca_new'),
    url(r'^marca/listar', marca_list, name='marca_list'),
    url(r'^marca/editar/(?P<pk>[0-9]+)', marca_edit, name='marca_edit'),
    url(r'^marca/remover/(?P<pk>[0-9]+)', marca_delete, name='marca_delete'),
    url(r'^marca/produto/(?P<pk>[0-9]+)',marca_produto_list, name='marca_produto_list'),

    url(r'^produto/cadastrar/', produto_new, name='produto_new'),
    url(r'^produto/listar', produto_list, name='produto_list'),
    url(r'^produto/editar/(?P<pk>[0-9]+)', produto_edit, name='produto_edit'),
    url(r'^produto/remover/(?P<pk>[0-9]+)', produto_delete, name='produto_delete'),
]