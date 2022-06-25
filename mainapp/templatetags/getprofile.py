from django import template
from mainapp.models import profile

register = template.Library()

@register.filter
def get_grade(username) :
    if username != '' :
        p = profile.objects.get(username=username)
        return str(p.grade)
    return None

@register.filter
def get_photo(username) :
    if username != '' :
        p = profile.objects.get(username=username)
        if p.photo:
            return p.photo.url
        return '/static/images/empty.png'
    return '/static/images/empty.png'

@register.inclusion_tag('slideshow.html')
def slideshow():
    return


@register.simple_tag 
def qlinks():
    a = [["/asdfextra","Music"],["/asdfevents","Exhibitions"], ["/asdfevents","Trips"], ["/asdfextra","Student Teaching Assistant"], ]
    return a

@register.simple_tag
def announcements():
    return ["Summer holidays are till 30th of June. Students have to come to school in 1st of July", "July monthly exam datesheet we be shared soon."]