import random

def jogar():
    print("=" * 40)
    print("Bem vindo ao jogo da Adivinhação!!!")
    print("=" * 40)

    numero_secreto = random.randrange(0, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?\n[1]Fácil  [2]Médio  [3]Difícil\n")

    nivel = int(input('Defina o nível: '))

    if(nivel == 1):
      total_tentativas = 20
    elif(nivel == 2):
      total_tentativas = 10
    elif(nivel == 3):
      total_tentativas = 5
    else:
      print("Número inválido")
        
    for rodada in range(1, total_tentativas + 1):
      print(f'Tentativa { rodada } de {total_tentativas}')
      numero_chute = int(input("Digite um número entre 1 e 100: "))
      print(f'O número digitado é { numero_chute }')
      
      if(numero_chute < 1 or numero_chute > 100):
        print("Número inválido digite um número entre 1 e 100")
        continue

      if(numero_chute == numero_secreto):
        print(f'Parabéns, você acertou! Você fez { pontos } pontos!')
        break
      elif(numero_chute > numero_secreto):
        print("Você errou! O número inserido é maior que o número secreto.")
      elif(numero_chute < numero_secreto):
        print("Você errou! O número inserido é menor que o número secreto.")
      pontos_perdidos = abs(numero_secreto - numero_chute)
      pontos = pontos - pontos_perdidos
      print("=" * 70)
    print(f'O número secreto era: { numero_secreto }')
    print("Fim do jogo!")

if(__name__ == "__main__"):
  jogar()