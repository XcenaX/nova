from django.contrib import admin
from .models import User, Category, Blog, Comment

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Blog)
admin.site.register(Category)
