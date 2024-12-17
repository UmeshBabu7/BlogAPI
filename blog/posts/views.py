from django.shortcuts import render

# Create your views here.

def posts_home(request):
    return render(request,'index.html')
