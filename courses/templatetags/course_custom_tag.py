from django import template
from courses.models import UserCourse
import math


register = template.Library()


@register.simple_tag
def apply_discount(price, discount):
    if price is None or discount is 0:
        return price
    price = (price - (price * discount / 100))
    return math.floor(price)


@register.filter
def rupee(price):
    return f'₹ {price}'


@register.simple_tag
def is_enrolled(user, course):
    try:
        UserCourse.objects.get(user=user, course=course)
        return True
    except:
        return False

# def is_preview(video):
#     return video.is