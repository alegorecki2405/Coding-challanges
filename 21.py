# You are given three inputs: a string, one letter, and a second letter.
# Write a function that returns True if every instance of the first letter occurs before
# every instance of the second letter.


def first_before_second(s, first, second):
    lista = list(s)
    jeden = []
    dwa = []

    for i in range(0,len(s)):
        if lista[i] == first:
            jeden.append(i)
        elif lista[i] == second:
            dwa.append(i)
    print(jeden)
    print(dwa)
    for x in range(0,len(jeden)):
        for y in range(0,len(dwa)):
            if jeden[x] > dwa[y]:
                return False
    return True
print(first_before_second("happy birthday", "a", "y"))
