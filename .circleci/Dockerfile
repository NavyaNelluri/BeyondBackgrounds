#python image
FROM python:3.10.2

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

EXPOSE 80

# Install dependencies
RUN pip install pytest
RUN pip install snowflake-connector-python
RUN pip install flask

# Run pytest when the container launches
CMD ["python", "app.py"]
