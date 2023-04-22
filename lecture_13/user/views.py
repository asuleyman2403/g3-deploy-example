from django.shortcuts import render, redirect
from user.forms import UserRegistrationForm, LoginForm, ProfileForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout
from user.models import Profile


def login_page(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = auth.authenticate(username=username, password=password)
            try:
                profile = Profile.objects.get(owner_id=user.id)
            except:
                profile = Profile(owner_id=user.id)
                profile.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/login.html', {'form': form})


def register_page(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'user/registration.html', {'form': form})
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            profile = Profile(owner_id=user.id)
            profile.save()
            password = form.data.get('password')
            auth_data = auth.authenticate(request, email=user.email, password=password)
            login(request, user)
            if auth_data is not None:
                return redirect('/')
            return redirect('/auth/login/')
        else:
            return render(request, 'user/registration.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('/auth/login/')


def settings_page(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            profile = Profile.objects.get(owner_id=request.user.id)
            form = ProfileForm(data={'bio': profile.bio}, files={'image': profile.image, 'resume': profile.resume})
            return render(request, 'user/profile.html', {'profile': profile, 'form': form})
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            profile = Profile.objects.get(owner_id=request.user.id)
            if form.is_valid():
                profile.bio = form.data.get('bio')
                profile.image = form.files.get('image')
                profile.resume = form.files.get('resume')
                profile.save()
                return render(request, 'user/profile.html', {'profile': profile, 'form': form})
            else:
                return render(request, 'user/profile.html', {'profile': profile, 'form': form})
    else:
        return redirect('/')

