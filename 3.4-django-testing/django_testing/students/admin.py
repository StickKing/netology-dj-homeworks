from django.contrib import admin
from students.models import Student, Course
# Register your models here.

admin.site.register([Student, Course])