# traits/lnmo_trait.py
import requests
from datetime import datetime
from flask import current_app

class LNMOTrait:
    # Hardcoded configurations
    MPESA_LNMO_CONSUMER_KEY = 'uKxU78Y9q2cFruO2fKRWuofRCObzMQh8'
    MPESA_LNMO_CONSUMER_SECRET = 'By9NUqT7NGhzy5Pj'
    MPESA_LNMO_ENVIRONMENT = 'sandbox'
    MPESA_LNMO_INITIATOR_PASSWORD = 'HaVh3tgp'
    MPESA_LNMO_INITIATOR_USERNAME = 'testapi779'
    MPESA_LNMO_PASS_KEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    MPESA_LNMO_SHORT_CODE = '174379'

    def generate_access_token(self):
        """
        Generate an access token for MPESA API.
        """
        endpoint = f'https://{self.MPESA_LNMO_ENVIRONMENT}.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        headers = {
            'Authorization': 'Basic ' + self._get_basic_auth(),
            'Content-Type': 'application/json'
        }

        response = requests.get(endpoint, headers=headers)
        response_data = response.json()

        if 'access_token' in response_data:
            return response_data['access_token']
        else:
            raise Exception("Failed to generate access token: " + str(response_data))

    def _get_basic_auth(self):
        """
        Generate the Basic Auth string for the MPESA API.
        """
        import base64
        credentials = f"{self.MPESA_LNMO_CONSUMER_KEY}:{self.MPESA_LNMO_CONSUMER_SECRET}"
        return base64.b64encode(credentials.encode()).decode()

    def submit(self, url, data):
        """
        Submit a request to the specified URL with the given data.
        """
        access_token = self.generate_access_token()
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=data, headers=headers)
        return response.json()
