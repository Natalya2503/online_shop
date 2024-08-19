from django import template
from goods.models import YarnCategories
from goods.models import CategoriesAdaptations

register = template.Library()

@register.simple_tag()
def tag_categories():
    return YarnCategories.objects.all()

@register.simple_tag()
def tag_categories_adapt():
    return CategoriesAdaptations.objects.all()