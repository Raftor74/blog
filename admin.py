from django.contrib import admin

# Register your models here.
from blog.models import News

admin.site.register(News)