from django import template

register = template.Library()


@register.filter
def discounted_price(product):
    return product.price - (product.price * (product.discount/100))
