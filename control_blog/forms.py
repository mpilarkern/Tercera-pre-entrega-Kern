from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(required = True, max_length=256)
    length = forms.DurationField(required=False)
    release_year = forms.IntegerField(required=True, max_value=3000)
    plot = forms.CharField(required=False)
