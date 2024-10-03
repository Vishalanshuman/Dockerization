FROM python:3.12.4

WORKDIR  /app
COPY  requirements.txt .
COPY main.py .
RUN pip install -r requirements.txt 


CMD [ "uvicorn","python",'main:app',"--host","127.0.0.1","--port","8000" ]