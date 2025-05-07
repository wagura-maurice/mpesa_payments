# repositories/lnmo_repository.py
import requests
from models.transaction import Transaction, db
from datetime import datetime

class LNMORepository:
    # Hardcoded configurations
    MPESA_LNMO_CONSUMER_KEY = 'uKxU78Y9q2cFruO2fKRWuofRCObzMQh8'
    MPESA_LNMO_CONSUMER_SECRET = 'By9NUqT7NGhzy5Pj'
    MPESA_LNMO_ENVIRONMENT = 'sandbox'
    MPESA_LNMO_INITIATOR_PASSWORD = 'HaVh3tgp'
    MPESA_LNMO_INITIATOR_USERNAME = 'testapi779'
    MPESA_LNMO_PASS_KEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    MPESA_LNMO_SHORT_CODE = '174379'

    def transact(self, data):
        # Implement the transaction logic here
        endpoint = f'https://{self.MPESA_LNMO_ENVIRONMENT}.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {
            'Authorization': 'Bearer ' + self.generate_access_token(),
            'Content-Type': 'application/json'
        }
        payload = {
            "BusinessShortCode": self.MPESA_LNMO_SHORT_CODE,
            "Password": self.generate_password(),
            "Timestamp": datetime.now().strftime('%Y%m%d%H%M%S'),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": data['Amount'],
            "PartyA": data['PhoneNumber'],
            "PartyB": self.MPESA_LNMO_SHORT_CODE,
            "PhoneNumber": data['PhoneNumber'],
            "CallBackURL": "https://example.com/callback",  # Replace with your callback URL
            "AccountReference": data['AccountReference'],
            "TransactionDesc": "Payment for order " + data['AccountReference']
        }

        response = requests.post(endpoint, json=payload, headers=headers)
        response_data = response.json()

        # Save transaction to the database
        transaction = Transaction(
            _pid=data['AccountReference'],
            party_a=data['PhoneNumber'],
            party_b=self.MPESA_LNMO_SHORT_CODE,
            account_reference=data['AccountReference'],
            transaction_category=0,  # Assuming 0 for purchase order
            transaction_type=1,  # Assuming 1 for credit
            transaction_channel=1,  # Assuming 1 for LNMO
            transaction_aggregator=0,  # Assuming 0 for MPESA
            transaction_id=response_data.get('CheckoutRequestID'),
            transaction_amount=data['Amount'],
            transaction_code=None,
            transaction_timestamp=datetime.now(),
            transaction_details="Payment for order " + data['AccountReference'],
            _feedback=response_data,
            _status=1  # Assuming 1 for processing
        )
        db.session.add(transaction)
        db.session.commit()

        return response_data

    def query(self, transaction_id):
        # Implement the query logic here
        endpoint = f'https://{self.MPESA_LNMO_ENVIRONMENT}.safaricom.co.ke/mpesa/stkpushquery/v1/query'
        headers = {
            'Authorization': 'Bearer ' + self.generate_access_token(),
            'Content-Type': 'application/json'
        }
        payload = {
            "BusinessShortCode": self.MPESA_LNMO_SHORT_CODE,
            "Password": self.generate_password(),
            "Timestamp": datetime.now().strftime('%Y%m%d%H%M%S'),
            "CheckoutRequestID": transaction_id
        }

        response = requests.post(endpoint, json=payload, headers=headers)
        return response.json()

    def callback(self, data):
        # Implement the callback logic here
        # Process the callback data and update the transaction status
        checkout_request_id = data['Body']['stkCallback']['CheckoutRequestID']
        transaction = Transaction.query.filter_by(transaction_id=checkout_request_id).first()

        if transaction:
            transaction._feedback = data
            result_code = data['Body']['stkCallback']['ResultCode']
            if result_code == 0:
                transaction._status = 4  # Assuming 4 for accepted
            else:
                transaction._status = 3  # Assuming 3 for rejected
            db.session.commit()

        return data

    def generate_access_token(self):
        # Implement access token generation logic here
        return "your_access_token"  # Replace with actual token generation logic

    def generate_password(self):
        # Implement password generation logic here
        return "your_password"  # Replace with actual password generation logic
