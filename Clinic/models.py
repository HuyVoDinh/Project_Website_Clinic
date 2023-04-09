from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean, Text, Enum
from sqlalchemy.orm import relationship
from Clinic import db, app
from enum import Enum as UserEnum
from datetime import datetime
from flask_login import UserMixin


# category_id = Column(Integer,ForeignKey(Account.id))

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)

class NhanVien(BaseModel):
    # __tablename__ = 'nhanvien'
    # nv_id = Column(Integer, primary_key=True, autoincrement=True)
    ngay_lam_viec = Column(DateTime, default=datetime.now())
    kinh_nghiem = Column(Float, default=0)
    chuc_vu = Column(String(255), nullable=False)
    hinh_anh = Column(String(255), nullable=False)
    ten_nv = Column(String(30), nullable=False)
    ho_nv = Column(String(30), nullable=False)
    ngay_sinh = Column(DateTime, default=datetime.now())
    id_cccd = Column(Integer, nullable=False)
    dia_chi = Column(String(255), nullable=False)
    email = Column(String(255))
    gioi_tinh = Column(Boolean, default=True)
    taikhoan = relationship('TaiKhoan', backref='NhanVien', lazy=True)
    yTa = relationship('YTa', backref='NhanVien', lazy=True)
    thuNgan = relationship('ThuNgan', backref='NhanVien', lazy=True)
    qtv = relationship('QTV', backref='NhanVien', lazy=True)


    def __str__(self):
        return self.name

class BacSi(BaseModel):

    bs_id = Column(Integer, ForeignKey(NhanVien.id), nullable=False)

    def __str__(self):
        return self.name

class YTa(BaseModel):
    yt_id = Column(Integer, ForeignKey(NhanVien.id), nullable=False)
    def __str__(self):
        return self.name

class ThuNgan(BaseModel):
    tn_id = Column(Integer, ForeignKey(NhanVien.id), nullable=False)
    hoadon = relationship('HoaDonThuoc', backref='thungan', lazy=True)


    def __str__(self):
         return self.name
#
#
class QTV(BaseModel):
    qtv_id = Column(Integer, ForeignKey(NhanVien.id), nullable=False)
    dsquydinh = relationship('QuyDinh', backref='qtv', lazy=True)
    def __str__(self):
        return self.name

class VaiTro(BaseModel):
    #VaiTro_id = Column(Integer, primary_key=True, autoincrement=True)
    ten_vai_tro = Column(String(30))
    #taikhoan = relationship('TaiKhoan', backref='VaiTro', lazy=True)

    def __str__(self):
        return self.name


class TaiKhoan(BaseModel, UserMixin):
    #taikhoan_id = Column(Integer, primary_key=True, autoincrement=True)
    ten_nguoi_dung = Column(String(30), nullable=False)
    mat_khau = Column(String(30), nullable=False)
    hinh_anh = Column(String(255))
    trang_thai = Column(Boolean, default=True)
    vaitro_id = Column(Integer, ForeignKey(VaiTro.id), nullable=False)
    # nhanvien = relationship('NhanVien', backref='TaiKhoan', lazy=True)
    nhanvien_id = Column(Integer, ForeignKey(NhanVien.id), nullable=False)
    def __str__(self):
        return self.name

class LoaiThuoc(BaseModel):
    # loaithuoc_id = Column(Integer, primary_key=True, autoincrement=True)
    ten_loai_thuoc = Column(String(100), nullable=False)
    thuoc = relationship('Thuoc', backref='LoaiThuoc', lazy=True)

    def __str__(self):
        return self.name
class Thuoc(BaseModel):
    # thuoc_id = Column(Integer, primary_key=True, autoincrement=True)
    ten_thuoc = Column(String(30), nullable=False)
    so_luong = Column(Integer, default=0)
    gia = Column(Float, default=0)
    ngay_nhap = Column(DateTime, default=datetime.now())
    lieu_luong = Column(String(255), nullable=False)
    nha_san_xuat = Column(String(255), nullable=False)
    mo_ta = Column(Text)
    loaithuoc_id = Column(Integer, ForeignKey(LoaiThuoc.id), nullable=False)

    def __str__(self):
        return self.name



class KhachHang(BaseModel):
    # khach_id = Column(Integer, primary_key=True, autoincrement=True)
    ho_khach = Column(String(30), nullable=False)
    ten_khach = Column(String(30), nullable=False)
    #ngay_sinh = Column(DateTime, default=datetime.date())
    id_cccd = Column(String(50), nullable=False)
    dia_chi = Column(String(50))
    email = Column(String(50))
    gioi_tinh = Column(Boolean, default=True)
    sdt = Column(String(50))

    # tailieu = relationship('TaiLieu', backref='khachhang', lazy=True)

    def __str__(self):
        return self.name



class TaiLieu(BaseModel):
    # id = Column(Integer, primary_key=True, autoincrement=True)
    ngay_tao = Column(DateTime, default=datetime.now())
    loai_tai_lieu = Column(String(100))
    khachhang_id = Column(Integer, ForeignKey(KhachHang.id), nullable=False)

    def __str__(self):
        return self.name


class ChiTietPhieuKham(db.Model):
    thuoc = Column('thuoc_id', Integer, ForeignKey(Thuoc.id), nullable=False, primary_key=True)
    tailieu = Column('tailieu_id', Integer, ForeignKey(TaiLieu.id), nullable=False, primary_key=True)
    so_luong = Column(Integer, default=0)
    lieu_luong = Column(Text)
    cach_su_dung = Column(Text)

    def __str__(self):
        return self.name


class PhieuKhamBenh(BaseModel):
    # id = Column(Integer, ForeignKey('TaiLieu.id'), primary_key=True)
    trieu_chung = Column(Text)
    chan_doan = Column(Text)

    bs_id = Column(Integer, ForeignKey(BacSi.id))
    hoadon = relationship('HoaDonThuoc', backref='phieukhambenh', lazy=True)
    dsthuoc = relationship('Thuoc', secondary='ChiTietPhieuKham', backref='dsphieukhambenh', lazy=True)

    def __str__(self):
        return self.name


class HoaDonThuoc(BaseModel):

    gia_thuoc = Column(Float, default=0, nullable=False)
    gia_kham_benh = Column(Float, default=0, nullable=False)
    tong_hoa_don = Column(Float, default=0, nullable=False)

    thungnan_id = Column(Integer, ForeignKey(ThuNgan.id), nullable=False)
    phieukham_id = Column(Integer, ForeignKey(PhieuKhamBenh.id), nullable=False)

    def __str__(self):
        return self.name


class QuyDinh(BaseModel):

    ten = Column(String(50), nullable=False)
    mo_ta = Column(String(255))
    ngay_tao = Column(DateTime, default=datetime.now())
    trang_thai = Column(Boolean, default=True)

    qtv_id = Column(Integer, ForeignKey(QTV.id), nullable=False)

    def __str__(self):
        return self.name


class Role(UserEnum):
    ADMIN = 1,
    NURSE = 2,
    DOCTOR = 3,
    CASHIER = 4


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

