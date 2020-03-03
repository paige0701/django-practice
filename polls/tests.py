import datetime
import json

from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIRequestFactory, APITestCase

from polls.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
            is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recnetly_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """

        time = timezone.now() - datetime.timedelta(hours=23, minutes=59)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), True)


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionListViewTests(APITestCase):
    def test_no_questions(self):

        url = reverse('questions')
        response = self.client.get(url)
        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'No polls are available')
