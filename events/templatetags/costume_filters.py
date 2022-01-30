from django.template.defaulttags import register


@register.filter(name='lookup')
def lookup(value, arg):

    return value[arg]


@register.filter(name='mf')
def in_category(things, month,center):
    return things.filter(month=month,center=center)

@register.filter(name='to_int')
def in_category(value):
    if isinstance(value,str):
        return value
    if str(value) == 'nan':
        value=0
    return int(value)
