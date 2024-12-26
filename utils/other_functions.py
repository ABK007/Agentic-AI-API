import random

def cleaning_html_response(response: str) -> str:
    """ This function cleans the response from the model by extracting the text between the <div> tags """
    start = response.find("<div>")
    end = response.find("</div>") + len("</div>")

    if start != -1 and end != -1:
        cleaned_response = response[start:end]
    else:
        cleaned_response = {"message":"The response was not formatted in HTML"}  # If no <div> tags are found, return an empty string

    return cleaned_response



def select_rand_api_key(api_keys: list[str]) -> str:
    """ This function selects a random API key from the list of API keys """
    return random.choice(api_keys)