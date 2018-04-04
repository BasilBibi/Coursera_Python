def computepay(h, r):
    overtime = compute_overtime(h, r)
    normal = compute_normalpay(h, r)
    return normal + overtime


def compute_overtime(h, r):
    if (h > 40):
        return r * 1.5 * (h - 40)
    else:
        return 0


def compute_normalpay(h, r):
    if( h <= 40 ):
        return h * r
    else:
        return 40 * r
