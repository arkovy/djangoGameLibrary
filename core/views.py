from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DeleteView

from core.forms import GameCreate
from core.models import Post


def post_list_view(request):
    posts = Post.objects.all()
    return render(request,  template_name='posts_list.html', context={'posts': posts})


class IndexView(TemplateView):
    template_name = 'index.html'
    form_class = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter().select_related('author').prefetch_related('tags')

        return context


class GameCreateView(CreateView):
    template_name = 'game_create.html'
    form_class = GameCreate
    success_url = '/game-create/'

    def form_valid(self, form):
        form.save(user=self.request.user)
        return redirect(self.success_url)

    def get_initial(self):
        return {
            'title': 'Введите назване игры',
        }


class PostDeleteView(DeleteView):
    template_name = 'delete-game.html'
    model = Post
    success_url = '/'


