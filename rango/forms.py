from django import forms
from .models import Page, Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the category name.")
    #views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    #likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    #initial values are only intended for initial form display(not fallback data)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    #title = forms.CharField(max_length=128,
    #                        help_text="Please enter the title of the page.")
    #url = forms.URLField(max_length=200,
    #                     help_text="Please enter the URL of the page.")
    #views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        fields = ('title', 'url',)
        help_texts = {
            'title': "Please enter the page title.",
            'url': "Please enter the page URL."
        }


    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            return cleaned_data

