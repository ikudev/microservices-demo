from fastapi import FastAPI, Request
import uvicorn
import json

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get('/agent')
def show_agent():
    return {"agent": "running"}


@app.post("/agent")
async def root_agent(request: Request):
    """
    This endpoint receives the webhook request from the conversational agent.
    """
    req_data = await request.json()

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

    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
