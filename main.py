from ContasBancos import ContaCorrente, CartaoCredito

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

print(conta_Ruivo.__dict__) #__dict__ mostra todos atributos da instância da classe
print(cartao_Ruivo.__dict__)

# #depositando saldo
# conta_Ruivo.depositar(1000)
# conta_Ruivo.consultar_saldo()
#
# time.sleep(5)
# #sacando dinheiro da conta
# conta_Ruivo.sacar_dinheiro(750)
#
# print('Saldo Final:')
# conta_Ruivo.consultar_saldo()
# conta_Ruivo.consultar_limite_chequespecial()
#
# print('-' * 20)
# print(conta_Ruivo.consultar_historico_transacoes())
#
# print('-' * 20)
# conta_talita = ContaCorrente('Talita', '111.222.333-55', 1234, 34063)
# conta_Ruivo.transferir(200, conta_talita)
#
# conta_Ruivo.consultar_saldo()
# conta_talita.consultar_saldo()
#
# conta_Ruivo.consultar_historico_transacoes()
# conta_talita.consultar_historico_transacoes()

