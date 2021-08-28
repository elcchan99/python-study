def field_map(dictseq, name, func):
    for d in dictseq:
        d[name] = func(d[name])
    yield d
