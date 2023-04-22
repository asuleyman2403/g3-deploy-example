from django.shortcuts import render, redirect
from blogs.models import Blog, Post
from blogs.forms import CreateBlogForm, CreatePostForm


def index_page(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(owner_id=request.user.id)
        return render(request, 'blogs/index.html', {'blogs': blogs, 'user': request.user})
    else:
        return redirect('/auth/login/')


def create_blog(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = CreateBlogForm()
            return render(request, 'blogs/create-blog.html', {'form': form})
        if request.method == 'POST':
            form = CreateBlogForm(request.POST)
            if form.is_valid():
                title = form.data.get('title')
                description = form.data.get('description')
                blog = Blog(title=title, description=description, owner_id=request.user.id)
                blog.save()
                return redirect('/')
            else:
                return render(request, 'blogs/create-blog.html', {'form': form})
    else:
        return redirect('/auth/login/')


def blog_details(request, pk):
    if request.user.is_authenticated:
        blog = Blog.objects.get(id=pk)
        posts = Post.objects.filter(blog_id=pk).order_by('-created_at')
        form = CreatePostForm()
        return render(request, 'blogs/blog-details.html', {'blog': blog, 'posts': posts, 'form': form})
    else:
        return redirect('/auth/login/')


def blogs_post_create(request, pk):
    if request.user.is_authenticated:
        blog = Blog.objects.get(id=pk)
        if request.method == 'POST':
            form = CreatePostForm(request.POST)
            print('okokokokok')
            if form.is_valid():
                title = form.data.get('title')
                content = form.data.get('content')
                post = Post(title=title, content=content, blog_id=pk)
                post.save()
                return redirect('/blogs/' + str(blog.id) + '/')
    else:
        return redirect('/auth/login/')


def delete_post(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)
        blog = Blog.objects.get(id=post.blog.id)
        if blog.owner.id == request.user.id:
            post.delete()
            return redirect('/blogs/' + str(blog.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')


def delete_blog(request, pk):
    if request.user.is_authenticated:
        blog = Blog.objects.get(id=pk)
        if blog.owner.id == request.user.id:
            blog.delete()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')

