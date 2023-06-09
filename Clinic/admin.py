from Clinic import app, db
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user
from flask import redirect, url_for
from Clinic.models import *
# from Clinic.models import Account, Employee

class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.vaitro_id == 1

class TaiKhoanView(AuthenticatedAdmin):
    column_display_pk = True
    can_delete = True
    can_view_details = True
    edit_modal = True
    column_searchable_list = ['ten_nguoi_dung']
    form_excluded_columns = ['vaiTro']
    column_labels = {
        'ten_nguoi_dung': 'Tên Người Dùng',
        'mat_khau': 'Mật Khẩu',
        'hinh_anh': 'Hình Đại Diện',
        'trang_thai': 'Trạng Thái',
    }


class NhanVienView(AuthenticatedAdmin):
    column_display_pk = True
    can_delete = True
    can_view_details = True
    edit_modal = True
    column_searchable_list = ['ten_nv']


class ThuocView(AuthenticatedAdmin):
    column_display_pk = True
    can_delete = True
    can_view_details = True
    edit_modal = True
    column_searchable_list = ['ten_thuoc']

class PhieuKhamView(AuthenticatedAdmin):
    column_display_pk = True
    can_delete = True
    can_view_details = True
    can_export = True
    edit_modal = True

class KhachHangView(AuthenticatedAdmin):
    column_display_pk = True
    can_delete = True
    can_view_details = True
    edit_modal = True
    column_searchable_list = ['ten_khach']

class HoaDonView(AuthenticatedAdmin):
    column_display_pk = True
    can_delete = True
    can_view_details = True
    can_export = True
    edit_modal = True

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if current_user.is_authenticated and current_user.vaitro_id == 1:
            return self.render('admin/index.html')
        return redirect(url_for('user_login'))


admin = Admin(app=app, name="E-connerce Administration", template_mode='bootstrap4', index_view=MyAdminIndexView())
admin.add_view(NhanVienView(NhanVien, db.session, name='Nhân Viên'))
admin.add_view(TaiKhoanView(TaiKhoan, db.session, name='Tài Khoản'))
admin.add_view(ThuocView(Thuoc, db.session, name='Thuốc'))
admin.add_view(HoaDonView(HoaDonThuoc, db.session, name='Hóa đơn'))
admin.add_view(PhieuKhamView(PhieuKhamBenh, db.session, name='Phiếu Khám'))
admin.add_view(KhachHangView(KhachHang, db.session, name='Khách Hàng'))

# admin.add_view(ModelView(Account, db.session))