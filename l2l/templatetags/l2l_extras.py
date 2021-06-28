from django import template
from datetime import datetime

register = template.Library()


DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
ISO_FORMAT = '%Y-%m-%dT%H:%M:%S'


def l2l_dt(value):
    if type(value) == datetime:
        return value.strftime(DATE_FORMAT)
    else:
        return (datetime.strptime(value, ISO_FORMAT)).strftime(DATE_FORMAT)




register.filter('l2l_dt', l2l_dt)