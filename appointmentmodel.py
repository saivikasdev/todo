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


    def __init__(self, id, start_time, end_time,patient__id,executive_id,doctor_id):

        self.start_time = start_time
        self.end_time = end_time
        self.patient__id = patient__id
        self.executive_id = executive_id
        self.doctor_id = doctor_id
