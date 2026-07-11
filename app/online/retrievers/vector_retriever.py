from app.online.interfaces.base_vector import BaseVectorRetriever
from app.online.models import Query, RetrievedChunk


class VectorRetriever:

    def __init__(
        self,
        vector_store: BaseVectorRetriever
    ):
        self.vector_store = vector_store

    def retrieve(
        self,
        query: Query
    ) -> list[RetrievedChunk]:

        return self.vector_store.search(query)