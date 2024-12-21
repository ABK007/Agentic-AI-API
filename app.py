from fastapi import FastAPI
import uvicorn as uv
from router.nutritionist_router import router as nutrition_router
from router.review_summariser import router as review_router
from router.emotion_art_router import router as emotion_router
from router.python_code_guru import router as code_guru_router

app = FastAPI()


# Include routers
app.include_router(nutrition_router, tags=["Nutritionist"])
app.include_router(review_router, tags=["Review Summariser"])
app.include_router(emotion_router, tags=["Emotion Art"])
app.include_router(code_guru_router, tags=["Python Code Guru"])

@app.get("/")
def home():
    return {"message": "Welcome to the Nutritionist API"}

def start():
    uv.run("todos.main:app", host="127.0.0.1", port=8000, reload=True)
