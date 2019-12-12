def digital_vowel_ban(n, ban):
    x = list(str(n))
    z = []
    wynik = ""
    y = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in x:
        z.append(y[int(i)])

    for e in z:
        if ban not in e:
            wynik+=str(y.index(e))
    if wynik == "":
        return "Banned Number"
    else:
        return int(wynik)




digital_vowel_ban(14266330, "e")
