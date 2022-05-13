from rest_framework import serializers
from .models import Employee,Departament

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    departament = serializers.CharField(source='departament.name')
    class Meta:
        model = Employee
        fields = ('name','email','departament')

class DepartamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departament
        fields = ('name',)