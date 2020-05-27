#character frequency
a=str(input("Enter the word: "))

def cf(a):
    dict = {}
    for n in a:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(cf(a))
