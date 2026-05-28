import wikipedia
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/wiki/path/{title}")
def wiki_path(title: str):
 return wikipedia.summary({title}, sentences = 10)

class wiki(BaseModel):
 title: str = Query()

@app.get("/wiki/quary")
def wiki_query(title: str):
 return wikipedia.summary({title}, sentences = 10)

class wiki_p(BaseModel):
 title: str = Field(title="Wiki")

@app.post("/wiki/body")
def wiki_post(wik_p: wiki_p):
 return wikipedia.summary(wik_p.title, sentences = 10)