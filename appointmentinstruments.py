from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
import datetime
app.app_context().push()
app.secret_key = "Secret Key"
from sqlalchemy import Column, Integer, DateTime
# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/eyegenie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Creating model table for our CRUD database
class Appointmentinstruments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    appointment_id = db.Column(db.String(100))
    instrument_id = db.Column(db.String(100))


    def __init__(self,  appointment_id, instrument_id):

        self.appointment_id = appointment_id
        self.instrument_id = instrument_id




       
appo_instruments_= Appointmentinstruments.query.all()

@app.route('/appo_instruments', methods = ['GET','POST'])
def appo_instruments():

    if request.method == 'POST':

        appointment_id = request.form['appointment_id']
        instrument_id = request.form['instrument_id']

        appo_data = Appointmentinstruments(appointment_id,instrument_id)
        db.session.add(appo_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

       # return redirect(url_for('Index'))
    return render_template("appo_instruments.html",appo_instrument=appo_instruments_)

if __name__ == "__main__":
    app.run(debug=True)

