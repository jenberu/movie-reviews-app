# blog/templatetags/profile_tags.py
from django import template
from ..models import UserProfile

register = template.Library()

@register.simple_tag(takes_context=True)
def get_profile_image(context):
    request = context['request']
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            return profile.image.url
        except UserProfile.DoesNotExist:
            return None
    return None

