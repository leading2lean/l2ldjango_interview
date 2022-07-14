from datetime import datetime
from . import register

@register.filter(name='l2l_dt')
def l2l_dt(value):
    '''
    Takes a date in format: "%Y-%m-%dT%H:%M:%S"
    Returns format: "%Y-%m-%d %H:%M:%S".
    '''
    if isinstance(value, str):
        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
    return value.strftime('%Y-%m-%d %H:%M:%S')
