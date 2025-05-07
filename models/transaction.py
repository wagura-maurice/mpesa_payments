# models/transaction.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Enum
from extension import db 

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    # Define the transaction status as an Enum for better clarity
    PENDING = 0
    PROCESSING = 1
    PROCESSED = 2
    REJECTED = 3
    ACCEPTED = 4

    # Define the transaction categories
    PURCHASE_ORDER = 0
    PAYOUT = 1

    # Define the transaction types
    DEBIT = 0
    CREDIT = 1

    # Define the transaction channels
    C2B = 0
    LNMO = 1
    B2C = 2
    B2B = 3

    # Define the transaction aggregator
    MPESA_KE = 0
    PAYPAL_USD = 1

    id = db.Column(db.Integer, primary_key=True)
    _pid = db.Column(db.String, unique=True, nullable=False)  # Unique ID for the transaction
    party_a = db.Column(db.String, nullable=False)  # Payer identity
    party_b = db.Column(db.String, nullable=False)  # Payee identity
    account_reference = db.Column(db.String, nullable=False)  # Reference from the purchase order or payout
    transaction_category = db.Column(db.Integer, nullable=False)  # Purchase order or payout
    transaction_type = db.Column(db.Integer, nullable=False)  # Credit or debit
    transaction_channel = db.Column(db.Integer, nullable=False)  # LNMO/C2B or B2C
    transaction_aggregator = db.Column(db.Integer, nullable=False)  # Payment gateway service provider
    transaction_id = db.Column(db.String, unique=True, nullable=True)  # Unique transaction ID
    transaction_amount = db.Column(db.Numeric(10, 2), nullable=False)  # Amount of the transaction
    transaction_code = db.Column(db.String, unique=True, nullable=True)  # Transaction code
    transaction_timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of the transaction
    transaction_details = db.Column(db.Text, nullable=False)  # Details of the transaction
    _feedback = db.Column(db.JSON, nullable=False)  # Full JSON response from the processor
    _status = db.Column(db.Integer, default=PENDING)  # Status of the transaction
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Creation timestamp
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Update timestamp

    def __repr__(self):
        return f'<Transaction {self.id} - {self._pid}>'
