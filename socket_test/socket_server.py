import socket
server = socket.socket()
server.bind(('0.0.0.0', 8000))
server.listen()

sock, addr = server.accept()
data = ""
while True:
    sock.send("welcome to server!".encode("utf8"))

    tmp_data = sock.recv(1024)
    print(tmp_data.decode("utf8"))
    input_data = input()
    sock.send(input_data.encode("utf8"))


    # if tmp_data:
    #     data += tmp_data.decode("utf8")
    #
    #     if tmp_data.decode("utf8").endswith("#"):
    #         break
    # else:
    #     break

# print(data)
# sock.close()
