from socket import *
import random
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# Acima estão as bibliotecas disponibilizadas no arquivo python socket (Utilizei o TCP).

print("O servidor esta pronto esperando mensagens")

filas = {
    "Valorant": [],
    "LOL": [],
    "CS": [],
    "FIFA": [],
    "Minecraft": []
}
# Fila com os jogos disponíveis

jogadoresNecessarios = {
    "Valorant": 4,
    "LOL": 5,
    "CS": 4,
    "FIFA": 2,
    "Minecraft": 3
}
# Quantos jogadores que são necessário para iniciar cada partida

while True:
    connectionSocket, addr = serverSocket.accept()

    nome = connectionSocket.recv(1024).decode()
    print("Nome:", nome)
    connectionSocket.send(b"OK")
    #Os nomes serão armazenados aqui pelo servidor

    nivel = connectionSocket.recv(1024).decode()
    print("Nível:", nivel)
    connectionSocket.send(b"OK")
    #Os niveis serão armazenados aqui

    jogo = connectionSocket.recv(1024).decode()
    print("Jogo:", jogo)
    #Aqui ficara o jogo solicitado

    if jogo not in filas:#Se os jogos não estiverem na fila...
        resposta = "Jogo" + jogo + " não encontrado na lista de jogos disponíveis."
        connectionSocket.send(resposta.encode())
        connectionSocket.close()
        continue

    filas[jogo].append(nome)
    print("Fila atual de ", jogo ,": " , filas[jogo])

    necessarios = jogadoresNecessarios[jogo]

    if len(filas[jogo]) >= necessarios:
        participantes = filas[jogo][:necessarios]
        filas[jogo] = filas[jogo][necessarios:]

        idPartida = random.randint(1, 999)#O ID da partida será gerado de forma random

        print("\n------------------------------------------------")
        print("Partida criada!")
        print("Jogo: ", jogo)
        print("ID da partida: ", idPartida)
        print("Participantes: ", participantes)

        resposta = (
            f"Uma nova partida foi criada.\n"
            f"Jogo: { jogo }\n"
            f"ID da partida: {idPartida}\n"
            f"{len(participantes)} jogadores foram selecionados\n"
            f"Participantes: {', '.join(participantes)}"
        )
    else:
        posicao = len(filas[jogo])# A posição pega o tamanho da quantidade dos jogos para subtrair com os necessarios
        resposta = (
            f"Você foi adicionado à fila de espera.\n"
            f"Jogo: {jogo}\n"
            f"Posição na fila: {posicao}\n"
            f"Faltam {necessarios - posicao} jogador para formar uma partida."
        )

    connectionSocket.send(resposta.encode())
    connectionSocket.close()
