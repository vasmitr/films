from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SeanceList, SeanceDetail


urlpatterns = [
    url(r'^api/seances/$', SeanceList.as_view(), name='seance'),
    url(r'^api/seances/(?P<pk>[0-9]+)/$',
        SeanceDetail.as_view(), name='seance-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
