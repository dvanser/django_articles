from .models import Article
from taggit.models import Tag
from django.views.generic import ListView,DetailView


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class ArticleList(TagMixin, ListView):
    queryset = Article.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'


class TagIndexView(TagMixin, ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.filter(status=1).filter(tags__name=self.kwargs.get('tag_slug')).order_by('-created')
