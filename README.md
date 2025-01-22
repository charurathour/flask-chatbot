# Flask Chatbot

This project is a simple chatbot interface built using Flask. It allows users to interact with a chatbot through a web interface.

## Project Structure

```
flask-chatbot
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   └── style.css
│   └── templates
│       └── index.html
├── venv
├── requirements.txt
└── README.md
```

## Requirements

To run this project, you need to have Python installed. You can create a virtual environment and install the required packages using the following commands:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

## Running the Application

To start the Flask application, run the following command:

```bash
flask run
```

By default, the application will be accessible at `http://127.0.0.1:5000/`.

## Usage

Once the application is running, open your web browser and navigate to the URL above to interact with the chatbot. You can type messages and receive responses from the chatbot interface.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.