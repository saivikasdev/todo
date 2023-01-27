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
class Tests(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    test_name = db.Column(db.String(100))


    def __init__(self,test_name):

        self.id = id
        self.test_name = test_name



        
tests= Tests.query.all()

@app.route('/addtest', methods = ['GET','POST'])
def addtest():

    if request.method == 'POST':

        test_name = request.form['test_name']

        test_data = Tests(test_name)
        db.session.add(test_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

       # return redirect(url_for('Index'))
    return render_template("test_form.html",tests=tests)

if __name__ == "__main__":
    app.run(debug=True)