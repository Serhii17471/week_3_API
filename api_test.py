import requests 

url = url = "https://api.github.com/repos/microsoft/vscode"

response = requests.get(url)
print("Status:", response.status_code)

data = response.json()

print("Назва:", data["name"])
print("Повна назва:", data["full_name"])
print("Зірки:", data["stargazers_count"])
print("Відкриті issues:", data["open_issues_count"])
print("Мова:", data["language"])