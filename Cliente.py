from socket import *
import random

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:

    nome = input('\nDigite seu nome: ')
    clientSocket.send(nome.encode())
    clientSocket.recv(1024).decode()
    print('Olá', nome)

    nivel = input('Digite sua nivel (1 a 100): ')
    clientSocket.send(nivel.encode())
    clientSocket.recv(1024).decode()
    print("Seu nivel é: ", nivel)

    Jogo = input('\nQual jogo gostaria de jogar? ')
    clientSocket.send(Jogo.encode())
    clientSocket.recv(1024).decode()

    jogadores = int(clientSocket.recv(1024).decode())

    if Jogo == 'Valorant':
        necessarios = 4 - jogadores
        players = [jogadores]
        if necessarios > 0:
            print("Sao necessarios mais ", necessarios, " para jogar, você foi adicionado a fila de valorant.")
        else:
            ID = random.randint(1, 300)
            print("Quantidade de jogadores alcançada!: ", jogadores)
            print("Partida criada!")
            print("Jogo: Valorant")
            print("ID da partida:",ID)
            print("Participantes:")
            break

    clientSocket.close()
