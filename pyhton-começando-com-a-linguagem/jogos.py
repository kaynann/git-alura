import advinhacao
import forca

def escolha_jogo():
    print("=" * 40)
    print("Qual jogo você quer jogar?")
    print("[1]Advinhação  [2]Forca")

    jogo = int(input('Informe o jogo que quer jogar: '))

    if(jogo == 1):
      print("Jogando Advinhação")
      advinhacao.jogar()
    elif(jogo == 2):
      print("Jogando Forca")
      forca.jogar()
    else:
      print("Número inválido")

if(__name__ == "__main__"):
   escolha_jogo()