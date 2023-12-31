# Use an official Python runtime as a base image
FROM python:3.8.10

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
