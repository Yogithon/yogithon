from django.forms import ModelForm, TextInput, EmailInput, Textarea, FileInput
from .models import Pet, User

class PetForm(ModelForm):
    class Meta :
        model = Pet
        fields = (
            'title',
            'p_name',
            'school',
            'author',
            'description',
            'image',
            'insta_url'
        )
        widgets = {
            'title': TextInput(attrs={
                'class': "input",
                'style': "width:300px",
                'placeholder': 'title'
            }),
            'p_name': TextInput(attrs={
                'class': "input",
                'style': "width:300px",
                'placeholder': 'pet_name'
            }),
            'school': TextInput(attrs={
                'class': "input",
                'style': "width:300px",
                'placeholder': 'school'
            }),
            'author': TextInput(attrs={
                'class': "input",
                'style': "width:300px",
                'placeholder': 'author'
            }),
            'description': Textarea(attrs={
                'class': "input",
                'style':"overflow: hidden; resize: none; height: 396px;",
                'placeholder': 'description'
            }),
            'image': FileInput(attrs={
                'class': "input",
                'style': "width:300px",
                'placeholder': 'image'
            }),
            'insta_url': EmailInput(attrs={
                'class': "input",
                'style': "width:300px",
                'placeholder': 'insta_url'
            })
        }

class UserForm(ModelForm) :
    class Meta :
        model = User
        fields = (
            'first_name',
            'last_name',
            'user_id',
            'user_pw',
            'email'
        )