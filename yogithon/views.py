from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import PetForm

from allauth.account.views import login
from django.contrib import messages
from django.contrib.sites import requests
from django.core.files.base import ContentFile
import os
import environ

from .exception import SocialLoginException, GithubException

# Create your views here.

def main(request):
  pets = Pet.objects.all()
  return render(request, "yogithon/main.html", {"pets": pets})

def detail(request, pk):
    pet = get_object_or_404(Pet, id=pk)
    return render(request, 'yogithon/detail.html', {"pet":pet})

def new(request) :
    return render (request,'create.html')

def create(request):
    # new_pet = Pet()   # object 생성
    # new_pet.title = request.POST['title']          # 필드 값 할당
    # new_pet.p_name = request.POST['p_name']        # 필드 값 할당
    # new_pet.school = request.POST['school']            # 필드 값 할당
    # new_pet.author = request.POST['author']
    # new_pet.description = request.POST['description']
    # new_pet.image = request.POST['image']
    # # pub_date는 장고에서 제공하는 모듈을 쓸 것임.
    # new_pet.save()

    if request.method == "POST" :
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.save()
            return redirect('yogithon:home')
    else :
        form = PetForm()
    return render(request, 'yogithon/create.html', {'form':form})

def update(request, pk) :
    pet = Pet.objects.get(id=pk)
    if request.method == "POST":
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.save()
            return redirect('p_list')
    else :
        form = PetForm(instance=list)
    return render(request, 'pet/update.html', {'form':form})

def delete(request, pk) :
    pet = Pet.objects.get(id=pk)
    if request.method == "POST" :
        pet.delete()
        return redirect('p_list')
    return render(request, 'pet/delete.html', {'pet':pet})

@csrf_exempt
def vote(request, pk):
    try:
        pet = get_object_or_404(Pet, pk=pk)
    except(KeyError, Pet.DoesNotExist):
        return render(request, 'pet/p_detail.html', {'pet': pet, 'error_message': "You didn't select a choice."})
    else:
        pet.like += 1
        pet.save()

    return render(request, 'pet/p_detail.html', {'pet': pet})

# 깃허브 로그인
def github_login(request):
    try:
        if request.user.is_authenticated:
            raise SocialLoginException("User already logged in")
        client_id = os.environ.get("GITHUB_CLIENT_ID")
        redirect_uri = "http://127.0.0.1:8000/users/login/github/callback/"
        scope = "read:user"
        return redirect (
            f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
        )
    except SocialLoginException as error:
        messages.error(request, error)
        return redirect("core:home")

def github_login_callback(request):
    try:
        if request.user.is_authenticated:
            raise SocialLoginException("User already logged in")
        code = request.GET.get("code", None)
        if code is None:
            raise GithubException("Can't get code")

        client_id = os.environ.get("GITHUB_CLIENT_ID")
        client_secret = os.environ.get("GITHUB_CLIENT_SECRETS")

        token_request = requests.post(
            f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
            headers={"Accept": "application/json"},
        )
        token_json = token_request.json()
        error = token_json.get("error", None)

        if error is not None:
            raise GithubException("Can't get access token")

        access_token = token_json.get("access_token")
        profile_request = requests.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"token {access_token}",
                "Accept": "application/json",
            },
        )
        profile_json = profile_request.json()
        username = profile_json.get("login", None)

        if username is None:
            raise GithubException("Can't get username from profile_request")

        avatar_url = profile_json.get("avatar_url", None)
        if avatar_url is None:
            raise GithubException("Can't get avatar_url from profile_request")

        name = profile_json.get("name", None)
        if name is None:
            raise GithubException("Can't get name from profile_request")

        email = profile_json.get("email", None)
        if email is None:
            raise GithubException("Can't get email from profile_request")

        bio = profile_json.get("bio", None)
        if bio is None:
            raise GithubException("Can't get bio from profile_request")

        try:
            user = models.User.objects.get(email=email)

            if user.login_method != models.User.LOGIN_GITHUB:
                raise GithubException(f"Please login with {user.login_method}")
        except models.User.DoesNotExist:
            user = models.User.objects.create(
                username=email,
                first_name=name,
                email=email,
                bio=bio,
                login_method=models.User.LOGIN_GITHUB,
            )
            photo_request = requests.get(avatar_url)

            user.avatar.save(f"{name}-avatar", ContentFile(photo_request.content))
            user.set_unusable_password()
            user.save()
            messages.success(request, f"{user.email} logged in with Github")
        login(request, user)
        return redirect(reverse("core:home"))

    except GithubException as error:
        messages.error(request, error)
        return redirect(reverse("core:home"))
    except SocialLoginException as error:
        messages.error(request, error)
        return redirect(reverse("core:home"))
