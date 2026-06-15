from socket import *


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('O servidor esta pronto esperando mensagens')

Valorant = 0
LOL = 0
CS = 0
FIFA = 0
Minecraft = 0

while True:
    connectionSocket, addr = serverSocket.accept()

    nome = connectionSocket.recv(1024).decode()
    print("Nome: ", nome)
    connectionSocket.send(nome.encode())

    nivel = connectionSocket.recv(1024).decode()
    print("Nível: ", nivel)
    connectionSocket.send(nivel.encode())

    jogo = connectionSocket.recv(1024).decode()
    print("jogo: ", jogo)
    connectionSocket.send(jogo.encode())


    if jogo == "Valorant":
        Valorant += 1
        connectionSocket.send(str(Valorant).encode())
    elif jogo == "LOL":
        LOL += 1
        connectionSocket.send(str(LOL).encode())
    elif jogo == "CS":
        CS += 1
        connectionSocket.send(str(CS).encode())
    elif jogo == "FIFA":
        FIFA += 1
        connectionSocket.send(str(FIFA).encode())
    elif jogo == "Minecraft":
        Minecraft += 1
        connectionSocket.send(str(Minecraft).encode())

    connectionSocket.close()
