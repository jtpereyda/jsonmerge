def overwrite(merger, base, head, _schema):
    return head

def version(merger, base, head, _schema):
    if base is None:
        base = []
    else:
        base = list(base)

    base.append(merger.add_meta(head))
    return base

def version_last(merger, base, head, _schema):
    return merger.add_meta(head)

def append(merger, base, head, _schema):
    if base is None:
        base = []
    else:
        base = list(base)

    base += head
    return base

def object_merge(merger, base, head, _schema):
    if base is None:
        base = {}
    else:
        base = dict(base)

    for k, v in head.iteritems():

        p = _schema.get('properties')
        if p is not None:
            s = p.get(k)
        else:
            s = None

        base[k] = merger.descend(base.get(k), v, s)

    return base
