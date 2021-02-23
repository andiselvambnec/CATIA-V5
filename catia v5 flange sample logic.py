'''
#D2 = float(input("flange dia D2="))
D2 = (D2 / 2)

#tf = float(input("thickness of flange tf="))

#D0 = float(input("diameter of hub D0="))
D0 = (D0 / 2)

#L0 = float(input("length of hub L0="))

#D1 = float(input("pitch of flange bolt D1"))
D1 = (D1 / 2)

#d0 = float(input("diameter of bolt d0="))

#n0 = int(input("no of bolt="))
a0 =(360 / n0)

#ds = float(input("shaft dia ds="))
ds = (ds / 2)

L1 = float(input("length of shaft L1 ="))
'''

p = float(input("enter a power="))
n = float(input("enter speed="))
t = float(input("enter shear stress"))

mt = ((p * 60)/(2 * 3.14 * n))
mt = mt * 1000

ds = (((mt * 16)/(3.14 * t)) ** (1/3))
ds = round(ds)

D0 = (2 * ds)   #dia of hub

D1 = (3 * ds)    # pitch dia of flange bolt

D2 = (4 * ds)   #outside dia of flange

L0 = (1.5 * ds) # length of hub

tf = (0.5 * ds)  #thickness of flange

L1 = (3 * ds)  ########lenth of shaft

if(ds < 56):
    n0 = 4
elif(55 < ds < 151):
    n0 = 6
elif(150 < ds < 231):
    n0 = 8
elif(230 < ds < 391):
    n0 = 10
else:
    n0 = 12


d0 = (((mt * 4 * 2)/(3.14 * t * n0 * D1)) ** (1/2))
d0 = round(d0)


print(ds)
print(D0)
print(D1)
print(D2)
print(L0)
print(tf)
print(L1)
print(n0)
print(d0)



