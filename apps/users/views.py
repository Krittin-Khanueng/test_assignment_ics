from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status, generics
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views import View
from django.http import HttpResponse
from apps.users.serializers import UserSerializer


User = get_user_model()


class CustomObtainJSONWebToken(ObtainAuthToken):
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        response = Response({
            'token': token.key,
            'user': UserSerializer(user).data
        })

        if response.status_code == status.HTTP_200_OK:
            # Login with Django for session authentication
            user = authenticate(
                username=request.data['username'],
                password=request.data['password']
            )
            login(request, user)
        return response
