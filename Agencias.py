class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do recomendado. Caixa atual: R$ {:,.2f}'.format(self.caixa))
        else:
            print('Valor de caixa está OK. Caixa atual: R$ {:,.2f}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro insuficiente em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


agencia1 = Agencia('11 4111-3333', '111.222.333/001-50', 4568)

agencia1.caixa = 1000000
agencia1.verificar_caixa()

agencia1.adicionar_cliente('Ruivo', '11122233301', 10000)
print(agencia1.clientes)

agencia1.emprestar_dinheiro(1500, '11122233301', 0.02)
print(agencia1.emprestimos)