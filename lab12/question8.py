import datetime
nome1 = input("Pessoa 1: Digite seu nome: ")
data_str1 = input(f"Digite a data de nascimento de {nome1} (dd/mm/aaaa): ")
data1 = datetime.datetime.strptime(data_str1, "%d/%m/%Y")

nome2 = input("Pessoa 2: Digite seu nome: ")
data_str2 = input(f"Digite a data de nascimento de {nome2} (dd/mm/aaaa): ")
data2 = datetime.datetime.strptime(data_str2, "%d/%m/%Y")
hoje = datetime.datetime.now()
anive1 = datetime.datetime(hoje.year, data1.month, data1.day)
anive2 = datetime.datetime(hoje.year, data2.month, data2.day)
if anive1 < hoje:
    anive1 = datetime.datetime(hoje.year + 1, data1.month, data1.day)
if anive2 < hoje:
    anive2 = datetime.datetime(hoje.year + 1, data2.month, data2.day)
dife1 = anive1 - hoje
dife2 = anive2 - hoje
if dife1 < dife2:
    print(f"O aniversário de {nome1} está mais próximo! ")
else:
    print(f"O aniversário de {nome2} está mais próximo! ")