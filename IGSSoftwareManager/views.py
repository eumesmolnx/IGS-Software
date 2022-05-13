from rest_framework import viewsets
from .serializers import EmployeeSerializer, DepartamentSerializer
from .models import Employee,Departament

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Create your views here.
class DepartamentViewSet(viewsets.ModelViewSet):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer