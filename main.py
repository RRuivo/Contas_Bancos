import time
from ContasBancos import ContaCorrente, CartaoCredito
from Agencias import Agencia, AgenciaComum, AgenciaPremium, AgenciaVirtual

#Programa
conta_Ruivo = ContaCorrente('Ruivo', '111.222.333-44', 1234, 34062)
conta_Ruivo.consultar_saldo()

cartao_Ruivo = CartaoCredito('Ruivo', conta_Ruivo)
print(cartao_Ruivo.conta_corrente.num_conta)
print(cartao_Ruivo.numero)
print(cartao_Ruivo.cod_seguranca)
print(cartao_Ruivo.validade)

cartao_Ruivo.senha = '2345'
print(cartao_Ruivo.senha)

print(conta_Ruivo.__dict__) 
print(cartao_Ruivo.__dict__)

#depositando saldo
conta_Ruivo.depositar(1000)
conta_Ruivo.consultar_saldo()

time.sleep(5)

#sacando dinheiro da conta
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

#Criando agências
agencia1 = Agencia('11 4111-3333', '111.222.333/001-50', 4568)
agencia1.caixa = 1000000
agencia1.verificar_caixa()

agencia1.adicionar_cliente('Ruivo', '11122233301', 10000)
print(agencia1.clientes)

agencia1.emprestar_dinheiro(1500, '11122233301', 0.02)
print(agencia1.emprestimos)

#agência virtual
agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', '11 4111-0000', '111.222.333/001-51')
agencia_virtual.verificar_caixa()
print('O site de nossa agência virtual é : {}'.format(agencia_virtual.site))

agencia_virtual.depositar_paypal(20000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)

#agência física
agencia_comum = AgenciaComum('11 4111-3334', '111.222.333/001-52')
print(agencia_comum.verificar_caixa())
print('O número da agência é: {}'.format(agencia_comum.numero))
agencia_comum.adicionar_cliente('Ruivo', '111.222.333-45', 5000)
print(agencia_comum.clientes)

#agência premium
agencia_premium = AgenciaPremium('11 4111-3335', '111.222.333/001-52')
agencia_premium.verificar_caixa()
print('O número da agência premium é: {}'.format(agencia_premium.numero))
agencia_premium.adicionar_cliente('Rodrigo', '111.222.333-44', 1000001)
print(agencia_premium.clientes)