from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    queryset=Post.objects.all()
    context={
        "queryset":queryset,
        "title":"home page...."
    }
    return render(request,'index.html',context)

def post_detail(request):
    instance=get_object_or_404(Post,id=8)
    context={
        "instance":instance,
        "title":instance.title

    }
    return render(request,'post_detail.html',context)

