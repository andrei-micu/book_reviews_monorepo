import logging

from src.classifiers.naive_bayes import NaiveBayes
from src.model.api.review_sentence_request import ReviewSentenceRequest
from src.storage.reviewed_sentences_store import ReviewedSentencesStore

from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger()

reviewed_sentences_store = ReviewedSentencesStore()
reviewed_sentences = reviewed_sentences_store.read_reviewed_sentences()

naive_bayes = NaiveBayes(logger, reviewed_sentences[0: 2000], batch_size=1000)

app = FastAPI()

@app.post("/analyse/")
async def post_analyse(request: ReviewSentenceRequest):
    results = {}
    try:
        results = naive_bayes.classify(request.text)
    except Exception:
        logger.error(f"Exception occurred while classifying text: {request.text}")

    return {
        "results": results
    }