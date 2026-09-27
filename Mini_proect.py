import requests 
import json 

url = "https://api.github.com/repos/microsoft/vscode"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    repo = {

        "name": data["name"],
        "owner": data["owner"]["login"],
        "stars": data["stargazers_count"],
        "language": data["language"],
        "url": data["html_url"]
    }
    print("Дані успішно отримано:")
    print(repo)

    with open ("repository.json", "w", encoding="utf-8") as file:
        json.dump(repo, file, ensure_ascii=False, indent=4)
    print("Дані збережено у repository.json")
else:
    print ("Помилка:", response.status_code)