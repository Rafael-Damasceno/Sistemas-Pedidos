# definição da classe
class Funcionario:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor 
    def __init__(self, nome, telefone, salario, funcao):
        self.__nome = nome # __ modificador de acesso private
        self.__telefone = telefone
        self.__salario = salario
        self.__funcao = funcao

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

    @property
    def _salario(self):
        return self.__salario

    @_salario.setter
    def _salario(self, value):
        self.__salario = value

    @property
    def _funcao(self):
        return self.__funcao

    @_funcao.setter
    def _funcao(self, value):
        self.__funcao = value