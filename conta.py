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
            lista.append(contas(nome))
            lista.append(contas(agencia))
            lista.append(contas(numero_conta))
            lista.append(contas(saldo))
            print("Nome:{}\nAgencia:{}\nConta:{}\nSaldo:{}\n".format(row["NOME"], row["AGENCIA"], row["CONTA"], row["SALDO"]))

    def extrato():
        planilha_caminho = 'contas.xlsx'
        planilha = pandas.read_excel(planilha_caminho)
        for index, row in planilha.iterrows():
            print("Saldo:{}".format(row["SALDO"]))

    def retornardadosconta(numero):
        planilha_caminho = 'contas.xlsx'
        planilha = pandas.read_excel(planilha_caminho)
        print(planilha.iloc[numero])

    def mudarvalor(iloc, valor):
        planilha = pandas.read_excel('contas.xlsx')
        planNome = planilha["NOME"]
        planAg = planilha["AGENCIA"]
        planConta = planilha["CONTA"]
        planSaldo = planilha["SALDO"].astype("int64")
        index = 0
        for row in planConta:
            if row == iloc:
                planSaldo[index] = int(valor)
            index += 1
        valor = {
            "NOME":planNome,
            "AGENCIA": planAg,
            "CONTA": planConta,
            "SALDO": planSaldo.astype("int64")
        }
        df = pandas.DataFrame(valor).round(1)
        df.to_excel('contas.xlsx', index = False)
        

        
    


        
        