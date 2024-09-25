from django.urls import path
from .views import VisitorTableListCreateView

urlpatterns = [
    path('visitors/', VisitorTableListCreateView.as_view(), name='visitor-list-create'),
]
