test_dic={
    "Education":2,
    "is":2,
    "the":2,
    "weapon":2,
    "which":2,
    "we":2,
    "can":2,
    "use":2,
    "to":2,
    "change":2,
    "the":2,
    "world":1
}

print("the dictionary is:" +str(test_dic))

k=2
res=0

for key in test_dic:
    if test_dic[key]==k:
        res=res+1

        print(res)