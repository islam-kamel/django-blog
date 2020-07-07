from django import template
from blog.models import Post , comment

register = template.Library()

@register.inclusion_tag('blog/latest_post.html')

def latest_posts():
    context = {
        'l_post' : Post.objects.all()[0:5],
    }
    return context

@register.inclusion_tag('blog/latest_comments.html')

def latest_comments():

    context = {
        'l_comment' : comment.objects.filter(active=True)[:5],

    }

    return context