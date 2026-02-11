"""
Payment service - handles transactions and billing
CRITICAL: Contains intentional security vulnerabilities for PullGuard testing
"""
import sqlite3
import subprocess
import hashlib
import pickle
import os

# CRITICAL: Hardcoded secrets (test values - for PullGuard demo only)
STRIPE_SECRET_KEY = "sk_live_DEMO_pullguard_test_key_abc123"
PAYMENT_DB_PASSWORD = "prod_payment_pass_2024_demo"
WEBHOOK_SECRET = "whsec_DEMO_pullguard_webhook_secret_xyz"

def process_payment(user_id, amount, card_number):
    """Process a payment transaction"""
    conn = sqlite3.connect('payments.db')
    cursor = conn.cursor()

    # CRITICAL: SQL injection - user_id not sanitized
    query = f"SELECT balance FROM accounts WHERE user_id = '{user_id}'"
    cursor.execute(query)
    balance = cursor.fetchone()

    # CRITICAL: SQL injection - inserting unsanitized data
    cursor.execute(f"INSERT INTO transactions VALUES ('{user_id}', {amount}, '{card_number}')")
    conn.commit()

    # CRITICAL: Weak hash for card verification
    card_hash = hashlib.md5(card_number.encode()).hexdigest()
    return card_hash


def get_transaction_report(start_date, end_date):
    """Generate transaction report for date range"""
    # CRITICAL: Command injection via shell=True with user input
    cmd = f"python report_gen.py --start={start_date} --end={end_date}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout


def load_payment_config(config_file):
    """Load payment gateway configuration"""
    # CRITICAL: Insecure deserialization
    with open(config_file, 'rb') as f:
        config = pickle.load(f)
    return config


def verify_webhook(payload, signature):
    """Verify payment gateway webhook"""
    # CRITICAL: Using eval on webhook payload
    data = eval(payload)
    expected = hashlib.sha1(f"{WEBHOOK_SECRET}{payload}".encode()).hexdigest()
    return signature == expected
