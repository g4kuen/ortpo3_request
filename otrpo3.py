import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')
user_id = os.getenv('USER_ID')

# базовый url VK API откуда мы берем методы и сами запросы
base_url = 'https://api.vk.com/method/'

#базовые параметры для всех запросов
params = {
    'access_token': access_token,
    'v': '5.131'  # версия VK API
}

# базовый лог лля отловли ошибок
def check_vk_response(response):
    data = response.json()
    if 'error' in data:
        print(f"Ошибка VK API: {data['error']['error_msg']}")
        return None
    return data['response']


user_info_response = requests.get(
    base_url + 'users.get',
    params={**params, 'user_ids': user_id, 'fields': 'followers_count'}
)

user_info = check_vk_response(user_info_response)
if user_info:
    user_info = user_info[0]
    print(f"Информация о пользователе: {user_info}")
else:
    exit()

# получение списка подписчиков
followers_response = requests.get(
    base_url + 'users.getFollowers',
    params={**params, 'user_id': user_id, 'count': 100}
)

followers = check_vk_response(followers_response)
if not followers:
    exit()

# подписки пользователя
subscriptions_response = requests.get(
    base_url + 'users.getSubscriptions',
    params={**params, 'user_id': user_id, 'extended': 1}
)

subscriptions = check_vk_response(subscriptions_response)
if not subscriptions:
    exit()

# группы пользователя
groups_response = requests.get(
    base_url + 'groups.get',
    params={**params, 'user_id': user_id, 'extended': 1}
)

groups = check_vk_response(groups_response)
if not groups:
    exit()


data = {
    "user_info": user_info,
    "followers": followers,
    "subscriptions": subscriptions,
    "groups": groups
}

output_file = 'vk_data.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f'Данные сохранены в файл {output_file}')
