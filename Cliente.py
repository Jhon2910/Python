from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
nome = input('Digite seu nome: ')
clientSocket.send(nome.encode())

BoasVindas = clientSocket.recv(1024)
print ('Olá', BoasVindas.decode())

Jogo = input('\nQual jogo gostaria de jogar? ')
clientSocket.send(Jogo.encode())



clientSocket.close()
