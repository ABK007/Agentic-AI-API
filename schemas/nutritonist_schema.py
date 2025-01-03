from pydantic import BaseModel


class UserNutritionData(BaseModel):
    userInput: str
    weight: float 
    height: float
    language: str | None = None
    

