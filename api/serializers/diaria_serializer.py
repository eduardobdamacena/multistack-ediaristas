from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models import Diaria

class DiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diaria
        fields = '__all__'
