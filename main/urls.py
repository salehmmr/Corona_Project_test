from django.conf.urls import url, include
from . import views

app_name = 'main_app'
urlpatterns = [
    url(r'^signup$', views.signup, name='signup'),
    url(r'^login$', views.login, name='login'),
    url(r'^example$', views.example, name='example'),
]