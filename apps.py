from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

#####################

# myapp/views.py
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django!")

