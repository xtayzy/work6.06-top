from django import forms

from top.models import Top, Category, Type


class TopForm(forms.ModelForm):
    class Meta:
        model = Top
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

