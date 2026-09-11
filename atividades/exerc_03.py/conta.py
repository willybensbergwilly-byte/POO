class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")

    @property
    def saldo(self):
        return self._saldo


# Criando duas contas
conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)


# Operações da conta 1
conta1.depositar(200)
conta1.sacar(300)

print("Titular:", conta1.titular)
print("Saldo:", conta1.saldo)


# Operações da conta 2
conta2.depositar(100)
conta2.sacar(700)

print("Titular:", conta2.titular)
print("Saldo:", conta2.saldo)

             