from django import forms
from .models import Post, Category

#hardcode choices inside category - Create a list with categories
#choices = [('Coding', 'Coding'), ('Movies', 'Movies'), ('Books', 'Books')]

#inside category should be "forms.Select(choices=choices" 

#when we don't hardcode the categories, we create a query to grab each category
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
  choice_list.append(item)



class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'author', 'category', 'body')

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add title here'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'author': forms.Select(attrs={'class': 'form-control'}),
      'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
    }


class EditForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'body')

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please add your title'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
    }