from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# ModelSerializer saves us from writing a lot of duplicate information that's already in our model.
# It is a shortcut for creating serializer classes with an automatically determined set of fields
# and simple default implementations of create and update methods.
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
