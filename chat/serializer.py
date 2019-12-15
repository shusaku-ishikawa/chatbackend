from rest_framework import serializers
from .models import *
from django.core.exceptions import ObjectDoesNotExist
import time
from datetime import datetime, timedelta
from myauth.serializer import UserSerializer
from drf_extra_fields.fields import Base64ImageField

class AttachmentSerializer(serializers.ModelSerializer):
    uploaded_user = UserSerializer(many = False, read_only = True)
    class Meta:
        model = Attachment
        fields = ('id', 'file','file_url', 'file_name', 'uploaded_user', 'uploaded_at')

class TimestampField(serializers.Field):
    def to_representation(self, value):
        return int(time.mktime(value.timetuple())) + 60 * 60 * 9

class ChatMessageSerializer(serializers.ModelSerializer):
    speaker = UserSerializer(many = False, read_only = True)
    sent_at = TimestampField()
    attachments = AttachmentSerializer(many = True, read_only = True)
    class Meta:
        model = ChatMessage
        fields = ('pk', 'speaker', 'message', 'attachments', 'sent_at', 'is_read', 'read')
  
class ChatRoomMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False, read_only = True)
    # room = ChatRoomSerializer(many = False, read_only = True)
    class Meta:
        model = ChatRoomMember
        fields = ('user',)
    # def get_new_messages(self, obj):
    #     unread = [unread_message for unread_message in obj.room.messages.all() if not unread_message.read]
    #     return len(unread)

class ChatRoomSerializer(serializers.ModelSerializer):
    #latest_message = ChatMessageSerializer(many = False, read_only = True)
    
    #messages = ChatMessageSerializer(many = True, read_only = True)
    members = ChatRoomMemberSerializer(many = True, read_only = True)
    class Meta:
        model = ChatRoom
        fields = ('id', 'title', 'members')

