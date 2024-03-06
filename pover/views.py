from django.shortcuts import render
from .models import Link

def main_page(request):
    links = Link.objects.all()
    return render(request, 'pover/index.html', {'links': links})
# Create your views here.
