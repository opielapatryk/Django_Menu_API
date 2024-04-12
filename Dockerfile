FROM python:3

ENV PYTHONUNBUFFERED 1

# RUN apt-get update && apt-get install -y mongodb-clients && rm -rf /var/lib/apt/lists/*

# Set working directory
RUN mkdir /opt/code
WORKDIR /opt/code

# Copy requirements and install
COPY requirements /opt/requirements
RUN pip install -r /opt/requirements/prod.txt

# Copy the rest of the application code
COPY . /opt/code

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]