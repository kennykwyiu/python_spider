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
