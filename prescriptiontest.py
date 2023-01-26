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
class prescriptionstests(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    prescription_id =  db.Column(db.String(100))
    test_id = db.Column(db.String(100))
    advice = db.Column(db.String(100))


    def __init__(self, id, prescription_id, test_id,advice):

        self.id = id
        self.prescription_id = prescription_id
        self.test_id = test_id
        self.advice = advice
