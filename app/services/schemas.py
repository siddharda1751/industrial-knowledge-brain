DOCUMENTS_TABLE = """
CREATE TABLE IF NOT EXISTS documents(

    document_id TEXT PRIMARY KEY,

    filename TEXT NOT NULL,

    resource_uri TEXT UNIQUE NOT NULL,

    checksum TEXT,

    status TEXT,

    parser_version INTEGER,

    chunk_count INTEGER,

    created_at TEXT,

    updated_at TEXT

)
"""

TABLES_SCHEMA = [
    DOCUMENTS_TABLE
]