from django.contrib import admin
from .models import Contact


# Register your models here.
class Contact_admin(admin.ModelAdmin):
    list_display=('name','email','subject')

admin.site.register(Contact,Contact_admin)