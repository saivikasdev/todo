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
class drugs(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tradeName = db.Column(db.String(100))
    genericName = db.Column(db.String(100))
    note = db.Column(db.String(100))
    unit = db.Column(db.String(100))
    type = db.Column(db.String(100))
    tags = db.Column(db.String(100))


    def __init__(self, id, tradeName, genericName,note,unit,type,tags):

        self.id = id
        self.tradeName = tradeName
        self.genericName = genericName
        self.note = note
        self.unit = unit
        self.type = type
        self.tags = tags



Drugs= drugs.query.all()

@app.route('/drug', methods = ['GET','POST'])
def drug():

    if request.method == 'POST':

        tradeName = request.form['tradeName']
        genericName =request.form['genericName']
        note = request.form['note']
        unit = request.form['unit']
        is_active =request.form['type']
        is_deleted = request.form['tags']

        drug_data = drugs(id,tradeName,genericName,note,unit,is_active,is_deleted)
        db.session.add(drug_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

       # return redirect(url_for('Index'))
    return render_template("drug_form.html",drug=Drugs)

if __name__ == "__main__":
    app.run(debug=True)