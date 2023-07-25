import pandas as pd

caminhoplanilha = r'c:\Users\maycon.henrique\Downloads\input.xlsx'
planilha = pd.read_excel(caminhoplanilha)

for index, row in planilha.iterrows():
    caminhoplanilha = r'c:\Users\maycon.henrique\Downloads\input.xlsx'
    planilha = pd.read_excel(caminhoplanilha)
    lista = []
    codlote = row["CODLOTE"]
    data = row["DATA"]
    debito = row["DEBITO"]
    valor = row["VALOR"]
    data2 = row["DATA2"]
    codhistp = row["CODHISTP"]
    complemento = row["COMPLEMENTO"]
    lista.append(planilha[codlote])
    lista.append(planilha[data])
    lista.append(planilha[debito])
    lista.append(planilha[valor])
    lista.append(planilha[data2])
    lista.append(planilha[codhistp])
    lista.append(planilha[complemento])
    valor = {
            "CODLOTE":codlote,
            "DATA": data,
            "DEBITO": debito,
            "VALOR": valor,
            "DATA2": data2,
            "CODHISTP": codhistp,
            "COMPLEMENTO": complemento
 
        }

    df = pd.DataFrame(valor).round(1)
    df.to_excel('contas.xlsx', index = False)

    print[df.at['0', 'CODLOTE']]
