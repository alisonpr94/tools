from rest_framework import generics
from .models import Tool
from .serializers import ToolSerializer
from rest_framework.response import Response
from rest_framework import status

class ToolListCreateView(generics.ListCreateAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class ToolRetrieveView(generics.RetrieveAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class ToolDeleteView(generics.DestroyAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class ToolListCreateView(generics.ListCreateAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag', None)
        if tag:
            return Tool.objects.filter(tags__contains=[tag])
        return Tool.objects.all()

class ToolListByTagView(generics.ListAPIView):
    serializer_class = ToolSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag', None)
        if tag:
            return Tool.objects.filter(tags__contains=[tag])
        return Tool.objects.all()
    
class ToolRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        tags = request.data.get('tags', None)

        if tags:
            instance.tags = tags
            instance.save()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)