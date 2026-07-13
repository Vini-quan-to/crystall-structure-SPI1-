# =================================================================
#    lets start with genrealising the code for any lattice type
# =================================================================

from matplotlib.pylab import normal
import numpy as np
import matplotlib.pyplot as mp


name=input("enter you good name pls:")
print(f"welcome {name} generate your own world of crystalls")
print("NOTE- THIS TO INFORM  YOU THAT FOR OUR SIMPLICITY WE HAVE WRITTEN X Y Z  FOR  THE DIRECTION BUT BASED ON  THE INPUT ANY LATTICE WITH THE BASIS CAN BE CREATED ")
basis=[]
cl=[]                                         #crystall lattice vector
lp=[]                                         # lattice points 
rlv=[]                                        # relative lattice vector
rlp=[]                                        # reciprocal lattice point
basis1_x=[]
basis1_y=[]
basis1_z=[]

lattice_x=[]
lattice_y=[] 
lattice_z=[]
layers={}      # constant for the atom belonging the same layer


# INPUT FOR THE LATTICE CONSTANT AND THE NUMBER OF LATTICE POINTS IN THE X Y Z DIRECTION
a=float(input("enter the lattice constant a :"))
n1=int(input("enter the number of lattice points in  the x direction:"))
n2=int(input("enter the number of lattice points in  the y direction:"))    
n3=int(input("enter the number of lattice points in  the z direction:")) 
print("Enter your lattice vector ")

# INPUT FOR THE LATTICE VECTOR IN THE X Y Z DIRECTION
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
        

print(f' These are all the lattice vector given as input {cl}')

print("""=========================================================================================================""")
print("NOTE: for the simple cubic enter(SC ) ,for body centered enter (BCC) , Face centered enter (FCC) and for something else enter (0) ")
print("""=========================================================================================================""")


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

# INPUT FOR THE MILLER INDICES OF THE PLANES IN THE CRYSTALL

h=int(input("enter the miller  index  h :"))
k=int(input("enter the miller  index  k :"))
l=int(input("enter the miller  index  l :"))
print(f' The given miller indices are {h} {k} {l} and the plane is {h} {k} {l}')

# enter the number of layers to see the normal view of the crystall plane

number_layers=int(input("enter the number of layers to see the normal view of the crystall plane:"))

# USE THE FORMULA TO CALCULATE THE RECIPROCAL LATTICE VECTOR

a1=cl[0]
a2=cl[1]
a3=cl[2]
z=np.cross(a2, a3)
v=np.dot(a1, z)
b1=(2*np.pi*z)/v
b2=(2*np.pi*(np.cross(a3,a1)))/v
b3=(2*np.pi*(np.cross(a1,a2)))/v

rlv.extend([b1 ,b2 ,b3])

print(f" this are  your reciprocal lattice vector formed from the  given primitibe attice vector {rlv}")

print("""=========================================================================================================""")
print("NOTE: for just to  crystall(lattice + basis) enter the  (CRY) and for only normal veiw (NV) for both  crsytall and the normal view (BOTH)")
print("""=========================================================================================================""")

#=====================================================================================================================================================================================================================================================================

def crystall(n1,n2 ,n3 ,cl,basis):
    for j in range(number_basis):
        for n in range(n1):
            for m in range(n2):
                for p in range(n3):

                    r=(n*cl[0] + m*cl[1] + p*cl[2])
                    lattice_x.append(r[0])
                    lattice_y.append(r[1])
                    lattice_z.append(r[2])       
                    
                    r1=(n*cl[0] + m*cl[1] + p*cl[2]) + basis[j]
                    basis1_x.append(r1[0])
                    basis1_y.append(r1[1])
                    basis1_z.append(r1[2])

    fig = mp.figure(figsize=(12,5))

    ax1 = fig.add_subplot(121, projection="3d")

    ax1.scatter(basis1_x,basis1_y,basis1_z, s=70, color="red",label="atoms")

    ax1.scatter(lattice_x,lattice_y,lattice_z,s=70,color="blue",label="lattice")

    ax1.set_title("Complete Crystal")

    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_zlabel("z")

    ax1.legend()
    mp.show()

