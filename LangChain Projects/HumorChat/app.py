from fastapi import FastAPI
from pydantic import BaseModel
from humorchatbot import generate_humorous_response
import uvicorn

class Question(BaseModel):
    question: str

app = FastAPI()

@app.get('/')
def home():
    return {"greetings":"Welcome to HumorChat. add '/docs' at the end of the URL to get to the API Swagger"}

@app.post('/generate_humor_response')
def response_from_llm(query: Question):
    response = generate_humorous_response(query.question)
    return {
        "your_question": f"{query.question}",
        "answered_by_llm": f"{response.strip()}"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="debug")
