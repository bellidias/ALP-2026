import datetime
nome1 = input("Pessoa 1: Digite o seu nome: ")
data_str1 = input(f"Digite a data de nascimento de {nome1} (dd/mm/aaaa): ")
data1 = datetime.datetime.strptime(data_str1, "%d/%m/%Y")

nome2 = input("Pessoa 2: Digite o seu nome: ")
data_str2 = input(f"Digite a data de nascimento de {nome2} (dd/mm/aaaa): ")
data2 = datetime.datetime.strptime(data_str2, "%d/%m/%Y")

if data1 < data2:
    print(f"{nome1} é mais velho!")
elif data2 < data1:
    print(f"{nome2} é o mais velho!")
else:
    print("Ambos têm a mesma idade!")