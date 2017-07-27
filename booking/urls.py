from django.conf.urls import url

from . views import (
    index,
    userProfile,
    book_ticket,
    ticket_detail,
    ticket_update,
    booking_history,

)


urlpatterns = [
    url(r'^$',index,name='index'),
    url('^profile/$', userProfile, name='profile'),
    url(r'^book-ticket/$',book_ticket,name='book'),
    url(r'^ticket-detail/(?P<id>\d+)/$',ticket_detail,name='detail'),
    url(r'^(?P<id>\d+)/edit/$',ticket_update,name='update'),
    url(r'^booking-history/$',booking_history,name='history'),
    # url(r'^about/$',index,name='about'),
]
