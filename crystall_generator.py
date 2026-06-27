import numpy as np
import matplotlib.pyplot as mp

# # ================================================================
# #       lets start with the lattice Generator
# # ================================================================

# name=input("enter your name :")
# print(f" hello  {name} welcome to the lattice generator  pls enter the parameters of the lattice")
# a=float(input("enter the lattice constant a :"))
# n1=int(input("enter the number of lattice points in  the x direction:"))
# n2=int(input("enter the number of lattice points in  the y direction:"))    
# n3=int(input("enter the number of lattice points in  the z direction:")) 

# def SCC(a,n1,n2,n3):
#     a1 =a*np.array([1,0,0])
#     a2 = a*np.array([0,1,0])
#     a3 = a*np.array([0,0,1])
#     x_points = []
#     y_points = []
#     z_points = []

#     for n in range(n1):
#         for m in range(n2):
#             for p in  range(n3):
                 
#                  r = n*a1 + m*a2 + p*a3
#                  x_points.append(r[0])
#                  y_points.append(r[1])
#                  z_points.append(r[2])
#     print(x_points)
#     print(y_points)
#     print(z_points)
#     from mpl_toolkits.mplot3d import Axes3D
#     fig = mp.figure(figsize=(8,8))

#     sumo=fig.add_subplot(111, projection='3d')
#     sumo.scatter(x_points, y_points, z_points, color='blue' , label="SCC lattice")
#     sumo.set_xlabel('X axis')
#     sumo.set_ylabel('Y axis')
#     sumo.set_zlabel('Z axis')
#     sumo.set_title("SCC lattice")
#     ax=mp.gca()
#     ax.set_facecolor("lightyellow")
#     sumo.legend()
#     mp.show()    
             
# def BCC(a,n1,n2,n3):
#     a1 =a*np.array([1,1,-1])/2
#     a2 = a*np.array([1,-1,1])/2
#     a3 = a*np.array([-1,1,1])/2
#     x_points = []
#     y_points = []
#     z_points = []

#     for n in range(n1):
#         for m in range(n2):
#             for p in  range(n3):
                 
#                  r = n*a1 + m*a2 + p*a3
#                  x_points.append(r[0])
#                  y_points.append(r[1])
#                  z_points.append(r[2])
#     print(x_points)
#     print(y_points)
#     print(z_points)
#     from mpl_toolkits.mplot3d import Axes3D
#     fig = mp.figure(figsize=(8,8))

#     sumo=fig.add_subplot(111, projection='3d')
#     sumo.scatter(x_points, y_points, z_points, color='blue' , label="BCC lattice")  
#     sumo.set_xlabel('X axis')
#     sumo.set_ylabel('Y axis')
#     sumo.set_zlabel('Z axis')
#     sumo.set_title("BCC lattice")
#     ax=mp.gca()
#     ax.set_facecolor("lightyellow")
#     sumo.legend()
#     mp.show()

# def FCC(a,n1,n2,n3):
#     a1 =a*np.array([1/2,1/2,0])
#     a2 = a*np.array([0,1/2,1/2])
#     a3 = a*np.array([1/2,0,1/2])
#     x_points = []
#     y_points = []
#     z_points = []

#     for n in range(n1):
#         for m in range(n2):
#             for p in  range(n3):
                 
#                  r = n*a1 + m*a2 + p*a3
#                  x_points.append(r[0])
#                  y_points.append(r[1])
#                  z_points.append(r[2])
#     print(x_points)
#     print(y_points)
#     print(z_points)
#     from mpl_toolkits.mplot3d import Axes3D
#     fig = mp.figure(figsize=(8,8))

#     sumo=fig.add_subplot(111, projection='3d')
#     sumo.scatter(x_points, y_points, z_points, color='blue' , label="FCC lattice")  
#     sumo.set_xlabel('X axis')
#     sumo.set_ylabel('Y axis')
#     sumo.set_zlabel('Z axis')
#     sumo.set_title("FCC lattice")
#     ax=mp.gca()
#     ax.set_facecolor("lightyellow")
#     sumo.legend()
#     mp.show()

# type= input("enter the type of lattice you want to generate (SCC, BCC, FCC):")
# if type=="SCC":
#     SCC(a,n1,n2,n3)
# elif type=="BCC":
#     BCC(a,n1,n2,n3)
# elif type=="FCC":
#     FCC(a,n1,n2,n3)
# elif type=="all":
#     SCC(a,n1,n2,n3)
#     BCC(a,n1,n2,n3)
#     FCC(a,n1,n2,n3) 


# print("thank you for using the lattice generator  in PSI1")
# print(" I have made changes from the phone ")


# =================================================================
#    lets start with genrealising the code for any lattice type
# =================================================================
name=input("enter you good name pls:")
print(f"welcome {name} generate your own world of crystalls")
print("NOTE- THIS TO INFORM  YOU THAT FOR OUR SIMPLICITY WE HAVE WRITTEN X Y Z  FOR  THE DIRECTION BUT BASED ON  THE INPUT ANY LATTICE WITH THE BASIS CAN BE CREATED ")
basis=[]
cl=[]
lp=[]
basis1_x=[]
basis1_y=[]
basis1_z=[]

basis2_x=[]
basis2_y=[]
basis2_z=[]
a=float(input("enter the lattice constant a :"))
n1=int(input("enter the number of lattice points in  the x direction:"))
n2=int(input("enter the number of lattice points in  the y direction:"))    
n3=int(input("enter the number of lattice points in  the z direction:")) 
print("Enter your lattice vector ")
for i in range(3):
    ax=int(input("enter the x-direction of your lattice vector:  "))
    ay=int(input("enter the y-direction of your lattice vector:  "))
    az=int(input("enter the z-direction of your lattice vector:  "))
    a1=np.array([ax,ay,az])
    print(f'your given lattice vector {a1} is stored in the system')
    cl.append(a1)
print(f' These are all the lattice vector given as input {cl}')

number_basis=int(input("enter the number of basis atom in the crystall:"))
for i in range(number_basis):
    bx=float(input("enter the x-direction of the basis vector:"))
    by=float(input("enter the y-direction of the  basis vector:"))
    bz=float(input("enter the z-direction of  the basis vector:"))
    b1=np.array([bx,by,bz])
    print(f'your given basis {b1} is stored in the system')
    basis.append(b1)
print(f' These are all the basis given as input {basis}')



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
fig = mp.figure(figsize=(6,6))

s=fig.add_subplot(111, projection='3d')
s.scatter(basis1_x,basis1_y,basis1_z, color="blue", marker="o" ,markersize=10 ,markercolor="red")
s.scatter(basis2_x,basis2_y,basis2_z,color="red", marker="o" ,markersize=10 ,markercolor="blue")
mp.show()


print("updates are pending to come so lets wait")
