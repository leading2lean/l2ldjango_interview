from datetime import datetime
from . import register
from typing import (
    Union
)

@register.filter(name='l2l_dt_format')
def l2l_dt_format(value: Union[datetime, str]) -> str:
    if isinstance(value, str):
        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
    return value.strftime('%Y-%m-%d %H:%M:%S')
