from msilib import init_database
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.db'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


dbusers=SQLAlchemy(app)
class Users(dbusers.Model):
    id = dbusers.Column(dbusers.Integer, primary_key=True)
    username = dbusers.Column(dbusers.String(20), nullable=False)
    password = dbusers.Column(dbusers.String(20), nullable=False)
    email = dbusers.Column(dbusers.String(20), nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.id

dbitems=SQLAlchemy(app)
class Item(dbitems.Model):
    id = dbitems.Column(dbitems.Integer, primary_key=True)
    name = dbitems.Column(dbitems.String(20), nullable=False)
    price = dbitems.Column(dbitems.String(20), nullable=False)
    quantity = dbitems.Column(dbitems.String(20), nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.id


@app.route('/')
def index():
    return render_template("html/index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        user = Users(username=username, password=password, email=email)
        
        try:
            dbusers.session.add(user)
            dbusers.session.commit()
            return redirect('/')
        except: 
            return "error"
    else:
        return render_template("html/login.html")


@app.route('/additem', methods=['POST', 'GET'])
def additem():
    if request.method == "POST":
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']

        item = Item(name=name, price=price, quantity=quantity)
        
        try:
            dbitems.session.add(item)
            dbitems.session.commit()
            return redirect('/')
        except: 
            return "error"
    else:
        return render_template("html/additem.html")

# test
if __name__=="__main__":
    app.run(debug=True)

