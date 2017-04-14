from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SeatDetail, SeatList, TicketList, TicketDetail


urlpatterns = [
     url(r'^api/seats/$', SeatList.as_view(), name='seat'),
    url(r'^api/seats/(?P<pk>[0-9]+)/$',
        SeatDetail.as_view(), name='seat-detail'),
    url(r'^api/tickets/$', TicketList.as_view(), name='ticket'),
    url(r'^api/tickets/(?P<pk>[0-9]+)/$',
        TicketDetail.as_view(), name='ticket-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
