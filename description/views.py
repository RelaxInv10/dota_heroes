from django.shortcuts import render, get_object_or_404

from .models import Hero

# Create your views here.
def heroes(request):
    hero_list = Hero.objects.filter(is_published=True).select_related('attribute').prefetch_related('positions')

    return render(request, 'description/heroes.html', {'hero_list': hero_list})

def hero_detail(request, pk):
    hero = get_object_or_404(
        Hero.objects
        .select_related('attribute')
        .prefetch_related('positions')
        .filter(is_published=True),
        pk=pk,
    )

    return render(request, 'description/hero_detail.html', {'hero': hero})