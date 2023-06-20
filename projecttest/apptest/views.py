from django.shortcuts import render
from django.http import HttpResponse

pets = [
  { "petname": "Fido", "animal_type": "dog"},
  { "petname": "Clementine", "animal_type": "cat"},
  { "petname": "Cleo", "animal_type": "cat"},
  { "petname": "Oreo", "animal_type": "dog"},
]

# Create your views here.
def home(request):
  context = {"name": "Junior"}
  return render(request, "apptest/home.html", context)

def simplecalc(request):
  return render(request, "apptest/simplecalc.html")

def about(request):
  context = {"name": "Djangoer", "pets": pets}
  return render(request, "apptest/about.html", context)

def marketchart(request):
  return render(request, "apptest/marketchart.html")
