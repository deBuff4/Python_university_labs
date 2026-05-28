from fastapi import FastAPI, HTTPException
import pyjokes
from pydantic import BaseModel, Field

app = FastAPI()

class JokeInput(BaseModel):
    friend: str = Field(min_length = 3, max_length = 100)
    jokes_number: int = Field(gt = 0)

@app.post("/multi/{friend}")
def create_joke(joke_input: JokeInput):
    result = ""
    if joke_input.jokes_number > 10:
        raise HTTPException(status_code = 400, detail = "Максимум 10 шуток")

    for i in range(joke_input.jokes_number):
        result += f"{joke_input.friend} tells his joke #{i + 1}: " + pyjokes.get_joke() + " "

    return result