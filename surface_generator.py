import numpy as np
import matplotlib as mp



a=float(input("enter the lattice constant a :"))
n1=int(input("enter the number of lattice points in  the x direction:"))
n2=int(input("enter the number of lattice points in  the y direction:"))    
n3=int(input("enter the number of lattice points in  the z direction:")) 


cl=[]
rlv=[]
spv=[]


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

a1=cl[0]
a2=cl[1]
a3=cl[2]
z=np.cross(a2, a3)
v=np.dot(a1, z)
b1=(2*np.pi*z)/v
b2=(2*np.pi*(np.cross(a3,a1)))/v
b3=(2*np.pi*(np.cross(a1,a2)))/v
                                                                                                           #  r=ms1​+ns2​+pdn^
rlv.extend([b1 ,b2 ,b3])

# INPUT FOR THE MILLER INDICES OF THE PLANES IN THE CRYSTALL

h=int(input("enter the miller  index  h :"))
k=int(input("enter the miller  index  k :"))
l=int(input("enter the miller  index  l :"))
print(f' The given miller indices are {h} {k} {l} and the plane is {h} {k} {l}')

g=(h*b1 + k*b2 + l*b3)

for n in range(n1):
    for m in range(n2):
        for p in range(n3):

            r=(n*cl[0] + m*cl[1] + p*cl[2])
            x=np.dot(g,r)
            if x==0:
                sp=np.array([n,m,p])
                spv.append(sp)
print( f"  this are the  {spv}")