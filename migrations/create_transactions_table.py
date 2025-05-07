# migrations/create_transactions_table.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    _pid = db.Column(db.String, unique=True)
    party_a = db.Column(db.String)
    party_b = db.Column(db.String)
    account_reference = db.Column(db.String)
    transaction_category = db.Column(db.Integer)
    transaction_type = db.Column(db.Integer)
    transaction_channel = db.Column(db.Integer)
    transaction_aggregator = db.Column(db.Integer)
    transaction_id = db.Column(db.String, unique=True)
    transaction_amount = db.Column(db.Numeric(10, 2))
    transaction_code = db.Column(db.String, unique=True)
    transaction_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    transaction_details = db.Column(db.Text)
    _feedback = db.Column(db.JSON)
    _status = db.Column(db.Integer, default=0)  # Default to PENDING
