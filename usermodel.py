from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
import datetime
app.app_context().push()
app.secret_key = "Secret Key"
from sqlalchemy import Column, Integer, DateTime ,Boolean
# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/eyegenie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Creating model table for our CRUD database
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name =  db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    password = db.Column(db.String(100))
    role =db.Column(db.String(100))
    address = db.Column(db.String(100))


    def __init__(self, first_name, last_name,email,phone,password,role,address):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password
        self.role = role
        self.address = address

users= User.query.all()

@app.route('/createuser', methods = ['GET','POST'])
def createuser():

    if request.method == 'POST':

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email =request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        role =request.form['role']
        address = request.form['address']

        user_data = User(first_name,last_name,email,phone,password,role,address)
        db.session.add(user_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

       # return redirect(url_for('Index'))
    return render_template("user_form.html",users=users)

if __name__ == "__main__":
    app.run(debug=True)