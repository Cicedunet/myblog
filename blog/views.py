from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'blog/base.html')

def list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 1)  # 5 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post_detail.html", {"post_detail": post})

