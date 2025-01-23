from datetime import timedelta
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'quantum-superposition-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///quantum.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)