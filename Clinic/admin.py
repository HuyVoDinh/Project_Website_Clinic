from Clinic import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import  ModelView
# from Clinic.models import Account, Employee

admin = Admin(app=app, name="E-connerce Administration", template_mode='bootstrap4')

# admin.add_view(ModelView(Account, db.session))