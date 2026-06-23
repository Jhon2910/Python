from socket import *

serverName = 'localhost'
serverPort = 12000

jogosDisponiveis = ["Valorant", "LOL", "CS", "FIFA", "Minecraft"]

while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    nome = input("\nDigite seu nome: ")
    print("Olá,", nome)
    clientSocket.send(nome.encode())
    clientSocket.recv(1024)#Envia o nome para o servidor

    nivel = input("Digite seu nível (1 a 100): ")
    print("Seu nível é:", nivel)
    clientSocket.send(nivel.encode())
    clientSocket.recv(1024)#Envia o nivel para o servidor

    print("Jogos disponíveis:", jogosDisponiveis)
    jogo = input("Qual jogo gostaria de jogar? ")
    clientSocket.send(jogo.encode())#Envia o jogo desejado para o servidor

    resposta = clientSocket.recv(1024).decode()#recebe a resposta do servidor
    clientSocket.close()

    print("\nResposta do servidor")
    print(resposta)

    continuar = input("\nDeseja adicionar outro jogador (S/N)? ")
    if continuar.upper() != "S":
        break
