import requests
import logging
import json
from jsonpath_ng import jsonpath, parse
from flask import Flask, request

app = Flask(__name__)

@app.route('/fetch_url', methods=['POST', 'GET', 'OPTIONS'])
def fetch_url(*args):

    try:
        """Setup Header CORS response"""
        if request.method == "OPTIONS":
            # Allows GET requests from any origin with the Content-Type
            # header and caches preflight response for an 1000s
            headers = {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Max-Age": "1000",
            }
            return ("ready to continue", 200, headers)
        else:
            # Set CORS headers for the main request
            headers = {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Content-Type": "application/json; charset=utf-8",
                }

        logging.info(f"Headers Dump: { headers }")

        """ Fetches a URL and returns the data in an HTML card format.
            Returns:
            A Flask response object containing the HTML card or an error message
        """
        # Extract URL and card_type from request body
        url, card_type, path = None, None, None
        try:
            url = request.json.get('url')
            card_type = request.json.get('card_type')
            path = request.json.get('path')
        except Exception as e:
            logging.error(f"Error parsing request body: {e}")
            return (f'<p>400 ERROR: Error parsing request body: {e}</p>', 400, headers)


        # Validate arguments
        if not url or not card_type or not path:
            logging.error("Missing required parameters: url, card_type, or path")
            return ('<p>400 ERROR: Please provide both url, card_type, and path in the request body.</p>', 400, headers)

        content = "EMPTY"
        try:
            # Fetch data and handle errors
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for non-200 status codes
            content = response.content.decode()

        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching URL: {e}")
            # return (f'<p>500 ERROR: Error fetching URL: {e}</p>', 500, headers)
            content = "Error fetching URL"
            return (f'<p>500 ERROR: {content} </p>', 500, headers)

        if path and content != "Error fetching URL":
            content = json.loads(content)
            jsonpath_expression = parse(path)
            matches = jsonpath_expression.find(content)
            content = matches[0].value

        # Generate HTML card based on card_type
        if card_type == 'basic':
            card_html = f"""
            <div class="card">
              <div class="card-body">
                <p class="card-text">{content}</p>
              </div>
            </div>
            """
        elif card_type == 'pre':
            card_html = f"""
            <div class="card">
                <pre>{content}</pre>
            </div>
            """
        elif card_type == 'image':
            # Assuming response content is a valid image URL
            card_html = f"""
            <div class="card">
                <img src="{content}" class="card-img-top">
            </div>
            """
        elif card_type == "none":
            card_html = f"""{ content }"""
        else:
            logging.warning(f"Invalid card_type: {card_type}")
            return ('<p>400 ERROR: Invalid card_type. Please use "basic", "pre", none" or "image".</p>', 400, headers)

        return (card_html, 200, headers)

    except Exception as e:
        logging.error(f"Error creating content: {e}")
        return (f'<p>500 ERROR: Error creating content: {e}</p>', 500, headers)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)  # Configure basic logging
    app.run(debug=True)