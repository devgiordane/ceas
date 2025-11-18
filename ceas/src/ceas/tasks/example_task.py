from ceas.core import task
from ceas.integrations.http import http

@task(schedule="interval", seconds=60)
def fetch_data_task():
    print("Fetching data from an API...")
    try:
        data = http.get("https://api.publicapis.org/random")
        print("Successfully fetched data:")
        print(data)
    except Exception as e:
        print(f"An error occurred: {e}")

@task
def send_data_task(data):
    print("Sending data to another service...")
    try:
        response = http.post("https://httpbin.org/post", json=data)
        print("Successfully sent data:")
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
