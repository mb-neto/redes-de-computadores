from socket import *

serverName = 'localhost'
serverPort = 61000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('Digite um comando: ')
clientSocket.send(sentence.encode('utf-8'))
modifiedSentence = clientSocket.recv(1024)
print (modifiedSentence.decode('utf-8'))
clientSocket.close()
