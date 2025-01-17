# msn  client
import json
import socket
import threading

client = socket.socket()
client.connect(('127.0.0.1', 8000))

user = "Bobby2"

# 1. login
login_template = {
    "action": "login",
    "user": user
}

client.send(json.dumps(login_template).encode("utf8"))
res = client.recv(1024)
print(res.decode("utf8"))

# 2. get online user

get_user_template = {
    "action": "list_user",
}

client.send(json.dumps(get_user_template).encode("utf8"))
res = client.recv(1024)
print("current online users: {}".format(res.decode("utf8")))

# 3. get historical message

offline_msg_template = {
    "action": "history_msg",
    "user": user,
}

client.send(json.dumps(offline_msg_template).encode("utf8"))
res = client.recv(1024)
print("historical message: {}".format(res.decode("utf8")))

exit = False
def handle_receive():
    while True:
        if not exit:
            try:
                res = client.recv(1024)
            except:
                break
            res = res.decode("utf8")
            try:
                res_json = json.loads(res)
                msg = res_json["data"]
                from_user = res_json["from"]
                print("")
                print("msg received from ({}): {}".format(from_user, msg))
            except:
                print("")
                print(res)
        else:
            break

def handle_send():
    while True:
        op_type = input("pls input your action: 1. send message, 2. exit, 3. get online user")
        if op_type not in ["1", "2", "3"]:
            print("don't have this action!!!")
            op_type = input("pls input your action: 1. send message, 2. exit, 3. get online user")
        elif op_type == "1":
            to_user = input("pls input who will you send: ")
            msg = input("pls input your message ")
            send_data_temple = {
                "action": "send_msg",
                "to": user,
                "from": to_user,
                "data": msg
            }
            client.send(json.dumps(send_data_temple).encode("utf8"))
        elif op_type == "2":
            exit_template = {
                "action": "exit",
                "user": user
            }
            client.send(json.dumps(exit_template).encode("utf8"))
            exit = True
            client.close()
            break
        elif op_type == "3":
            get_user_template = {
                "action": "list_user",
            }
            client.send(json.dumps(get_user_template).encode("utf8"))

if __name__ == '__main__':
    send_thread = threading.Thread(target=handle_send)
    receive_thread = threading.Thread(target=handle_receive)
    send_thread.start()
    receive_thread.start()


