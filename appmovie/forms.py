from django import forms

class ApiForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput)
    director = forms.CharField(max_length=30, required=True, widget=forms.TextInput)

    def __str__(self) -> str:
        return self.name 