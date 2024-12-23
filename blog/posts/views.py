from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>Create</h1>")


def post_detail(request,id):
    instance=get_object_or_404(Post,id=id)
    context={
        "title":"detail",
        "instance":instance
    }
    return render(request,"post_detail.html",context)


def post_list(request):
    queryset=Post.objects.all()
    context={
        "title":"List of posts",
        "object_list":queryset
    }
    return render(request,'post_list.html',context)


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")




