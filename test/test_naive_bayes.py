import logging
import unittest

from src.classifiers.naive_bayes import NaiveBayes
from src.model.reviewed_sentence import ReviewedSentence

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger()


class TestNaiveBayes(unittest.TestCase):

    def setUp(self):
        self.unit = NaiveBayes(
            logger,
            reviewed_sentences=[ReviewedSentence("Test sentence.", "POSITIVE")],
            batch_size=1
        )

    def test_classify_sentence(self):
        self.assertEqual(
            self.unit.classify("Another test sentence"),
            [('Another test sentence', 'POSITIVE')]
        )

    def test_classify_empty_string(self):
        self.assertEqual(
            self.unit.classify(""),
            []
        )

    def test_classify_number(self):
        with self.assertRaises(TypeError):
            self.unit.classify(55)
