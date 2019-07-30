from django.shortcuts import render , redirect, get_object_or_404
from .models import Post
from django.utils import timezone
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})


def new(request):
    return render(request,'new.html')

def create(request):
    
    post = Post()
    post.title = request.POST['post_title']
    post.body = request.POST['post_body']
    post.pub_date = timezone.datetime.now()
    if request.FILES:
      post.image = request.FILES['post_image']
    post.save()

    return redirect('home')



def read(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'read.html', {'post' : post})

def renew(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'renew.html',{'post' : post})

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.title = request.POST["post_title"]
    post.body = request.POST["post_body"]
    post.pub_date = timezone.datetime.now()
    if request.FILES:
      post.image = request.FILES['post_image']
    post.save()
    return redirect('read', post_id=post_id)

def delete(request, post_id):
    if request.POST:
      post = get_object_or_404(Post, pk=post_id)
      post.delete()
      return redirect('home')
    else:
      return redirect('read', post_id=post_id)