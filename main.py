###Jogo de Jokenpo###
import random

print("Olá! Vamos jogar?")

print("""
pedra
      
papel
      
tesoura
      """)

suaEscolha = input("Jogador - Escolha pedra, papel ou tesoura: ")
minhaEscolha = random.choice(["pedra", "papel", "tesoura"])
if suaEscolha == "pedra":
    if minhaEscolha == "tesoura":
        print("Jogador ganhou! Computador escolheu ", minhaEscolha)
    elif minhaEscolha == "papel":
        print("Jogador perdeu! Computador escolheu ", minhaEscolha)
    else:
        print("Empate! Ambos escolheram ", minhaEscolha)
elif suaEscolha == "papel":
    if minhaEscolha == "tesoura":
        print("Jogador perdeu! Computador escolheu ", minhaEscolha)
    elif minhaEscolha == "pedra":
        print("Jogador ganhou! Computador escolheu ", minhaEscolha)
    else:
        print("Empate! Ambos escolheram ", minhaEscolha)
elif suaEscolha == "tesoura":
    if minhaEscolha == "papel":
        print("Jogador ganhou! Computador escolheu ", minhaEscolha)
    elif minhaEscolha == "pedra":
        print("Jogador perdeu! Computador escolheu ", minhaEscolha)
    else:
        print("Empate! Ambos escolheram ", minhaEscolha)
else:
    print("Algo deu errado!")