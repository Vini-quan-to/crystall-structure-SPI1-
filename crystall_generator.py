import numpy as np
import matplotlib.pyplot as mp

# ================================================================
#       lets start with the lattice Generator
# ================================================================

name=input("enter your name :")
print(f" hello  {name} welcome to the lattice generator  pls enter the parameters of the lattice")
a=float(input("enter the lattice constant a :"))
n1=int(input("enter the number of lattice points in  the x direction:"))
n2=int(input("enter the number of lattice points in  the y direction:"))    
n3=int(input("enter the number of lattice points in  the z direction:")) 

def SCC(a,n1,n2,n3):
    a1 =a*np.array([1,0,0])
    a2 = a*np.array([0,1,0])
    a3 = a*np.array([0,0,1])
    x_points = []
    y_points = []
    z_points = []

    for n in range(n1):
        for m in range(n2):
            for p in  range(n3):
                 
                 r = n*a1 + m*a2 + p*a3
                 x_points.append(r[0])
                 y_points.append(r[1])
                 z_points.append(r[2])
    print(x_points)
    print(y_points)
    print(z_points)
    from mpl_toolkits.mplot3d import Axes3D
    fig = mp.figure(figsize=(8,8))

    sumo=fig.add_subplot(111, projection='3d')
    sumo.scatter(x_points, y_points, z_points, color='blue' , label="SCC lattice")
    sumo.set_xlabel('X axis')
    sumo.set_ylabel('Y axis')
    sumo.set_zlabel('Z axis')
    sumo.set_title("SCC lattice")
    ax=mp.gca()
    ax.set_facecolor("lightyellow")
    sumo.legend()
    mp.show()
             
def BCC(a,n1,n2,n3):
    a1 =a*np.array([1,1,-1])/2
    a2 = a*np.array([1,-1,1])/2
    a3 = a*np.array([-1,1,1])/2
    x_points = []
    y_points = []
    z_points = []

    for n in range(n1):
        for m in range(n2):
            for p in  range(n3):
                 
                 r = n*a1 + m*a2 + p*a3
                 x_points.append(r[0])
                 y_points.append(r[1])
                 z_points.append(r[2])
    print(x_points)
    print(y_points)
    print(z_points)
    from mpl_toolkits.mplot3d import Axes3D
    fig = mp.figure(figsize=(8,8))

    sumo=fig.add_subplot(111, projection='3d')
    sumo.scatter(x_points, y_points, z_points, color='blue' , label="BCC lattice")  
    sumo.set_xlabel('X axis')
    sumo.set_ylabel('Y axis')
    sumo.set_zlabel('Z axis')
    sumo.set_title("BCC lattice")
    ax=mp.gca()
    ax.set_facecolor("lightyellow")
    sumo.legend()
    mp.show()

def FCC(a,n1,n2,n3):
    a1 =a*np.array([1/2,1/2,0])
    a2 = a*np.array([0,1/2,1/2])
    a3 = a*np.array([1/2,0,1/2])
    x_points = []
    y_points = []
    z_points = []

    for n in range(n1):
        for m in range(n2):
            for p in  range(n3):
                 
                 r = n*a1 + m*a2 + p*a3
                 x_points.append(r[0])
                 y_points.append(r[1])
                 z_points.append(r[2])
    print(x_points)
    print(y_points)
    print(z_points)
    from mpl_toolkits.mplot3d import Axes3D
    fig = mp.figure(figsize=(8,8))

    sumo=fig.add_subplot(111, projection='3d')
    sumo.scatter(x_points, y_points, z_points, color='blue' , label="FCC lattice")  
    sumo.set_xlabel('X axis')
    sumo.set_ylabel('Y axis')
    sumo.set_zlabel('Z axis')
    sumo.set_title("FCC lattice")
    ax=mp.gca()
    ax.set_facecolor("lightyellow")
    sumo.legend()
    mp.show()

type= input("enter the type of lattice you want to generate (SCC, BCC, FCC):")
if type=="SCC":
    SCC(a,n1,n2,n3)
elif type=="BCC":
    BCC(a,n1,n2,n3)
elif type=="FCC":
    FCC(a,n1,n2,n3)
elif type=="all":
    SCC(a,n1,n2,n3)
    BCC(a,n1,n2,n3)
    FCC(a,n1,n2,n3) 


print("thank you for using the lattice generator  in PSI1")