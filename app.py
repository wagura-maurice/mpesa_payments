# app.py
from flask import Flask
from extension import db
from controllers.lnmo_controller import lnmo_controller


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://postgres:2345@localhost:5432/mpesa"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize db with app
    db.init_app(app)

    # Import models after db initialization to avoid circular imports
    with app.app_context():
        from models.transaction import Transaction

        db.create_all()

    # Register blueprints
    app.register_blueprint(lnmo_controller, url_prefix="/ipn/daraja")

    @app.route("/")
    def index():
        return "Welcome to the MPESA Payments API!"

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
