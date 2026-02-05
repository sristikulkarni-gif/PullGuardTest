"""
Cryptography module with weak security
"""
import hashlib
from Crypto.Cipher import DES
import random

# MEDIUM: Hardcoded encryption key
ENCRYPTION_KEY = b"12345678"

def hash_password(password):
    """
    HIGH VULNERABILITY: Using MD5 for password hashing
    """
    return hashlib.md5(password.encode()).hexdigest()

def encrypt_data(data):
    """
    HIGH VULNERABILITY: Using deprecated DES encryption
    """
    cipher = DES.new(ENCRYPTION_KEY, DES.MODE_ECB)
    # ECB mode is insecure
    encrypted = cipher.encrypt(data.encode())
    return encrypted

def generate_random_key():
    """
    MEDIUM VULNERABILITY: Weak random number generation for crypto
    """
    # Using random instead of secrets module
    key = random.randint(1000, 9999)
    return str(key)

def simple_hash(text):
    """
    LOW VULNERABILITY: Using SHA1 (deprecated)
    """
    return hashlib.sha1(text.encode()).hexdigest()
