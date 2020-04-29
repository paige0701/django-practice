from django.contrib import admin

# Register your models here.
from languageprac.models import Vocabulary, Category, Record, FavouriteVocabulary, FavouriteRecord


class VocabularyInLine(admin.TabularInline):
    model = Vocabulary
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]

    inlines = [VocabularyInLine]


admin.site.register(Vocabulary)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Record)
admin.site.register(FavouriteVocabulary)
admin.site.register(FavouriteRecord)