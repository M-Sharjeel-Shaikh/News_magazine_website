from django.contrib import admin
from django.urls import path
from post.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='Home'),
    path('contact/', contact, name='Contact'),
    path('search/', search, name='search'),
    path('detail/<slug>', detail, name='Detail'),
    path('Business/', business, name='Business'),
    path('Technology/', technology, name='Technology'),
    path('Health/', health, name='Health'),
    path('Fashion/', fashion, name='Fashion'),
    path('Food/', food, name='Food'),
    path('Education/', education, name='Education'),
    path('Entertainment/', entertainment, name='Entertainment'),
    path('Sports/', sport, name='Sport'),
    path('Others/', other, name='Other'),

    path('header/', header, name='header'),
    path('footer/', footer, name='footer'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT   )