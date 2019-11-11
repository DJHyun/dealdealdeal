from .models import hotdeal
from rest_framework import serializers
# from django.contrib.auth.models import User


class HotdealSerializer(serializers.HyperlinkedModelSerializer):
    # genres_array = serializers.ReadOnlyField()
    # rating_set = RatingListSerializer(many=True)
    # cluster = serializers.ReadOnlyField(source='cluster.cluster')
    # movie_poster = serializers.ImageField(use_url=True)
    
    class Meta:
        model = hotdeal
        fields = ('id', 'title', 'link','time')