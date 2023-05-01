import socket
import time
import random

HOST = 'localhost'
PORT = 50000

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # Gerando um número inteiro aleatório de até 30 casas
    num = random.randint(1, 10**30)
    print(f'ENVIADO: {num}')

    # Convertendo o número para bytes e enviando ao servidor
    s.send(str(num).encode())

    # Recebendo a resposta do servidor e convertendo de volta para inteiro
    data = s.recv(2048)
    response = data.decode()

    # Imprimindo o valor recebido e a mensagem "FIM"
    print(f'RECEBIDO: {response} FIM')

    # Encerrando a conexão
    s.close()

    # Esperando 10 segundos antes de iniciar a próxima iteração
    time.sleep(3)