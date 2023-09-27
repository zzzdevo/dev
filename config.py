from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 5964012315
bot_user = "jvfhhcfhhbot"
api_id = 10823881
api_hash = "339886e2109eb67203ce12022b32e035"
session = "BABJpCyfNw6x-3aCTepEtHHLiH8frdPeLwwL_pMBer_ITlUYv-98QafvSHsOZTQmQWNuFGHBq8YzoISSQljsOw_-XmotDYn8dn3C8jVfyhAR8w47Bza7maVEPHNQlOE4dhwSe2It1yiK8ryI-7s54SQ0318e5o8oTS7QivJVBawdzLD-6ChYV8JYpGd1zO_5d6S0S9k0b4sq5C3smow6KETPrXZ19e9xwjJkLhRSKPKo5RBLnoC331t6K3cjN4RcoG8pQiUlYgLW9YlF3NkcHK0CtDyaNrVPmeoEHSS5j0wVjprzgajrbVmTZpi4bkja8lMwVkqubUY2mviyK6V3ygoHAAAAAWN7mxsA"
token = "6174014309:AAEPXnzyWgOO0ESVUUIqKDlpNOZwCeRHVD0"
sudo_command = [1804133252, 5912085775]
pm = "5964012315"
mention = "5964012315"
plugins = dict(root="plugins")
app = Client("user:jvfhhcfhhbot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("jvfhhcfhhbot",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
