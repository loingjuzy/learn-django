from django import template
from django.utils.safestring import mark_safe

# 必须是register对象
register = template.Library()


@register.simple_tag
def func(a1, a2):
    return a1 + a2
