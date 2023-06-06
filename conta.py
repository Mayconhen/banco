import pandas
import openpyxl

planilha_caminho = 'contas.xlsx'

class contas:
    def __init__(self, nome):
        self.nome = nome

    def criarcontas():
        planilha_caminho = 'contas.xlsx'
        planilha = pandas.read_excel(planilha_caminho)
        lista = []
        print("Criando contas...")
        for index, row in planilha.iterrows():
            nome = row["NOME"]
            agencia = row["AGENCIA"]
            numero_conta = row["CONTA"]
            saldo = row["SALDO"]
            limite = row["LIMITE"]
            lista.append(contas(nome))
            lista.append(contas(agencia))
            lista.append(contas(numero_conta))
            lista.append(contas(saldo))
            print("Nome:{}\nAgencia:{}\nConta:{}\nSaldo:{}\n".format(row["NOME"], row["AGENCIA"], row["CONTA"], row["SALDO"]))

    def extrato(conta):
        planilha = pandas.read_excel('contas.xlsx')
        planConta = planilha["SALDO"]
        print(planConta[conta])
        valor ={"SALDO": planConta}


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
        

        
    


        
        