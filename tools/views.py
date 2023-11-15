from rest_framework import generics
from .models import Tool
from .serializers import ToolSerializer

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