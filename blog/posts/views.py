from django.shortcuts import render
from .models import Post

# Create your views here.

def posts_home(request):
    queryset=Post.objects.all()
    context={
        "queryset":queryset,
        "title":"home page...."
    }
    return render(request,'index.html',context)

