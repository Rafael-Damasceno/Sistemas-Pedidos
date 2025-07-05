# definição da classe
class Pedido:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor
    def __init__(self, codigo_pedido, cliente_pedido, tipo_entrega, local):
        self.__codigo_pedido = codigo_pedido
        self.__cliente_pedido = cliente_pedido
        self.__status = 0  # 0 = aberto, 1 = finalizado/pago
        self.__tipo_entrega = tipo_entrega
        self.__local = local
        # criando uma estrutura map em python para armzenar itens do pedido
        self.__itens_pedidos = []

    @property
    def _status(self):
        return self.__status

    @_status.setter
    def _status(self, value):
        self.__status = value

    @property
    def _codigo_pedido(self):
        return self.__codigo_pedido

    @_codigo_pedido.setter
    def _codigo_pedido(self, value):
        self.__codigo_pedido = value

    @property
    def _cliente_pedido(self):
        return self.__cliente_pedido

    @_cliente_pedido.setter
    def _cliente_pedido(self, value):
        self.__cliente_pedido = value

    @property
    def _tipo_entrega(self):
        return self.__tipo_entrega

    @_tipo_entrega.setter
    def _tipo_entrega(self, value):
        self.__tipo_entrega = value        

    @property
    def _local(self):
        return self.__local

    @_local.setter
    def _local(self, value):
        self.__local = value   

    @property
    def _itens_pedidos(self):
        return self.__itens_pedidos

    @_itens_pedidos.setter
    def _itens_pedidos(self, value):
        self.__itens_pedidos = value

    def adicionar_item_ao_pedido(self, itempedido):
        self.__itens_pedidos.append(itempedido)

    def remover_item_pedido(self, codigo_item):
        self.__itens_pedidos.pop(codigo_item)

    def quantidade_itens_pedido(self):
        return int(len(self.__itens_pedidos))
        # return self.__itens_pedidos.__sizeof__

       # 🔽 Novo método público que retorna o preço total
    def calcular_preco_total(self):
        return sum(item._preco_item for item in self.__itens_pedidos)   

    def toString(self):
        print("** INÍCIO DAS INFORMAÇÕES DO PEDIDO **")
        print("CÓDIGO DO PEDIDO:", self._codigo_pedido, end='\t')
        print("STATUS DO PEDIDO:", self._status)
        print("QUANTIDADE DE ITENS DO PEDIDO:", self.quantidade_itens_pedido())

        for i, item in enumerate(self._itens_pedidos):
            print(f"\t #ITEM: {i}", end='\t')
            print("PRODUTO:", item._produto._descricao, end='\t')
            print("QTD (#):", item._quantidade, end='\t')
            print("SUBTOTAL (R$):", item._preco_item)

        print("PREÇO TOTAL DO PEDIDO:", self.calcular_preco_total())
        print("** FIM DAS INFORMAÇÕES DO PEDIDO **")
