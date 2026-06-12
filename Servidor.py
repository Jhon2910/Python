from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('O servidor esta pronto esperando mensagens')
while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	print("mensagem recebida: ", sentence)
	capitalizedSentence = sentence.upper()
	print("mensagem que sera enviada: ", capitalizedSentence)
	connectionSocket.send(capitalizedSentence.encode())
	connectionSocket.close()
