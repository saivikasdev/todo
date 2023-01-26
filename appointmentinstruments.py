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
    appointment_id = db.Column(DateTime, default=datetime.datetime.utcnow)
    instrument_id = db.Column(db.String(100))


    def __init__(self, id, appointment_id, instrument_id):

        self.appointment_id = appointment_id
        self.instrument_id = instrument_id
