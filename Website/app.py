from flask import Flask, render_template, url_for,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import os
from database import load_reservations, write_reservations


app = Flask(__name__)

def __repr__(self):
    return '<Task %r>' % self.id

@app.route('/')
def index():
    reserves = load_reservations()
    return render_template('FrontPage.html', reserves = reserves)

@app.route('/staff')
def index1():
    return render_template('Staff.html')

@app.route('/menu')
def index2():
    return render_template('star_light_flyer.pdf')

@app.route('/contactus')
def index3():
    return render_template('ContactUs.html')

@app.route("/reservations/<id>", methods=['post'])
def reservation(id):
    data = request.form
    write_reservations(id, data) 
    return ('submitted.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)