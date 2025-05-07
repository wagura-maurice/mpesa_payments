# controllers/lnmo_controller.py
from flask import Blueprint, request, jsonify
from repositories.lnmo_repository import LNMORepository

lnmo_controller = Blueprint('lnmo_controller', __name__)
lnmo_repository = LNMORepository()

@lnmo_controller.route('/lnmo/transact', methods=['POST'])
def transact():
    """
    Handle the transaction request for MPESA LNMO.
    """
    try:
        data = request.json
        # Validate input data
        if not data or 'Amount' not in data or 'PhoneNumber' not in data or 'AccountReference' not in data:
            return jsonify({'status': 'danger', 'message': 'Invalid input data', 'data': {}}), 400
        
        response = lnmo_repository.transact(data)
        return jsonify({'status': 'info', 'message': 'Transaction processing', 'data': response}), 200
    except Exception as e:
        return jsonify({'status': 'danger', 'message': str(e), 'data': {}}), 400

@lnmo_controller.route('/lnmo/query', methods=['POST'])
def query():
    """
    Handle the query request for MPESA LNMO transactions.
    """
    try:
        transaction_id = request.json.get('transaction_id')
        if not transaction_id:
            return jsonify({'status': 'danger', 'message': 'Transaction ID is required', 'data': {}}), 400
        
        response = lnmo_repository.query(transaction_id)
        return jsonify({'status': 'info', 'message': 'Query processing', 'data': response}), 200
    except Exception as e:
        return jsonify({'status': 'danger', 'message': str(e), 'data': {}}), 400

@lnmo_controller.route('/lnmo/callback', methods=['POST'])
def callback():
    """
    Handle the callback request from MPESA LNMO.
    """
    try:
        data = request.json
        if not data:
            return jsonify({'status': 'danger', 'message': 'Invalid callback data', 'data': {}}), 400
        
        response = lnmo_repository.callback(data)
        return jsonify({'status': 'info', 'message': 'Callback processing', 'data': response}), 200
    except Exception as e:
        return jsonify({'status': 'danger', 'message': str(e), 'data': {}}), 400
