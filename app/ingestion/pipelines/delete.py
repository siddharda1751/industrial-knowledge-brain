

class DeletePipeline:
    def __init__(self,services):
        self.registry = services.registry
        self.vector = services.vector

    async def delete_file(self,resource_uri):
        document_id = self.registry.get_document_id(resource_uri)
        
        if not document_id:
            print(f"No document found with URI {resource_uri}. Nothing to delete.")
            return 
        try:
            self.registry.delete_document(document_id)
            self.vector.delete_document(document_id)
            print(f"Document with URI {resource_uri} and ID {document_id} is deleted.")
        except Exception as e:
            print(f"Error occurred while deleting document {document_id}: {e}")
            raise