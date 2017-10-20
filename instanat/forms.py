from django import forms
from .models import Post, Comment

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=128)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):

    CNT_USERNAME = {
    'class':"form-control",
    'placeholder':"Username",
    'name':"username",
    'type':"text"
    'autofocus'
    }

    CNT_PASSWORD = {
    'class':"form-control",
    'placeholder':"Password",
    'name':"password",
    'type':"password",
    'value':""
    }

    CNT_REPEAT_PASSWORD = {
    'class':"form-control",
    'placeholder':"Repeat password",
    'name':"password",
    'type':"password",
    'value':""
    }

    username = forms.CharField(label='Username', max_length=128, widget=forms.TextInput(attrs=CNT_USERNAME))
    password = forms.CharField(widget=forms.PasswordInput(attrs=CNT_PASSWORD))
    second_password = forms.CharField(widget=forms.PasswordInput(attrs=CNT_REPEAT_PASSWORD))

# class AddCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         exclude = ['added_date']
#
#     post = models.ForeignKey(Post)
#     user = models.ForeignKey(User)
#     text = models.CharField(max_length=256)
#     added_date = models.DateTimeField(auto_now_add=True)
