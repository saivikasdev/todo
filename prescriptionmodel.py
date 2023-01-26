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
class prescriptions(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    appointment_id =  db.Column(db.String(100))
    patient_id = db.Column(db.String(100))
    drugs = db.Column(db.String(100))
    tests = db.Column(db.String(100))
    node = db.Column(db.String(100))
    address = db.Column(db.String(100))
    role =db.Column(db.String(100))


    def __init__(self, id, appointment_id, patient_id,drugs,tests,node):

        self.id = id
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.drugs = drugs
        self.tests = tests
        self.node = node
