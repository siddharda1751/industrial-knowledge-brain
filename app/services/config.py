from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

SQLITE_DB = str(DATA_DIR / "industrial_registry.db")

KUZU_DB_PATH = str(DATA_DIR / "kuzu_db")

CHROMA_DB_PATH = str(DATA_DIR / "chroma_db")
COLLECTION_NAME = "industrial_knowledge"
EMBEDDING_DIMENSION = 384      # Change later based on your embedding model