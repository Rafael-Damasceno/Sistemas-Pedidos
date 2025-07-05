from class_endereco import Endereco
from class_item_pedido import ItemPedido
from class_pedido import Pedido
from class_produto import Produto
from class_cliente import Cliente
from class_mesa import Mesa
from class_funcionario import Funcionario
from class_nota_fiscal import NotaFiscal

from datetime import datetime

def menu_principal():  
    """
    Exibe o menu principal com opções para o usuário interagir com o sistema.

    Returns:
        str: A opção escolhida pelo usuário.
    """
    print('''
        MENU Principal:
        [1] - Controle de vendas
        [2] - Cadastrar novo produto
        [3] - Remover um produto
        [4] - Pesquisar um produto
        [5] - Cadastrar funcionário
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

def menu_pedido():
    """
    Exibe o menu de controle de vendas com opções relacionadas a pedidos.

    Returns:
        str: A opção escolhida pelo usuário.
    """
    print('''
        MENU Vendas:
        [1] - Abrir novo pedido 
        [2] - Adicionar item ao pedido
        [3] - Remover item do pedido
        [4] - Listar itens do pedido
        [5] - Finalizar pedido e imprimir
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

def pedido_adicionar():
    """
    Cria um novo pedido com um endereço fornecido pelo usuário.

    Returns:
        Pedido: Um objeto da classe Pedido com código gerado automaticamente.
    """
    # Gera o código do pedido automaticamente com base na quantidade atual de pedidos
    codido_pedido = len(pedidos) + 1

    # Cadastra o cliente
    cliente_pedido = cadastrar_cliente()

    # Escolha da modalidade de entrega
    print('''
        Escolha a modalidade de entrega:
        [1] - Presencial
        [2] - Entrega
    ''')
    opcao = input('Escolha uma opção: ')

    if opcao == "1":
        local = cadastrar_mesa() 
        tipo_entrega = "Presencial"

    elif opcao == "2":
        local = cadastrar_endereco()
        tipo_entrega = "Entrega"    

    else:
        print("Opção inválida. Pedido não será criado.")
        return None

    return Pedido(codido_pedido, cliente_pedido, tipo_entrega, local)


def pedido_adicionar_item():
    """
    Adiciona um item a um pedido existente, solicitando o código do pedido, 
    código do produto e a quantidade. 
    Exibe mensagens de erro caso o pedido ou produto não existam.

    Returns:
        bool: False se o pedido não existir. None caso contrário.
    """

    int_pedido_selecionado = int(input('Informe o código do pedido para adicionar um novo item: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_produto = int(input('Informe o código do produto para adicionar ao pedido: '))
        produto = buscar_produto_por_codigo(int_codigo_produto)
        if produto:
            int_quantidade_item = int(input('Informe a quantidade do item:'))
            novo_item_pedido = ItemPedido(produto, int_quantidade_item)
            pedido.adicionar_item_ao_pedido(novo_item_pedido)
        else:
            print("Não foi possível adicionar este produto, pois o código do produto não existe!")
        #return Pedido(codido_pedido, endereco_pedido)
    else:
        print("Pedido inexistente")
        return False
    
def pedido_remover_item():
    """
    Remove um item de um pedido existente, solicitando o código do pedido 
    e o número do item.

    Returns:
        bool: False se o pedido não existir. None caso contrário.
    """

    int_pedido_selecionado = int(input('Informe o código do pedido para remover um item selecionado: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_item = int(input('Informe o número do item para remover deste pedido ' + str(pedido._codigo_pedido) + ': '))
        # verifica se número intem informado existe: não faz sentido remover item 5 se ele não existe
        #if pedido.quantidade_itens_pedido() <= int_codigo_item:
        pedido.remover_item_pedido(int_codigo_item)
    else:
        print("Pedido inexistente")
        return False
    
def pedido_listar_items():
    """
    Lista os detalhes de todos os itens de um pedido selecionado.

    Returns:
        bool: False se o pedido não existir. None caso contrário.
    """

    int_pedido_selecionado = int(input('Informe o código do pedido para mais detalhes: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        pedido.toString()
    else:
        print("Pedido inexistente")
        return False



def cadastrar_cliente():
    """
    Solicita os dados do usuario e cria um objeto cliente.

    Returns:
        Cliente: Objeto contendo os dados informados pelo usuário.
    """

    str_nome = str(input('Informe o nome do cliente: '))
    int_telefone = int(input('Informe o telefone do cliente: '))
    
    cliente = Cliente(str_nome, int_telefone,)
    return cliente


def cadastrar_mesa():

    int_numero_mesa = int(input('Informe o número da mesa: '))
    mesa = Mesa(int_numero_mesa)
    return mesa

def cadastrar_endereco():
    """
    Solicita os dados de endereço ao usuário e cria um objeto Endereco.

    Returns:
        Endereco: Objeto contendo os dados informados pelo usuário.
    """

    str_cep = str(input('Informe o cep do endereço: '))
    str_rua = str(input('Informe a rua: '))
    int_num = int(input('Informe o número: '))
    str_complemento = str(input('Informe o complemento do endereço: '))
    str_bairro = str(input('Informe o bairro: '))
    str_cidade = str(input('Informe a cidade: '))
    endereco = Endereco(str_cep, str_rua, int_num,
                        str_complemento, str_bairro, str_cidade)
    return endereco

def cadastrar_produto():
    """
    Solicita os dados do produto ao usuário e cria um objeto Produto.

    Returns:
        Produto: Objeto contendo os dados do produto.
    """

    int_codigo = int(input('Informe o código identificador do produto: '))
    str_nome = str(input('Qual o nome/descrição do produto? '))
    flt_preco = float(input('Informe o valor (ex. 0.00): '))
    date_validade = (input('Informe a validade do produto (formato dd/mm/aaaa): '))
    date_validade = datetime.strptime(date_validade, '%d/%m/%Y')
    int_quantidade = int(input('Informe a quantidade do produto: '))
    return Produto(int_codigo, str_nome, flt_preco, date_validade, int_quantidade)

def remover_produto():
    """
    Remove um produto do dicionário de estoque com base no código informado
    pelo usuário. Exibe mensagem com a descrição do produto removido.
    """

    int_codigo_remocao = int(input('Informe o código do produto para remoção: '))
    produto_remover = estoque_produtos[int_codigo_remocao]
    print("Produto (" + produto_remover._descricao + ") removido!") 
    del estoque_produtos[int_codigo_remocao]

def buscar_produto_por_codigo(int_codigo_produto):
    """
    Busca um produto no dicionário de estoque com base no código informado.

    Args:
        int_codigo_produto (int): Código do produto a ser buscado.

    Returns:
        Produto | bool: O objeto Produto encontrado ou False se não existir.
    """

    # Verifica se existe produto cadastrado
    for chave in estoque_produtos.keys():
        if chave == int_codigo_produto:
            return estoque_produtos[int_codigo_produto]
    return False

def buscar_pedido_por_codigo(int_codigo_pedido):
    """
    Busca um pedido no dicionário de pedidos com base no código informado.

    Args:
        int_codigo_pedido (int): Código do pedido a ser buscado.

    Returns:
        Pedido | bool: O objeto Pedido encontrado ou False se não existir.
    """

    # Verifica se existe produto cadastrado
    for chave in pedidos.keys():
        if chave == int_codigo_pedido:
            return pedidos[int_codigo_pedido]
    return False


def cadastrar_funcionario():

    str_nome = str(input('Qual o nome do funcionário: '))
    int_telefone = int(input('Informe o telefone do funcionário: '))
    float_salario = float(input('Informe o salário do funcionário: '))
    str_funcao = str(input('Informe a função do funcionário: '))
    return Funcionario(str_nome, int_telefone, float_salario, str_funcao)

    
def emitir_nota_fiscal():
    int_codigo_pedido = int(input('Digite o código do pedido: '))
    pedido = buscar_pedido_por_codigo(int_codigo_pedido)
    
    if not pedido:
        print("Pedido não encontrado.")
        return None

    precoFinal = pedido.calcular_preco_total()  # <-- agora sim
    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    nota = NotaFiscal(int_codigo_pedido, precoFinal, data)
    print(f"Nota Fiscal emitida para o pedido {int_codigo_pedido} no valor de R$ {precoFinal:.2f}")
    return nota


estoque_produtos = {}
pedidos = {}

while True:
    # menu_principal
    opcao_escolhida = menu_principal()
    # verificando escolha
    # opc sair
    if (opcao_escolhida == "s"):
        break
    # opc 1
    elif (opcao_escolhida == "1"):
        while True:
            opcao_escolhida = menu_pedido()
            # opc menu vendas - novo pedido
            if (opcao_escolhida == "1"):
                pedido = pedido_adicionar()
                if (pedido):
                    # adiciona pedido ao sistema
                    pedidos[pedido._codigo_pedido] = pedido
            # opc menu vendas - adicionar item    
            elif (opcao_escolhida == "2"):
                pedido_adicionar_item()
            elif (opcao_escolhida == "3"):
                pedido_remover_item()
            elif (opcao_escolhida == "4"):
                pedido_listar_items()
            elif (opcao_escolhida == "5"):
                emitir_nota_fiscal()
            else:
                # Volta para o menu principal
                break
               
    # opc 2
    elif (opcao_escolhida == "2"):
        produto = cadastrar_produto()
        if (produto):
            # adiciona produto ao nosso estoque
            estoque_produtos[produto._codigo_produto] = produto
    # opc 3
    elif (opcao_escolhida == "3"):
        remover_produto()
    # opc 4
    elif (opcao_escolhida == "4"):
        int_codigo_produto = int(input('Informe o código do produto para busca: '))
        produto_pesquisa = buscar_produto_por_codigo(int_codigo_produto)
        if (produto_pesquisa):
            print("Produto encontrado:")
            print(">Código=" + str(produto_pesquisa._codigo_produto))
            print(">Descricao=" + produto_pesquisa._descricao)
            print(">Valor=" + str(produto_pesquisa._preco))
            print(">Validade=" + str(produto_pesquisa._validade))
            print(">Quantidade=" + str(produto_pesquisa._quantidade))
        else:
            print("Produto nâo cadastrado/encontrado.")

    # opc 5
    elif (opcao_escolhida == "5"):
        funcionario = cadastrar_funcionario()
    else:
        print("A opção escolhida é inválida.")
