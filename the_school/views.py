from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from the_school.models import School, Student
from the_school.serializers import SchoolSerializer, StudentSerializer


# GET or POST lists of objects with the API
def schools_list(request):
    if request.method == 'GET':
        these_schools = School.objects.all()
        serializer = SchoolSerializer(these_schools, many=True)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SchoolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    
# GET, UPDATE or DELETE objects given their id with the API
def school_unique(request, id):
    try:
        this_school = School.objects.get(id=id)
    except School.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = SchoolSerializer(this_school)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SchoolSerializer(this_school, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        this_school.delete()
        return HttpResponse(status=204)

def students_list(request):
    if request.method == 'GET':
        these_students = Student.objects.all()
        serializer = StudentSerializer(these_students, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        import requests
        import json
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        """
        Constraint of school's capacity
        Get the current headcount and capacity of the school
        """
        this_school = json.loads(requests.get('the_school/schools/'+str(data['its_school'])).text)
        if this_school['headcount']<this_school['capacity']:
            if serializer.is_valid():
                serializer.save()
                """
                Update school headcount
                """
                requests.put('the_school/schools/'+str(data['its_school']), data={'headcount' : this_school['headcount']+1})
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors)
        else:
            from rest_framework.exceptions import APIException
            raise APIException("School's capacity was overflowed, Student cannot apply to this school")


def student_unique(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        this_student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = StudentSerializer(this_student)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(this_student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        this_student.delete()
        return HttpResponse(status=204)