#=====================================================================================================================================================================================================================================================================


def normal_view(n1,n2, n3, number_basis,cl,basis ,h,k,l):
    for j in range(number_basis):
        for n in range(n1):
            for m in range(n2):
                for p in range(n3):

                    r=(n*cl[0] + m*cl[1] + p*cl[2])
                    lattice_x.append(r[0])
                    lattice_y.append(r[1])
                    lattice_z.append(r[2])       
                    
                    r1=(n*cl[0] + m*cl[1] + p*cl[2]) + basis[j]
                    basis1_x.append(r1[0])
                    basis1_y.append(r1[1])
                    basis1_z.append(r1[2])
                    g=(h*b1 + k*b2 + l*b3)
            
                    d=np.dot(g,r1)

                    d=round(d,5)
                                                                                        #   this part of the code is used to make list of the atoms belonging to a particulatr layers
                    if d not in layers:
                        layers[d]=[]

                    layers[d].append(r1)
            
    for key,value in layers.items():
        print("layer:",key)
        print(value)

    print(layers.keys())

    layer_numbers = sorted(layers.keys())
    normal = g / np.linalg.norm(g)
    random=np.array([1,0,0])

    u=np.cross(normal,random)

    u=u/np.linalg.norm(u)

    v=np.cross(normal,u)

    v=v/np.linalg.norm(v)
    fig = mp.figure(figsize=(12,5))

    ax1 = fig.add_subplot(121, projection="3d")


    for i in range(number_layers):

        layer_atoms=np.array(layers[layer_numbers[i]])

        X=[]
        Y=[]


        for atom in layer_atoms:

            x_new=np.dot(atom,u)
            y_new=np.dot(atom,v)

            X.append(x_new)
            Y.append(y_new)

            ax.scatter( X, Y, s=70, label=f"layer {i}" )

    ax.set_title(f"({h}{k}{l}) surface view")
    mp.show()

#=====================================================================================================================================================================================================================================================================


def crystall_surface_view(n1,n2, n3, number_basis,cl,basis , h , k , l ):
    for j in range(number_basis):
         for n in range(n1):
             for m in range(n2):
                for p in range(n3):

                    r=(n*cl[0] + m*cl[1] + p*cl[2])
                    lattice_x.append(r[0])
                    lattice_y.append(r[1])
                    lattice_z.append(r[2])       
                    
                    r1=(n*cl[0] + m*cl[1] + p*cl[2]) + basis[j]
                    basis1_x.append(r1[0])
                    basis1_y.append(r1[1])
                    basis1_z.append(r1[2])
                    g=(h*b1 + k*b2 + l*b3)
                
                    d=np.dot(g,r1)

                    d=round(d,5)
                                                                                        #   this part of the code is used to make list of the atoms belonging to a particulatr layers
                    if d not in layers:
                        layers[d]=[]

                    layers[d].append(r1)
                

    for key,value in layers.items():
        print("layer:",key)
        print(value)

    print(layers.keys())

    fig = mp.figure(figsize=(12,5))

    ax1 = fig.add_subplot(121, projection="3d")

    ax1.scatter(basis1_x,basis1_y,basis1_z, s=70, color="red",label="atoms")

    ax1.scatter(lattice_x,lattice_y,lattice_z,s=70,color="blue",label="lattice")

    ax1.set_title("Complete Crystal")

    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_zlabel("z")

    ax1.legend()

    layer_numbers = sorted(layers.keys())
    normal = g / np.linalg.norm(g)
    random=np.array([1,0,0])

    u=np.cross(normal,random)

    u=u/np.linalg.norm(u)

    v=np.cross(normal,u)

    v=v/np.linalg.norm(v)

    ax2 = fig.add_subplot(122)


    for i in range(number_layers):

        layer_atoms=np.array(layers[layer_numbers[i]])

        X=[]
        Y=[]


        for atom in layer_atoms:

            x_new=np.dot(atom,u)
            y_new=np.dot(atom,v)

            X.append(x_new)
            Y.append(y_new)

        ax2.scatter( X, Y, s=70, label=f"layer {i}" )

    ax2.set_title(f"({h}{k}{l}) surface view")

    ax2.legend()

    mp.show()
    
