from django.views.generic import ListView, DeleteView
from .models import Cheese
from django.http import HttpResponse

class CheeseListView(ListView):
    model = Cheese

def test(request):
    return HttpResponse("Hello world, you are at this basic test view!")
