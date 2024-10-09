import requests
from flask import Blueprint, request, jsonify
import os
from .dal import save_record
from .open_ai import ask_open_ai


main = Blueprint('main', __name__)

@main.route("/ask",methods=['POST'])
def ask():
    question = request.json.get('question')
    

    if not question or not isinstance(question, str):
        return jsonify({'error': 'Invalid input: input_string is required and must be a non-empty string.'}), 400

    try:
        response = ask_open_ai(question)
        
        if response['status_code'] == 200:
            output_data = response['content'].strip()
            save_record(question=question, response=output_data, status_code=200)
            return jsonify({'output_string': output_data})
        else:
            error_message = response.get('error', 'Unknown error')
            save_record(question=question, error=error_message, status_code=response['status_code'])
            return jsonify({'error': error_message}), response['status_code']
    
    except Exception as ex:
        save_record(question=question, error=str(ex), status_code=500)
        return jsonify({'error': 'An unexpected error occurred.'}), 500

   

