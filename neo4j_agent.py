from neo4j import GraphDatabase

# Neo4j Connection Setup
class Neo4jAgent:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def save_preference(self, user_id, key, value):
        with self.driver.session() as session:
            session.run(
                """
                MERGE (u:User {id: $user_id})
                MERGE (p:Preference {key: $key, value: $value})
                MERGE (u)-[:HAS_PREFERENCE]->(p)
                """,
                user_id=user_id, key=key, value=value
            )

    def get_preferences(self, user_id):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (u:User {id: $user_id})-[:HAS_PREFERENCE]->(p)
                RETURN p.key AS key, p.value AS value
                """,
                user_id=user_id
            )
            return {record["key"]: record["value"] for record in result}

neo4j_agent = Neo4jAgent("bolt://localhost:7687", "neo4j", "password")
