# definição da classe
class NotaFiscal:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor 
    def __init__(self, precoFinal, data, id):
        self.__id = id # __ modificador de acesso private
        self.__precoFinal = precoFinal
        self.__data = data
        

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _precoFinal(self):
        return self.__precoFinal

    @_precoFinal.setter
    def _precoFinal(self, value):
        self.__precoFinal = value

    @property
    def _data(self):
        return self.__data

    @_data.setter
    def _data(self, value):
        self.__data = value

  