from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from quantum.circuit import QuantumCircuit
from quantum.gates import H, X, Y, Z, CNOT
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from database import db
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists')
        else:
            new_user = User(username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/simulation')
@login_required
def simulation():
    return render_template('simulation.html')

@app.route('/run_simulation', methods=['POST'])
@login_required
def run_simulation():
    data = request.json
    num_qubits = data['num_qubits']
    gates = data['gates']

    circuit = QuantumCircuit(num_qubits)

    for gate in gates:
        if gate['name'] == 'H':
            circuit.apply_gate(H, gate['target'])
        elif gate['name'] == 'X':
            circuit.apply_gate(X, gate['target'])
        elif gate['name'] == 'Y':
            circuit.apply_gate(Y, gate['target'])
        elif gate['name'] == 'Z':
            circuit.apply_gate(Z, gate['target'])
        elif gate['name'] == 'CNOT':
            circuit.apply_gate(CNOT, gate['target'], gate['control'])

    circuit.run()
    measurements = circuit.measure_all()
    state_vector = circuit.get_state_vector().tolist()

    return jsonify({
        'measurements': measurements,
        'state_vector': state_vector
    })

@app.route('/explanation')
def explanation():
    return render_template('explanation.html')

@app.route('/wave_function')
def wave_function():
    return render_template('wave_function.html')

@app.route('/comparison')
def comparison():
    return render_template('comparison.html')

if __name__ == '__main__':
    app.run(debug=True)