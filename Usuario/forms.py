from django import forms

class ProfileForm(forms.Form):
    profile_pic = forms.ImageField()
