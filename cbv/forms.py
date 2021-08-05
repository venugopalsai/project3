from django import forms

class sturegister(forms.Form):
    male_female = (('Male','male'),('Female','female'))
    sname = forms.CharField()
    gender = forms.ChoiceField( choices=male_female)
    dob = forms.DateField()
    email= forms.EmailField()
    phone = forms.IntegerField(widget=forms.TextInput)