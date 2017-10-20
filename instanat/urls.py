from django.conf.urls import url
from django.contrib import admin
from instanat.views import(
LoginView,
UserView,
RegisterView,
LogoutView,
UploadView,
DeleteImageView,
ShowPostView,
AddCommentView,
)


app_name = 'instanat'

urlpatterns = [
    url(r'^post/(?P<post_id>(\d)+)/$', ShowPostView.as_view(), name='show_post'),
    url(r'^post/(?P<post_id>(\d)+)/add_comment$', AddCommentView.as_view(), name='add_comment'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^upload/$', UploadView.as_view(), name='upload'),
    url(r'^delete/(?P<id>(\d)+)/$', DeleteImageView.as_view(), name='delete'),
    url(r'^(?P<username>[\w]+)/$', UserView.as_view(), name='user'),
]
