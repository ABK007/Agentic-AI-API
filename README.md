# Agentic AI API

## Description

Agentic AI API is a Python-based api built using fast api and uv package manager. It leverages AI to provide personalized diet plans and calorie calculations, product reviews analysis, generate textual art based on the emotions of the user and python code guru that explains the code snippet or any problem that is given to it.
It integrates with Google LLM Gemini-Flash-1.5 model for generating content.

## Installation

1. **Clone the repository:**

    
    git clone https://github.com/yourusername/agentic-ai-api.git
    

2. **Create and activate a virtual environment:**

    
    uv init

3. **Install the dependencies:**

    RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev



## Running the Project

1. **Run the FastAPI application:**

    
    uvicorn app:app --host 127.0.0.1 --port 8000 --reload


2. **Access the application:**

    Open your browser and navigate to `http://127.0.0.1:8000`.

## Using Docker

1. **Build the Docker image:**

    ```sh
    docker build -t agentic-ai-api .
    ```

2. **Run the Docker container:**

    First create .env file inside the project folder and add api keys for the LLM Model being used.

    ```sh
    docker run -d -p 8000:8000 --env-file .env agentic-ai-api
    ```

3. **Access the api:**

    Open your browser and navigate to `http://localhost:8000`.

. **Access api documentation:**

    Open your browser and navigate to `http://localhost:8000/docs`.

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.

