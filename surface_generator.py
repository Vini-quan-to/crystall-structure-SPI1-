# =================================================================
#    surface lattice normal to the given miller indices
# =================================================================

import numpy as np
import matplotlib.pyplot as mp
import random as r

name=input("Enter your good name pls:")

print("HELLO wlecome to the plane perpendicular to {100}")

# input for the  surface size and the crystall size

a=float(input("enter the lattice constant a :"))
n1=int(input("enter the number of lattice points in  the x direction:"))
n2=int(input("enter the number of lattice points in  the y direction:"))    
n3=int(input("enter the number of lattice points in  the z direction:")) 

basis=[]  
cl=[]
rlv=[]
slv=[]
spv=[]
spv_x=[]
spv_y=[]
spv_z=[]
basis1_x=[]
basis1_y=[]
basis1_z=[]


# this part is to choose type of latttices conventioanl or primitive
print("""=========================================================================================================""")
print(" NOTE:  For The  conventional lattice enter (con) and for the particular or custom lattice enter (cus)")
print("""=========================================================================================================""")


custom_conventional = input(" Enter the type of lattice you want conventional or custom:")

if custom_conventional=="con":
    a1=np.array([1,0,0])
    a2=np.array([0,1,0])
    a3=np.array([0,0,1])
    cl.extend([a1,a2,a3])
else:
    for i in range(3):
        ax=int(input("enter the x-direction of your lattice vector:  "))
        ay=int(input("enter the y-direction of your lattice vector:  "))
        az=int(input("enter the z-direction of your lattice vector:  "))
        a1=np.array([ax,ay,az])
        print(f'your given lattice vector {a1} is stored in the system')
        cl.append(a1)

print(f" This is the lattice vector choosen for the crystall {cl}")

print("""=============================================================================================================================================""")
print("NOTE: for the simple cubic enter(SC ) ,for body centered enter (BCC) , Face centered enter (FCC) and for something else enter (0) ")
print("""=============================================================================================================================================""")



SC_BCC_FCC_O=input("Enter the type of cell you wnat in the lattice based on the note just given above :")
if SC_BCC_FCC_O=="SC":
    b1=np.array([0,0,0])
    basis.append(b1)

elif SC_BCC_FCC_O=="BCC":
    b1=np.array([0,0,0])
    b2=np.array([.5,.5,.5])
    basis.extend([b1 ,b2])

elif SC_BCC_FCC_O=="FCC":
    b1=np.array([0,0,0])
    b2=np.array([0.5,0.5,0])
    b3=np.array([0.5,0,0.5])
    b4=np.array([0,0.5,0.5])
    basis.extend([b1,b2,b3,b4])

elif SC_BCC_FCC_O=="0":
    number_basis=int(input("enter the number of basis atom in the crystall:"))
    for i in range(number_basis):
        bx=float(input("enter the x-direction of the basis vector:"))
        by=float(input("enter the y-direction of the  basis vector:"))
        bz=float(input("enter the z-direction of  the basis vector:"))
        b1=np.array([bx,by,bz])
        print(f'your given basis {b1} is stored in the system')
        basis.append(b1)

print(f' These are all the basis given as input {basis}')



# here we are try to form reciprocal lattice vector b1 b2 b3 and then stored in reciprocal lattice vector(rlv)

a1=cl[0]
a2=cl[1]
a3=cl[2]
z=np.cross(a2, a3)
v=np.dot(a1, z)
b1=(2*np.pi*z)/v
b2=(2*np.pi*(np.cross(a3,a1)))/v
b3=(2*np.pi*(np.cross(a1,a2)))/v
                                                                                                          
rlv.extend([b1 ,b2 ,b3])

print(f"  this is your reciprocal lattice vector {rlv}")



# INPUT FOR THE MILLER INDICES OF THE PLANES IN THE CRYSTALL

h=int(input("enter the miller  index  h :"))
k=int(input("enter the miller  index  k :"))
l=int(input("enter the miller  index  l :"))
print(f' The given miller indices are {h} {k} {l} and the plane is {h} {k} {l}')

g=(h*b1 + k*b2 + l*b3)                                                         # reciprocal vector 

print(f"  this is your  normal  vector {g}")

# here we are trying to  all possible ventor perpendicular to g and then the one have least magnitude

for n in range(-n1, n1+1):
    for m in range(-n2, n2+1):
        for p in range(-n3, n3+1):

            r=(n*cl[0] + m*cl[1] + p*cl[2])
            x = np.dot(g, r)

            if np.isclose(x,0):
                 ui = n*a1 + m*a2 + p*a3

                 if np.linalg.norm(ui) > 1e-8:
                    slv.append(ui)
                
                
print( f"  this are the  {slv}")


slv.sort(key=np.linalg.norm)

u = slv[0]                                           # a vector in the surface  perpendicular to g
normal = g / np.linalg.norm(g)


for x in slv[1:]:
    cross = np.cross(u, x)
    if np.linalg.norm(np.cross(u,x)) > 1e-8:
        v = x
        

print(f" this my v vector {v}")

d = 2*np.pi / np.linalg.norm(g)                       # interplaner distance between the plans 

number_layers=int(input("enter the number of layer you want :"))

# this part is to generate all the points in the surface 
for j in range(len(basis)):
    for n in range(n1):
        for m in range(n2):
            for p in range(number_layers):

                s=n*u+ m*v + p*d*normal
                spv.append(s)
                spv_x.append(s[0])
                spv_y.append(s[1])
                spv_z.append(s[2])

                sb= s + basis[j]

                basis1_x.append[sb[0]]
                basis1_y.append[sb[1]]
                basis1_z.append[sb[2]]

print(f" hello {spv}")

# this part is the plot

fig = mp.figure(figsize=(6,5))

ax = fig.add_subplot(121, projection="3d")

ax.scatter(spv_x, spv_y, spv_z, s=80,color="red",label="surface lattice points")
ax.scatter(basis1_x,basis1_y,basis1_z, s=70, color="red",label="atoms")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()

ax.set_title(f"({h}{k}{l}) surface view")

mp.show()




