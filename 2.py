#9a d2 c6 d0 c2 8b 05 14 98 ea c4 d2 14 9e d8 ca 14 82 14 9e d8 c2 14 9a d2 c6 d0 c2 8b 05 c2
lst2 = []
lst = ["9a","d2","c6","d0","c2","8b","05","14","98","ea","c4","d2","14","9e","d8","ca","14","82","14","9e","d8","c2","14","9a","d2","c6","d0","c2","8b","05","c2"]
for i in lst:
    x = bin(int(i,16))
    x= x[2:]
    lst2.append(x)

print(lst2)




