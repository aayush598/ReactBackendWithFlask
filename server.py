from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/send-data', methods=['POST'])
def receive_data():
    data = request.json  # Get JSON data from request
    print("Received data:", data)

    # Process the received data
    response_data = {"message": "Data received successfully", "received": data}

    return jsonify(response_data)  # Send JSON response

if __name__ == '__main__':
    app.run(debug=True)
