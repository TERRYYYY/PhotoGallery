from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search_images, name='search_images'),
    url(r'^image/(\d+)', views.get_image, name='image_results'),
    # url(r'^location/(?P<location>\w{0,50})/', views.location, name='location_results'),
    url(r'^category/(?P<category>\w{0,50})/', views.category, name='category_results'),
     url(r'^location/(?P<location>\w+)/', views.location, name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)