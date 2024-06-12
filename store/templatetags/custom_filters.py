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


@register.filter
def mod(value, arg):
      return (value + 2) % arg

@register.filter
def mod_plus(value, arg):
      return (value + 3) % arg


@register.filter
def shorten(value: str):
      return value.replace('http://127.0.0.1:8000/store/shopcart/', '')[1:]