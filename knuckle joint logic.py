
p=int(input("power transmitted="))
t=int(input("tensile stress="))

d=((4*p)/(3.14*t))**(1/2)    #dia of rod

print(round(d))

d1=(d)                       #dia of pin

print(round(d1))

d2=(2*d)               #outer dia of the eye

print(round(d2))

d3=(1.5*d)           #dia of pin head

print(round(d3))

t=(1.25*d)           #thickness of eye

print(round(t))

t1=(0.75*d)          #thickness of fork

print(round(t1))

t2=(0.5*d)            #thickness of pin head

print(round(t2))

