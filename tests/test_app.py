import requests

# Define your endpoint here
ENDPOINT = "http://localhost:5000/ask"  # Ensure this matches your Flask app's URL

def test_can_call_endpoint():
    # Test to see if the main endpoint is reachable
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_ask_record():
    # Prepare the payload for creating a new ask record
    payload = {
        "question": "What is the capital of France?",  # Required field based on your model
        # "response": "",  # Optional field, can be added if needed
        # "error": "",     # Optional field, can be added if needed
        # "status_code": 200  # Optional field, can be added if needed
    }

    # Send a POST request to create a new ask record
    create_ask_response = requests.post(ENDPOINT + "/ask", json=payload)
    assert create_ask_response.status_code == 201  # Assuming 201 Created is the expected response

    # Retrieve the response data
    data = create_ask_response.json()

    # Get the ask record ID from the response
    ask_id = data["ask"]["id"]  # Adjust based on your response structure

    # Now, check if we can retrieve the created ask record
    get_ask_response = requests.get(ENDPOINT + f"/ask/{ask_id}")
    assert get_ask_response.status_code == 200

    # Validate the retrieved ask record data
    get_ask_data = get_ask_response.json()
    assert get_ask_data["question"] == payload["question"]
    assert get_ask_data.get("response") is None  # Check if response is None since it's not provided
    assert get_ask_data.get("error") is None  # Check if error is None since it's not provided
    assert get_ask_data.get("status_code") is None  # Check if status_code is None since it's not provided

# To run the tests, use pytest in your terminal:
# pytest test_todo_api.py
