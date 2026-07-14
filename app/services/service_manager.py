from .registry_service import RegistryService
from .kuzu_graph_service import GraphService
from .vector_service import VectorService


class ServiceManager:

    def __init__(self):

        self.registry = RegistryService()
        self.graph = GraphService()
        self.vector = VectorService()

    def initialize(self):

        print("Initializing Services...\n")

        self.registry.initialize()
        self.graph.intialize()
        self.vector.initialize()

        print("Services Ready.\n")

    def shutdown(self):
        print("\nClosing Services\n")
        self.registry.close()
        self.graph.close()
        self.vector.close()
        print("Services Closed.")