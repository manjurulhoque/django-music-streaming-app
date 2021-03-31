from django import template

from core.models import Favorite

register = template.Library()


@register.simple_tag(name='is_favorited', takes_context=True)
def is_favorited(context, song, user):
    request = context['request']
    if not request.user.is_authenticated:
        return 'make'
    favorited = Favorite.objects.filter(user=user, song=song)
    if favorited:
        return 'remove'
    else:
        return 'make'
