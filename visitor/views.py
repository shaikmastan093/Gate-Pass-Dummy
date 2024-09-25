# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from .models import VisitorTable
from .serializers import VisitorTableSerializer

class VisitorTableListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = VisitorTable.objects.all()
    serializer_class = VisitorTableSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of Visitor objects or create a new visitor.",
        responses={200: VisitorTableSerializer(many=True), 201: VisitorTableSerializer()},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new visitor object.",
        request_body=VisitorTableSerializer(),
        responses={201: VisitorTableSerializer(), 400: "Bad Request"},
    )
    def post(self, request):
        serializer = VisitorTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
