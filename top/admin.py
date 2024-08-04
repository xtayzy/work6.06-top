from django.contrib import admin

# Register your models here.


from top.models import *

admin.site.register(Top)
admin.site.register(Category)
admin.site.register(Type)