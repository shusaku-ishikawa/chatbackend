# chat/urls.py
from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from rest_framework import routers

app_name = 'chat'

urlpatterns = [
    path('upload/', views.ChatMessageAttachmentView.as_view(), name="attachment")
]
router = routers.SimpleRouter()
router.register('chatrooms', views.ChatRoomViewSet)
router.register('chatroommembers', views.ChatRoomMemberViewSet)
router.register('chatmessages', views.ChatMessageViewSet)
urlpatterns += router.urls


