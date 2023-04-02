from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from Clinic import db, app
from datetime import datetime

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

class vaitro:
    ten_vai_tro = Column(String(30))
    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
