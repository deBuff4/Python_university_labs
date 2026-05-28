from fastapi import FastAPI
import pyjokes
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/", status_code=200, description="OK")
def joke():
    return pyjokes.get_joke()

class Joke(BaseModel):
    friend: str = Field(min_length = 3, max_length = 100)
    jokes_number: int = Field(gt = 0, le = 10)

@app.post("/multi/{friend}",status_code=201, description="Created")
def create_joke(joke_input: Joke):
    result = ""

    for i in range(joke_input.jokes_number):
        result += f"{joke_input.friend} tells his joke #{i + 1}: " + pyjokes.get_joke() + " "

    return result