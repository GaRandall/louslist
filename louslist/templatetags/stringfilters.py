from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def time_beautifier(value):
    v = value
    hour_string = ""
    minute_string = ""
    dot_count = 0
    for c in value:
        if c == '.':
            if dot_count == 0:
                dot_count += 1
            if dot_count == 1:
                break
        else:
            if dot_count == 0:
                hour_string += c
            if dot_count == 1:
                minute_string += c
    hour = int(hour_string)
    if hour >= 12:
        time_string = str(hour - 12) + minute_string + "PM"
    else:
        time_string = str(hour) + minute_string + "AM"
    return time_string
