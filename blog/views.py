from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.models import User
from .forms import AddPostForm
from django .contrib.auth.decorators import login_required
from .models import Post
from django.template.defaultfilters import slugify


def post_list(request):
    object_list = Post.objects.all()
    context = {'posts':object_list}
    return render(request, 'blog/posts.html', context)


def post_user(request, get_username):
    object_list = Post.objects.filter(author = User.objects.get(username = get_username).pk)
    context = {'posts':object_list}
    return render(request, 'blog/posts_user.html', context)


def post_user_detail(request, get_username, posts_slug):
    object_list = get_object_or_404(Post, author = User.objects.get(username = get_username).pk, slug = posts_slug)
    context = {'post':object_list}
    return render(request, 'blog/posts_user_detail.html', context)


@login_required(login_url = 'accounts:login')
def post_add(request):
    form = AddPostForm()
    if request.method == 'POST':
        author=User.objects.get(username = request.user)
        title = request.POST.get('title')
        body = request.POST.get('body')
        results = Post.objects.create(
                                    author=author,
                                    title=title,
                                    slug = slugify(title),
                                    body=body)
        return render(request, 'blog/posts.html')
    context = {'form':form}
    return render(request, 'blog/create_post.html', context)