###Jogo de Jokenpo###
import random

print("Olá! Vamos jogar?")


print("""
pedra
      
papel
      
tesoura
      """)
try:
    suaEscolha = input("Jogador 2 - Escolha pedra, papel ou tesoura: ")
    if minhaEscolha == "pedra":
        if suaEscolha == "papel":
            print("Jogador 2 ganhou! Jogador 1 escolheu ", minhaEscolha)
        elif suaEscolha == "tesoura":
            print("Jogador 2 perdeu! Jogador 1 escolheu ", minhaEscolha)
        else:
            print("Empate! Ambos escolheram ", minhaEscolha)
    elif minhaEscolha == "papel":
        if suaEscolha == "pedra":
            print("Jogador 2 perdeu! Jogador 1 escolheu ", minhaEscolha)
        elif suaEscolha == "tesoura":
            print("Jogador 2 ganhou! Jogador 1 escolheu ", minhaEscolha)
        else:
            print("Empate! Ambos escolheram ", minhaEscolha)
    elif minhaEscolha == "tesoura":
        if suaEscolha == "pedra":
            print("Jogador 2 ganhou! Jogador 1 escolheu ", minhaEscolha)
        elif suaEscolha == "papel":
            print("Jogador 2 perdeu! Jogador 1 escolheu ", minhaEscolha)
        else:
            print("Empate! Ambos escolheram ", minhaEscolha)
    minhaEscolha = random.choice(["pedra", "papel", "tesoura"])
    print("Jogador 1 já escolheu")
except:
    print("Algo deu errado!")