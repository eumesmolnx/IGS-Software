from rest_framework import serializers
from .models import Employee,Departament

class EmployeeSerializer(serializers.ModelSerializer):
    #departament = serializers.CharField(source='departament.name')
    class Meta:
        model = Employee
        fields = ('name','email','departament')
    def to_representation(self, instance):
        self.fields['departament'] =  serializers.CharField(source='departament.name')
        return super(EmployeeSerializer, self).to_representation(instance)

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = ('name',)