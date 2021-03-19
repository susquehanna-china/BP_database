from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'login_api/$', UserView.as_view()),
    url(r'create/$', CreateView.as_view()),
    url(r'edit/$', EditView.as_view()),
    url(r'edit_index/$', EditIndexView.as_view()),
    url(r'search/$', SearchView.as_view()),
    url(r'default/$', SearchDefaultView.as_view()),
    url(r'changepasswd/$', ChangeView.as_view()),
]
