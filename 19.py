def cast_out_nines(a, b, r):
    def dr(x):
        xx=0
        for i in x:
            xx += int(i)
        if xx >=10:
            return dr(list(str(xx)))
        return xx
    a1 = list(str(a))
    b1 = list(str(b))
    r1 = list(str(r))
    ax = dr(a1)
    bx = dr(b1)
    rx = dr(r1)
    zx = dr(list(str(ax*bx)))

    if a*b == r and zx == rx:
        return str(ax)+","+str(bx)+","+str(rx)+","+str(zx)+" = Correct!"
    elif zx == rx:
        return str(ax)+","+str(bx)+","+str(rx)+","+str(zx)+" = False positive!"
    else:
        return str(ax)+","+str(bx)+","+str(rx)+","+str(zx)+" = Wrong!"


print(cast_out_nines(467,78,36426))