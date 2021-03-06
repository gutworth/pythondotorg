from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
    url(r'operating-systems/$', views.DownloadFullOSList.as_view(), name='download_full_os_list'),
    url(r'release/(?P<release_slug>[-_\w]+)/$', views.DownloadReleaseDetail.as_view(), name='download_release_detail'),
    url(r'(?P<slug>[-_\w]+)/$', views.DownloadOSList.as_view(), name='download_os_list'),
    url(r'$', views.DownloadHome.as_view(), name='download'),
)
