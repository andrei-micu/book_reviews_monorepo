# Book Reviews Sentiment Analysis
A solution for classifying book review sentences by polarity

## Monorepo

This project hold all the code for the solution. The system has two parts:
1. The pipeline that processes the dataset: [reviews_import_pipeline.py](reviews_import_pipeline.py)
2. The API backed by a classifier for new sentences: [main.py](main.py)

## Data pipeline
The data piepline is a simple Python script that:
1. Reads the [dataset](dataset/Books_10k.jsonl)
2. Gathers the sentences from the titles and descriptions
3. Remaps the rating into polarity labels
4. Writes the results into an output file

## API
The API is [built](build.bat) and [deployed](deploy.bat) using Docker.

The Swagger UI can be accessed at http://127.0.0.1:8080/docs#/

There is also a load test in place for the endpoint, [run_load_test.bat](run_load_test.bat), which builds and instantiates everything.
Access the Locust interface from the link outputted in the console, once everything has finished loading.