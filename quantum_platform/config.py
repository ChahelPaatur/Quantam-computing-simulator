import os
from datetime import timedelta

# Determine the base directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Configuration for the Quantum Nexus Platform"""
    # Ensure the instance folder exists
    INSTANCE_PATH = os.path.join(basedir, 'instance')
    os.makedirs(INSTANCE_PATH, exist_ok=True)

    # Database configuration using the instance path
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(INSTANCE_PATH, 'quantum_nexus.db')
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # Additional configuration options
    DEBUG = True
    TESTING = False