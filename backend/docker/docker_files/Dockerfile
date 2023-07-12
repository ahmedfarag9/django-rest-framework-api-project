# Use Python 3.10 as base image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install netcat and gettext
RUN set -e; \
    apt-get update ;\
    apt-get -y install netcat-openbsd ;\
    apt-get -y install gettext ;

# Create a directory for the code and copy the code to the container
RUN mkdir /code
COPY . /code/
WORKDIR /code

# Upgrade pip, install requirements and set execute permission for entrypoint script
RUN set -e; \
    /usr/local/bin/python -m pip install --upgrade pip ;\
    python -m pip install -r /code/requirements.txt ;\
    chmod +x /code/docker/entrypoints/entrypoint.sh ;

# Expose port 8000 and set entrypoint
EXPOSE 8000
ENTRYPOINT []
