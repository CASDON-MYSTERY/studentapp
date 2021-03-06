from rest_framework import serializers
from .models import Examination, Exam_day_and_venue


class Examination_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Examination
        fields= "__all__"


class Exam_day_and_venue_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Exam_day_and_venue
        fields= "__all__"