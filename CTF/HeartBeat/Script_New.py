from socket import *
serverName = '10.1.8.96'
serverPort = 45434
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('0.0.0.0',2020))
clientSocket.connect((serverName,serverPort))
sentence = "1000\x08stillhavenotslept"
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode())
clientSocket.close()
