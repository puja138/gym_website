from django import forms
from .models import Contact
from .models import Membership

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


PLAN_CHOICES = [
    ('Basic', 'Basic'),
    ('Standard', 'Standard'),
    ('Premium', 'Premium'),
]

class JoinNowForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    plan = forms.ChoiceField(choices=PLAN_CHOICES, widget=forms.HiddenInput())


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['full_name', 'email', 'phone', 'plan']
