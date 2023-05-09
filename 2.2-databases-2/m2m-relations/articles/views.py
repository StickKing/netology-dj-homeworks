from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    acricles = Article.objects.all().prefetch_related('scopes')
    ordering = '-published_at'
    context = {'object_list': acricles.order_by(ordering)}
    return render(request, template, context)
