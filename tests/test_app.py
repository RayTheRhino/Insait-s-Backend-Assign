import pytest
from flask import json
from app import create_app
from unittest.mock import patch
import os

@pytest.fixture
def client():
    with patch.dict(os.environ, {'DATABASE_URL': 'sqlite:///:memory:'}):

        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        with app.test_client() as client:
            with app.app_context():
                from app.models import db
                db.create_all()  
            yield client  

def test_ask_success(client):
    with patch('app.routes.ask_open_ai') as mock_ask_open_ai, \
         patch('app.routes.save_record') as mock_save_record:

        mock_ask_open_ai.return_value = {
            'status_code': 200,
            'content': 'This is a test response'
        }

        response = client.post('/ask', json={'question': 'What is AI?'})

        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'output_string' in data
        assert data['output_string'] == 'This is a test response'

        mock_save_record.assert_called_once_with(
            question='What is AI?',
            response='This is a test response',
            status_code=200
        )

def test_ask_invalid_input(client):
    response = client.post('/ask', json={'question': 123})

    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == 'Invalid input: input_string is required and must be a non-empty string.'

def test_ask_error_response(client):
    with patch('app.routes.ask_open_ai') as mock_ask_open_ai, \
         patch('app.routes.save_record') as mock_save_record:

        mock_ask_open_ai.return_value = {
            'status_code': 500,
            'error': 'API error'
        }

        response = client.post('/ask', json={'question': 'What is AI?'})

        assert response.status_code == 500
        data = json.loads(response.data)
        assert 'error' in data
        assert data['error'] == 'API error'

        mock_save_record.assert_called_once_with(
            question='What is AI?',
            error='API error',
            status_code=500
        )
