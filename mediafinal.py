nota1 = float(input("Digite sua nota da N1: "))
nota2 = float(input("Digite sua nota da N2: "))
nota3 = float(input("Digite sua nota da N3: "))
nota4 = float(input("Digite sua nota da N4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print(f"Parabéns, você foi aprovado(a) com média {media:.1f}!")

elif media >= 5:
    print(f"Ânimo! Nem tudo está perdido. Sua média é {media:.1f} e você está de recuperação.")
    recup = float(input("Digite sua nota da Recuperação Final: "))
    mediafinal = (media + recup) / 2

    if mediafinal >= 7:
        print(f"Parabéns, você foi aprovado(a) com média final {mediafinal:.1f}!")
    else:
        print(f"Infelizmente você foi reprovado(a) com média final {mediafinal:.1f}.")
else:
    print(f"Infelizmente você foi reprovado(a) com média {media:.1f}.")
