
import functions_framework
from flask import jsonify
import json

@functions_framework.http
def root_agent(request):
    """
    This endpoint receives the webhook request from the conversational agent.
    """
    req_data = request.get_json()

    # Log the request for debugging purposes
    print(f"Received request:\n{json.dumps(req_data, indent=4)}")

    tag = req_data.get('fulfillmentInfo', {}).get('tag')

    response = {}

    if tag == 'greet':
        response = {
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": ["Hello from your friendly neighborhood webhook!"]
                        },
                    }
                ]
            }
        }
    else:
        response = {
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": ["Webhook received a request for tag: " + tag if tag else "None"]
                        },
                    }
                ]
            }
        }

    return jsonify(response)
