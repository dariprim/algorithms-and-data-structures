import requests

url = "https://www.youtube.com"

payload={'login_username': '89628493323',
'login_password': 'KANAEV_57_147_154'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.cookies)
