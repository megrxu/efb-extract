import pickle
from typing import List
from .config import PICKLE_PATH
from .model import User, Chat

f_wxpy = open(f"{PICKLE_PATH}/wxpy.pkl", 'rb')
f_puid = open(f"{PICKLE_PATH}/wxpy_puid.pkl", 'rb')

wxpy = pickle.load(f_wxpy)
puid = pickle.load(f_puid)

f_wxpy.close()
f_puid.close()


def get_users_raw():
    return wxpy['storage']['memberList']


def get_user_ids_query():
    return puid[2]


def get_ids_query():
    return puid[0]


def get_chats_raw():
    return wxpy['storage']['chatroomList']


def get_users() -> List[User]:
    user_ids_query = get_ids_query()
    users = []
    for raw_user in get_users_raw():
        identity = user_ids_query.get(raw_user['UserName'])
        users.append(User(identity, raw_user))
    return users


def get_chats() -> List[Chat]:
    chat_ids_query = get_ids_query()
    chats = []
    for raw_user in get_chats_raw():
        identity = chat_ids_query.get(raw_user['UserName'])
        chats.append(Chat(identity, raw_user))
    return chats


def get_self() -> User:
    return User('__self__', wxpy['loginInfo']['User'])


def get_raws():
    return wxpy
