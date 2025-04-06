import logging

from src.classifiers.naive_bayes import NaiveBayes
from src.model.api.review_sentence_request import ReviewSentenceRequest
from src.storage.reviewed_sentences_store import ReviewedSentencesStore

from fastapi import FastAPI, HTTPException

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger()

# In a cloud environment, these values will be loaded from environment variables (os.getenv(...))
TRAINING_BATCH_SIZE = 1000
TRAINING_SET_LIMIT = 2000

reviewed_sentences_store = ReviewedSentencesStore()
reviewed_sentences = reviewed_sentences_store.read_reviewed_sentences()

naive_bayes = NaiveBayes(
    logger,
    reviewed_sentences[0: TRAINING_SET_LIMIT],
    batch_size=TRAINING_BATCH_SIZE
)

app = FastAPI()


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
