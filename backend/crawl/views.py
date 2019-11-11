from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

# from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import hotdeal
from .serializers import HotdealSerializer
# Create your views here.


class HotdealView(viewsets.ModelViewSet):
    queryset = hotdeal.objects.all()
    serializer_class = HotdealSerializer
    
    # def perform_create(self,serializer):
    #     serializer.save()
