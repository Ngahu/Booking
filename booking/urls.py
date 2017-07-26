from django.conf.urls import url

from . views import (
    index,
    userProfile,

)


urlpatterns = [
    url(r'^$',index,name='index'),
    url('^profile/$',userProfile,name='profile')
    # url(r'^about/$',index,name='about'),
]