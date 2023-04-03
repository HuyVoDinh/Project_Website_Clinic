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
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check_login(username=username, password = password)
        if user:
            login_user(user=user)
            return redirect(url_for('home'))
        else:
            err_msg = "Sai thông tin tài khoản hoặc mật khẩu"

    return render_template('login.html',err_msg = err_msg)

@app.route('/user-logout')
def user_logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/customerlist')
def customer_list():
    return render_template('customer-list.html')

@login.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id)

@app.route("/medicalregister")
def medical_register():
    return render_template('medical-register.html')

@app.route("/registerdirectly")
def register_directly():
    return render_template('register-directly.html')

if __name__ == "__main__":
    from Clinic.admin import *

    app.run(debug=True)

