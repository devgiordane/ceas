# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy the project files into the container
COPY ./ceas/pyproject.toml /app/
COPY ./ceas/src/ceas /app/src/ceas
COPY ./ceas/tasks /app/tasks
COPY ./ceas/config /app/config
COPY ./ceas/main.py /app/main.py
COPY ./ceas/cli /app/cli

# Install project dependencies
RUN poetry install --no-root

# Command to run the application
CMD ["poetry", "run", "ceas", "run"]
