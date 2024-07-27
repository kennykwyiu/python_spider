# msn server
"""
1. forward msg
2. handle login
3. handle exit
4. check msg history, check online user and check user connection
"""

import socket
from collections import defaultdict


def init_user():
    return {
        "name": "Bobby",
        "sock": "sock"
    }


# maintain user connection
online_users = defaultdict(init_user)

online_users["Bobby"]["name"] = "Bobby"
# online_users["name"] = "Bobby"
print(online_users)

# a = online_users.get("a", "")
# print(a)
