from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder':'Enter Username'}))
    password = forms.CharField(label='Password', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder':'Enter Password', 'type':'password'}))
class RegistrationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'name', 'placeholder':'Enter Your Name'}))
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder':'Enter Your Username'}))
    email = forms.CharField(label='Email', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email', 'placeholder':'Enter Your Email'}))
    password = forms.CharField(label='Password', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder':'Enter Your Password', 'type':'password'}))
    confirmPassword = forms.CharField(label='Password', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name':'confirmPassword', 'placeholder':'Re-enter Your Password', 'type':'password'}))
    status = forms.ChoiceField(choices = ((1,"developer"),(0,"player")),
                                widget=forms.Select(attrs={'class': 'form-control', 'name': 'status'}))
class AddGameForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'name', 'placeholder':'Enter Game Name'}))
    category = forms.CharField(label='category', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'category', 'placeholder':'Enter Your Category'}))
    price = forms.FloatField(label='price',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'price', 'placeholder':'Enter Price'}))
    url = forms.CharField(label='url', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'url', 'placeholder':'Enter Game URL'}))
    imagepath = forms.CharField(label='Image Path', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name':'imagepath', 'placeholder':'Enter Game Image URL'}))
    description = forms.CharField(label='Description', max_length=100,
                               widget=forms.Textarea(attrs={'class': 'form-control', 'name':'description', 'placeholder':'Enter Game description'}))
