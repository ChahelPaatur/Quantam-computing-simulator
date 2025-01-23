import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from quantum_app import create_app, db
from quantum_app.models import User, Simulation

# Ensure the .env file is loaded
load_dotenv()

# Create the application
app = create_app()

# Initialize Flask-Migrate
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    """Provide shell context for Flask CLI"""
    return {
        'db': db,
        'User': User,
        'Simulation': Simulation
    }

def create_database():
    """Create database tables"""
    with app.app_context():
        # Create all tables
        db.create_all()
        print(" Quantum Database Initialized")

def main():
    """Main application entry point"""
    # Validate critical configurations
    if not os.getenv('SECRET_KEY'):
        raise RuntimeError(" Quantum Encryption Key Missing!")

    print("""
    ╔══════════════════════════════════════════╗
    ║             QUANTUM  PLATFORM            ║
    ║   Transforming Computational Potential   ║
    ╚══════════════════════════════════════════╝
    """)

    # Ensure database is created
    create_database()

    # Run the application
    app.run(
        host='0.0.0.0', 
        port=5000, 
        debug=True
    )

if __name__ == "__main__":
    main()