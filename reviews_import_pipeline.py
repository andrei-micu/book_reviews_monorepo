import json
import logging

from textblob import TextBlob

from src.constants.constants import polarity
from src.model.reviewed_sentence import ReviewedSentence
from src.store.reviewed_sentences_store import ReviewedSentencesStore

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger()

def read_reviews(file_path: str) -> list[dict]:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return [json.loads(line) for line in lines]


def extract_reviewed_sentences(
        reviews: list[dict],
        rating_baseline: float
) -> list[ReviewedSentence]:
    review_sentences = []
    for review in reviews:
        extracted_sentences = (
                extract_sentences(review["title"]) +
                extract_sentences(review["text"])
        )
        review_sentences = review_sentences + list(map(
            lambda extracted_sentence: ReviewedSentence(
                sentence=extracted_sentence,
                polarity=rating_to_polarity(review["rating"], rating_baseline)
            ),
            extracted_sentences
        ))
    return review_sentences

def extract_sentences(text: str) -> list[str]:
    return [sentence.string for sentence in TextBlob(text).sentences]

def rating_to_polarity(rating: str, baseline: float) -> str:
    rating_number = float(rating)
    if rating_number < baseline:
        return polarity.NEGATIVE
    elif rating_number == baseline:
        return  polarity.NEUTRAL
    else:
        return polarity.POSITIVE

def main(
        file_path: str,
        rating_baseline: float
):
    logger.info("Importing reviews...")
    reviews = read_reviews(file_path)
    review_sentences = extract_reviewed_sentences(reviews, rating_baseline)
    ReviewedSentencesStore().write_reviewed_sentences(review_sentences)
    logger.info("Imported reviews successfully!")



# In a cloud environment, these values will be loaded from environment variables (os.getenv(...))
BOOK_REVIEWS_FILE_PATH = "dataset/Books_10k.jsonl"
RATING_BASELINE = 3.0
main(BOOK_REVIEWS_FILE_PATH, RATING_BASELINE)
