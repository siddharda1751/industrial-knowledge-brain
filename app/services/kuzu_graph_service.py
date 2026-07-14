import kuzu

from .config import KUZU_DB_PATH


class GraphService:

    def __init__(self):
        self.db = None
        self.connection = None

    def intialize(self):
        print("Initializing Graph Service...")
        self.db = kuzu.Database(KUZU_DB_PATH)
        self.connection = kuzu.Connection(self.db)
        self.create_schema()
        print("Graph Service Ready.\n")

    def create_schema(self):
        self.connection.execute("""
            CREATE NODE TABLE IF NOT EXISTS Entity(
                id STRING,
                name STRING,
                label STRING,
                document_id STRING,
                PRIMARY KEY(id)
            );
        """)
        self.connection.execute("""
            CREATE REL TABLE IF NOT EXISTS RELATED_TO(FROM Entity TO Entity);
        """)
    
    def create_entity(self,entity_id,name,label,document_id):
        self.connection.execute(f"""
            CREATE (:Entity {{
                id:'{entity_id}',
                name:'{name}',
                label:'{label}',
                document_id:'{document_id}'
            }});
        """)

    def create_relationship(self,source_id,target_id):
        self.connection.execute(f"""
            MATCH (a:Entity),(b:Entity)

            WHERE a.id='{source_id}'
            AND b.id='{target_id}'

            CREATE (a)-[:RELATED_TO]->(b);
        """)

    def search(self,entity_name):
        result = self.connection.execute(f"""
            MATCH (n:Entity)
            WHERE n.name='{entity_name}'
            OPTIONAL MATCH (n)-[r]->(m)
            RETURN n,r,m;
        """)
        return result.get_as_df()
    
    def delete_document(self,document_id):
        self.connection.execute(f"""
            MATCH (n:Entity)
            WHERE n.document_id='{document_id}'
            DELETE n;
        """)
    
    def update_entity(self,entity_id,name):
        self.connection.execute(f"""
            MATCH (n:Entity)
            WHERE n.id='{entity_id}'
            SET n.name='{name}';
        """)

    def close(self):
        self.connection = None
        self.db = None
        print("Graph Service Closed.")