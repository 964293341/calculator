def ya(n):
    '''(int)return n!'''
    L = list(range(n + 1))
    m = 1
    for x in L:
        if x == L[0]:
            continue
        else:
            m = m * x
    return m
###
def e(n):
    '''(int>0)求e的值evaluate e, and n is the precision'''
    L = list(range(n + 1))
    e = 0
    for x in L:
        e = e + (1 / ya(x))
    return e

