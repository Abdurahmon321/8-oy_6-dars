from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Hudud, QurilishTashkiloti, QurilishBinisi
from .serializers import HududSerializer, QurilishTashkilotiSerializer, QurilishBinisiSerializer

class HududViewSet(viewsets.ModelViewSet):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer

class QurilishTashkilotiViewSet(viewsets.ModelViewSet):
    queryset = QurilishTashkiloti.objects.all()
    serializer_class = QurilishTashkilotiSerializer

class QurilishBinisiViewSet(viewsets.ModelViewSet):
    queryset = QurilishBinisi.objects.all()
    serializer_class = QurilishBinisiSerializer