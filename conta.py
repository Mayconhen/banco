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
            cpf = (row["CPF"])
            senha = (row["SENHA"])
            lista.append(contas(nome))
            lista.append(contas(agencia))
            lista.append(contas(numero_conta))
            lista.append(contas(saldo))
            lista.append(contas(limite))
            lista.append(contas(cpf))
            lista.append(contas(senha))
            print("Nome:{}\nAgencia:{}\nConta:{}\nSaldo:{}\nCPF:{}\n".format(row["NOME"], 
            row["AGENCIA"], row["CONTA"], row["SALDO"], row["CPF"], row["SENHA"]))

    def extrato(conta):
        planilha = pandas.read_excel('contas.xlsx')
        planConta = planilha["SALDO"]
        print("Saldo da conta selecionada:R${}".format(planConta[conta]))

    def retornarcontas():
        planilha_caminho = 'contas.xlsx'
        planilha = pandas.read_excel(planilha_caminho)
        print(planilha)       

    def retornardadosconta(numero):
        planilha = pandas.read_excel('contas.xlsx')
        print(planilha.iloc[[numero]])

    def depositar(conta, valor):
        planilha = pandas.read_excel('contas.xlsx')
        planNome = planilha["NOME"]
        planAg = planilha["AGENCIA"]
        planConta = planilha["CONTA"]
        planSaldo = planilha["SALDO"].astype("int64")
        planLimite = planilha["LIMITE"]
        planSaldo[conta] = planSaldo[conta] + valor
        valor = {
            "NOME":planNome,
            "AGENCIA": planAg,
            "CONTA": planConta,
            "SALDO": planSaldo,
            "LIMITE": planSaldo
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
        planCpf = planilha["CPF"]
        planSenha = planilha["SENHA"]
        valor = {
            "NOME":planNome,
            "AGENCIA": planAg,
            "CONTA": planConta,
            "SALDO": planSaldo,
            "LIMITE": planLimite,
            "CPF": planCpf,
            "SENHA": planSenha
        }
        df = pandas.DataFrame(valor).round(1)
        df.to_excel('contas.xlsx', index = False)

        if usuario in planCpf and senha in planSenha:
            return True
        else:
            return False

        
    


        
        