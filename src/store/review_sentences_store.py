import json
import os
from dataclasses import asdict

from src.model.review_sentence import ReviewSentence


class ReviewSentencesStore:

    def __init__(self, file_path = "./review_sentences.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w'):
                pass

    def write_review_sentences(self, review_sentences: list[ReviewSentence]):
        review_sentences_dicts = list(map(asdict, review_sentences))
        review_sentences_string = json.dumps(review_sentences_dicts)
        with open(self.file_path, "w") as file:
            file.write(review_sentences_string)

    def read_review_sentences(self):
        with open(self.file_path, "r") as file:
            review_sentences_json = json.load(file)
            return [
                ReviewSentence(**review_sentence_json)
                for review_sentence_json in review_sentences_json
            ]