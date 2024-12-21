from pydantic import BaseModel


class CodeGuruSchema(BaseModel):
    user_code: str