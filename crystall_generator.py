# =================================================================
#    lets start with genrealising the code for any lattice type
# =================================================================

import numpy as np
import matplotlib.pyplot as mp


name=input("enter you good name pls:")
print(f"welcome {name} generate your own world of crystalls")
print("NOTE- THIS TO INFORM  YOU THAT FOR OUR SIMPLICITY WE HAVE WRITTEN X Y Z  FOR  THE DIRECTION BUT BASED ON  THE INPUT ANY LATTICE WITH THE BASIS CAN BE CREATED ")
basis=[]
cl=[]
lp=[]
rlv=[]
rlp=[]
basis1_x=[]
basis1_y=[]
basis1_z=[]

basis2_x=[]
basis2_y=[]
basis2_z=[]

# INPUT FOR THE LATTICE CONSTANT AND THE NUMBER OF LATTICE POINTS IN THE X Y Z DIRECTION
a=float(input("enter the lattice constant a :"))
n1=int(input("enter the number of lattice points in  the x direction:"))
n2=int(input("enter the number of lattice points in  the y direction:"))    
n3=int(input("enter the number of lattice points in  the z direction:")) 
print("Enter your lattice vector ")

# INPUT FOR THE LATTICE VECTOR IN THE X Y Z DIRECTION
for i in range(3):
    ax=int(input("enter the x-direction of your lattice vector:  "))
    ay=int(input("enter the y-direction of your lattice vector:  "))
    az=int(input("enter the z-direction of your lattice vector:  "))
    a1=np.array([ax,ay,az])
    print(f'your given lattice vector {a1} is stored in the system')
    cl.append(a1)
print(f' These are all the lattice vector given as input {cl}')

# INPUT FOR THE BASIS VECTOR IN THE X Y Z DIRECTION

number_basis=int(input("enter the number of basis atom in the crystall:"))
for i in range(number_basis):
    bx=float(input("enter the x-direction of the basis vector:"))
    by=float(input("enter the y-direction of the  basis vector:"))
    bz=float(input("enter the z-direction of  the basis vector:"))
    b1=np.array([bx,by,bz])
    print(f'your given basis {b1} is stored in the system')
    basis.append(b1)
print(f' These are all the basis given as input {basis}')

# INPUT FOR THE MILLER INDICES OF THE PLANES IN THE CRYSTALL

h=int(input("enter the miller  index  h :"))
k=int(input("enter the miller  index  k :"))
l=int(input("enter the miller  index  l :"))
print(f' The given miller indices are {h} {k} {l} and the plane is {h} {k} {l}')


# USE THE FORMULA TO CALCULATE THE RECIPROCAL LATTICE VECTOR

a1=cl[0]
a2=cl[1]
a3=cl[2]
z=np.cross(a2, a3)
v=np.dot(a1, z)
b1=(2*np.pi*z)/v
b2=(2*np.pi*(np.cross(a1,a3)))/v
b3=(2*np.pi*(np.cross(a1,a2)))/v

rlv.append(b1)
rlv.append(b2)
rlv.append(b3)
print(f" this are  your reciprocal lattice vector formed from the  given primitibe attice vector {rlv}")

# Condtion used for  the lattice point generation  with the given basis as well

for n in range(n1):
    for m in range(n2):
        for p in range(n3):
                    
            r=(n*cl[0] + m*cl[1] + p*cl[2])
            lp.append(r)
        
            for j in range(number_basis):
                    if j==0:
                         
                        r1=(n*cl[0] + m*cl[1] + p*cl[2]) + basis[j]
                        basis1_x.append(r1[0])
                        basis1_y.append(r1[1])
                        basis1_z.append(r1[2])
                    else:
                         r1=(n*cl[0] + m*cl[1] + p*cl[2]) + basis[j]
                         basis2_x.append(r1[0])
                         basis2_y.append(r1[1])
                         basis2_z.append(r1[2])
print(lp)


from mpl_toolkits.mplot3d import Axes3D
fig = mp.figure(figsize=(8,8))

s=fig.add_subplot(111, projection='3d')
s.scatter(basis1_x,basis1_y,basis1_z, color="blue",s=100)      # this for  the lattice point with basis [0 0 0]
s.scatter(basis2_x,basis2_y,basis2_z,color="red",s=50)         # this for  the lattice point  for  thr rest of the basis 
mp.show()






