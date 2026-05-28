from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
import wikipedia

app = FastAPI()

class Title(BaseModel):
    title: str = Field(min_length=2)


@app.get("/")
def welcome():
    return "Welcome Page"

# Пункт 1.
@app.get("/wiki/path/{title}")
def summary(title: Title = Depends()):
    return wikipedia.summary(title.title)

# Пункт 2.
@app.get("/wiki/query")
def summary(title: Title = Depends()):
    return wikipedia.summary(title.title)

# Пункт 3.

@app.post("/wiki/body")
def body(title: Title):
    return wikipedia.summary(title.title)