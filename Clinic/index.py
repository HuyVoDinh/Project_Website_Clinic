from Clinic import app
from flask import Flask, render_template
import utils

@app.route("/")
def home():
    cates = utils.load_categories()
    return render_template('index.html', categories = cates)

@app.route("/test")
def test():
    return "Welcome to my website"

if __name__ == "__main__":
    app.run(debug=True)

