from django.urls import path

from languageprac import views

urlpatterns = [
    path('categories/', view=views.get_categories, name='categories'),
    path('records/', view=views.RecordView.as_view(), name='records'),
    path('word/', view=views.get_word_of_the_day, name='word_of_the_day'),
    path('favourite/category/', view=views.FavouriteCategoryView.as_view(), name='favourite_category_word'),
    path('<slug:id>/', view=views.get_records_by_id, name='record_detail')
]