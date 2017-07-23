from django.conf.urls import url
from Cscapp import views

urlpatterns = [
    url(r'^$', views.course, name='course'),
    url(r'^course/(?P<course_code>[\w\-]+)/$', views.show_course, name='show_course'),
]