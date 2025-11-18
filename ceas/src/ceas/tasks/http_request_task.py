from ceas.core import task
from ceas.integrations.http import http
import json
import logging

logger = logging.getLogger(__name__)

@task(schedule="interval", seconds=300)  # Runs every 5 minutes by default
def send_http_request_task(endpoint="https://httpbin.org/post", method="POST", data=None, headers=None):
    """
    Task that sends an HTTP request to a specified endpoint at regular intervals.
    
    Args:
        endpoint (str): The URL endpoint to send the request to
        method (str): HTTP method to use (GET, POST, PUT, DELETE)
        data (dict): Data to send in the request body (for POST/PUT)
        headers (dict): Custom headers to include in the request
    """
    logger.info(f"Sending {method} request to {endpoint}")
    
    try:
        # Prepare request arguments
        kwargs = {}
        if headers:
            kwargs['headers'] = headers
        if data and method.upper() in ['POST', 'PUT']:
            kwargs['json'] = data
        
        # Send the request using the appropriate method
        if method.upper() == 'GET':
            response = http.get(endpoint, **kwargs)
        elif method.upper() == 'POST':
            response = http.post(endpoint, **kwargs)
        elif method.upper() == 'PUT':
            response = http.put(endpoint, **kwargs)
        elif method.upper() == 'DELETE':
            response = http.delete(endpoint, **kwargs)
        else:
            logger.error(f"Unsupported HTTP method: {method}")
            return
        
        logger.info(f"Request successful. Response: {json.dumps(response, indent=2)}")
        return response
    
    except Exception as e:
        logger.error(f"Error sending HTTP request: {str(e)}")
        raise
