from conta import contas
import pandas

print("\n**BANCO**\n")
planilha = pandas.read_excel('contas.xlsx')
cpf = (input("Digite seu CPF:"))
senha= int(input("Digite sua senha:"))

if contas.validar(cpf, senha):
     print("Logado com sucesso!")
     opcao = None
     while True:
          opcao =int(input("1 - Verificar Extrato\n2 - Sacar\n3 - Depositar\n"))
          if opcao == 1:
               contas.extrato(cpf, senha)
          elif opcao == 2:
               quantia = int(input("Digite a quantia que deseja sacar: "))
               if contas.validar(cpf, senha):
                    contas.sacar(cpf, senha, quantia)
          elif opcao == 3:
               deposito = int(input("Digite a quantia que deseja depositar: "))
               if contas.validar(cpf, senha):
                    contas.depositar(cpf, senha, deposito)
          elif opcao != 4:
               print("Opção inválida.")
          else:
               print("Opção inválida.")
else: 
     print("Dados inseridos não existem.")





