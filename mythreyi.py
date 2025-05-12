import pandas as abc
v=[1,4,6,7]
sahana=abc.Series(v)
print(sahana)

b=[5,4,2,9,8]
gs=abc.Series(b)
print(gs[4])

g=[3,5,8]
rat=abc.Series(g,index=["r","a","t"])
print(rat)


g=[3,5,8]
orange=abc.Series(g,index=["r","a","t"])
print(orange["r"])

d={"r":2,"a":5,"t":7}
polar=abc.Series(d)
print(polar)




