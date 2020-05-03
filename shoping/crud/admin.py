from django.contrib import admin

from .models import Lecture
from .models import Eval

admin.site.register(Lecture)
admin.site.register(Eval)
