from socket import * # sockets

serverName = ''
serverPort = 61000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    sentence = sentence.decode('utf-8')
    if sentence == "obter arquivo.txt":
        with open('arquivo.txt', 'r') as file:
            capitalizedSentence = file.read()
        print ('Cliente %s enviou: %s' % (addr, sentence))
        connectionSocket.send(capitalizedSentence.encode('utf-8'))
        
    else:
        capitalizedSentence = "Comando inválido"
        connectionSocket.send(capitalizedSentence.encode('utf-8'))
    connectionSocket.close()
serverSocket.close()
