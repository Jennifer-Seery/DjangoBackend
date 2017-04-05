## File to create links to different site features

from django.conf.urls import url
from django.contrib import admin
from StudentDatabase import views


## Creating URLS
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^students/',views.StudentList.as_view()),
]


