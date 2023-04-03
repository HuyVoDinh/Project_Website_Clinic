import hashlib
import json
import os.path

from Clinic import app
from Clinic.models import taikhoan

def read_json(path):
    with open(path,"r") as f:
        return json.load(f)

def load_categories():
    return read_json(os.path.join(app.root_path,'data/categories.json'))

def check_login(username, password):
    # if username and password:
        # password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return taikhoan.query.filter(taikhoan.ten_nguoi_dung.__eq__(username.strip()), taikhoan.mat_khau.__eq__(password)).first()


def get_user_by_id(user_id):
    return taikhoan.query.get(user_id)