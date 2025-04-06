from pydantic import BaseModel

class ReviewSentenceRequest(BaseModel):
    text: str