# HTTP Request Tasks for CEAS

This module provides tasks for sending HTTP requests at specified intervals to any endpoint.

## Available Tasks

### 1. Generic HTTP Request Task

The `send_http_request_task` is a configurable task that can send HTTP requests to any endpoint at specified intervals.

**File:** `http_request_task.py`

**Default Configuration:**
- Runs every 5 minutes (300 seconds)
- Sends a POST request to https://httpbin.org/post by default

**Parameters:**
- `endpoint` (str): The URL endpoint to send the request to
- `method` (str): HTTP method to use (GET, POST, PUT, DELETE)
- `data` (dict): Data to send in the request body (for POST/PUT)
- `headers` (dict): Custom headers to include in the request

### 2. Example Custom HTTP Tasks

The `custom_http_example.py` file contains examples of how to create specialized tasks that use the generic HTTP request task with specific configurations.

**Examples:**
1. `hourly_weather_check`: Sends a GET request to a weather API every hour
2. `send_status_update`: Sends a POST request with system status data every 30 minutes
3. `send_daily_report`: Uses a cron schedule to send a daily report at 8 AM

## How to Use

### Basic Usage

1. Register the task in `config/config.yaml`:
   ```yaml
   tasks:
     - ceas.tasks.http_request_task.send_http_request_task
   ```

2. Configure the task parameters in your environment or configuration file.

### Creating Custom HTTP Tasks

You can create your own custom HTTP tasks by following these patterns:

#### Example 1: Simple Interval-based Task

```python
from ceas.core import task
from ceas.tasks.http_request_task import send_http_request_task

@task(schedule="interval", minutes=15)
def my_custom_api_check():
    """Task that runs every 15 minutes"""
    return send_http_request_task(
        endpoint="https://api.example.com/status",
        method="GET",
        headers={"Authorization": "Bearer YOUR_TOKEN"}
    )
```

#### Example 2: Cron-based Task

```python
from ceas.core import task
from ceas.tasks.http_request_task import send_http_request_task

@task(schedule="cron", day_of_week="mon-fri", hour=9, minute=0)
def weekday_morning_report():
    """Task that runs at 9 AM on weekdays"""
    data = {
        "report_type": "morning_check",
        "source": "automated_task"
    }
    
    return send_http_request_task(
        endpoint="https://api.example.com/reports",
        method="POST",
        data=data,
        headers={"Content-Type": "application/json"}
    )
```

## Testing

You can test the HTTP request tasks using the provided unit tests:

```bash
poetry run pytest ceas/tests/test_http_request_task.py
```

Or run a specific task manually:

```bash
poetry run ceas run ceas.tasks.http_request_task.send_http_request_task
```

## Scheduling Options

The task decorator supports different scheduling options:

### Interval-based Scheduling

```python
@task(schedule="interval", seconds=30)  # Run every 30 seconds
@task(schedule="interval", minutes=5)   # Run every 5 minutes
@task(schedule="interval", hours=1)     # Run every hour
@task(schedule="interval", days=1)      # Run every day
```

### Cron-based Scheduling

```python
@task(schedule="cron", minute="*/15")           # Run every 15 minutes
@task(schedule="cron", hour=9, minute=0)        # Run at 9:00 AM every day
@task(schedule="cron", day_of_week="mon", hour=9, minute=0)  # Run at 9:00 AM every Monday
```

For more scheduling options, refer to the APScheduler documentation.
