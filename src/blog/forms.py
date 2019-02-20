from django import forms
from .models import Article

# class ProductForm(forms.ModelForm):
#     author       = forms.CharField(label='', 
#                     widget=forms.TextInput(attrs={"placeholder": "Your name"}))
#     content = forms.CharField(
#                         required=False, 
#                         widget=forms.Textarea(
#                                 attrs={
#                                     "placeholder": "Your post",
#                                     "class": "new-class-name two",
#                                     "id": "my-id-for-textarea",
#                                     "rows": 20,
#                                     'cols': 120
#                                 }
#                             )
#                         )
class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'author',
            'content',
        ]
