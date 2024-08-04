from django import template
from goods.models import YarnCategories

register = template.Library()

@register.simple_tag()
def tag_categories():
    return YarnCategories.objects.all()