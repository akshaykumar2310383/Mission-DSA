def toys(w):  
    if not w:
        return 0
    w.sort()
    containers = 1  
    max_allowed_weight = w[0] + 4
    for i in range(1, len(w)):
        if w[i] > max_allowed_weight:
            containers += 1
            max_allowed_weight = w[i] + 4
    return containers
