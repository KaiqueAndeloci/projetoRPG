import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind(('localhost', 12000))

while True:
    menssagem_bytes, enderc_ip_cliente = servidor.recvfrom(2048)
    print(enderc_ip_cliente)
    print(f"O cliente escreveu: {menssagem_bytes.decode()}.")
    resposta = input("Escreva uma mensagem: ")
    servidor.sendto(resposta.encode(), enderc_ip_cliente)
    print("pronto")