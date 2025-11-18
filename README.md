# CEAS - Condensed Everyday Automation System

**CEAS** is a Python library designed to simplify the deployment and management of everyday automations.

With a single Docker instance, you can run multiple small automation tasks ("micro-functions") to handle things like:

- Sending periodic reports
- Receiving and processing webhooks
- Integrating with external APIs (e.g., Gmail, Slack, Notion)
- Performing lightweight scraping or ETL
- Scheduling recurring jobs
- Triggering scripts on demand via CLI

---

## Key Features:

- ✅ Queue-based task execution
- ✅ Built-in scheduler for recurring jobs
- ✅ API connectors for popular services
- ✅ Simple web interface for logs and job status
- ✅ Single-instance Docker deployment
- ✅ Easily extendable with your own Python scripts
- ✅ CLI for running, scheduling, and monitoring tasks

---

## Project Philosophy:

CEAS was created to centralize all those small, scattered automations developers often build ad-hoc: forgotten crons, loose scripts, manual jobs...

Now, everything is structured, version-controlled, and running in a unified stack.

---

## Quick Start:

1. Install using Poetry
2. Write your tasks inside the `tasks/` folder
3. Run everything with:
```bash
ceas run
