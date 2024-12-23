from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages


# Create your views here.

def post_create(request):
    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()

        messages.success(request,"successfully created")
    else:
        messages.error(request,"not successfully created")


    context={
            "form":form
        }

    return render(request,"post_form.html",context)


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


def post_update(request,id):
    instance=get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()

        return redirect('posts:detail', id=instance.id) 
        messages.success(request,"saved.")
    
    context={
        "title":instance.title,
        "instance":instance,
        "form":form
    }
    
    return render(request,"post_form.html",context)


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")




