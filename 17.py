def pie_chart(data):
    suma = 0
    x=0
    wynik = {}
    for i in data:
        suma+=data[i]
        x+=1
    for x in data:
        wynik[x]=(data[x]/suma)*360
        wynik[x] = round(wynik[x],1)
    return wynik



pie_chart({ "a": 30, "b": 15, "c": 55 })
