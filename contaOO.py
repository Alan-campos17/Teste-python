class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de ${self.__saldo} do titular ${self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saque(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite