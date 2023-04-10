from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserList(APIView):

    # permission_classes = [                  #Need to be logged in to see user list
    #     permissions.IsAuthenticated           #However, this code required someone to be authenticated to create an account
    # ]

    def get_queryset(self,request):
        if request.user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(pk=request.user.id)    #to hide anon users, filter by is_hidden=False (add t model)


    def get(self, request):
        users = self.get_queryset(request)
        serialiazer = CustomUserSerializer(users, many=True)
        return Response(serialiazer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CustomUserDetail(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)