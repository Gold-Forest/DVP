from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Bb
# Create your views here.


def index(request):
    bbs = Bb.objects.all()
    context = {'bbs': bbs}
    return render(request, 'bboard/index.html', {'bbs': bbs})
