import json
import os

DATA_FILE = 'data/data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        return {"users": {}}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_user_score(user_id, data):
    return data["users"].get(str(user_id), {"score": 0})["score"]

def update_user_score(user_id, score, data):
    if str(user_id) not in data["users"]:
        data["users"][str(user_id)] = {"score": 0}
    data["users"][str(user_id)]["score"] += score
    save_data(data)
