from conta import contas
import pandas

# opcao = int(input("Digite qual conta quer consultar: "))

# contas.retornardadosconta(opcao)
coluna = int(input("Digite o que deseja mudar: 1- CONTA\n2-AGÊNCIA\n3-CONTA\n4-SALDO\n:"))    
iloc = int(input("Digite a conta que deseja mudar: "))
valor = input("Digite o valor que deseja mudar: ")

contas.mudarvalor(iloc,coluna, valor)
contas.extrato()



