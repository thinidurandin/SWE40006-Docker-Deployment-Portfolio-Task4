from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Read environment variable for Task 4.3 requirements
    environment = os.environ.get('ENVIRONMENT', 'Development')
    return f"""
    <h1>Hello from the SWE40006 Docker Container!</h1>
    <p>This is a simple Python Flask web application.</p>
    <p>Current Environment Configuration: <strong>{environment}</strong></p>
    """

if __name__ == '__main__':
    # Listen on all network interfaces on port 5000
    app.run(host='0.0.0.0', port=5000)
