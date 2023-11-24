from rest_framework import serializers
from .models import Article, Journalist
from datetime import datetime
from django.utils.timesince import timesince



class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()
    # thay's show the str name for the author
    # author = serializers.StringRelatedField()
    # author = JournalistSerializer()

    class Meta:
        model = Article
        fields = '__all__'

    def get_time_since_publication(self, obj):
        publication_date = obj.publication_date
        current_date = datetime.now()
        time_delta = timesince(publication_date, current_date)
        return time_delta


    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and description cannot be the same")
        return data
    
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('The title must contain at least 5 characters')
        return value
    
    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('The description must contain at least 10 characters')
        return value
    
    def validate_author(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('The author must contain at least 3 characters')
        return value



class JournalistSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    # articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="detail_class")

    class Meta:
        model = Journalist
        fields = '__all__'
       