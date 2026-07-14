class EntityExtractor:

    def __init__(self):
        pass

    def extract(self, chunks):
        """
        Input:
            List[str]

        Output:
            {
                "entities": [...],
                "relationships": [...]
            }
        """
        raise NotImplementedError