def fret_freq(g_str, fret):
    x = {"1":329.63,"2":246.94,"3":196.00,"4":146.83,"5":110.00, "6":82.41}
    out = x[str(g_str)] * 2**(fret/12)
    return round(out,2)

print(fret_freq(4, 6))
