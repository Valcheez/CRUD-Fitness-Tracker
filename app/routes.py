from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import FitnessEntry
from datetime import datetime

@app.route('/')
def index():
    entries = FitnessEntry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    date_str = request.form.get('day')
    workout = request.form.get('workout')
    exercises = request.form.get('exercises')

    day = datetime.strptime(date_str, "%Y-%m-%d").date() #converts date into a string


    new_entry = FitnessEntry(day=day, workout=workout, exercises=exercises)
    db.session.add(new_entry)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_entry(id):
    entry = FitnessEntry.query.get(id)
    db.session.delete(entry)
    db.session.commit()

    return redirect(url_for('index'))


