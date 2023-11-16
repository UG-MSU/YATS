import requests

r = requests.get("http://127.0.0.1:8000/contest/contest-tasks/",
                 params={"id": 9})

print(r.json())