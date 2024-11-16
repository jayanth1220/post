from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.forms import ModelForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')
class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=('title','description','body' ,'Category')