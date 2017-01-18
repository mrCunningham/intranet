from django.contrib import admin
from .models import Post, Department

# Register your models here.
admin.site.register(Department)
admin.site.register(Post)
