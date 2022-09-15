from django.contrib import admin
from .models import *

# Register your models here.
class Categoryadmin(admin.ModelAdmin):
    list_display = ('category', )

class Bookadmin(admin.ModelAdmin):
    list_display = ('b_name',"b_author",'b_isbn_no','b_category' )

admin.site.register(Book_Category,Categoryadmin)
admin.site.register(Book,Bookadmin)