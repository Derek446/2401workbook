from django.shortcuts import render, get_object_or_404
# Below load the post model from the models.py file
# . means same directory
from .models import Post

# Create your views here.
# this is what will handle the request and retrun a response
def post_list(request):
    # get all the posts from the database
    posts = Post.objects.all()
    # breakpoint()
    # the following will render the template we created
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk): #pk is primary key
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
