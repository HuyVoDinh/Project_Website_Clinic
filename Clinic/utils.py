import hashlib
import json
import os.path
from datetime import datetime
from Clinic import app
from Clinic.models import *



def check_login(username, password):
    # if username and password:
        # password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return taikhoan.query.filter(taikhoan.ten_nguoi_dung.__eq__(username.strip()), taikhoan.mat_khau.__eq__(password)).first()


def get_user_by_id(user_id):
    return taikhoan.query.get(user_id)


def number_current_customer_list():
    return khachhang.query.filter(khachhang.lich_kham.__eq__(datetime.date(datetime.now()))).count()

def add_examination(ho,ten,ngaysinh,cccd,diachi,email,gioitinh,sdt):
    m_khachhang = khachhang(ho_khach = ho,ten_khach = ten, ngay_sinh = ngaysinh,id_cccd = cccd,dia_chi = diachi,email = email,gioi_tinh = gioitinh,sdt = sdt)
    db.session.add(m_khachhang)
    db.session.commit()


def load_medicine(kw = None):
    if kw:
        return thuoc.query.filter(thuoc.ten_thuoc.contains(kw))



def load_role():
    return vaitro.query.filter().all()

