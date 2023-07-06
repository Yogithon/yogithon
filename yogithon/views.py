from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Pet
from .forms import PetForm

# Create your views here.

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
