from Clinic import app, login
from flask import Flask, render_template, request, url_for, redirect,session, jsonify
import utils
from flask_login import login_user, logout_user

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods= ['get', 'post'])
def user_login():
    err_msg = ''
    role_list = utils.load_role()
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check_login(username=username, password = password)
        roles = request.form.get('vaitro')
        if str(user.vaitro_id) == roles:
            login_user(user=user)
            if utils.check_role(user):
                return redirect('/admin')
            else:
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
    cus_list = utils.load_customer_list()

    return render_template('customer-list.html', cus_list=cus_list)

@login.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id)

@app.route("/medicalregister", methods = ['get', 'post'])
def medical_register():
    cr_list = utils.load_current_customer_list()
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
    return render_template('medical-register.html', cr_list = cr_list, size = current_customer_list, err_msg = err_msg)

@app.route("/registerdirectly")
def register_directly():
    return render_template('register-directly.html')

@app.route("/paybill")
def paybill():
    id_phieukham = request.form.get('maPhieu')
    bill = utils.get_phieukham_by_id(id_phieukham)
    if bill is None:
        bill = -1

    return render_template('pay-bill.html', bill=bill, maPhieu=id_phieukham)

@app.route("/taophieukham",  methods = ['get', 'post'])
def taophieukham():

    return render_template('taophieukham.html')


@app.route("/timkiemthuoc",  methods = ['get', 'post'])
def timkiemthuoc():
    kw = request.args.get('kw')
    medicine_list = utils.load_medicine(kw)
    return render_template('timkiemthuoc.html', ls = medicine_list)

@app.route('/api/them_thuoc', methods=['post'])
def them_thuoc():
    data = request.json
    id = str(data.get('id'))
    ten_thuoc = data.get('name')
    gia = data.get('gia')
    soluong = data.get('soLuong')

    import pdb
    pdb.set_trace()

    donthuoc = session.get('donthuoc')
    if donthuoc:
        donthuoc = {}

    if id in donthuoc:
        donthuoc[id]['soluong'] = donthuoc[id]['soluong'] + 1
    else:
        donthuoc[id] ={
            'id': id,
            'ten_thuoc': ten_thuoc,
            'gia': gia,
            'soluong': soluong

        }
    session['donthuoc'] = donthuoc

    return jsonify()

if __name__ == "__main__":
    from Clinic.admin import *

    app.run(debug=True)

