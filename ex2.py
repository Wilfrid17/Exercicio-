import random 

numero_secreto = random.randint(1, 100)
print("Bem-vindo ao programa ADIVINHA")
print("Tente adivinha o numero secreto")

palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Digite o numero do palpite: "))

    if palpite > numero_secreto:
        print("Seu palpite está acima do numero")
    elif palpite < numero_secreto:
        print("seu palpite esta abaixo do numero secreto")
    else:
        print(f"Você aceitou numero secreto: {numero_secreto}")