from random import randint

count = 0
sala = "1"

def caminho1():
    caminho = {
        "1": "2", 
        "2": "3"
    }
    escolheu = input("\n[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]
def caminho2():
    caminho = {
        "1": "3", 
        "2": "4"
    }
    escolheu = input("\n[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]
def caminho3():
    caminho = {
        "1": "4", 
        "2": "5"
    }
    escolheu = input("[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]
def caminho4():
    caminho = {
        "1": "5", 
        "2": "6"
    }
    escolheu = input("\n[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]
def caminho5():
    caminho = {
        "1": "6", 
        "2": "7"
    }
    escolheu = input("\n[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]
def caminho6():
    input("\n[1] - Caminho preto\n\n")
    return "8"
def caminho7():
    caminho = {
        "1": "8", 
        "2": "9"
    }
    escolheu = input("\n[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]
def caminho8():
    caminho = {
        "1": "9", 
        "2": str(randint(1, 5))
    }
    escolheu = input("\n[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]

caminhos = {
    "1": caminho1,
    "2": caminho2,
    "3": caminho3,
    "4": caminho4,
    "5": caminho5,
    "6": caminho6,
    "7": caminho7,
    "8": caminho8
    }

while True:

    print("Você está na sala ", sala)

    if sala == "9": 
        print("\nParabnéns!! Você encontrou o fim da caverna!!")
        break
    elif count == 7: 
        print("\nHmm... O limite de tentativas foi excedido, tente novamente!")
        break

    sala = caminhos[sala]()

    count += 1




