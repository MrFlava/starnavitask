from django import forms
from .models import Post, Profile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        labels = {'title': "Title", "content": "Content"}


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    first_name = forms.CharField(label='Enter your first name', min_length=4, max_length=150)
    last_name = forms.CharField(label='Enter your last name', min_length=4, max_length=150)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        new_user = User.objects.create_user(self.cleaned_data['username'],
                                            self.cleaned_data['email'],
                                            self.cleaned_data['password1'])
        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        if commit:
            new_user.save()
        return new_user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['about_yourself', 'avatar']
        labels = {'about_yourself': "Tell about yourself", 'avatar': "Load your avatar"}

    def clean_about_yourself(self):
        about_yourself = self.cleaned_data['about_yourself']

        return about_yourself

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(u'Please use an image that is %s x %s pixels or smaller.' % (max_width, max_height))

            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, GIF or PNG image.')

            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(u'Avatar file size may not exceed 20k.')

        except AttributeError:
            print('error')

        return avatar
