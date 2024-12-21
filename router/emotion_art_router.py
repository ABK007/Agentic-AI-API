from fastapi import APIRouter
from utils.prompts import get_emotion_prompt
from services.gemini_service import call_llm
from utils.other_functions import cleaning_html_response
from schemas.emotion_art_schema import EmptionArtData

router = APIRouter()

@router.post("/emotion_art")
def generate_emotion_art(userInput: EmptionArtData):
    """This route generates textual art based on the user's input"""
    
    prompt: str = get_emotion_prompt(userInput.emotion,
                                     userInput.art_form,
                                     userInput.style,
                                     userInput.context,
                                     userInput.language)
    response = call_llm(prompt)
    cleaned_response = cleaning_html_response(response)
    return cleaned_response
    
