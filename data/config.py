import os

from SQL import get_bot_token, get_bot_admins

BOT_TOKEN = get_bot_token()
print(f'токен: {BOT_TOKEN}')

admins = get_bot_admins()
print(f'администраторы: {admins}')

# ip = os.getenv("ip")
#
# aiogram_redis = {
#     'host': ip,
# }
#
# redis = {
#     'address': (ip, 6379),
#     'encoding': 'utf8'
# }
