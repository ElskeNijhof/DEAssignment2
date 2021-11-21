# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory fo /app 
WORKDIR /myapp

# Copy the current directory contents into the container /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install google-cloud-storage
RUN pip install --no-cache-dir -r requirements.txt
# Make port 5000 available to the world outside the container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"] 