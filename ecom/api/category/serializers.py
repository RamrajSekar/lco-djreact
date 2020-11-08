from rest_framework import serializers
from .models import Category

# This is to serialize the data in JSON format

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name','description')