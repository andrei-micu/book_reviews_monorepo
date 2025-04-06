from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

from src.model.reviewed_sentence import ReviewedSentence


class NaiveBayes:

    def __init__(self, logger, reviewed_sentences: list[ReviewedSentence], batch_size: int):
        self._classifier = NaiveBayesClassifier([])
        training_data = [
            (reviewed_sentence.sentence, reviewed_sentence.polarity)
            for reviewed_sentence in reviewed_sentences
        ]

        i = 0
        training_length = len(training_data)
        while i < training_length:
            batch = training_data[i:i + batch_size]
            logger.info(f"Training with items {i}/{training_length}")
            self._classifier.update(batch)
            i = i + batch_size

    def classify(self, text: str) -> list[(str, str)]:
        blob = TextBlob(text, classifier=self._classifier)
        return [
            (sentence.string, sentence.classify())
            for sentence in blob.sentences
        ]
