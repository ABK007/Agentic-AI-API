from langchain_google_genai import GoogleGenerativeAI




def call_llm(prompt:str) -> str:
    """this function calls the Google Generative AI model to generate a response based on the prompt"""
    from core.config import key_abubakar, key_massab
    from utils.other_functions import select_rand_api_key
    
    key = select_rand_api_key([key_abubakar, key_massab])
    llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key=key)
    result = llm.invoke(prompt)
    return result
