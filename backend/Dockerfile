#Dockerfile for a Django application.
#This Dockerfile sets up the environment for running a Django application in a Docker container.
#The key steps are:

# 1. Use the official Python 3.11.6 Alpine image as the base image, which provides a lightweight and secure foundation.
# 2. Set the working directory to '/app', which will be the root directory for the Django application.
# 3. Copy the 'requirements.txt' file to the container, which lists the Python dependencies for the application.
# 4. Upgrade the pip package manager to the latest version.
# 5. Install the Python dependencies listed in the 'requirements.txt' file using pip, with the '--no-cache-dir' option to avoid caching the downloaded packages.

#This Dockerfile should be used to build a Docker image that can be used to run the Django application in a containerized environment.

FROM python:3.11.9-alpine


# Create Environment variable for the image
# PYTHONBUFFERED: Will give the output directly to the terminal (use for logging)
# PYTHONDONTWRITEBYTECODE: Prevent python from creating .pyc which we do not use and bring bugs
ENV PYTHONBUFFERD=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container
WORKDIR '/app'

# Copy the requirements file to the working directory
COPY ./requirements.txt .

# Upgrade pip and install dependencies
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# # Copy the current directory contents into the container at the working directory
# COPY ./ .


# Copy entrypoint script into the container
COPY ./entrypoint.sh /app/entrypoint.sh

# Change entrypoint.sh permissions to make it executable
RUN chmod +x /app/entrypoint.sh

# Specify the command to run on container start
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
