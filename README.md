<!-- README.md -->

Here is the complete content for the `README.md` file that you can save at the specified path `/home/wagura-maurice/Documents/Projects/mpesa_payments/README.md`.

### **/home/wagura-maurice/Documents/Projects/mpesa_payments/README.md**

````markdown
# MPESA Payments API

This project is a Flask application that integrates with the MPESA LNMO (Lipa na MPESA Online) API to handle payment transactions. It provides endpoints for processing transactions, querying transaction status, and handling callbacks from the MPESA API.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python 3.6 or higher
- pip (Python package installer)
- A database (SQLite is used in this project for simplicity)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd mpesa_payments
   ```
````

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Database Configuration**:

   - The application is configured to use SQLite by default. You can change the database URI in `app.py` if you want to use a different database (e.g., PostgreSQL, MySQL).

2. **MPESA API Credentials**:
   - Update the MPESA API credentials in `models/transaction.py` or `traits/lnmo_trait.py` as needed. Ensure you have valid credentials for the MPESA API.

## Running the Application

1. **Run the migration to create the database tables**:

   ```bash
   python migrations/create_transactions_table.py
   ```

2. **Start the Flask application**:

   ```bash
   python app.py
   ```

3. **Access the application**:
   - Open your web browser and navigate to `http://127.0.0.1:5000/` to see the welcome message.
   - The API endpoints for MPESA LNMO transactions can be accessed at:
     - `POST /ipn/daraja/lnmo/transact` - To initiate a transaction.
     - `POST /ipn/daraja/lnmo/query` - To query the status of a transaction.
     - `POST /ipn/daraja/lnmo/callback` - To handle callbacks from MPESA.

## API Endpoints

### 1. Transaction

- **Endpoint**: `/ipn/daraja/lnmo/transact`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "Amount": 100,
    "PhoneNumber": "2547XXXXXXXX",
    "AccountReference": "123456"
  }
  ```

### 2. Query Transaction

- **Endpoint**: `/ipn/daraja/lnmo/query`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "transaction_id": "unique_transaction_id"
  }
  ```

### 3. Callback

- **Endpoint**: `/ipn/daraja/lnmo/callback`
- **Method**: `POST`
- **Request Body**: (This will be sent by MPESA, structure will depend on the callback data)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### **Instructions to Save the File**
1. Open a text editor of your choice (e.g., VSCode, Nano, Vim).
2. Copy the above content.
3. Paste it into the editor.
4. Save the file as `README.md` in the directory `/home/wagura-maurice/Documents/Projects/mpesa_payments/`.

This `README.md` file will provide clear instructions for anyone looking to set up and run the MPESA payments project locally.
```
