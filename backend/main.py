from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.document_loaders import WebBaseLoader
from chain import Chain
from db_setup import ChromaDB

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root(url: str):
    try:
        loader = WebBaseLoader(url)
        page_data = loader.load().pop().page_content

        chain = Chain()
        extracted_job_posting = chain.extract_job_posting(page_data)
        
        chroma_db = ChromaDB()
        chroma_db.create_collection()
        res = []
        for job_posting in extracted_job_posting:
            skills = job_posting.get("skills", [])
            metadata = chroma_db.query_data(skills)
            print(len(metadata.items()))
            if len(metadata) > 0:
                email = chain.wrtie_a_cold_email(job_posting.get("description"), metadata)
                res.append(email)
            else:
                    res.append("No metadata found")
            return {"message": res}
    except Exception as e:
        return {"message": [str(e)]}
