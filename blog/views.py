from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'blog/base.html')

def list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   # paginator = Paginator(post_list, 2)  # 5 posts per page

   # page_number = request.GET.get('page')
   # page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, "blog/post_detail.html", {
        "post_detail": post,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form
    })

