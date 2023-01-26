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
class prescriptionsdrugs(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    prescription_id =  db.Column(db.String(100))
    drug_id = db.Column(db.String(100))
    dose = db.Column(db.String(100))
    node = db.Column(db.String(100))
    advice = db.Column(db.String(100))
    duration =db.Column(db.String(100))


    def __init__(self, id, prescription_id, drug_id,dose,advice,duration):

        self.id = id
        self.prescription_id = prescription_id
        self.drug_id = drug_id
        self.dose = dose
        self.advice = advice
        self.duration = duration
