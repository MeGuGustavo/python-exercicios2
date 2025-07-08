peso = float(input("Qual seu peso?(kg) "))
altura = float(input("Qual sua altura?(m) "))
imc = peso / (altura ** 2)

print(f"Seu IMC é {imc: .2f}")

if imc < 18.5:
    print("Você está abaixo do peso!")

elif imc < 25:
    print("Seu peso está normal!")

elif imc < 30:
    print("Você está em sobrepeso!")

else:
    print("Você está em obesidade") 