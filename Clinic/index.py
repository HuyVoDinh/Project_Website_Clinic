from Clinic import app
from flask import Flask, render_template
import utils

@app.route("/")
def home():
    cates = utils.load_categories()
    return render_template('index.html', categories = cates)

@app.route("/medicalregister")
def medical_register():
    return render_template('medical-register.html')

if __name__ == "__main__":
    app.run(debug=True)

