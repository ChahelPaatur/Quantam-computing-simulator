from flask import Flask
from quantum_app.auth.routes import auth_bp
from quantum_app.main.routes import main_bp
from quantum_app.quantum.routes import quantum_bp
from quantum_app.db.models import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quantumplatform.db'
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(main_bp, url_prefix="/")
app.register_blueprint(quantum_bp, url_prefix="/quantum")

if __name__ == "__main__":
    app.run(debug=True)
