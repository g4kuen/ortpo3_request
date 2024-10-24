# VK Data Extractor

Этот скрипт предоставляет данные с помощью внешнего VK API, включая информацию о пользователе: подписчики, подписки, группы и сохраняет их в отдельны .json файл

## Features
- Собирает информацию о пользователе (включая количество подписчиков)
- Собирает список подписчиков
- Собирает подписки пользователя
- Собирает группы пользователя
- Сохраняет данные в .json

## Requirements

1.**VK API access token**
2.**Pip packages**:
   - `requests`
   - `python-dotenv`

## Installation

1. Склонируйте проект: https://github.com/g4kuen/ortpo3_request

2. Создайте `.env` файл в корневой директории проекта с соответствующими полями:

   ```
   ACCESS_TOKEN=your_access_token
   USER_ID=your_user_id
   ```

   - замените `your_access_token` на ваш ACCES_TOKEN.
   - замените `your_user_id` на user_id информацию о котором необходимол получить.

## Usage

1. Запуск скрипта:

   ```bash
   python otrpo3.py
   ```

## Example

Here's an example of the output file `vk_data.json`:

```json
{
    "user_info": {
        "id": 123456789,
        "first_name": "Jane",
        "last_name": "Doe",
        "followers_count": 100
    },
    "followers": {
        "count": 100,
        "items": [...]
    },
    "subscriptions": {
        "count": 10,
        "items": [...]
    },
    "groups": {
        "count": 5,
        "items": [...]
    }
}
```