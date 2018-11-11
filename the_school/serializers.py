"""
Serializing Object instances into JSon
for the Django Rest Framework API
"""

from rest_framework import serializers
from the_school.models import School, Student


class SchoolSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) #Create an ID for the object when created with POST
    name = serializers.CharField(max_length=20)
    capacity = serializers.PositiveIntegerField()
    headcount = serializers.PositiveIntegerField()
    def create(self, data):
        return School.objects.create(**data)

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.capacity = data.get('capacity', instance.capacity)
        instance.headcount = data.get('headcount', instance.headcount)
        instance.save()
        return instance

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    ID_number = serializers.CharField(max_length=20)
    
    def create(self, data):
        return Student.objects.create(**data)

    def update(self, instance, data):
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.ID_number = data.get('ID_number', instance.ID_number)
        instance.save()
        return instance