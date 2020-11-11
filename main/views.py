from . import models
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status

# use django authentication for User authentication, We can also use django rest SessionAuthentication.
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# use django user model
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from .Authentication import token_expire_handler


@api_view(['POST'])
@permission_classes(())
def login(request):
    try:
        params = request.data
        user = authenticate(username=params['username'], password=params['password'], )
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            is_expired, token = token_expire_handler(token)
            tmp_response = {
                'access': token.key,
                'userid': token.user_id
            }
            return Response(tmp_response, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Wrong username or password"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes(())
def signup(request):
    try:
        data = request.data
        data_username = data['username']
        data_password = data['password']
        data_email = data['email']
        newUser = User.objects.create(username=data_username, email=data_email)
        newUser.set_password(data_password)
        newUser.save()
        if newUser:
            return Response({"message": "Created Successfully!"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Something might be Wrong!"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)