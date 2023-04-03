from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from Clinic import db, app
from datetime import datetime
from flask_login import UserMixin

# category_id = Column(Integer,ForeignKey(Account.id))

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class nhanvien(BaseModel):
    __tablename__ = 'nhanvien'
    ngay_lam_viec = Column(DateTime)
    kinh_nghiem = Column(Float)
    chuc_vu = Column(String(255))
    hinh_anh = Column(String(255))
    ten_nv = Column(String(30))
    ho_nv = Column(String(30))
    ngay_sinh = Column(DateTime)
    id_cccd = Column(Integer)
    dia_chi = Column(String(255))
    email = Column(String(255))
    gioi_tinh = Column(Boolean)

    def __str__(self):
        return self.name

class vaitro(BaseModel):
    ten_vai_tro = Column(String(30))

    def __str__(self):
        return self.name

class taikhoan(BaseModel, UserMixin):
    ten_nguoi_dung = Column(String(30))
    mat_khau = Column(String(30))
    hinh_anh = Column(String(255))
    trang_thai = Column(Boolean)

    def __str__(self):
        return self.name

class bacsi(BaseModel):
    nhanvien_id = Column(Integer, ForeignKey(nhanvien.id))

    def __str__(self):
        return self.name

class yta(BaseModel):
    nhanvien_id = Column(Integer, ForeignKey(nhanvien.id))

    def __str__(self):
        return self.name

class thungan(BaseModel):
    nhanvien_id = Column(Integer, ForeignKey(nhanvien.id))

    def __str__(self):
        return self.name

class QTV(BaseModel):
    nhanvien_id = Column(Integer, ForeignKey(nhanvien.id))

    def __str__(self):
        return self.name

class thuoc(BaseModel):
    ten_thuoc = Column(String(30))
    so_luong = Column(Integer)
    gia = Column(Float)
    ngay_nhap = Column(Integer)
    lieu_luong = Column(String(255))
    nha_san_xuat = Column(String(255))
    mo_ta = Column(Text)

    def __str__(self):
        return self.name

class loaithuoc(BaseModel):
    ten_loai_thuoc =  Column(String(100))

    def __str__(self):
        return self.name

class tailieu(BaseModel):
    ngay_tao =  Column(DateTime)
    loai_tai_lieu = Column(String(50))

    def __str__(self):
        return self.name

class phieukhambenh(BaseModel):
    trieu_chung = Column(Text)
    chan_doan = Column(Text)

    def __str__(self):
        return self.name

class hoadonthuoc(BaseModel):
    gia_thuoc = Float
    gia_kham_benh = Float
    tong_hoa_don = Float

    def __str__(self):
        return self.name

class quytrinh(BaseModel):
    ten = Column(String(50))
    mo_ta = Column(String(255))
    ngay_tao = Column(DateTime)
    trang_thai = Column(Boolean)

    def __str__(self):
        return self.name


class khachhang(BaseModel):
    ho_khach = Column(String(30))
    ten_khach = Column(String(30))
    ngay_sinh = Column(DateTime)
    id_cccd = Column(String(50))
    dia_chi = Column(String(50))
    email = Column(String(50))
    gioi_tinh = Column(Boolean)
    sdt = String(String(50))

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
