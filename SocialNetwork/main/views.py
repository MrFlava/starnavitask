from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ObjectDoesNotExist

from .forms import PostCreationForm, CustomUserCreationForm, ProfileForm
from .models import Post, Profile, Preference

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
            return redirect("main:edit_profile")

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


def add_profile_info(request):

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


def edit_profile_info(request):

    if request.method == "POST":
        user_profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance= user_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('main:profile')
    else:
        form = ProfileForm()
    return render(request, 'main/edit_profile.html', {'form': form})


def postpreference(request, id, val):
    if request.method == "POST":
        eachpost = get_object_or_404(Post, pk=id)

        obj = ''

        valueobj = ''

        try:
            obj = Preference.objects.get(user=request.user, post=eachpost)

            valueobj = obj.value

            valueobj = int(valueobj)

            userpreference = int(val)

            if valueobj != userpreference:
                obj.delete()

                upref = Preference()
                upref.user = request.user

                upref.post = eachpost

                upref.value = userpreference

                if userpreference == 1 and valueobj != 1:
                    eachpost.likes += 1
                    eachpost.dislikes -= 1
                elif userpreference == 2 and valueobj != 2:
                    eachpost.dislikes += 1
                    eachpost.likes -= 1

                upref.save()

                eachpost.save()

                context = {'eachpost': eachpost,
                           'postid': id}

                return render(request, 'main/post.html', context)

            elif valueobj == userpreference:
                obj.delete()

                if userpreference == 1:
                    eachpost.likes -= 1
                elif userpreference == 2:
                    eachpost.dislikes -= 1

                eachpost.save()

                context = {'eachpost': eachpost,
                           'postid': id}

                return render(request, 'main/post.html', context)

        except ObjectDoesNotExist:
            upref = Preference()

            upref.user = request.user

            upref.post = eachpost

            upref.value = val

            userpreference = int(val)

            if userpreference == 1:
                eachpost.likes += 1
            elif userpreference == 2:
                eachpost.dislikes += 1

            upref.save()

            eachpost.save()

            context = {'eachpost': eachpost,
                       'postid': id}

            return render(request, 'main/post.html', context)

    else:
        eachpost = get_object_or_404(Post, pk=id)
        context = {'eachpost': eachpost,
                   'postid': id}

        return render(request, 'main/post.html', context)

