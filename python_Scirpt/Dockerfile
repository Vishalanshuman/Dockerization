FROM python:3.12.4

ADD main.py .

RUN pip install pandas

CMD [ "paython",'./main.py' ]

#1.docker build -t python-roll . create image - [docker build -t image-name-as-you-want file_location]
# 2. run---docker run python-roll(image_name) 
#3. if we taking user input then we use command docker run -t -i image-name