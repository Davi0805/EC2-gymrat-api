from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Fichaname, Exercparametros, Log
from .serializers import FichanameSerializer, ExercparametrosSerializer, LogSerializer

class ExercparametrosCreateView(generics.CreateAPIView):
    queryset = Exercparametros.objects.all()
    serializer_class = ExercparametrosSerializer
    http_method_names = ['post']

class ExercparametrosListView(generics.ListAPIView):
    queryset = Exercparametros.objects.all()
    serializer_class = ExercparametrosSerializer
    http_method_names = ['get']

class ExercparametrosUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Exercparametros.objects.all()
    serializer_class = ExercparametrosSerializer
    http_method_names = ['put']

class FichanameCreateView(generics.CreateAPIView):
    queryset = Fichaname.objects.all()
    serializer_class = FichanameSerializer
    http_method_names = ['post']

class FichanameListView(generics.ListAPIView):
    queryset = Fichaname.objects.all()
    serializer_class = FichanameSerializer
    http_method_names = ['get']

class LogCreateView(generics.CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    http_method_names = ['post']

class LogListView(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    http_method_names = ['get']