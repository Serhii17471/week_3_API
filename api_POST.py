import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Telegram bot",
    "body": "Створюю свого першого телеграм бота",
    "userId": 7
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Вілповідь сервера:")
print(response.json())