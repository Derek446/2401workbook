from django.shortcuts import render
# Below load the post model from the models.py file
from .models import Post

# Create your views here.
# this is what will handle the request and retrun a response
def post_list(request):
    # get all the posts from the database
    posts = Post.objects.all()
    # breakpoint()
    # the following will render the template we created
    return render(request, 'blog/post_list.html', {'posts': posts})
