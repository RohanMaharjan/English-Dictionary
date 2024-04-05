from django.contrib import admin
from .models import Word,Meaning,Synonym,Antonym

admin.site.register(Word)
admin.site.register(Meaning)
admin.site.register(Synonym)
admin.site.register(Antonym)