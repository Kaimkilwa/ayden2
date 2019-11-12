from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import *
GOT_US = {
  ('f', 'FRIENDS'),
  ('S', 'SEARCH ENGINE'),
  ('A', 'ADVERTISEMENT'),
  ('O', 'OTHERS'),
  ('N', 'NEWS LETTER')

}

class ContactForm(forms.ModelForm):
  name = forms.CharField(label=_("Your name"),max_length=200,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Enter your name........'}))
  email = forms.CharField(label=_("Email"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'example@gmail.xom'}))
  got_us_through = forms.ChoiceField(choices =GOT_US, widget=forms.Select({ 'class':'form-control'
                              }))
  comment = forms.CharField(max_length=200,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': 'Enter yor comment here......'}))
  class Meta:
    model  = Contactmodel
    fields = ( 'name' ,'email','got_us_through', 'comment')
 	
 		