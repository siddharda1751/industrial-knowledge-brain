from .registry_service import RegistryService


class ServiceManager:

    def __init__(self):

        self.registry = RegistryService()

    def initialize(self):

        print("Initializing Services...\n")

        self.registry.initialize()

        print("Services Ready.\n")

    def shutdown(self):

        self.registry.close()

        print("Services Closed.")