from .load import get_users, wxpy
from .config import FILE_STORE_PATH
import requests
import datetime
from os import stat, path


def refresh_avatars():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    session = requests.Session()
    session.cookies.update(wxpy['cookies'])
    for user in get_users():
        params = {
            'userName': user.username,
            'skey': wxpy['loginInfo']['skey'],
            'type': 'big'}
        url = f"https://wx.qq.com{user.head_img_url}"
        f_path = f"{FILE_STORE_PATH}/{user.username}.jpg"
        if not path.exists(f_path) or datetime.datetime.now().timestamp() - stat(f_path).st_mtime > 86400:
            print(f"Downloading avatar for `{user.nickname}`")
            with open(f_path, 'wb') as file:
                response = session.get(
                    url, params=params, stream=True, headers=headers)
                file.write(response.content)
        else:
            print(f"Avatar for `{user.nickname}` is new enough.")
