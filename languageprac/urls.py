from django.urls import path

from languageprac import views

urlpatterns = [
    path('categories/', view=views.get_categories),
    path('records/', view=views.RecordView.as_view()),
    path('<slug:id>/', view=views.get_records_by_id),

]