from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user, login_user, logout_user
from app.models import User, Simulation
from app import db

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__, url_prefix='/auth')
quantum = Blueprint('quantum', __name__, url_prefix='/quantum')

@main.route('/')
def home():
    return render_template('home.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('main.home'))
        flash('Invalid username or password')
    return render_template('auth/login.html')

@quantum.route('/simulator')
@login_required
def simulator():
    return render_template('quantum/simulator.html')

@quantum.route('/wave-function')
@login_required
def wave_function():
    return render_template('quantum/wave_function.html')