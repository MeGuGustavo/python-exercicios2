idade = int(input("Qual a sua idade? "))

habilitacao = input("Você possui habilitação? (s/n): ").strip().lower()

tem_carteira = habilitacao == 's'

if idade >= 18 and tem_carteira:
    print("Permitido dirigir!")
else:
    print("Proibido dirigir!")

