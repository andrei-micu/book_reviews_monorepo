import json
import os
from dataclasses import asdict

from src.model.reviewed_sentence import ReviewedSentence


class ReviewedSentencesStore:

    def __init__(self, file_path = "./reviewed_sentences.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w'):
                pass

    def write_reviewed_sentences(self, reviewed_sentences: list[ReviewedSentence]):
        reviewed_sentences_dicts = list(map(asdict, reviewed_sentences))
        reviewed_sentences_string = json.dumps(reviewed_sentences_dicts)
        with open(self.file_path, "w") as file:
            file.write(reviewed_sentences_string)

    def read_reviewed_sentences(self):
        with open(self.file_path, "r") as file:
            reviewed_sentences_json = json.load(file)
            return [
                ReviewedSentence(**reviewed_sentence_json)
                for reviewed_sentence_json in reviewed_sentences_json
            ]