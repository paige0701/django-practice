from django.contrib import admin
from .models import Question, Choice

# Admin 사이트에서 Question 모델을 관리 하려면 여기에 등록해야한다 !!

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra =  3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)