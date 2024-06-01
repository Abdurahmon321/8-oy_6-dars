from rest_framework import serializers
from .models import Hudud, QurilishTashkiloti, QurilishBinisi


class HududSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hudud
        fields = '__all__'


class QurilishTashkilotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = QurilishTashkiloti
        fields = '__all__'


class QurilishBinisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = QurilishBinisi
        fields = '__all__'
