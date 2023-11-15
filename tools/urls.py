from django.urls import path
from .views import ToolListCreateView, ToolDeleteView, ToolRetrieveView, ToolListByTagView

urlpatterns = [
    path('tools/', ToolListCreateView.as_view(), name='tool-list-create'),
    path('tools/<int:pk>/', ToolRetrieveView.as_view(), name='tool-retrieve'),
    path('tools/<int:pk>/delete/', ToolDeleteView.as_view(), name='tool-delete'),
    path('tools/by-tag/<str:tag>/', ToolListByTagView.as_view(), name='tool-list-by-tag'),
]