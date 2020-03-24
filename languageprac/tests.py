import pytest

# Create your tests here.
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework.authtoken.models import Token


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def test_password():
    return 'jenny'

@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'email' not in kwargs:
            kwargs['email'] = 'jenny@jenny.com'
        return django_user_model.objects.create_user(**kwargs)
    return make_user

@pytest.fixture
def get_or_create_token(db, create_user):

    user = authenticate(email=create_user(), password='jenny')
    token, _ = Token.objects.get_or_create(user=user)
    return token

@pytest.mark.django_db
def test_unauthorized_request(api_client, get_or_create_token):
   url = reverse('categories')
   api_client.credentials(HTTP_AUTHORIZATION='Token ' + str(get_or_create_token))
   response = api_client.get(url)
   assert response.status_code == 200