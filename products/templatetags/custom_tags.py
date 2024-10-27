from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def break_tag(context):
    context["break_loop"] = True
    return ""
