from django.shortcuts import render

from description.models import Hero

# Create your views here.
def index(request):
    template_name = 'page/index.html'

    hero_list = (
        Hero.objects
        .filter(
            is_published=True,
            is_on_main=True,
        )
        .select_related('attribute')
        .prefetch_related('positions')
    )

    context = {
        'hero_list': hero_list,
    }

    return render(request, template_name, context)


def news(request):
    return render(request, 'page/news.html')

def about(request):
    return render(request, 'page/about.html')
