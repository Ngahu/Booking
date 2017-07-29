from django.conf.urls import url
from . views import (
    index,
    userProfile,
    book_ticket,
    ticket_detail,
    ticket_update,
    booking_history,
    update_profile,
    #profile,

)


urlpatterns = [
    url(r'^$',index,name='index'),
    url('^profile/$', userProfile, name='profile'),

    ##
    #url('^profile/(?P<profile_user>\d+/)$',profile, name='profile'), #external user viewing the profile
    url('^profile-update/$',update_profile, name='profile-update'),  #profile updating
    #url('^my-profile/$', name=''),  #My profile view


    ##
    url(r'^book-ticket/$',book_ticket,name='book'),
    url(r'^ticket-detail/(?P<id>\d+)/$',ticket_detail,name='detail'),
    url(r'^(?P<id>\d+)/edit/$',ticket_update,name='update'),
    url(r'^booking-history/$',booking_history,name='history'),
    # url(r'^about/$',index,name='about'),
]

