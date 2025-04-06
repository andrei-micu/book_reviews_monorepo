import random

from locust import HttpUser, between, task

from src.store.review_sentences_store import ReviewSentencesStore


class AnalyseApiUser(HttpUser):
    wait_time = between(5, 15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.review_sentences_store = ReviewSentencesStore()
        self.review_sentences = self.review_sentences_store.read_review_sentences()

    @task
    def analyse(self):
        random_sentence_index = random.randint(0, len(self.review_sentences))
        sentence = self.review_sentences[random_sentence_index].sentence
        self.client.post("/analyse/", json={
            "text": sentence
        })
