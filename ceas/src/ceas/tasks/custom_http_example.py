from ceas.core import task
from ceas.tasks.http_request_task import send_http_request_task

# Example 1: Send a GET request to a weather API every hour
@task(schedule="interval", hours=1)
def hourly_weather_check():
    """
    Task that fetches weather data every hour.
    This is an example of how to create a task that runs at a specific interval
    and calls our generic HTTP request task with specific parameters.
    """
    endpoint = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": "YOUR_API_KEY",  # Replace with actual API key in production
        "q": "Sao Paulo",
        "aqi": "no"
    }
    
    # Call our generic HTTP request task with specific parameters
    return send_http_request_task(
        endpoint=endpoint,
        method="GET",
        data=params,
        headers={"Content-Type": "application/json"}
    )

# Example 2: Send a POST request with JSON data every 30 minutes
@task(schedule="interval", minutes=30)
def send_status_update():
    """
    Task that sends a status update every 30 minutes.
    """
    endpoint = "https://httpbin.org/post"
    data = {
        "status": "operational",
        "timestamp": "{{current_time}}",  # This would be replaced with actual timestamp in production
        "metrics": {
            "cpu": "45%",
            "memory": "60%",
            "disk": "30%"
        }
    }
    
    # Call our generic HTTP request task with specific parameters
    return send_http_request_task(
        endpoint=endpoint,
        method="POST",
        data=data,
        headers={"Content-Type": "application/json"}
    )

# Example 3: Using a cron schedule to send a daily report at 8 AM
@task(schedule="cron", hour=8, minute=0)
def send_daily_report():
    """
    Task that sends a daily report at 8 AM.
    This demonstrates using a cron schedule instead of an interval.
    """
    endpoint = "https://httpbin.org/post"
    data = {
        "report_type": "daily",
        "date": "{{current_date}}",  # This would be replaced with actual date in production
        "summary": "Daily operations report"
    }
    
    # Call our generic HTTP request task with specific parameters
    return send_http_request_task(
        endpoint=endpoint,
        method="POST",
        data=data,
        headers={"Content-Type": "application/json"}
    )
