from neo4j import GraphDatabase

class Neo4JClient:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query(self, query):
        with self.driver.session() as session:
            ret = session.run(query)
            return ret.data()

if __name__ == "__main__":
    client = Neo4JClient("bolt://localhost:7687", "neo4j", "admin")
    ret = client.query('MATCH (M:Measure {topic:"sensors/edge1/cpu/0"})-[BELONGING_OF]->(A) RETURN M.name, M.analytic, A.name')
    print(ret)
    ret = client.query('MATCH (M:Measure) RETURN M.name, M.topic')
    print(ret)

    client.close()