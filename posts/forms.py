from django import forms

from posts.models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['auth', 'image', 'description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['auth'].initial = self.initial['user'].id
        self.fields['auth'].widget = forms.HiddenInput()
        #import ipdb; ipdb.set_trace()