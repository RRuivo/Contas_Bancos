class ContaCorrente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None #inicializar atributos sem valor

    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def _limite_conta(self): #colocar o _ no nome do método indica que esse método só pode ser usado dentro da classe
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Saldo insuficiente para sacar esse valor R$ {:,.2f}'.format(valor))
            self.consultar_saldo()
        else:
            self.saldo -= valor

    def consultar_limite_chequespecial(self):
        print('Seu limite de cheque especial é de R$ {:,.2f}'.format(self._limite_conta()))


#Programa
conta_Ruivo = ContaCorrente('Ruivo', '111.222.333-44')
conta_Ruivo.consultar_saldo()

#depositando saldo
conta_Ruivo.depositar(1000)
conta_Ruivo.consultar_saldo()

#sacando dinheiro da conta
conta_Ruivo.sacar_dinheiro(2850)

print('Saldo Final:')
conta_Ruivo.consultar_saldo()
conta_Ruivo.consultar_limite_chequespecial()
