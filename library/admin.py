from django.contrib import admin
from .models import Student, LibraryHistory, FeesHistory

admin.site.register(Student)
admin.site.register(LibraryHistory)
admin.site.register(FeesHistory)

