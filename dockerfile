FROM python:latest

# Set the working directory
WORKDIR /app

COPY requirements.txt requirements.txt


RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . .

EXPOSE 8501
ENTRYPOINT [ "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0 0.0" ]