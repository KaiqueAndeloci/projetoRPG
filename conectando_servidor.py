import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_user = socket.gethostbyname(socket.gethostname())

servidor.bind((ip_user, 12000))

while True:
    print("Escutando...")
    menssagem_bytes, enderc_ip_cliente = servidor.recvfrom(2048)
    print(enderc_ip_cliente)
    print(f"O cliente escreveu: {menssagem_bytes.decode()}.")
    resposta = input("Escreva uma mensagem: ")
    servidor.sendto(resposta.encode(), enderc_ip_cliente)
    print("Enviado")