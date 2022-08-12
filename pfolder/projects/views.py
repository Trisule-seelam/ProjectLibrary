from msilib.schema import tables
from unicodedata import name
from django.shortcuts import render, HttpResponse,redirect
# from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Projects

def home(request):
    return render(request, 'home.html')



def contacts(request):
    return render(request, 'Contact.html')


# @csrf_exempt
# def  search(request):
#     x=request.POST.get("search1")
#     if x:
#         x=table.objects.filter(name__icontains=x).values()
#         print(x)
#     return redirect("/")
@csrf_exempt
def projects(request):
    if  request.method=="POST":
        Projects.objects.create(project_owner=request.user,project_name=request.POST.get("title"),project_files=request.FILES.get("upload_file"))
    return render(request, 'projects.html')