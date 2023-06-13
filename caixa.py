from conta import contas
import pandas


print("\n**BANCO**\n")
planilha = pandas.read_excel('contas.xlsx')
usuario = int(input("Digite sua conta:"))
senha= int(input("Digite sua senha:"))


if contas.validar(usuario, senha) == True:
     while True:
          opcao =int(input("1 - Verificar Extrato\n2 - Sacar\n3 - Depositar\n4 - Sair do banco\n"))
          if opcao == 1:
               contas.extrato(usuario)
          elif opcao == 2:
               quantia = int(input("Digite a quantia que deseja sacar: "))
               contas.sacar(usuario, quantia)
          elif opcao == 3:
               deposito = int(input("Digite a quantia que deseja depositar: "))
               contas.depositar(usuario,deposito)
          elif opcao == 4:
               print("Saindo do banco...")
               break
          else:
               print("Dados inseridos inválidos.")
               






