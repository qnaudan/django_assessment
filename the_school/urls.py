"""
URLs for the application the_school
Precisely URLs for the API
"""

from django.urls import path
from snippets import views

urlpatterns = [
    path('the_school/schools/', views.schools_list),
    path('the_school/students/', views.students_list),
    path('the_school/schools/<int:id>', views.school_unique),
    path('the_school/students/<int:id>', views.student_unique),
]