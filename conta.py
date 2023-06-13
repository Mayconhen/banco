import pandas
import openpyxl

planilha_caminho = 'contas.xlsx'

class contas:
    def __init__(self, nome):
        self.nome = nome

    def retornarcontas(usuario, senha):
        planilha_caminho = 'contas.xlsx'
        planilha = pandas.read_excel(planilha_caminho)
        lista = []
        for index, row in planilha.iterrows():
            nome = row["NOME"]
            agencia = row["AGENCIA"]
            numero_conta = row["CONTA"]
            saldo = row["SALDO"]
            limite = row["LIMITE"]
            usuario = (row["USUARIO"])
            senha = (row["SENHA"])
            lista.append(contas(nome))
            lista.append(contas(agencia))
            lista.append(contas(numero_conta))
            lista.append(contas(saldo))
            lista.append(contas(limite))
            lista.append(contas(usuario))
            lista.append(contas(senha))
            print("Nome:{}\nAgencia:{}\nConta:{}\nSaldo:{}\nCPF:{}\n".format(row["NOME"], 
            row["AGENCIA"], row["CONTA"], row["SALDO"], row["USUARIO"], row["SENHA"]))

    def extrato(usuario):
        planilha = pandas.read_excel('contas.xlsx')
        planSaldo = planilha["SALDO"].astype("int64")
        print("Saldo da conta: R$ {}".format(planSaldo[usuario])) 

    def retornardadosconta(numero):
        planilha = pandas.read_excel('contas.xlsx')
        print(planilha.iloc[[numero]])

    def depositar(usuario,valor):
        planilha = pandas.read_excel('contas.xlsx')
        planNome = planilha["NOME"]
        planAg = planilha["AGENCIA"]
        planConta = planilha["CONTA"]
        planSaldo = planilha["SALDO"].astype("int64")
        planLimite = planilha["LIMITE"]
        planUsuario = planilha["USUARIO"].astype("int64")
        planSenha = planilha["SENHA"].astype("int64")
        planSaldo[usuario] = planSaldo[usuario] + valor
        print("Foi depositado R${} na sua conta!".format(valor))
        valor = {
            "NOME":planNome,
            "AGENCIA": planAg,
            "CONTA": planConta,
            "SALDO": planSaldo,
            "LIMITE": planLimite,
            "USUARIO": planUsuario,
            "SENHA": planSenha
        }
        df = pandas.DataFrame(valor).round(1)
        df.to_excel('contas.xlsx', index = False)


    def sacar(usuario, valor):
        planilha = pandas.read_excel('contas.xlsx')
        planNome = planilha["NOME"]
        planAg = planilha["AGENCIA"]
        planConta = planilha["CONTA"]
        planSaldo = planilha["SALDO"].astype("int64")
        planLimite = planilha["LIMITE"]
        planUsuario = planilha["USUARIO"].astype("int64")
        planSenha = planilha["SENHA"].astype("int64")
        planSaldo[usuario] = planSaldo[usuario] - valor
        print("Foi sacado R${} da sua conta!".format(valor))
        valor = {
            "NOME":planNome,
            "AGENCIA": planAg,
            "CONTA": planConta,
            "SALDO": planSaldo,
            "LIMITE": planLimite,
            "USUARIO": planUsuario,
            "SENHA": planSenha
        }
        df = pandas.DataFrame(valor).round(1)
        df.to_excel('contas.xlsx', index = False)
        

    def validar(usuario, senha):
        planilha = pandas.read_excel('contas.xlsx')
        planNome = planilha["NOME"]
        planAg = planilha["AGENCIA"]
        planConta = planilha["CONTA"]
        planSaldo = planilha["SALDO"].astype("int64")
        planLimite = planilha["LIMITE"]
        planUsuario = planilha["USUARIO"].astype("int64")
        planSenha = planilha["SENHA"].astype("int64")
        valor = {
            "NOME":planNome,
            "AGENCIA": planAg,
            "CONTA": planConta,
            "SALDO": planSaldo,
            "LIMITE": planLimite,
            "USUARIO": planUsuario,
            "SENHA": planSenha
        }
        df = pandas.DataFrame(valor).round(1)
        df.to_excel('contas.xlsx', index = False)
        if any((planUsuario == usuario) & (planSenha == senha)):
            return True
        else:
            return False
                
        
    


        
        