from django.shortcuts import render
from django.http import HttpResponse
from .models import Backpack

# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World!')

def hello_test(request):
    # backpack_list = Backpack.objects.all()
    return render(request, 'hello_test.html')