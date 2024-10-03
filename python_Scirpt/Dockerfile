FROM python:3.12.4

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
# COPY requirements.txt /app/
RUN pip install pandas

# Copy the rest of the application code
COPY main.py .

# Command to run the script
CMD ["python", "main.py"]


#1.docker build -t python-roll . create image - [docker build -t image-name-as-you-want file_location]
# 2. run---docker run python-roll(image_name) 
#3. if we taking user input then we use command docker run -t -i image-name