import logging
import unittest
import os

from src.store.reviewed_sentences_store import ReviewedSentencesStore
from src.model.reviewed_sentence import ReviewedSentence

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger()


class TestReviewSentencesStore(unittest.TestCase):

    file_path = "./test_reviewed_sentences.json"

    def setUp(self):
        self.unit = ReviewedSentencesStore(TestReviewSentencesStore.file_path)

    def tearDown(self):
        os.remove(TestReviewSentencesStore.file_path)

    def test_write_and_read(self):
        sentences = [
            ReviewedSentence("This is a review sentence.", "NEUTRAL"),
            ReviewedSentence("This is a good review sentence.", "POSITIVE")
        ]
        self.unit.write_reviewed_sentences(sentences)
        self.assertEqual(
            self.unit.read_reviewed_sentences(),
            sentences
        )

    def test_write_nothing_read_nothing(self):
        sentences = []
        self.unit.write_reviewed_sentences(sentences)
        self.assertEqual(
            self.unit.read_reviewed_sentences(),
            sentences
        )

