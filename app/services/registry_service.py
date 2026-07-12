import sqlite3
from .config import SQLITE_DB
from .schemas import TABLES_SCHEMA

class RegistryService:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def initialize(self):
        print("Initializing Registry Service...")
        self.connection = sqlite3.connect(SQLITE_DB)
        self.cursor = self.connection.cursor()
        self.create_tables()
        print("Registry Ready.\n")
    
    def create_tables(self):
        for schema in TABLES_SCHEMA:
            self.cursor.execute(schema)
        self.connection.commit()
        print("Documents table ready.")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Registry Closed.")

    def add_document(self):
        pass

    def get_document(self):
        pass

    def update_document(self):
        pass

    def delete_document(self):
        pass