from django.contrib import admin
from post.models import Post

# Register your models here.

class Postadmin(admin.ModelAdmin):
    list_display=('title','slug','category')

admin.site.register(Post,Postadmin)