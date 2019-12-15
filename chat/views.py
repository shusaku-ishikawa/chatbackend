from django.shortcuts import render, get_object_or_404
from chat.models import *
from chat.serializer import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from rest_framework import status

class ChatRoomViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    def list(self, request, **kwargs):
        rm_list = request.user.rooms.all()
        rooms = [rm.room for rm in rm_list]
        data = ChatRoomSerializer(rooms, many = True).data
        return Response(status=status.HTTP_200_OK, data = data)

class ChatRoomMemberViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = ChatRoomMember.objects.all()
    serializer_class = ChatRoomSerializer
    def list(self, request, **kwargs):
        rm_list = request.user.rooms.all()
        members = [rm.opponent for rm in rm_list]
        data = ChatRoomMemberSerializer(members, many = True).data
        return Response(status=status.HTTP_200_OK, data = data)

class ChatMessageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = ChatMessage.objects.all()
    serializer_class = ChatRoomSerializer
    def list(self, request, **kwargs):
        page_count = 10
    
        if not 'room' in request.GET:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        if not 'page' in request.GET:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        room_id = request.GET.get('room')
        page = int(request.GET.get('page'))
        offset = (page - 1) * page_count

        room = get_object_or_404(ChatRoom, id = room_id)
        messages = ChatMessage.objects.filter(room = room).order_by('-id')[offset:offset + page_count]
        messages = reversed(messages)
        data = ChatMessageSerializer(messages, many = True).data
        return Response(status=status.HTTP_200_OK, data = data)

class ChatMessageAttachmentView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def get(self, request):
        if 'room' not in request.GET:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        room = get_object_or_404(ChatRoom, id = request.GET.get('room'))
        attachments = Attachment.objects.filter(parent_message__room = room)
        data = AttachmentSerializer(attachments, many = True).data
        return Response(status = status.HTTP_200_OK, data = data)
        
    def post(self, request):
        files = request.FILES
        print(files)
        obj_list = []
        for file in files:
            file_content = request.FILES[file]
            obj = Attachment()
            obj.file.save(file, file_content)
            obj.save()
            obj_list.append(obj)

        data = AttachmentSerializer(obj_list, many = True).data
        return Response(status = status.HTTP_200_OK, data = data)

