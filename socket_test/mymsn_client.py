# msn  client
import json
import socket

client = socket.socket()
client.connect(('127.0.0.1', 8000))

user = "Bobby1"

#1. login
login_template = {
    "action": "login",
    "user": "Bobby1"
}

client.send(json.dumps(login_template).encode("utf8"))
res = client.recv(1024)
print(res.decode("utf8"))

#2. get online user

get_user_template = {
    "action": "list_user",
}

