from rest_framework import serializers
from .models import Fichaname, Exercparametros, Log

class FichanameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fichaname
        fields = '__all__'

class ExercparametrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercparametros
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'