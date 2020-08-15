from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .post_creation_form import PostCreationForm
from .models import Post

# Create your views here.


def homepage(request):
    return render(request, 'main/homepage.html', context={'posts': Post.objects.all})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
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

