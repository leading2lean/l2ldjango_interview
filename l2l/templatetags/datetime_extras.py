from django import template
import datetime
register = template.Library()


@register.filter(is_safe=True, expects_localtime=True)
def to_numerical_datetime(date_time):

    def convert_to_datetime_from_string():
        nonlocal date_time
        date_time = datetime.datetime.strptime(
            date_time, "%Y-%m-%dT%H:%M:%S")

    if type(date_time) is str:
        convert_to_datetime_from_string()

    return(date_time.strftime("%Y-%m-%d %H:%M:%S"))
