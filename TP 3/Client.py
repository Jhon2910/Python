from socket import *

serverName = 'localhost'
serverPort = 12000

jogosDisponiveis = ["Valorant", "LOL", "CS", "FIFA", "Minecraft"]

while True:

    # Cria uma conexão TCP com o servidor.
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    nome = input("\nDigite seu nome: ")
    print("Olá,", nome)

    # Envia o nome do jogador para o servidor.
    clientSocket.send(nome.encode())
    clientSocket.recv(1024)

    nivel = input("Digite seu nível (1 a 100): ")
    print("Seu nível é:", nivel)

    # Envia o nível informado pelo jogador.
    clientSocket.send(nivel.encode())
    clientSocket.recv(1024)

    print("Jogos disponíveis:", jogosDisponiveis)
    jogo = input("Qual jogo gostaria de jogar? ")

    # Envia ao servidor o jogo escolhido pelo usuário.
    clientSocket.send(jogo.encode())

    # Recebe a resposta contendo informações da fila ou da partida criada.
    resposta = clientSocket.recv(1024).decode()

    # Encerra a conexão após concluir a comunicação.
    clientSocket.close()

    print("\nResposta do servidor")
    print(resposta)

    # Permite cadastrar novos jogadores sem reiniciar o programa.
    continuar = input("\nDeseja adicionar outro jogador (S/N)? ")

    if continuar.upper() != "S":
        break