from django.shortcuts import render,get_object_or_404
from .models import Post
from .forms import PostForm



# Create your views here.

def post_list(request):
    queryset=Post.objects.all()
    context={
        "queryset":queryset,
        "title":"home page...."
    }
    return render(request,'index.html',context)

def post_detail(request,id):
    instance=get_object_or_404(Post,id=id)
    context={
        "instance":instance,
        "title":instance.title

    }
    return render(request,'post_detail.html',context)


def post_create(request):
    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        print(form.cleaned_data.get("title")) 
        instance.save()

    context={
        "form":form
    }
    return render(request,'post_form.html',context)
