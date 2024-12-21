from fastapi import APIRouter
from utils.prompts import review_summarizer_prompt
from schemas.product_review_schema import UserReviewInput
from services.gemini_service import call_llm
from utils.other_functions import cleaning_html_response


router = APIRouter()

@router.post("/product-reviewer")
def get_review_analysis(review: UserReviewInput):
    """This route generates a summary of a product review based on the user's input"""

    prompt: str = review_summarizer_prompt(review.reviewInput, 
                                           review.productTitle) # Generate the prompt
    response: str = call_llm(prompt) # Call the model
    cleaned_response = cleaning_html_response(response) # Clean the response
    

    return cleaned_response