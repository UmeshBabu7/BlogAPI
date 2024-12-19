from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages



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

        messages.success(request,'successful')
    else:
        messages.error(request,'not successful')

    context={
        "form":form
    }
    return render(request,'post_form.html',context)

def post_update(request,id):
    instance=get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None, instance=instance)
    if form.is_valid:
        instance=form.save(commit=False)
        instance.save()

        messages.success(request,'item saved.')

    context={
        "instance":instance,
        "form":form,
        "title":instance.title
    }
    return render(request,'post_form.html',context)


def post_delete(request,id):
    instance=get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,'successfully deleted.')
    return redirect('posts:list')




