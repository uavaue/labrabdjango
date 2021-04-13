from rest_framework import generics
from .models import *
from .serializers import *


class StudentListView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    def get_object(self):
        key = self.kwargs["pk"]
        student = Student.objects.get(pk = key)
        return student
