FROM python:3.10-slim

RUN useradd --create-home --shell /bin/bash wt_user

WORKDIR /home/wt_user 

COPY ./write_tight ./write_tight

COPY requirements.txt .

COPY setup.py .

RUN pip install --no-cache-dir -r requirements.txt

RUN ["python3", "-c", "import nltk; nltk.download('wordnet', download_dir='/usr/local/nltk_data')"]

RUN ["python3", "-c", "import nltk; nltk.download('omw-1.4', download_dir='/usr/local/nltk_data')"]

USER wt_user