from django.template.defaulttags import register


@register.filter(name='lookup')
def lookup(value, arg):

    return value[arg]


@register.filter(name='mf')
def in_category(things, month,center):
    return things.filter(month=month,center=center)