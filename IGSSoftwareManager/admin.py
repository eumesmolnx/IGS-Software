from django.contrib import admin
from .models import Employee,Departament
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name","email","departament")

@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ("name",)
