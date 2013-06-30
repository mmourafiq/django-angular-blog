from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    api_url = serializers.SerializerMethodField('get_api_url', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'url', 'api_url')
        read_only_fields = ('id', 'created_on', 'updated_on')

    def get_api_url(self, obj):
        return "#/post/%s" % obj.id
