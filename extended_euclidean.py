from prettytable import PrettyTable


def extended_euclidean(a, b):
    ptb = PrettyTable()
    r2, r1 = sorted([a, b])
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    ptb.field_names = ['q', 'r1', 'r2', 'r', 's1', 's2', 's', 't1', 't2', 't']
    while (r2 > 0):
        q = r1 // r2
        r = r1 % r2
        s = s1 - q * s2
        t = t1 - q * t2
        ptb.add_row([q, r1, r2, r, s1, s2, s, t1, t2, t])
        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t
    ptb.add_row(['-', r1, r2, '-', s1, s2, '-', t1, t2, '-'])
    return [r1, s1, t1, ptb]
