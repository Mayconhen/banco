from conta import contas
import pandas

print("**BEM VINDO AO BANCO HENRIQUE**")
planilha = pandas.read_excel('contas.xlsx')
usuario = int(input("Digite seu CPF:"))
senha= int(input("Digite sua senha:"))

if contas.validar(usuario, senha) == True:
     print("Logado com sucesso!")
else: 
     print("Conta não existe.")




