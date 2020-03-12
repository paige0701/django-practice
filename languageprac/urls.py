from django.urls import path

from languageprac import views

urlpatterns = [
    path('<int:id>/', view=views.get_words_by_category)
]