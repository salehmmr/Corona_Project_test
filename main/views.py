
from . import models
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import BasePermission


class IsAuthenticatedSaleh(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        condition = True
        return condition

@api_view(['POST'])
@permission_classes((IsAuthenticatedSaleh,))
def signup(request):
    if request.method == 'POST':
        data = request.data
        data_email = data['email']
        data_username = data['username']
        data_firstname = data['firstname']
        data_lastname = data['lastname']
        data_password = data['password']
        data_password2 = data['password2']
        if not models.User.objects.filter(username=data_username).exists():
            if data_password == data_password2:
                models.User.objects.create(username=data_username, fname=data_firstname, lname=data_lastname,
                                                      password=data_password, e_mail=data_email)
                return Response({"message": "Created Successfully!"})
            return Response({"message": "Passwords not matched!"})
        return Response({"message": "Username already exists!"})


@api_view(['POST'])
@permission_classes(())
def login(request):
    if request.method == 'POST':
        data = request.data
        data_username = data['username']
        data_password = data['password']
        if models.User.objects.filter(username=data_username).exists():
            current_user = models.User.objects.get(username=data_username)
            if not models.Session.objects.filter(userId=current_user.auto_increment_id):
                if current_user.password == data_password:
                    models.Session.objects.create(userId=current_user.auto_increment_id)
                    return Response({"message": "you are logged in!"})
                return Response({"message": "wrong password!"})
            return Response({"message": "you were logged in!"})
        return Response({"message": "wrong username!"})


@api_view(['GET'])
@permission_classes(())
def example(request):
    if request.method == 'GET':
        return Response({"message": "Done!"})