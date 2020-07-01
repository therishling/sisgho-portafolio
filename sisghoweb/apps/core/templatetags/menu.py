import re
from django import template
from django.urls import reverse, NoReverseMatch, reverse_lazy

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if pattern == path:
        return 'active'
    return ''

@register.simple_tag(takes_context=True)
def show(context, pattern_or_urlname):
    try:
        pattern = reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if pattern == path:
        return 'show'
    return ''

@register.simple_tag(takes_context=True)
def current(context, pattern_or_urlname):
    try:
        pattern = reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if pattern == path:
        return 'current'
    return ''

@register.simple_tag(takes_context=True)
def active_pagination(context, n):
    full_path = context['request'].get_full_path()
    
    path = context['request'].path
    
    if full_path == path:
        if n == 1:
            return 'active'

    rep_path = full_path.replace(path,'')
    
    if rep_path.find('?page=') == 0:
        number_page = int(rep_path.replace('?page=',''))
        if n == number_page:
            return 'active'
  
    
    if rep_path.find('?estado=') == 0:
        if rep_path.find('&') == -1:
            if n == 1:
                return 'active'
        else:
            rep2_path = rep_path.replace('?estado=','')
            datos = rep2_path.split('&')
            number_page = int(datos[1].replace('page=',''))

            if number_page == n:
                return 'active'
        
        
        


    return ''

@register.simple_tag
def fecha():
    return date.today()