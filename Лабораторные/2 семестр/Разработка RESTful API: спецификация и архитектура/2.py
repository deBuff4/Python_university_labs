from fastapi import FastAPI
import pyjokes
from pydantic import BaseModel, Field

app = FastAPI()

class Joke(BaseModel):
    friend: str = Field(min_length = 3, max_length = 100)
    jokes_number: int = Field(gt = 0, le = 10)

@app.post("/multi/{friend}")
def create_joke(joke_input: Joke):
    result = ""

    for i in range(joke_input.jokes_number):
        result += f"{joke_input.friend} tells his joke #{i + 1}: " + pyjokes.get_joke() + " "

    return result