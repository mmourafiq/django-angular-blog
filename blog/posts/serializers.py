from rest_framework import serializers
from posts.models import Post
from tags.serializers import TagSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.Field(source='author.username')
    tags_details = TagSerializer(source='tags', read_only=True)
    api_url = serializers.SerializerMethodField('get_api_url')

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'created_on', 'author', 'tags',
                  'tags_details', 'url', 'api_url')
        read_only_fields = ('id', 'created_on')

    def get_api_url(self, obj):
        return "#/post/%s" % obj.id
