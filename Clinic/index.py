from Clinic import app, login
from flask import Flask, render_template, request, url_for, redirect
import utils
from flask_login import login_user, logout_user

@app.route("/")
def home():
    cates = utils.load_categories()
    return render_template('index.html')

@app.route("/login", methods= ['get', 'post'])
def user_login():
    err_msg = ''
    role_list = utils.load_role()
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check_login(username=username, password = password)
        if user:
            login_user(user=user)
            return redirect(url_for('home'))
        else:
            err_msg = "Sai thông tin tài khoản hoặc mật khẩu"

    return render_template('login.html',err_msg = err_msg, role_list = role_list)

@app.route('/user-logout')
def user_logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/customerlist')
def customer_list():
    # current_customer_list = utils.load_current_customer_list()
    return render_template('customer-list.html', )

@login.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id)

@app.route("/medicalregister", methods = ['get', 'post'])
def medical_register():
    err_msg=""
    current_customer_list = utils.number_current_customer_list()
    current_customer_list = 40 - current_customer_list
    if current_customer_list < 0:
        current_customer_list = 0

    if request.method.__eq__('POST'):
        ho_khach = request.form.get('hotendem')
        ten_khach = request.form.get('ten')
        ngay_sinh = request.form.get('ngaysinh')
        id_cccd = request.form.get('cccd')
        dia_chi = request.form.get('diachi')
        email = request.form.get('Email')
        gioi_tinh = request.form.get('gioitinh')
        if gioi_tinh == 'Male':
            gioi_tinh = False
        else:
            gioi_tinh = True
        sdt = request.form.get('Sdt')

        try:
            utils.add_examination(ho_khach,ten_khach,ngay_sinh,id_cccd,dia_chi,email,gioi_tinh,sdt)
            return redirect(url_for('home'))
        except Exception as ex:
            err_msg = ex
    return render_template('medical-register.html', size = current_customer_list, err_msg = err_msg)

@app.route("/registerdirectly")
def register_directly():
    return render_template('register-directly.html')

@app.route("/paybill")
def paybill():
    return render_template('pay-bill.html')

@app.route("/taophieukham")
def taophieukham():
    return render_template('taophieukham.html')


if __name__ == "__main__":
    from Clinic.admin import *

    app.run(debug=True)

