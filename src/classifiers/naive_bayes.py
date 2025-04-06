from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

from src.model.review_sentence import ReviewSentence


class NaiveBayes:
    """Classifier that uses the Naive Bayes algorithm to label review sentences

    It's initialized using a set of sentences already labeled
    """

    def __init__(self, logger, review_sentences: list[ReviewSentence], batch_size: int):
        """Initializes the instance with a set of labeled sentences

        Args:
          logger: the logger instance
          review_sentences: the list of labeled sentences
          batch_size: the amount of sentences to process at a time when training
        """
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
        """Classifies the input text. The input may contain multiple sentences.
        Each sentence is attributed a label.

        Args:
          text: the text to process and classify
        Returns:
          A list of labeled sentences, with one of the polarities from the training set.
        """
        blob = TextBlob(text, classifier=self._classifier)
        return [
            ReviewSentence(sentence.string, sentence.classify())
            for sentence in blob.sentences
        ]
