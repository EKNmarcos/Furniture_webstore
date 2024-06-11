from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter
@stringfilter
def replace(value, arg):
      return value.replace(arg, '')


@register.filter
def less_than(value, arg):
      return value < arg