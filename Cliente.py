from socket import *
import random
import time
import sys

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def criando_jogo():
    print("\nCriando jogo", end="", flush=True)
    for _ in range(3):
        for pontos in range(1, 4):
            sys.stdout.write("\r" + "Criando jogo" + "." * pontos + "   ")
            sys.stdout.flush()
            time.sleep(0.33)
    print("\nJogo criado!")

criando_jogo()

listaDeJogos = {
    "Valorant": 4,
    "LOL": 5,
    "CS": 4,
    "FIFA": 2,
    "Minecraft": 3
}

while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    nome = input('\nDigite seu nome: ')
    print('Olá', nome)
    clientSocket.send(nome.encode())
    clientSocket.recv(1024).decode()

    nivel = input('Digite seu nivel (1 a 100): ')
    print("Seu nivel é: ", nivel)
    clientSocket.send(nivel.encode())
    clientSocket.recv(1024).decode()

    print("Lista de jogos: ", listaDeJogos)
    Jogo = input('Qual jogo gostaria de jogar? ')
    clientSocket.send(Jogo.encode())
    clientSocket.recv(1024).decode()

    jogadores = int(clientSocket.recv(1024).decode())
    clientSocket.close()

    if Jogo in listaDeJogos:
        necessarios = listaDeJogos[Jogo] - jogadores
        if necessarios > 0:
            print("\nSao necessarios mais ", necessarios, " para jogar, você foi adicionado a fila de ", Jogo )
            time.sleep(2)
        else:
            criando_jogo()
            ID = random.randint(1, 300)
            print("\n------------------------------------------------")
            print("Quantidade de jogadores alcançada!: ", jogadores)
            print("Partida criada!")
            print("Jogo:",Jogo)
            print("ID da partida:",ID)
            print("Participantes:",jogadores)

            continuar = input("Gostaria de continuar configurando os outros jogadores(S/N)?")
            if continuar == "S":
                print("Continuando!")
                time.sleep(1)
            elif continuar == "N":
                break

    else:
        print("Jogo não encontrado! Tente novamente.")
        break

