# Insait-s-Backend-Assign
This project is a Flask-based server that accepts questions, sends them to the OpenAI API for answers, and stores both in a PostgreSQL database. The setup includes Docker and Docker Compose for containerization, Alembic for database migrations, and pytest for testing.

Setup Instructions:
1. Clone the repo and create an .env file with:
please add your own 
OPEN_AI_KEY=<your_openai_key>
Run the application:

docker-compose up --build
The /ask endpoint accepts POST requests with a question in JSON and returns the API's response.
For example:
{
    "question": "What is the capital of France?"
}

Run the tests:

pytest tests/

Thanks,
Chen Maimon