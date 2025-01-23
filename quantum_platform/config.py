import os
from datetime import timedelta

class Config:
    """Configuration as the fundamental quantum state of our application."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'quantum_nexus.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    
    SIMULATION_SHOTS_DEFAULT = 1024
    WAVE_FUNCTION_PRECISION = 'float64'

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT', 'false').lower() in ['true', 'on', '1']