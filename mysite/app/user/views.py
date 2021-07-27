from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.user.models import Profile
from app.user.serializers import UserSerializer, ProfileSerializer


class ItemUserViews(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        id_user = request.user.id
        snippet = self.get_object(id_user)
        serializer = UserSerializer(snippet)
        return Response(serializer.data)

class ListUser(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class CreatProfile(APIView):

    def post(self, request, format=None):
        iphone = request.data.get("iphone")
        mail = request.data.get("mail")
        skype = request.data.get("skype")
        age = request.data.get("age")
        address = request.data.get("address")

        new_order = Profile(iphone = iphone, mail = mail, skype = skype, age = age, address = address,)
        new_order.save()
        rez = new_order.id


        return Response(rez, status=status.HTTP_201_CREATED)

class ListProfile(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return Profile.objects.all()

class ItemProfile(APIView):

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        id_user = request.user.id
        profile = Profile.objects.filter(user_id = id_user)[0]
        snippet = self.get_object(profile.id)
        serializer = ProfileSerializer(snippet)
        return Response(serializer.data)


class PatchProfileViews(APIView):

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def patch(self, request,):
        id_user = request.user.id
        profile = Profile.objects.filter(user_id=id_user)[0]
        testmodel_object = self.get_object(profile.id)
        serializer = ProfileSerializer(testmodel_object, data=request.data,
                                         partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)