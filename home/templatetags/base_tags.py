from django import template
from ..models import Category

register = template.Library()
@register.inclusion_tag("partials/category_navbar.html")
def Category_Navbar():
    return {"Category" : Category.objects.all()}