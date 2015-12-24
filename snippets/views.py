from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# decorator for working with function based views
@api_view(['GET', 'POST'])
# format lets us refer to specific formats in our URLs, like "/snippets.json"
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet
    """

    # gets all code snippets
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        # Response obj is a type of TemplateResponse that takes unrendered content and determines what content type to return
        return Response(serializer.data)

    # creates new snippet
    elif request.method == 'POST':
        # request.data handles arbitrary data, works for POST PUT and PATCH
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # good practice to use status code constants rather than just the numerical code
            # also, our responses are no longer explicitly tied to JSON
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update, or delete a code snippet
    """

    #ensures snippet exists
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # gets code snippet data
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    # updates code snippet data
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # deletes code snippet
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)