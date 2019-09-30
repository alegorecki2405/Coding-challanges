
lst = [1,2,3,4,5]
dl = len(lst)

def ile_mozliwosci(dl):
    if dl == 1:
        return 1
    elif dl == 2:
        return 2
    return ile_mozliwosci(dl-1) + ile_mozliwosci(dl-2)

def poprawki(lst,dl):
    ileod = 0
    for i in range(0,dl-1):
        if lst[i]*10 + lst[i+1] > 24:
            ileod+=1
    return ileod





print(ile_mozliwosci(dl)-poprawki(lst,dl))



