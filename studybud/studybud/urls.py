# This is Route Directories File
from django.contrib import admin

# django dont know about the other urls, use include
from django.urls import path, include

admin.site.site_header = "Ice-cream Admin"
admin.site.site_title = "Ice-cream Admin Portal"
admin.site.index_title = "Welcome to Ice-cream Admin"

urlpatterns = [
    # path, function name
    path('admin/', admin.site.urls),
    # Add this path for redirect to urls we build in base app
    path('', include('base.urls'))  # Location of the urls
]
