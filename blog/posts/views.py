from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote_plus
from django.utils import timezone


# Create your views here.

def post_create(request):
    if not request.user.is_staff or not  request.user.is_superuser:
        raise Http404

    form=PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        print(form.cleaned_data.get("title"))
        instance.save()

        messages.success(request,"successfully created")
    else:
        messages.error(request,"not successfully created")


    context={
            "form":form
        }

    return render(request,"post_form.html",context)


def post_detail(request,slug):
    instance=get_object_or_404(Post,slug=slug)
    if instance.publish > timezone.now().date() or instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

    share_string = quote_plus(instance.content)

    context={
        "title":"detail",
        "instance":instance,
        "share_string": share_string,
    }
    return render(request,"post_detail.html",context)


def post_list(request):
    today = timezone.now().date()
    queryset_list = Post.objects.active() #.order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()
    
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
        "object_list":queryset,
        "today": today,
    }
    return render(request,'post_list.html',context)


def post_update(request,slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    
    instance=get_object_or_404(Post,slug=slug)
    form=PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()

        return redirect('posts:detail', slug=instance.slug) 
        messages.success(request,"saved.")
    
    context={
        "title":instance.title,
        "instance":instance,
        "form":form
    }
    
    return render(request,"post_form.html",context)


def post_delete(request,slug):
    instance=get_object_or_404(Post,slug=slug)
    instance.delete()
    messages.success(request,"successfully deleted.")
    return redirect('posts:list')
    

    



