from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from quantum_app.main.routes import main_bp
    from quantum_app.auth.routes import auth_bp
    from quantum_app.quantum.routes import quantum_bp
    # from quantum_app.user.routes import user_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(quantum_bp, url_prefix='/quantum')
    # app.register_blueprint(user_bp, url_prefix='/user')

    return app