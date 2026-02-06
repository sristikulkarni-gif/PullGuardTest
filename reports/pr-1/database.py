"""
Database module with intentional security vulnerabilities for testing
"""
import sqlite3

# CRITICAL VULNERABILITY: Hardcoded database credentials
DB_HOST = "production-db.company.com"
DB_USER = "admin"
DB_PASSWORD = "SuperSecret123!"
API_KEY = "sk-prod-1234567890abcdef"

class DatabaseManager:
    def __init__(self):
        self.connection = None
        # Hardcoded connection string
        self.conn_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/maindb"

    def get_user(self, user_id):
        """
        HIGH VULNERABILITY: SQL Injection - using string formatting
        """
        query = f"SELECT * FROM users WHERE id = {user_id}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchone()

    def search_users(self, search_term):
        """
        HIGH VULNERABILITY: SQL Injection - using string concatenation
        """
        query = "SELECT * FROM users WHERE name LIKE '%" + search_term + "%'"
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def update_user_email(self, user_id, email):
        """
        CRITICAL VULNERABILITY: SQL Injection in UPDATE statement
        """
        query = f"UPDATE users SET email = '{email}' WHERE id = {user_id}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
