from telethon.sync import TelegramClient


api_id = 5065387
api_hash = "8795af0d9bf6f9b19afc8e4e8058dbdf"


def get_client():
    client = TelegramClient('client', api_id, api_hash)
    return client
