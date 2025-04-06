import logging

import statsd
from fastapi import FastAPI, HTTPException

from src.classifiers.naive_bayes import NaiveBayes
from src.model.api.review_sentence_request import ReviewSentenceRequest
from src.store.review_sentences_store import ReviewSentencesStore

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger()

# In a cloud environment, these values will be loaded from environment variables (os.getenv(...))
TRAINING_BATCH_SIZE = 1000
TRAINING_SET_LIMIT = 2000
METRICS_HOST = "0.0.0.0"
METRICS_PORT = 8125

review_sentences_store = ReviewSentencesStore()
review_sentences = review_sentences_store.read_review_sentences()

naive_bayes = NaiveBayes(
    logger,
    review_sentences[0: TRAINING_SET_LIMIT],
    batch_size=TRAINING_BATCH_SIZE
)

app = FastAPI()
metrics_client = statsd.StatsClient(host=METRICS_HOST, port=METRICS_PORT)

@metrics_client.timer('post_analyse')
@app.post("/analyse/")
async def post_analyse(request: ReviewSentenceRequest):
    results = []

    try:
        results = naive_bayes.classify(request.text)
    except Exception as e:
        logger.error(f"Exception occurred while classifying: {e}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while the text was analysed"
        )

    return {
        "results": results
    }
