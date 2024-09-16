from flask import Flask
import views
from extensions import db,security
import create_initial_data

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "my-secret-key"
    app.config['SQLALCHEMY_DATABASE_URI']  = "sqlite:///db.sqlite3"
    app.config['SECURITY_PASSWORD_SALT'] = "salty-password"
    
    db.init_app(app)
    
    with app.app_context():
        from models import User,Role
        from flask_security import SQLAlchemyUserDatastore
        user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        security.init_app(app,user_datastore)
        db.create_all()
        create_initial_data.create_data(user_datastore)
    
    views.create_view(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)