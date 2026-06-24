from socket import *
import random

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# Inicializa o servidor TCP e deixa a porta pronta para receber conexões.

print("O servidor esta pronto esperando mensagens")

filas = {
    "Valorant": [],
    "LOL": [],
    "CS": [],
    "FIFA": [],
    "Minecraft": []
}
# Estrutura que armazena os jogadores que aguardam partida em cada jogo.

jogadoresNecessarios = {
    "Valorant": 4,
    "LOL": 5,
    "CS": 4,
    "FIFA": 2,
    "Minecraft": 3
}
# Quantidade mínima de jogadores para formar uma partida de cada jogo.

while True:
    connectionSocket, addr = serverSocket.accept()

    nome = connectionSocket.recv(1024).decode()
    print("Nome:", nome)
    connectionSocket.send(b"OK")
    # Recebe e registra o nome do jogador.

    nivel = connectionSocket.recv(1024).decode()
    print("Nível:", nivel)
    connectionSocket.send(b"OK")
    # Recebe o nível informado pelo jogador.

    jogo = connectionSocket.recv(1024).decode()
    print("Jogo:", jogo)
    # Recebe o jogo escolhido para o matchmaking.

    if jogo not in filas:
        # Verifica se o jogo informado existe na lista de jogos suportados.
        resposta = "Jogo " + jogo + " não encontrado na lista de jogos disponíveis."
        connectionSocket.send(resposta.encode())
        connectionSocket.close()
        continue

    filas[jogo].append(nome)
    print("Fila atual de ", jogo, ": ", filas[jogo])

    necessarios = jogadoresNecessarios[jogo]

    if len(filas[jogo]) >= necessarios:

        # Seleciona os jogadores necessários para iniciar uma nova partida.
        participantes = filas[jogo][:necessarios]

        # Remove da fila os jogadores que já foram alocados.
        filas[jogo] = filas[jogo][necessarios:]

        # Gera um identificador aleatório para a partida.
        idPartida = random.randint(1, 999)

        print("\n------------------------------------------------")
        print("Partida criada!")
        print("Jogo: ", jogo)
        print("ID da partida: ", idPartida)
        print("Participantes: ", participantes)

        resposta = (
            f"Uma nova partida foi criada.\n"
            f"Jogo: {jogo}\n"
            f"ID da partida: {idPartida}\n"
            f"{len(participantes)} jogadores foram selecionados\n"
            f"Participantes: {', '.join(participantes)}"
        )

    else:
        # Mantém o jogador na fila e informa sua posição atual.
        posicao = len(filas[jogo])

        resposta = (
            f"Você foi adicionado à fila de espera.\n"
            f"Jogo: {jogo}\n"
            f"Posição na fila: {posicao}\n"
            f"Faltam {necessarios - posicao} jogador para formar uma partida."
        )

    # Envia o resultado da operação para o cliente e encerra a conexão.
    connectionSocket.send(resposta.encode())
    connectionSocket.close()
