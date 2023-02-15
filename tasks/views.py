from django.shortcuts import render, redirect
from .models import *


def index(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "index.html", context)