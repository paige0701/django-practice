from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import Question, Choice, User


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


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'full_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords  do not match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'full_name', 'is_staff')

    def clean_password(self):
        return self.initial['password']

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'full_name', 'is_staff')
    list_filter = ('is_staff',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ['is_staff']}),
    )

    add_fieldsets = (
        (None, { 'classes': ('wide', ),
                 'fields': ('email', 'full_name', 'password1', 'password2',)}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)