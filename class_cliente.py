# definição da classe
class Cliente:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor 
    def __init__(self, nome, telefone):
        self.__nome = nome # __ modificador de acesso private
        self.__telefone = telefone
      

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

  