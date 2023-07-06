# import django.shortcuts import render, redirect
# from .models import Pet
# from .forms import PetList

# def p_update(request, pk) :
#     pet = Pet.objects.get(id=pk)
#     if request.method == "POST":
#         form = PetForm(request.POST, instance=pet)
#         if form.is_valid():
#             pet = form.save(commit=False)
#             pet.save()
#             return redirect('p_list')
#     else :
#         form = PetForm(instance=list)
#     return render(request, 'pet/update.html', {'form':form})

# def p_delete(request, pk) :
#     pet = Pet.objects.get(id=pk)
#     if request.method == "POST" :
#         pet.delete()
#         return redirect('p_list')
#     return render(request, 'pet/delete.html', {'pet':pet})

# @csrf_exempt
# def vote(request, pk):
#     try:
#         pet = get_object_or_404(Pet, pk=pk)
#     except(KeyError, Pet.DoesNotExist):
#         return render(request, 'pet/p_detail.html', {'pet': pet, 'error_message': "You didn't select a choice."})
#     else:
#         pet.like += 1
#         pet.save()
#
#     return render(request, 'pet/p_detail.html', {'pet': pet})