from django.contrib import admin
from .models import comment, spams

# Register your models here.
admin.site.register(comment)
admin.site.register(spams)
