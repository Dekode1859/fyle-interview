# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Delete older .pyc files
RUN find . -type d \( -name env -o -name venv \) -prune -false -o -name "*.pyc" -exec rm -rf {} \;

# Run required migrations
ENV FLASK_APP=core/server.py
# RUN flask db init -d core/migrations/ && \
#     flask db migrate -m "Initial migration." -d core/migrations/ && \
#     flask db upgrade -d core/migrations/

# Expose the port inside the container
EXPOSE 7755

# Run app.py when the container launches with port mapping
CMD ["gunicorn", "-c", "gunicorn_config.py", "core.server:app"]
# CMD ["gunicorn", "-c", "gunicorn_config.py", "--bind", "0.0.0.0:8080", "core.server:app"]