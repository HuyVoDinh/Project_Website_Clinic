from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean, Text, Enum
from sqlalchemy.orm import relationship
from Clinic import db, app
from enum import Enum as UserEnum
from datetime import datetime
from flask_login import UserMixin


# category_id = Column(Integer,ForeignKey(Account.id))

class NhanVien(db.Model):
    # __tablename__ = 'nhanvien'
    # nv_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(Integer, primary_key=True, autoincrement=True)
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
    yTa = relationship('YTa', backref='NhanVien', lazy=True)
    thuNgan = relationship('ThuNgan', backref='NhanVien', lazy=True)
    qtv = relationship('QTV', backref='NhanVien', lazy=True)

    def __str__(self):
        return self.name


class BacSi(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    bs_id = Column(Integer, ForeignKey(NhanVien.id), nullable=False)

    def __str__(self):
        return self.name


class YTa(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    yt_id = Column(Integer, ForeignKey(NhanVien.id), nullable=False)
    def __str__(self):
        return self.name


class ThuNgan(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    tn_id = Column(Integer, ForeignKey(NhanVien.id), nullable=False)
    hoadon = relationship('HoaDonThuoc', backref='thungan', lazy=True)

    def __str__(self):
         return self.name
#
#
class QTV(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    qtv_id = Column(Integer, ForeignKey(NhanVien.id), nullable=False)
    dsquydinh = relationship('QuyDinh', backref='qtv', lazy=True)

    def __str__(self):
        return self.name

class VaiTro(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    #VaiTro_id = Column(Integer, primary_key=True, autoincrement=True)
    ten_vai_tro = Column(String(30))
    taikhoan = relationship('TaiKhoan', backref='vaitro', lazy=True)

    def __str__(self):
        return self.name


class TaiKhoan(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    #taikhoan_id = Column(Integer, primary_key=True, autoincrement=True)
    ten_nguoi_dung = Column(String(30), nullable=False)
    mat_khau = Column(String(30), nullable=False)
    hinh_anh = Column(String(255))
    trang_thai = Column(Boolean, default=True)
    vaitro_id = Column(Integer, ForeignKey(VaiTro.id), nullable=False)
    # nhanvien = relationship('NhanVien', backref='TaiKhoan', lazy=True)

    def __str__(self):
        return self.name


class LoaiThuoc(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # loaithuoc_id = Column(Integer, primary_key=True, autoincrement=True)
    ten_loai_thuoc = Column(String(100), nullable=False)
    thuoc_id = relationship('Thuoc', backref='LoaiThuoc', lazy=True)

    def __str__(self):
        return self.name


class Thuoc(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # thuoc_id = Column(Integer, primary_key=True, autoincrement=True)
    ten_thuoc = Column(String(30), nullable=False)
    so_luong = Column(Integer, default=0)
    gia = Column(Float, default=0)
    ngay_nhap = Column(DateTime, default=datetime.now())
    lieu_luong = Column(String(255), nullable=False)
    nha_san_xuat = Column(String(255), nullable=False)
    mo_ta = Column(Text)
    chi_tiet_phieu_kham = relationship('ChiTietPhieuKham', backref='thuoc', lazy=True)
    loaithuoc_id = Column(Integer, ForeignKey(LoaiThuoc.id), nullable=False)

    def __str__(self):
        return self.name


class KhachHang(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # khach_id = Column(Integer, primary_key=True, autoincrement=True)
    ho_khach = Column(String(30), nullable=False)
    ten_khach = Column(String(30), nullable=False)
    ngay_sinh = Column(DateTime, default=datetime.now())
    id_cccd = Column(String(50), nullable=False)
    dia_chi = Column(String(50))
    email = Column(String(50))
    gioi_tinh = Column(Boolean, default=True)
    sdt = Column(String(50))
    lich_kham = Column(DateTime, default=datetime.date(datetime.now()))
    phieukham = relationship('PhieuKhamBenh', backref='khachHang', lazy=True)
    # tailieu = relationship('TaiLieu', backref='khachhang', lazy=True)

    def __str__(self):
        return self.name



class TaiLieu(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ngay_tao = Column(DateTime, default=datetime.now())
    loai_tai_lieu = Column(String(100))
    khachhang_id = Column(Integer, ForeignKey(KhachHang.id), nullable=False)

    def __str__(self):
        return self.name


class PhieuKhamBenh(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    trieu_chung = Column(Text)
    chan_doan = Column(Text)
    bs_id = Column(Integer, ForeignKey(BacSi.id))
    khachHang_id = Column(Integer, ForeignKey(KhachHang.id), nullable=False)
    hoadon = relationship('HoaDonThuoc', backref='phieukhambenh', lazy=True)
    chi_tiet_phieu_kham = relationship('ChiTietPhieuKham', backref='phieuKhamBenh', lazy=True)

    def __str__(self):
        return self.name


class ChiTietPhieuKham(db.Model):
    thuoc_id = Column( Integer, ForeignKey(Thuoc.id), nullable=False, primary_key=True)
    phieuKhamBenh_id = Column(Integer, ForeignKey(PhieuKhamBenh.id), nullable=False, primary_key=True)
    so_luong = Column(Integer, default=0)
    lieu_luong = Column(Text)
    cach_su_dung = Column(Text)

    def __str__(self):
        return self.name


class HoaDonThuoc(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    gia_thuoc = Column(Float, default=0, nullable=False)
    gia_kham_benh = Column(Float, default=0, nullable=False)
    tong_hoa_don = Column(Float, default=0, nullable=False)
    thungnan_id = Column(Integer, ForeignKey(ThuNgan.id), nullable=False)
    phieukham_id = Column(Integer, ForeignKey(PhieuKhamBenh.id), nullable=False)

    def __str__(self):
        return self.name


class QuyDinh(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(50), nullable=False)
    mo_ta = Column(String(255))
    ngay_tao = Column(DateTime, default=datetime.now())
    trang_thai = Column(Boolean, default=True)
    qtv_id = Column(Integer, ForeignKey(QTV.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

