from django.urls import path

from languageprac import views

urlpatterns = [
    path('categories/', view=views.get_categories, name='categories'),
    path('records/', view=views.RecordView.as_view(), name='records'),
    path('<slug:id>/', view=views.get_records_by_id, name='record_detail')
]