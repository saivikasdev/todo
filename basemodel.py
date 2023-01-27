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
class Base(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.String(100))
    created_by = db.Column(db.String(100))
    updated_by = db.Column(db.String(100))
    is_active = db.Column(db.String(100))
    is_deleted =db.Column(db.String(100))


    def __init__(self, id, created_at, updated_at,created_by,updated_by,is_active,is_deleted):

        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by
        self.updated_by = updated_by
        self.is_active = is_active
        self.is_deleted = is_deleted
bases= Base.query.all()

@app.route('/base', methods = ['GET','POST'])
def base():

    if request.method == 'POST':

        id = request.form['id']
        created_at = request.form['created_at']
        updated_at =request.form['updated_at']
        created_by = request.form['created_by']
        updated_by = request.form['updated_by']
        is_active =request.form['isactive']
        is_deleted = request.form['isdeleted']

        base_data = Base(id,created_at,updated_at,created_by,updated_by,is_active,is_deleted)
        db.session.add(base_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

       # return redirect(url_for('Index'))
    return render_template("base_form.html",base=bases)

if __name__ == "__main__":
    app.run(debug=True)