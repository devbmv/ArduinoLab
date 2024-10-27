from django import template

register = template.Library()


@register.filter
def get_family(families, keyword):
    """Returnează familia care conține `keyword` în numele său."""
    # Caută familia care conține `keyword` în nume
    family = families.filter(name__icontains=keyword).first()
    return family.name if family else ""
