from flask import render_template, request, jsonify
from app import app
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the quantized model and tokenizer from Hugging Face
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)

@app.route('/')
def index():
    return render_template('index.html')  # Render the main HTML template

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')  # Get the user's message from the request
    inputs = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors='pt')
    outputs = model.generate(inputs, max_length=50, pad_token_id=tokenizer.eos_token_id)
    bot_response = tokenizer.decode(outputs[0], skip_special_tokens=True)  # Generate a response using the model
    return jsonify({'response': bot_response})  # Return the response as JSON