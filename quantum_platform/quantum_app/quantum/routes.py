from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.quantum.simulator import QuantumCircuit
from app.quantum.wave_function import WaveFunction
from app.models import Simulation

quantum_bp = Blueprint('quantum', __name__)

@quantum_bp.route('/simulator', methods=['GET', 'POST'])
@login_required
def simulator():
    if request.method == 'POST':
        circuit = QuantumCircuit(3)
        circuit.add_gate('H', 0)
        circuit.add_gate('X', 1)
        circuit.add_gate('CNOT', 1, 2)
        results = circuit.run()
        
        # Save the simulation
        simulation = Simulation(
            title='Sample Quantum Circuit',
            circuit_data=str(results),
            user_id=current_user.id
        )
        db.session.add(simulation)
        db.session.commit()
        
        flash('Quantum simulation saved successfully!', 'success')
        return redirect(url_for('quantum.simulator'))
    
    return render_template('quantum/simulator.html')

@quantum_bp.route('/wave-function')
@login_required
def wave_function():
    wave = WaveFunction([1/np.sqrt(2), 1j/np.sqrt(2)])
    wave_data = wave.get_probability_density()
    
    return render_template('quantum/wave_function.html', wave_data=wave_data)

@quantum_bp.route('/tutorial')
def tutorial():
    return render_template('quantum/tutorial.html')

@quantum_bp.route('/comparison')
def comparison():
    return render_template('quantum/comparison.html')