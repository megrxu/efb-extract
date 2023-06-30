# EFB-WX Extractor

Extract users information from `efb-wechat-slave` databases.

This is meant to be the only part that other languages cannot handle, since data is stored in the pickles.

## Usage

- Place the two pickle files under the folder `data/wxpy`.
- Run `poetry run gunicorn efb_extract:app --bind 127.0.0.1:8090` to serve the web api.
  - Avaliable routes: `/users/`, `/chats/` and `/self/`.
- Run `poetry run refresh-avatars` to refresh the new avatars.

## References

- https://github.com/ehForwarderBot/efb-wechat-slave
