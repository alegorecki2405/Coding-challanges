
#Find the index of a string within a hex encoded string.

#You will be given a string which needs to be found in another string which has previously
#been translated into hex. You will need to return the
#first index of the needle within the hex encoded string.



def first_index(hex_txt, needle):
    x = hex_txt.split()
    y  = ""
    for i in x:
        i = int(i, 16)
        y+=chr(i)
    return y.find(needle)








first_index("47 bf 6f 64 62 79 65 20 77 6f 72 6c 64", "world")

