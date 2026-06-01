chances = 5
palavra_secreta = 'batata'
while chances > 0: 
    palavra = input(f"Qual a palavra secreta? Você tem {chances} chances")
    chances -= 1
    if palavra == 'batata':
        print("Você acertou a palavra, toma aqui uma batata 🥔")
        break

#Ao errar a palavra, o programa diminui uma chance (subtrai 1 da variável 'chances'), fazendo com que o loop se repita até que a condição if seja atendida ou que as chances cheguem a 0.
#Ao acertar a palavra, o programa entra em if, imprime a mensagem do sucesso e o break é executado, fazendo com que saia do while.