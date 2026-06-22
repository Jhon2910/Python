from socket import *
import random
import time

serverName = 'localhost'
serverPort = 12000

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
    clientSocket.recv(1024)

    nivel = input('Digite seu nivel (1 a 100): ')
    print("Seu nivel é: ", nivel)
    clientSocket.send(nivel.encode())
    clientSocket.recv(1024)

    print("Lista de jogos: ", listaDeJogos)
    Jogo = input('Qual jogo gostaria de jogar? ')
    clientSocket.send(Jogo.encode())
    clientSocket.recv(1024)  # eco do jogo

    resposta = clientSocket.recv(1024).decode()  # resposta final do servidor
    clientSocket.close()

    print(resposta)

    if Jogo in listaDeJogos:
        jogadores = int(resposta.split(":")[-1].strip())
        necessarios = listaDeJogos[Jogo] - jogadores

        if necessarios > 0:
            print("\nSão necessários mais", necessarios, "para jogar, você foi adicionado à fila de", Jogo)
            time.sleep(2)
        else:
            ID = random.randint(1, 300)
            print("\n------------------------------------------------")
            print("Quantidade de jogadores alcançada!:", jogadores)
            print("Partida criada!")
            print("Jogo:", Jogo)
            print("ID da partida:", ID)
            print("Participantes:", jogadores)

            continuar = input("Gostaria de continuar configurando os outros jogadores (S/N)? ")
            if continuar == "S":
                print("Continuando!")
                time.sleep(1)
            elif continuar == "N":
                break
    else:
        print("Jogo não encontrado! Tente novamente.")
        break
