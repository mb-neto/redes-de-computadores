from socket import *

serverName = 'localhost'
serverPort = 61000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('Digite o texto em letras minusculas: ')
clientSocket.send(sentence.encode('utf-8'))
modifiedSentence = clientSocket.recv(1024)
print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedSentence.decode('utf-8')))
clientSocket.close()