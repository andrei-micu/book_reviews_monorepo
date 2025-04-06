import logging
import unittest
import os

from src.store.review_sentences_store import ReviewSentencesStore
from src.model.review_sentence import ReviewSentence

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger()


class TestReviewSentencesStore(unittest.TestCase):
    file_path = "./test_review_sentences.json"

    def setUp(self):
        self.unit = ReviewSentencesStore(TestReviewSentencesStore.file_path)

    def tearDown(self):
        os.remove(TestReviewSentencesStore.file_path)

    def test_write_and_read(self):
        sentences = [
            ReviewSentence("This is a review sentence.", "NEUTRAL"),
            ReviewSentence("This is a good review sentence.", "POSITIVE")
        ]
        self.unit.write_review_sentences(sentences)
        self.assertEqual(
            self.unit.read_review_sentences(),
            sentences
        )

    def test_write_nothing_read_nothing(self):
        sentences = []
        self.unit.write_review_sentences(sentences)
        self.assertEqual(
            self.unit.read_review_sentences(),
            sentences
        )
