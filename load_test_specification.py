import random

from locust import HttpUser, between, task

from src.store.reviewed_sentences_store import ReviewedSentencesStore


class AnalyseApiUser(HttpUser):
    wait_time = between(5, 15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reviewed_sentences_store = ReviewedSentencesStore()
        self.reviewed_sentences = self.reviewed_sentences_store.read_reviewed_sentences()

    @task
    def analyse(self):
        random_sentence_index = random.randint(0, len(self.reviewed_sentences))
        sentence = self.reviewed_sentences[random_sentence_index].sentence
        self.client.post("/analyse/", json={
            "text": sentence
        })
