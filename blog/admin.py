from django.contrib import admin

# Register your models here.

from django.contrib import admin
# from django.contrib.auth.models import 

from .models import Post 
# Register your models here.

# admin.site.register(User)
admin.site.register(Post)