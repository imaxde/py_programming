def gcd_bezu(a, b):
    r = (a, b)
    s = (1, 0)
    t = (0, 1)
    while r[1] > 0:
        q = r[0] // r[1]
        r = r[1], r[0] - q * r[1]
        s = s[1], s[0] - q * s[1]
        t = t[1], t[0] - q * t[1]
    print(r, s, t)
    return r[0], s[1], t[1]

print(gcd_bezu(240, 46))


