print("=" * 40)
print("Bem vindo ao jogo da adivinhação!!!")
print("=" * 40)

numero_secreto = 42
total_tentativas = 3

while(total_tentativas > 0):
  print(f'Tentativas restantes: { total_tentativas }')
  numero_chute = int(input("Digite um número: "))
  print(f'O número digitado é { numero_chute }')
  if(numero_chute == numero_secreto):
    print("Parabéns, você acertou!")
    break
  elif(numero_chute > numero_secreto):
    print("Você errou! O número inserido é maior que o número secreto.")
  elif(numero_chute < numero_secreto):
    print("Você errou! O número inserido é menor que o número secreto.")
  total_tentativas = total_tentativas - 1
  print("=" * 70)