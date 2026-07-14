import sqlite3
from .config import SQLITE_DB
from .schemas import TABLES_SCHEMA

import uuid
from pathlib import Path
from datetime import datetime

class RegistryService:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def initialize(self):
        print("Initializing Registry Service...")
        self.connection = sqlite3.connect(SQLITE_DB)
        self.connection.row_factory = sqlite3.Row
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

    def add_document(self,resource_uri,checksum=None,status="QUEUED"):
        document_id = str(uuid.uuid4())
        filename = Path(resource_uri).name
        now = datetime.now().isoformat()
        self.cursor.execute(
            """
            INSERT INTO documents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (document_id,filename,resource_uri,checksum,status,1,0,now,now)
        )
        self.connection.commit()
        return document_id

    def get_document(self,document_id):
        self.cursor.execute(
            """
            SELECT * FROM documents WHERE document_id = ?
            """,
            (document_id,)
        )
        row = self.cursor.fetchone()
        return dict(row) if row else None
    
    def get_document_id(self,resource_uri):
        self.cursor.execute(
            """
            SELECT document_id FROM documents WHERE resource_uri = ?
            """,
            (resource_uri,)
        )
        row = self.cursor.fetchone()
        return row["document_id"] if row else None
    
    def document_exists(self,resource_uri):
        self.cursor.execute(
            """
            SELECT 1 FROM documents WHERE resource_uri = ?
            """,
            (resource_uri,)
        )
        return self.cursor.fetchone() is not None
        
    def update_document(self, document_id, status,**fields):
        now = datetime.now().isoformat()
        self.cursor.execute(
            """
            UPDATE documents SET status = ?, updated_at = ? WHERE document_id = ?
            """,
            (status, now, document_id)
        )
        self.connection.commit()

    def delete_document(self,document_id):
        self.cursor.execute(
            """
            DELETE FROM documents WHERE document_id = ?
            """,
            (document_id,)
        )

        self.connection.commit()