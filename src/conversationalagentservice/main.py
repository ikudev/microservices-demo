
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    """
    This endpoint receives the webhook request from the conversational agent.
    """
    req_data = request.get_json()

    # Log the request for debugging purposes
    print(f"Received request: {req_data}")

    # TODO: Add your conversational agent logic here
    # For now, we'll just send a simple response
    response_text = "This is a response from the webhook."

    return jsonify({
        'fulfillmentText': response_text
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
