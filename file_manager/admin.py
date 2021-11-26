from django.contrib import admin

# Register your models here.

from .models import FileManager
from .models import FileDeletedLog

admin.site.register(FileManager)