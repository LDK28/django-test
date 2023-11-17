from django.contrib import admin
from hello.models import TestModel

class TestAdmin(admin.ModelAdmin):
    def get_number(self, obj):
        return '1'

    list_display = ['id', '__str__', 'string', 'number', 'get_number']
    # fields = ['string', 'number', 'file']
    # exclude = ['file']
    fieldsets = [
        (
            'Данные', {"fields": ['string', 'number']}
        ),
        (
            'Файлы', {"fields": ['file']}
        )
    ]

admin.site.register(TestModel, TestAdmin)