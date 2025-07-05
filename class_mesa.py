# definição da classe
class Mesa:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor 
    def __init__(self, numeroMesa ):
        self.__numeroMesa = numeroMesa # __ modificador de acesso private
      

    @property
    def _numeroMesa(self):
        return self.__numeroMesa

    @_numeroMesa.setter
    def _numeroMesa(self, value):
        self.__numeroMesa = value

    