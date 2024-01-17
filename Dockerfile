# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /recetteCuisine

# Copy the current directory contents into the container at /app
COPY . /recetteCuisine

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django application
EXPOSE 8080

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
