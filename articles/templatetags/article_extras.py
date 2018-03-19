import markdown2

from django.urls import resolve
from django import template
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
from django.template.defaultfilters import stringfilter


from ..models import Topic


register = template.Library()

@register.simple_tag
def nav_active(request, url):
    '''
    In template: {% nav_active request "url_name_here" %}
    '''
    url_name = resolve(request.path).url_name
    if url_name == url:
        return "active"
    return ""

# nav_active() will check the web request url_name and compare it 
# to the named url group within urls.py, 
# setting the active class if they match.


@register.inclusion_tag('articles/articles_nav.html')
def all_topics():
    '''
    Returns dictionary of topics to display in the navgation
    '''
    topics = Topic.objects.all()
    return {'topics': topics}

# all_topics() will query all the existing topics in the DB


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''
    Converts markdown to html
    '''
    html_body = markdown2.markdown(force_text(markdown_text), extras=['fenced-code-blocks', 'code-friendly'])
    return mark_safe(html_body)

# markdown_to_html() will convert markdown text into html to be rendered