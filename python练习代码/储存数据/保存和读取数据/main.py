from pathlib import Path
import json

path=Path('username.json')

if path.exists():
    data=path.read_text()
    username=json.loads(data)
    print(f"welcome back,{username}!")
else:
    username=input("what is your name? ")
    data=json.dumps(username)
    path.write_text(data)
    print(f"we'll remember you when you come back,{username}")
