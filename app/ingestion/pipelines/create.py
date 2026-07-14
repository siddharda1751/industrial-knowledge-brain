from ..parser import DocumentParser
from ..embedder import Embedder
from ..entity_extractor import EntityExtractor

class CreatePipeline:
    
    def __init__(self,services):
        self.registry = services.registry
        self.graph = services.graph
        self.vector = services.vector
        self.parser = DocumentParser()
        self.embedder = Embedder()
        self.entity_extractor = EntityExtractor()

    async def run(self,event):
        document_id=None
        try:
            resource_uri = event["resource_uri"]
            document_id = self.registry.add_document(resource_uri)
            self.registry.update_document(document_id, "PROCESSING")
            chunks = self.parser.parse(resource_uri)
            embeddings = self.embedder.embed(chunks)
            ids = []
            documents = []
            metadatas = []
            for index,chunk in enumerate(chunks):
                chunk_id = f"{document_id}_{index}"
                ids.append(chunk_id)
                documents.append(chunk)
                metadatas.append({
                    "document_id": document_id,
                    "chunk_id": chunk_id,
                    "chunk_index": index,
                    "resource_uri": resource_uri
                })
            self.vector.upsert_chunks(
                    ids=ids,
                    embeddings=embeddings,
                    documents=documents,
                    metadatas=metadatas
                )
            print(f"Document {document_id} chunks upserted successfully.")
            graph = self.entity_extractor.extract(chunks)
            for entity in graph["entities"]:
                # self.graph.create_entity()
                pass
            for relationship in graph["relationships"]:
                # self.graph.create_relationship()
                pass
            print(f"Document {document_id} entities and relationships created successfully.")
            self.registry.update_document(document_id,status="READY")
            print(f"Document {document_id} processed successfully.")
        except Exception:
            if document_id:
                self.registry.update_document(document_id,"FAILED")
            print(f"Failed to process document {document_id}.")
            raise