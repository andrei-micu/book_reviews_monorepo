FROM python:3.12

COPY . .

RUN pip install -r requirements.txt

RUN python -m textblob.download_corpora

EXPOSE 8080:8080

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]