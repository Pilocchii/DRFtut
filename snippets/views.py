from rest_framework import mixins
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# First, refactored to class based views. Feels good.
# Then refactored using model mixins. DRF is putting in some good work, now, but the params could be a little bulky.
# Going one step further, generics provide some generic views. Where'd all the code go? Much pythonic.
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer