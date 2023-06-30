from dataclasses import dataclass


@dataclass
class Chat(object):
    identity: str
    username: str
    head_img_url: str
    nickname: str

    def __init__(self, identity, raw_wxpy_user):
        self.identity = identity
        self.nickname = raw_wxpy_user['NickName']
        self.username = raw_wxpy_user['UserName']
        self.head_img_url = raw_wxpy_user['HeadImgUrl']


@dataclass
class User(Chat):
    remarkname: str
    gender: str
    signature: str
    state: str
    city: str
    head_img_url: str

    def __init__(self, identity, raw_wxpy_user):
        super().__init__(identity, raw_wxpy_user)
        self.remarkname = raw_wxpy_user['RemarkName']
        self.gender = raw_wxpy_user['Sex']
        self.signature = raw_wxpy_user['Signature']
        self.state = raw_wxpy_user['Province']
        self.city = raw_wxpy_user['City']
        self.state = raw_wxpy_user['Province']
