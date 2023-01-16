from django.contrib import admin
from .models import *


admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Result)
admin.site.register(CustomUser)

