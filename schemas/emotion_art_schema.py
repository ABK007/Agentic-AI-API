from pydantic import BaseModel


class EmptionArtData(BaseModel):
    emotion:str
    art_form:str
    style:str
    context:str
    language:str="English"