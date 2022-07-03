import os
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import get_user_model
from django.urls import reverse

from mood import settings
from post import models as post_models

# Create your views here.

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        print(f'>>> {user}')

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('post:home'))
        else:
            messages.error(request, 'Thông tin đăng nhập không chính xác!')
            
        

    return render(request, 'user/login.html', {

    })

def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('user:login'))

@login_required
def profile(request):
    
    moods = post_models.Post.active_posts.filter(author=request.user)
    
    return render(request, 'user/profile.html', {
        'moods': moods,
        'mood_count': moods.count(),
    })

@login_required
def change_avatar(request):
    if request.method == 'POST' and request.FILES['avatar']:
        avatar = request.FILES['avatar']
        
        request.user.avatar = avatar.name

        now = datetime.now()

        year =  now.strftime('%Y')
        month = now.strftime('%m')
        static_dir = os.path.join(settings.BASE_DIR, 'static', 'avatars', year, month)

        fss = FileSystemStorage(static_dir)
        file = fss.save(avatar.name, avatar)

        image_url = os.path.join(settings.STATIC_URL, 'avatars', year, month, avatar.name)

        get_user_model().objects.filter(username=request.user.username).update(
            avatar=image_url
        )

        return HttpResponseRedirect(reverse('user:profile'))

        
    return render(request, 'user/change_avatar.html', {

    })

@login_required
def change_password(request):

    if request.method == 'POST':
        old_password = request.POST['old_password']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

        user = authenticate(username=request.user.username, password=old_password)
        
        if user is not None:
            if password_1 == password_2:
                user.set_password(password_1)
                user.save()
                return HttpResponseRedirect(reverse('user:logout'))
                
            else:
                messages.error(request, 'Mật khẩu xác nhận không chính xác.')
        else:
            messages.error(request, 'Mật khẩu cũ không chính xác.')

    return render(request, 'user/change_password.html', {

    })