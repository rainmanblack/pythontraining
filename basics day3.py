l = []
l = [1, 4, 9, 10, 23]

print(l[1:3])
print(l[3:5])

l.append(90)

print(l)

print(sum(l)/len(l))

del l[1:3]

print(l)

#####

instuff= input()
lst = instuff.split(',')
print(lst)
lst.sort()

print(lst)

######

instuff= input()
print(instuff.upper())

#####

ages = {
"Peter": 10,
"Isabel": 11,
"Anna": 9,
"Thomas": 10,
"Bob": 10,
"Joseph": 11,
"Maria": 12,
"Gabriel": 10,
}

print(len(ages))

def avg(valstuff):

    tot = 0

    for age in valstuff.values():
        tot=tot+age

    print(tot/len(valstuff))

avg(ages)

def bigest(valstuff):

    maxi = 0

    for item in valstuff.items():
        if ager.value() > maxi:
            oldest=item.key()
