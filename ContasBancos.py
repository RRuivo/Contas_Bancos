from datetime import datetime
import pytz
import time

class ContaCorrente: 
    """
    Cria um objeto ContaCorrente para gerenciamento das contas dos clientes

    Atributos:
        nome (str): NOme do Client:
        cpf (str): CPF do cliente
        agencia (int): Agencia do banco do cliente
        num_conta (int): Número da Conta corrente
        saldo (int): saldo inicial da conta do cliente
        limite (int): Limite do cheque especial
        transacoes: Histórico de transações do cliente
    """


    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Saldo insuficiente para sacar esse valor R$ {:,.2f}'.format(valor))
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequespecial(self):
        print('Seu limite de cheque especial é de R$ {:,.2f}'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Histórico de transações:')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


#Programa
conta_Ruivo = ContaCorrente('Ruivo', '111.222.333-44', 1234, 34062)
conta_Ruivo.consultar_saldo()

conta_Ruivo.depositar(1000)
conta_Ruivo.consultar_saldo()

time.sleep(5)
conta_Ruivo.sacar_dinheiro(750)

print('Saldo Final:')
conta_Ruivo.consultar_saldo()
conta_Ruivo.consultar_limite_chequespecial()

print('-' * 20)
print(conta_Ruivo.consultar_historico_transacoes())

print('-' * 20)
conta_talita = ContaCorrente('Talita', '111.222.333-55', 1234, 34063)
conta_Ruivo.transferir(200, conta_talita)

conta_Ruivo.consultar_saldo()
conta_talita.consultar_saldo()

conta_Ruivo.consultar_historico_transacoes()
conta_talita.consultar_historico_transacoes()