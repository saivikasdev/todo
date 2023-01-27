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
class instruments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(100))
    description = db.Column(db.String(100))


    def __init__(self, id,name, image,description):

        self.id = id
        self.name = name
        self.image = image
        self.description = description






Instruments= instruments.query.all()

@app.route('/instrument', methods = ['GET','POST'])
def instrument():

    if request.method == 'POST':

        name = request.form['name']
        image =request.form['image']
        description = request.form['description']


        instrument_data = instruments(id,name,image,description)
        db.session.add(instrument_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

       # return redirect(url_for('Index'))
    return render_template("instrument.html",instrument=Instruments)

if __name__ == "__main__":
    app.run(debug=True)