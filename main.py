from fastapi import FastAPI, Request
from pydantic import BaseModel


app = FastAPI()


class MessageRequest(BaseModel):
    message: str


class MessageResponse(BaseModel):
    modified_message: str


@app.post("/modify")
async def modify_message(request: MessageRequest) -> MessageResponse:
    print(f"Received request: {request}")
    modified_message = request.message + " FastAPI visited!"
    return MessageResponse(modified_message=modified_message)
