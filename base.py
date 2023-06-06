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
            lista.append(contas(limite))
            print("Nome:{}\nAgencia:{}\nConta:{}\nSaldo:{}\nLimite:{}\n".format(row["NOME"], row["AGENCIA"], row["CONTA"], row["SALDO"], row["LIMITE"]))

    def extrato():
        planilha_caminho = 'contas.xlsx'
        planilha = pandas.read_excel(planilha_caminho)
        for index, row in planilha.iterrows():
            print("Saldo:{}".format(row["SALDO"]))

    def retornardadosconta(numero, coluna):
        planilha_caminho = 'contas.xlsx'
        planilha = pandas.read_excel(planilha_caminho)
        print(planilha.iloc[[numero]])

    def mudarvalor(iloc,coluna, valor):
        planilha = pandas.read_excel('contas.xlsx')
        planNome = planilha["NOME"]
        planAg = planilha["AGENCIA"]
        planConta = planilha["CONTA"]
        planSaldo = planilha["SALDO"].astype("int64")
        index = 0
        if coluna == 1:
            for row in planConta:
                if row == iloc:
                    planNome[index] = (valor)
                index += 1   
            
        elif coluna == 2:
            for row in planConta:
                if row == iloc:
                    planAg[index] = str(valor)
                index += 1

        elif coluna == 3:
            for row in planConta:
                if row == iloc:
                    planConta[index] = (valor)
                index += 1 

        elif coluna == 4:
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

    def emprestimo(numero, valor):
        planilha = pandas.read_excel('contas.xlsx')
        planLimite = planilha["LIMITE"].astype("int64")
        conta = (planLimite[numero])
        if valor >= conta:
            print("Analisando solicitação...")
            print("Você não possui limite para este empréstimo...")
        else:
            print("Analisando solicitação...")
            print("Valor do emprestimo aprovado.")
        valor = {
            "LIMITE": planLimite.astype("int64")
        }
        
        


# limite.astype("int64")
            # if valor >= limite:
            #     print("Analisando solicitação...")
            #     print("Você não possui limite para este empréstimo...")
            # else:
            #     print("Analisando solicitação...")
            #     print("Valor do emprestimo aprovado.")