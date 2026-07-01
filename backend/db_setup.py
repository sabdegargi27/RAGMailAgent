import chromadb
import pandas as pd
import uuid
from collections import defaultdict
class ChromaDB:
    def __init__(self, path="./resources/my_data.csv"):
        self.file_path = path
        self.data = pd.read_csv(self.file_path)
        self.client = chromadb.PersistentClient(path="backend/vector_db")
        self.collection = self.client.get_or_create_collection("portfolio")
    
    def update_collection(self):
        self.delete_collection()
        for index, row in self.data.iterrows():
            self.collection.add(ids=[str(uuid.uuid4())], documents=row["Tech Stack"], metadatas={"project": row["Project"], "description": row["Description"]})
        return self.collection.count()

    def create_collection(self):
        if not self.collection.count():
            for index, row in self.data.iterrows():
                self.collection.add(ids=[str(uuid.uuid4())], documents=row["Tech Stack"], metadatas={"project": row["Project"], "description": row["Description"]})

    def query_data(self, skills):
        res = self.collection.query(query_texts=skills, n_results=2).get("metadatas", [])
        ans = defaultdict(str)
        if len(res) > 0:
            for metadata in res[0]:
                ans[metadata.get("project")] = metadata.get("description")
            return ans
        return []
    
    def get_all_data(self):
        return self.collection.get()
    
    def delete_collection(self):
        ids = self.collection.get()["ids"]
        self.collection.delete(ids=ids)
# obj = ChromaDB()
# obj.create_collection()
# for i in obj.query_data("Payments").get("metadatas")[0]:
#     print(i.get("project"))