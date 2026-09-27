import requests
import csv

url = "https://api.github.com/repos/microsoft/vscode"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    repo = {
        "name": data["name"],
        "owner": data["owner"]["login"],
        "stars": data["stargazers_count"],
        "language": data["language"]
    }

    with open("repository.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Owner", "Stars", "Language"])

        writer.writerow([
            repo["name"],
            repo["owner"],
            repo["stars"],
            repo["language"]
        ])

    print("Дані збережено у repository.csv")

else:
    print("Помилка:", response.status_code)