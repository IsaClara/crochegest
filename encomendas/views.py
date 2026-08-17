from django.shortcuts import render, redirect
from .models import Cliente, Encomenda



def listar_encomendas(request):
    encomendas = Encomenda.objects.all()

    return render(
        request,
        'encomendas/listar_encomendas.html',
        {'encomendas': encomendas}
    )

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']

        Cliente.objects.create(
            nome=nome,
            telefone=telefone
        )

        return redirect('listar_encomendas')

    return render(request, 'encomendas/cadastrar_cliente.html')



def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        cliente.nome = request.POST['nome']
        cliente.telefone = request.POST['telefone']

        cliente.save()

        return redirect('listar_clientes')

    return render(
        request,
        'encomendas/editar_cliente.html',
        {'cliente': cliente}
    )

def excluir_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()

    return redirect('listar_clientes')



def cadastrar_encomenda(request):
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        produto = request.POST['produto']
        cor = request.POST['cor']
        data_entrega = request.POST['data_entrega']
        valor = request.POST['valor']
        status = request.POST['status']

        cliente = Cliente.objects.get(id=cliente_id)

        Encomenda.objects.create(
            cliente=cliente,
            produto=produto,
            cor=cor,
            data_entrega=data_entrega,
            valor=valor,
            status=status
        )

        return redirect('listar_encomendas')

    return render(
        request,
        'encomendas/cadastrar_encomenda.html',
        {
            'clientes': clientes,
            'status_choices': Encomenda.STATUS_CHOICES
        }
    )

def editar_encomenda(request, id):
    encomenda = Encomenda.objects.get(id=id)
    clientes = Cliente.objects.all()


    if request.method == 'POST':
        encomenda.cliente_id = request.POST['cliente']
        encomenda.produto = request.POST['produto']
        encomenda.cor = request.POST['cor']
        encomenda.data_entrega = request.POST['data_entrega']
        encomenda.valor = request.POST['valor']
        encomenda.status = request.POST['status']

        encomenda.save()

        return redirect('listar_encomendas')

    return render(
        request,
        'encomendas/editar_encomenda.html',
        {
            'encomenda': encomenda,
            'clientes': clientes,
            'status_choices': Encomenda.STATUS_CHOICES
        }
    )

def excluir_encomenda(request, id):
    encomenda = Encomenda.objects.get(id=id)
    encomenda.delete()

    return redirect('listar_encomendas')



def listar_clientes(request):
    clientes = Cliente.objects.all()

    return render(
        request,
        'encomendas/listar_clientes.html',
        {'clientes': clientes}
    )