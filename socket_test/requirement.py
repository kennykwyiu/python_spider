"""
requirement:
1. implement chat server
2. implement chat client

function :
1. login
2. exit
3. send message
4. get the offline message
5. get the online user
"""

login_template = {
    "action": "login",
    "user": "bobby1"
}

send_data_temple = {
    "action": "send_msg",
    "to": "user",
    "from": "user",
    "data": "I am Bobby"
}

offline_msg_template = {
    "action": "history_msg",
    "user": "user",
}

get_user_template = {
    "action": "list_user",
}

exit_template = {
    "action": "exit",
    "user": ""
}
