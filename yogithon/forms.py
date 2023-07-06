from django import forms
from .models import Pet, User

class PetForm(forms.ModelForm):
    class Meta :
        model = Pet
        fields = [
            'title',
            'p_name',
            'school',
            'author',
            'description',
            'image',
            'insta_url'
        ]

class UserForm(forms.ModelForm) :
    class Meta :
        model = User
        fields = [
            'first_name',
            'last_name',
            'user_id',
            'user_pw',
            'email'
        ]