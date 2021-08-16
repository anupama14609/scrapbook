from django.forms import fields, widgets
from .models import ScrapFriend
from django import forms
import datetime

class ScrapFriendForm(forms.ModelForm):
    dob = forms.DateField(
        label = "Enter Your Date Of Birth",
        widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year-5))    
    )

    def __init__(self, *args, **kwargs):
        super(ScrapFriendForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control my-2',
            })
 

    class Meta:
        model = ScrapFriend
        fields = ("__all__")
      