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
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(DateTime, default=datetime.datetime.utcnow)
    end_time = db.Column(db.String(100))
    patient_id = db.Column(db.String(100))
    executive_id = db.Column(db.String(100))
    doctor_id = db.Column(db.String(100))


    def __init__(self, id, start_time, end_time,patient_id,executive_id,doctor_id):

        self.start_time = start_time
        self.end_time = end_time
        self.patient_id = patient_id
        self.executive_id = executive_id
        self.doctor_id = doctor_id


        
appos= Appointment.query.all()

@app.route('/appo', methods = ['GET','POST'])
def appo():

    if request.method == 'POST':

        start_time = request.form['start_time']
        end_time = request.form['end_time']
        patient_id =request.form['patient_id']
        executive_id = request.form['executive_id']
        doctor_id = request.form['doctor_id']

        appo_data = Appointment(id,start_time,end_time,patient_id,executive_id,doctor_id)
        db.session.add(appo_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

       # return redirect(url_for('Index'))
    return render_template("appo_form.html",appo=appos)

if __name__ == "__main__":
    app.run(debug=True)