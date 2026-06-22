from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('O servidor esta pronto esperando mensagens')

Fila = {
    "Valorant": [],
    "LOL": [],
    "CS": [],
    "FIFA": [],
    "Minecraft": []
}

while True:
    connectionSocket, addr = serverSocket.accept()

    nome = connectionSocket.recv(1024).decode()
    print("Nome: ", nome)
    connectionSocket.send(nome.encode())

    nivel = connectionSocket.recv(1024).decode()
    print("Nível: ", nivel)
    connectionSocket.send(nivel.encode())

    jogo = connectionSocket.recv(1024).decode()
    print("Jogo: ", jogo)
    connectionSocket.send(jogo.encode())

    if jogo in Fila:
        if nome in Fila[jogo]:
            Fila[jogo].remove(nome)
            resposta = f"Removido. Jogadores na fila: {len(Fila[jogo])}"
        else:
            Fila[jogo].append(nome)
            resposta = f"Adicionado. Jogadores na fila: {len(Fila[jogo])}"

        print(Fila)
        connectionSocket.send(resposta.encode())
    else:
        connectionSocket.send("Jogo inválido".encode())

    connectionSocket.close()
