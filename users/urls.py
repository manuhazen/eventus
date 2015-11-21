from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/$', 'users.views.UserLogin', name="login"),
    url(r'^salir/$', 'users.views.UserLogOut', name="logout"),
)