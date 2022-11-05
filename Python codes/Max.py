# Max
# Just... calculate the maximum (not at all the max built-in function, not at all)

def Max(**_l) :
    l = tuple(_l)

    if len(l) == 0: raise Exception("Argument must not be empty")

    _max = l[0]
    for note in l :
        if note > _max :
            _max = note
    return _max