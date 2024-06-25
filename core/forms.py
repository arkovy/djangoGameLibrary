from django import forms

from core.models import Post


class GameCreate(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'tags', 'pegi', 'image')

    def save(self, user, commit=True):
        post = super(GameCreate, self).save(commit=False)
        post.author = user
        post.save()

        self.save_m2m()
        return post
