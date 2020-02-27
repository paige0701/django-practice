from django.contrib import admin
from .models import Question

# Admin 사이트에서 Question 모델을 관리 하려면 여기에 등록해야한다 !!
admin.site.register(Question)