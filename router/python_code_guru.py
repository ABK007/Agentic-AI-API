from fastapi import APIRouter
from utils.prompts import get_code_guru_prompt
from schemas.code_guru_schema import CodeGuruSchema
from services.gemini_service import call_llm



router = APIRouter()

@router.post("/python-code-guru")
def python_code_analysis(inputCode: CodeGuruSchema):
    """This route gives analysis on code based on the user's input code"""
    prompt: str = get_code_guru_prompt(inputCode.user_code) # Generate the prompt
    response: str = call_llm(prompt) # Call the model
    
    return response