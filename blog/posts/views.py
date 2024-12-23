from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def post_create(request):
    form=PostForm(request.POST or None, request.FILES or None)
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
    queryset_list=Post.objects.all()
    
    paginator=Paginator(queryset_list,5) # show 5 per page
    page=request.GET.get("page")
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1) # if page is not an integer, deliver first page

    except EmptyPage:
        queryset=paginator.page(paginator.num_pages) # if page is out of range, deliver last page


    context={
        "title":"List of posts",
        "object_list":queryset
    }
    return render(request,'post_list.html',context)


def post_update(request,id):
    instance=get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None, request.FILES or None, instance=instance)
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


def post_delete(request,id):
    instance=get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,"successfully deleted.")
    return redirect('posts:list')
    

    



