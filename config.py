from pyrogram import Client,filters,enums
import redis
r = redis.from_url(
    'redis://default:deviq7887@redis-12019.c91.us-east-1-3.ec2.cloud.redislabs.com:12019')

sudo_id = 833360381
bot_user = "IQDVBOT"
api_id = 12962251
api_hash = "b51499523800add51e4530c6f552dbc8"
session = "AgAhIHQAbL3A-bLILW5GWxODfKaejkGhpwTdJwT4-ILVxYfhMilcPV_W4mwKbfW_Mjc9yjEfmGV3ikctmQl1sGUWMKCTQx6WUCCYmRbrah8kkZVbAvq3MGIH_75D06_zt23t2baRmqVp-qkLgQeKOxKw6I6MvXuFm2nDrch6KOc3DpgGGSHrtP59Uzywl_93y2K0MBxRjANZQFyPKlKwxmKczjHafW8oum9K49B6KJ1Gbk_8XAu5Ra5T-TMO1yY1BI9wqW62z_CboFZ1mbYx95VGTZ3RpaLe7KFCruWwipWykK4w4CGykvfgaLXqzaBpjUHHd7c-uz_mlqdShRuYQtFE41-osAAAAAAxrBH9AA"
token = "6475201483:AAF5RMcasWoHV1K_jYsdYiP6CG7jkGDNNGQ"
sudo_command = [833360381, 1818734394]
pm = "833360381"
mention = "833360381"
plugins = dict(root="plugins")
app = Client("user:IQDVBOT",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("IQDVBOT",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
