from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# router.register(r'', views.QuestionViewSet)

urlpatterns = [
    path('', views.question_list, name='questions'),
    path('<int:pk>/', views.question_detail, name='detail'),
    path('<int:pk>/results/', views.question_result, name='result'),
    path('<int:pk>/vote/', views.vote, name='vote'),
]