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
  capitalizedSentence = sentence.upper()
  print ('Cliente %s enviou: %s, transformando em: %s' % (addr, sentence, capitalizedSentence))
  connectionSocket.send(capitalizedSentence.encode('utf-8'))
  connectionSocket.close()
serverSocket.close()