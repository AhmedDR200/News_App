from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'