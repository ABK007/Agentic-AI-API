from pydantic import BaseModel

class UserReviewInput(BaseModel):
    reviewInput: str
    productTitle: str


