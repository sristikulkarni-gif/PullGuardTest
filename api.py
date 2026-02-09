"""
API module with security vulnerabilities
"""
import os
import subprocess
import random
import pickle

# CRITICAL: Hardcoded API credentials (intentional for testing)
AWS_ACCESS_KEY_ID = "my_aws_access_key_id_12345"
AWS_SECRET_ACCESS = "my_aws_secret_key_abcdefghijklmnop"
PAYMENT_API_KEY = "payment_secret_key_production_xyz123"

def execute_command(user_input):
    """
    CRITICAL VULNERABILITY: Command Injection
    """
    # Directly using user input in shell command
    os.system(f"ls -la {user_input}")

    # Another command injection vulnerability
    subprocess.call(f"grep {user_input} /var/log/app.log", shell=True)

def run_script(script_name):
    """
    HIGH VULNERABILITY: Command Injection via subprocess
    """
    result = subprocess.run(["python3", script_name], capture_output=True)
    return result.stdout

def generate_session_token():
    """
    MEDIUM VULNERABILITY: Insecure random number generation
    """
    # Using predictable random for security-sensitive operation
    token = random.randint(100000, 999999)
    return str(token)

def deserialize_data(data):
    """
    CRITICAL VULNERABILITY: Insecure deserialization
    """
    # pickle.loads is unsafe with untrusted data
    return pickle.loads(data)

def eval_expression(expression):
    """
    CRITICAL VULNERABILITY: Use of eval() with user input
    """
    result = eval(expression)
    return result
# Trigger analysis - 1770623972
