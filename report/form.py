from django import forms

class UploadData(forms.Form):
  segment = forms.CharField(label="Cơ sở", widget=forms.TextInput(attrs={
    "class": "form-control"
  }))
  file = forms.FileField(label="File dữ liệu")