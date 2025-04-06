from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

from src.model.review_sentence import ReviewSentence


class NaiveBayes:

    def __init__(self, logger, review_sentences: list[ReviewSentence], batch_size: int):
        self._classifier = NaiveBayesClassifier([])
        training_data = [
            (review_sentence.sentence, review_sentence.polarity)
            for review_sentence in review_sentences
        ]

        i = 0
        training_length = len(training_data)
        while i < training_length:
            batch = training_data[i:i + batch_size]
            logger.info(f"Training with items {i}/{training_length}")
            self._classifier.update(batch)
            i = i + batch_size

    def classify(self, text: str) -> list[ReviewSentence]:
        blob = TextBlob(text, classifier=self._classifier)
        return [
            ReviewSentence(sentence.string, sentence.classify())
            for sentence in blob.sentences
        ]
