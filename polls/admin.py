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

    # Question 아래 choice 등록 할 수 있음
    inlines = [ChoiceInLine]

    # Question list 에서 보여줄 fields
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # 필터 옵션
    list_filter = ['pub_date']

    # 검색바 생김
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)