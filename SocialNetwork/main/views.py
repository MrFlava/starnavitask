from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from .forms import PostCreationForm, CustomUserCreationForm, ProfileForm
from .models import Post, Profile

# Create your views here.


def homepage(request):
    return render(request, 'main/homepage.html', context={'posts': Post.objects.all})


def show_post(request, pk):
    return render(request, 'main/post.html', context={'posts': Post.objects.get(id=pk)})


def show_profile(request):
    profile_info = Profile.objects.get(user=request.user)
    if profile_info:
        return render(request, 'main/profile.html', context={'profile': profile_info})
    else:
        print('does not exists')


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, 'Account created successfully')
            return redirect("main:edit_profile")
        # else:
        #     messages.error(request, 'Account created successfully')
        #     for msg in form.error_messages:
        #         print(form.error_messages[msg])

    form = CustomUserCreationForm()
    return render(request, "main/register.html", context={"form": form})


def logout_request(request):
    logout(request)
    return redirect("main:homepage")


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main:homepage")

    form = AuthenticationForm()
    return render(request, "main/login.html", {"form": form})


def create_a_post(request):

    if request.method == "POST":
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('main:homepage')
    else:
        form = PostCreationForm()
    return render(request, 'main/create_a_post.html', {'form': form})


def edit_profile(request):

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('main:homepage')
    else:
        form = ProfileForm()
    return render(request, 'main/edit_profile.html', {'form': form})


def like_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        post.likes += 1
        post.save()
        return show_post(request, pk)


def dislike_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        post.dislikes += 1
        post.save()
        return show_post(request, pk)
