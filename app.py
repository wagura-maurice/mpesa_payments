# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.lnmo_controller import lnmo_controller

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mpesa.db'  # Change this to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Register the LNMO controller routes
app.register_blueprint(lnmo_controller, url_prefix='/ipn/daraja')

@app.route('/')
def index():
    """
    Home route for the application.
    """
    return "Welcome to the MPESA Payments API!"

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
