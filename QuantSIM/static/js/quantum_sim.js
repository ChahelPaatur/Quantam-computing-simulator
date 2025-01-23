document.addEventListener('DOMContentLoaded', function() {
    const quantumSim = document.getElementById('quantum-sim');
    if (quantumSim) {
        const numQubitsInput = document.createElement('input');
        numQubitsInput.type = 'number';
        numQubitsInput.min = 1;
        numQubitsInput.max = 5;
        numQubitsInput.value = 2;
        quantumSim.appendChild(numQubitsInput);

        const gateSelect = document.createElement('select');
        ['H', 'X', 'Y', 'Z', 'CNOT'].forEach(gate => {
            const option = document.createElement('option');
            option.value = gate;
            option.textContent = gate;
            gateSelect.appendChild(option);
        });
        quantumSim.appendChild(gateSelect);

        const targetInput = document.createElement('input');
        targetInput.type = 'number';
        targetInput.min = 0;
        targetInput.max = 4;
        targetInput.value = 0;
        quantumSim.appendChild(targetInput);

        const controlInput = document.createElement('input');
        controlInput.type = 'number';
        controlInput.min = 0;
        controlInput.max = 4;
        controlInput.value = 1;
        controlInput.style.display = 'none';
        quantumSim.appendChild(controlInput);

        const addGateButton = document.createElement('button');
        addGateButton.textContent = 'Add Gate';
        quantumSim.appendChild(addGateButton);

        const gateList = document.createElement('ul');
        quantumSim.appendChild(gateList);

        const runButton = document.createElement('button');
        runButton.textContent = 'Run Simulation';
        quantumSim.appendChild(runButton);

        const resultDiv = document.createElement('div');
        quantumSim.appendChild(resultDiv);

        const gates = [];

        gateSelect.addEventListener('change', function() {
            if (this.value === 'CNOT') {
                controlInput.style.display = 'inline';
            } else {
                controlInput.style.display = 'none';
            }
        });

        addGateButton.addEventListener('click', function() {
            const gate = {
                name: gateSelect.value,
                target: parseInt(targetInput.value)
            };
            if (gate.name === 'CNOT') {
                gate.control = parseInt(controlInput.value);
            }
            gates.push(gate);
            const li = document.createElement('li');
            li.textContent = `${gate.name} on qubit ${gate.target}${gate.control !== undefined ? ` controlled by ${gate.control}` : ''}`;
            gateList.appendChild(li);
        });

        runButton.addEventListener('click', function() {
            fetch('/run_simulation', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    num_qubits: parseInt(numQubitsInput.value),
                    gates: gates
                })
            })
            .then(response => response.json())
            .then(data => {
                resultDiv.innerHTML = `
                    <h3>Measurements:</h3>
                    <p>${data.measurements.join(', ')}</p>
                    <h3>State Vector:</h3>
                    <p>${data.state_vector.map(c => `${c[0].toFixed(2)}${c[1] >= 0 ? '+' : ''}${c[1].toFixed(2)}i`).join(', ')}</p>
                `;
            });
        });
    }

    const waveFunctionVis = document.getElementById('wave-function-vis');
    if (waveFunctionVis) {
        // Add wave function visualization logic here
        waveFunctionVis.innerHTML = '<p>Wave function visualization coming soon!</p>';
    }
});