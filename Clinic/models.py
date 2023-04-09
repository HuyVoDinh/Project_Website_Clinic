from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean, Text, Enum
from sqlalchemy.orm import relationship
from Clinic import db, app
from datetime import datetime
from enum import Enum as UserEnum
from flask_login import UserMixin

# category_id = Column(Integer,ForeignKey(Account.id))

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class Nhanvien(BaseModel):
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

class Vaitro(UserEnum):
    ADMIN = 1
    DOCTOR = 2
    CASHIER = 3
    NURSER = 4

    def __str__(self):
        return self.name

class Taikhoan(BaseModel, UserMixin):
    ten_nguoi_dung = Column(String(30))
    mat_khau = Column(String(30))
    hinh_anh = Column(String(255))
    trang_thai = Column(Boolean)
    vai_tro = Column(Enum(Vaitro), default=Vaitro.ADMIN)

    def __str__(self):
        return self.name

class Bacsi(BaseModel):
    nhanvien_id = Column(Integer, ForeignKey(Nhanvien.id))
    phieu_kham = Column(Integer, ForeignKey('phieukhambenh.id'), nullable=True)

    def __str__(self):
        return self.name

class Yta(BaseModel):
    nhanvien_id = Column(Integer, ForeignKey(Nhanvien.id))
    khach_hang = Column(Integer, ForeignKey('khachhang.id'), nullable=True)

    def __str__(self):
        return self.name

class Thungan(BaseModel):
    nhanvien_id = Column(Integer, ForeignKey(Nhanvien.id))
    hoa_don = Column(Integer, ForeignKey('hoadon.id'), nullable=True)

    def __str__(self):
        return self.name

class QTV(BaseModel):
    nhanvien_id = Column(Integer, ForeignKey(Nhanvien.id))
    tai_lieu = Column(Integer, ForeignKey('tailieu.id'), nullable=True)

    def __str__(self):
        return self.name

class Thuoc(BaseModel):
    ten_thuoc = Column(String(30))
    so_luong = Column(Integer)
    gia = Column(Float)
    ngay_nhap = Column(Integer)
    lieu_luong = Column(String(255))
    nha_san_xuat = Column(String(255))
    mo_ta = Column(Text)
    loai_thuoc = relationship('loaithuoc', backref='thuoc', lazy=False)
    qtv = relationship('QTV', backref='Thuoc', lazy=False)


    def __str__(self):
        return self.name

class loaithuoc(BaseModel):
    ten_loai_thuoc =  Column(String(100))
    thuoc = Column(Integer, ForeignKey('thuoc.id'), nullable=False)

    def __str__(self):
        return self.name

class Tailieu(BaseModel):
    ngay_tao =  Column(DateTime)
    loai_tai_lieu = Column(String(50))
    phieu_kham_benh = relationship('Phieukhambenh', backref='tailieu', lazy=False)

    def __str__(self):
        return self.name

phieu_thuoc = db.Table('phieu_thuoc',
                       Column('phieukhambenh_id', Integer, ForeignKey('phieukhambenh.id'), primary_key=True),
                       Column('thuoc_id', Integer, ForeignKey('thuoc.id'), primary_key=True))


class Phieukhambenh(BaseModel):
    trieu_chung = Column(Text)
    chan_doan = Column(Text)
    tai_lieu = Column(Integer, ForeignKey('tailieu.id'), nullable=True)
    bac_si = relationship('Bacsi', backref='phieukhambenh', lazy=False)

    def __str__(self):
        return self.name

class Hoadonthuoc(BaseModel):
    gia_thuoc = Float
    gia_kham_benh = Float
    thu_ngan = relationship('Thungan', backref='hoadonthuoc', lazy=False)

    def __str__(self):
        return self.name

class Khachhang(BaseModel):
    ho_khach = Column(String(30))
    ten_khach = Column(String(30))
    ngay_sinh = Column(DateTime)
    id_cccd = Column(String(50))
    dia_chi = Column(String(50))
    email = Column(String(50))
    gioi_tinh = Column(Boolean)
    lich_kham = Column(DateTime, default=datetime.date(datetime.now()))
    sdt = Column(String(50))
    y_ta = relationship('Yta', backref='khachhang', lazy=False)


    def __str__(self):
        return self.name




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        #data = khachhang(ho_khach = "A", ten_khach = "B", ngay_sinh = datetime.date(datetime.now()), id_cccd= "1", dia_chi = "x",email = "a", gioi_tinh = 1, sdt = "1")

        #db.session.add(data)

        #db.session.commit()