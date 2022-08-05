from filters.SQL import get_bot_token, get_bot_admins

BOT_TOKEN = get_bot_token()
print(f'Токен: {BOT_TOKEN}')

admins = get_bot_admins()
print(f'Администраторы: {admins}')

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
