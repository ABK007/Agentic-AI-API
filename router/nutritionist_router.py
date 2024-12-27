from utils.prompts import nutritionist_prompt
from services.gemini_service import call_llm
from fastapi import APIRouter
from schemas.nutritonist_schema import UserNutritionData
router = APIRouter()


@router.post("/nutritionist")
def diet_plan(user: UserNutritionData):
    """This route generates a diet plan based on the user's input"""
    
    prompt: str = nutritionist_prompt(user_diet=user.userInput, 
                                      user_height=user.height, 
                                      user_weight=user.weight,
                                      user_language=user.language) # Generate the prompt
    
    response: str = call_llm(prompt) # Call the model

    
    return response