chances = 0
secreto = "246"

for i in range(10):
    chances += 1
    print(f'==> Chances: {chances} <==')
    palp = input("Palpite: ")

    if len(palp)!= 3:
        print("digite três números!!")
        continue
    if palp == secreto:
        print("Saída: +++")
        print("Você acertou! :)")
        break
    res1 = "_"
    res2 = "_"
    res3 = "_"
    s1 = secreto[0]
    s2 = secreto[1]
    s3 = secreto[2]
    if palp[0] == s1:
        res1 = "+"
        s1 = "*"
    if palp[1] == s2:
        res2 = "+"
        s2 = "*"
    if palp[2] == s3:
        res3 = "+"
        s3 = "*"
    if res1 == "_":
        if palp[0] == s2:
            res1 = "!"
            s2 = "*"
        elif palp[0] == s3:
            res1 = "!"
            s3 = "*"
    if res2 == "_":
        if palp[1] == s1:
            res2 = "!"
            s1 = "*"
        elif palp[1] == s3:
            res2 = "!"
            s3 = "*"
    if res3 == "_":
        if palp[2] == s1:
            res3 = "!"
            s1 = "*"
        elif palp[2] == s2:
            res3 = "!"
            s2 = "*"
    print("Saída:", res1 + res2 + res3)
if palp!= secreto:
    print("Você perdeu! O número era", secreto)