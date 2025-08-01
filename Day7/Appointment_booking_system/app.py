from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

appointments = []  

@app.route('/')
def book():
    return render_template('book.html')

@app.route('/submit', methods=['POST'])
def submit():
    appointment = {
        'name': request.form['name'],
        'email': request.form['email'],
        'date': request.form['date'],
        'time': request.form['time'],
        'message': request.form['message']
    }
    appointments.append(appointment)
    return render_template('confirmation.html', appointment=appointment)

@app.route('/appointments')
def view_appointments():
    return render_template('appointments.html', appointments=appointments)
