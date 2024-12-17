from django.shortcuts import render

# Create your views here.

def posts_home(request):
    context={
        "title":"home page...."
    }
    return render(request,'index.html',context)

