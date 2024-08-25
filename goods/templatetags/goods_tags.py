from django import template
from django.utils.http import urlencode
from goods.models import YarnCategories
from goods.models import CategoriesAdaptations

register = template.Library()

@register.simple_tag()
def tag_categories():
    return YarnCategories.objects.all()

@register.simple_tag()
def tag_categories_adapt():
    return CategoriesAdaptations.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)