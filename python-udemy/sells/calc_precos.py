from sells.format import price


def increase(value, percentage, formatar=False):
    if formatar:
        return price.real(value + (value * (percentage/100)))
    else:
        value + (value * (percentage / 100))

def decrease(value, percentage, formatar=False):
    if formatar:
        return price.real(value - (value * (percentage / 100)))
    else:
        return value - (value * (percentage / 100))
