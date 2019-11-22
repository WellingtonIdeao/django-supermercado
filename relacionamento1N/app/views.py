from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

# Create your views here.
from . models import *


class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['nome', 'categoria']


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco', 'marca']


def marca_list(request, template_name='marca/marca_list.html'):
    query = request.GET.get('busca')
    if query:
        marca= Marca.objects.filter(nome__icontains=query)
    else:
        marca = Marca.objects.all()
    marcas = {'lista': marca}
    return render(request, template_name, marcas)


def marca_new(request, template_name='marca/marca_form.html'):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('marca_list')
    return render(request, template_name, {'form': form})


def marca_edit(request, pk, template_name='marca/marca_form.html'):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('marca_list')
    else:
        form = MarcaForm(instance=marca)
    return render(request, template_name, {'form': form})


def marca_delete(request, pk, template_name='marca/marca_delete.html'):
    marca = Marca.objects.get(pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('marca_list')
    return render(request, template_name,{'marca': marca})


def produto_list(request, template_name='produto/produto_list.html'):
    query = request.GET.get('busca')
    if query:
        produto = Produto.objects.filter(descricao__icontains=query)
    else:
        produto = Produto.objects.all()
    produtos = {'lista': produto}
    return render(request, template_name, produtos)


def produto_new(request, template_name='produto/produto_form.html'):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request, template_name, {'form': form})


def produto_edit(request, pk, template_name='produto/produto_form.html'):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, template_name, {'form': form})


def produto_delete(request, pk, template_name='produto/produto_delete.html'):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('produto_list')
    return render(request, template_name, {'produto': produto})


def marca_produto_list(request, pk, template_name='marca/marca_produto_list.html'):
    produto = Produto.objects.filter(marca=pk)
    return render(request, template_name, {'produtos': produto})


