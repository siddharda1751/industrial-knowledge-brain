import chromadb

from .config import (CHROMA_DB_PATH,COLLECTION_NAME)


class VectorService:

    def __init__(self):
        self.client = None
        self.collection = None

    def initialize(self):
        print("Initializing Vector Service...")
        self.client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        self.collection = self.client.get_or_create_collection(name=COLLECTION_NAME)
        print("Vector Service Ready.\n")
    
    def upsert_chunks(self,ids,embeddings,documents,metadatas):
        self.collection.upsert(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )
    
    def search(self,embedding,limit=5):
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=limit
        )

    def delete_document(self,document_id):
        self.collection.delete(
            where={"document_id": document_id}
        )

    def close(self):
        self.client = None
        self.collection = None
        print("Vector Service Closed.")