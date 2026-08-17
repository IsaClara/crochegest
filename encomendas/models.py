from django.db import models

class Cliente(models.Model):
    '''Dados sobre o cliente cadastrado:
    Nome
    Telefone
    Encomenda
    '''
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural =  'Clientes'

    def __str__(self):
        return self.nome
    

class Encomenda(models.Model):
    '''Cada encomenda tem: 
    Cliente
    Produto
    Cor
    Data do pedido
    Data de entrega
    Valor
    Status
'''
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('A', 'Em andamento'),
        ('F', 'Finalizado'),
        ('E', 'Entregue'),
    ]
    produto = models.CharField(max_length=150)
    cor = models.CharField(max_length=20)
    data_pedido = models.DateTimeField(auto_now_add=True) #adiciona automaticamente a data do registro
    data_entrega = models.DateTimeField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=1, choices= STATUS_CHOICES, default= 'P')
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural =  'Encomendas'

    def __str__(self):
        return self.produto