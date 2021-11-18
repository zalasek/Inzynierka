from django.contrib import admin
from .models import Document, Assignment, Comment
# Register your models here.

admin.site.register(Document)
admin.site.register(Assignment)
admin.site.register(Comment)

