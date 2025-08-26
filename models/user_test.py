import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import json
from rich import print
from models import User
from pathlib import Path

def get_user(filepath) -> User:
    path = Path(__file__).parent.parent / filepath
    with open(path) as f:
        data = json.load(f)
    user = User.model_validate(data)
    return user

def get_users(filepath) -> list[User]:
    path = Path(__file__).parent.parent / filepath
    with open(path) as f:
        data = json.load(f)
    users = [User(**user) for user in data]
    return users


if __name__ == "__main__":
    # -------------------------------
    # user.json   (object)
    # -------------------------------
    user = get_user("data/user.json")    
    print(user)

    # -------------------------------
    # users.json  (list)
    # -------------------------------
    users = get_users("data/users.json")
    print(users)
