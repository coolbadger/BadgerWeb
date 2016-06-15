from django.conf.urls import include, url
from django.contrib import admin
from homePage import views as home_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'BadgerWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',home_view.default)
]
