from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice


class PollsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.question = Question.objects.create(question_text="Test Question", pub_date=timezone.now())
        self.choice = Choice.objects.create(question=self.question, choice_text="Test Choice", votes=0)

    def test_index_view(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Question")

    def test_detail_view(self):
        response = self.client.get(reverse('polls:detail', args=(self.question.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Question")

    def test_results_view(self):
        response = self.client.get(reverse('polls:results', args=(self.question.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Question")

    def test_vote_view(self):
        response = self.client.post(reverse('polls:vote', args=(self.question.id,)), {'choice': self.choice.id})
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.choice.refresh_from_db()
        self.assertEqual(self.choice.votes, 1)

    def test_question_viewset(self):
        response = self.client.get(reverse('question-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Question")

    def test_choice_viewset(self):
        response = self.client.get(reverse('choice-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Choice")
