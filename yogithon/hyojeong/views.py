from django.shortcuts import render, get_object_or_404, redirect
from .models import Pet

def main(request):
  pets = Pet.objects.all()
  return render(request, "main.html", {"pets": pets})

def detail(request, pet_id):
    pet = get_object_or_404(Pet, pk = id)
    return render(request, 'detail.html', {"pet":pet})

def new(request) :
    return render (request,'create.html')

def create(request):
    new_pet = Pet()   # object 생성
    new_pet.title = request.POST['title']          # 필드 값 할당
    new_pet.p_name = request.POST['p_name']        # 필드 값 할당
    new_pet.school = request.POST['school']            # 필드 값 할당
    new_pet.author = request.POST['author']
    new_pet.description = request.POST['description']
    new_pet.image = request.POST['image']
    # pub_date는 장고에서 제공하는 모듈을 쓸 것임.

    new_pet.save()

