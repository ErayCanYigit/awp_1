from django import template

register = template.Library()


@register.filter
def split_comma(value):
    """Virgülle ayrılmış metni listeye çevirir."""
    if value:
        return [item.strip() for item in value.split(',') if item.strip()]
    return []
