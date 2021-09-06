import socket

ip_user = socket.gethostbyname(socket.gethostname())
print(ip_user)
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
loop = True
while loop:
    mensagem = input("Digite: ")
    if mensagem != "/sair":
        cliente.sendto(mensagem.encode(), (ip_user, 12000))
        print("Enviado")
        mensagem_sever, endereco_sever = cliente.recvfrom(2048)
        print(f"O sever dissse: {mensagem_sever.decode()}")
    else:
        loop = False
