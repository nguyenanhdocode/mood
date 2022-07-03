from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import Post

# Create your views here.

@login_required
def home(request):

    posts = Post.active_posts.all()
    
    return render(request, 'post/home.html', {
        'posts': posts,
        # 'older_posts': older_posts
    })


@login_required
def new_mood(request):

    if request.method == 'POST':
        content = request.POST['content']

        post = Post.objects.create(
            content=content,
            author=request.user
        )

        messages.success(request, 'Đã thêm mood thành công gòi nè :3')

        

    return render(request, 'post/new_post.html')

@login_required
def remove_mood(request, pk):

    mood = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        
        mood.active = False
        mood.save()

        messages.success(request, 'Đã xóa mood thành công!')

    return render(request, 'post/remove_post.html', {

    })

@login_required
def edit_mood(request, pk):
    mood = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        content = request.POST['content']
        mood.content = content
        mood.save()

        messages.success(request, 'Đã chỉnh sửa mood thành công!')


    return render(request, 'post/edit_post.html', {
        'mood': mood,
    })