from django.contrib.auth import authenticate

# Create your views here.
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK

from polls.models import User


@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if email is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)

    user = authenticate(email=email, password=password)
    if not user:
        return Response({'error': 'Invalid credentials'}, status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({'token': token.key, 'user_id': user.id, 'full_name': user.full_name}, status=HTTP_200_OK)


@api_view(['POST'])
@permission_classes((AllowAny,))
def create(request):
    email = request.data.get('email')
    password = request.data.get('password')
    fullname = request.data.get('fullname')

    user = User.objects.create_user(email=email, password=password, full_name=fullname)
    if user:
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)