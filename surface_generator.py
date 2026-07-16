# =================================================================
#    surface lattice normal to the given miller indices
# =================================================================

import numpy as np
import matplotlib.pyplot as mp

name = input("Enter your good name pls:")

print("HELLO wlecome to the plane perpendicular to given miller indices")

# input for the surface size and the crystal size

a = float(input("enter the lattice constant a :"))
n1 = int(input("enter the number of lattice points in the x direction:"))
n2 = int(input("enter the number of lattice points in the y direction:"))
n3 = int(input("enter the number of lattice points in the z direction:"))

basis = []
cl = []
rlv = []
slv = []
spv = []
spv_x = []
spv_y = []
spv_z = []
basis1_x = []
basis1_y = []
basis1_z = []
layers = {}            

# this part is to choose type of lattice: conventional or custom
print("""=========================================================================================================""")
print(" NOTE:  For The  conventional lattice enter (con) and for the particular or custom lattice enter (cus)")
print("""=========================================================================================================""")

custom_conventional = input(" Enter the type of lattice you want conventional or custom:")

if custom_conventional == "con":
    a1 = np.array([a, 0, 0])
    a2 = np.array([0, a, 0])
    a3 = np.array([0, 0, a])
    cl.extend([a1, a2, a3])
else:
    for i in range(3):
        ax = float(input("enter the x-direction of your lattice vector:  "))
        ay = float(input("enter the y-direction of your lattice vector:  "))
        az = float(input("enter the z-direction of your lattice vector:  "))
        a1 = np.array([ax, ay, az])
        print(f'your given lattice vector {a1} is stored in the system')
        cl.append(a1)

print(f" This is the lattice vector chosen for the crystal {cl}")

print("""=============================================================================================================================================""")
print("NOTE: SC, BCC, FCC, are built in. Enter (0) to type in a custom basis for any other structure "
      "(monoclinic, diamond, rock salt, perovskite, etc.)")
print("""=============================================================================================================================================""")

SC_BCC_FCC_O = input("Enter the type of cell you want in the lattice based on the note just given above :")

if SC_BCC_FCC_O == "SC":
    b1 = np.array([0, 0, 0])
    basis.append(b1)

elif SC_BCC_FCC_O == "BCC":
    b1 = np.array([0, 0, 0])
    b2 = np.array([.5, .5, .5])
    basis.extend([b1, b2])

elif SC_BCC_FCC_O == "FCC":
    b1 = np.array([0, 0, 0])
    b2 = np.array([0.5, 0.5, 0])
    b3 = np.array([0.5, 0, 0.5])
    b4 = np.array([0, 0.5, 0.5])
    basis.extend([b1, b2, b3, b4])

elif SC_BCC_FCC_O == "0":
    number_basis = int(input("enter the number of basis atom in the crystal:"))
    for i in range(number_basis):
        bx = float(input("enter the x-direction of the basis vector:"))
        by = float(input("enter the y-direction of the  basis vector:"))
        bz = float(input("enter the z-direction of  the basis vector:"))
        b1 = np.array([bx, by, bz])
        print(f'your given basis {b1} is stored in the system')
        basis.append(b1)

print(f' These are all the basis given as input {basis}')

# here we form the reciprocal lattice vectors b1 b2 b3 and store them in reciprocal lattice vector(rlv)


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

# INPUT FOR THE MILLER INDICES OF THE PLANES IN THE CRYSTAL

h = int(input("enter the miller  index  h :"))
k = int(input("enter the miller  index  k :"))
l = int(input("enter the miller  index  l :"))
print(f' The given miller indices are {h} {k} {l} and the plane is {h} {k} {l}')

g = (h * b1 + k * b2 + l * b3)                                                # reciprocal vector

print(f"  this is your  normal  vector {g}")

# here we find all vectors perpendicular to g, then take the one with least magnitude

for n in range(-n1, n1 + 1):
    for m in range(-n2, n2 + 1):
        for p in range(-n3, n3 + 1):

            t = (n * cl[0] + m * cl[1] + p * cl[2])                     
            x = np.dot(g, t)

            if np.isclose(x, 0):
                ui = n * a1 + m * a2 + p * a3

                if np.linalg.norm(ui) > 1e-8:
                    slv.append(ui)

print(f"  this are the  {slv}")

slv.sort(key=np.linalg.norm)

u = slv[0]                                           # a vector in the surface perpendicular to g
normal = g / np.linalg.norm(g)

v = None
for vector in slv[1:]:
    cross = np.cross(u, vector)
    if np.linalg.norm(cross) > 1e-8:
        v = vector
        break

print(f" this my v vector {v}")

d = 2*np.pi / np.linalg.norm(g)                                             # interplaner distance between the plans 
          
number_layers = int(input("enter the number of layer you want :"))

# this part is to generate all the points in the surface 
for n in range(n1):
    for m in range(n2):
        for p in range(number_layers):
                s=n*u+ m*v + p*d*normal
                spv.append(s)
                spv_x.append(s[0])
                spv_y.append(s[1])
                spv_z.append(s[2])

demon = np.dot(np.cross(u, v), normal)

def surface_coords(pos):

    f = np.dot(pos, normal)                 # height above the surface
    pos_flat = pos - f * normal                # pos with the out-of-surface part removed
    a = np.dot(np.cross(pos_flat, v), normal) /demon
    b = np.dot(np.cross(u, pos_flat), normal) /demon
    return a, b, f
 
p = n1 + n2 + n3 + number_layers + 5            # generous search radius; basis shifts are simple fractions of a1,a2,a3
 
possible = []
for n in range(-p, p + 1):
    for m in range(-p, p + 1):
        for p in range(-p, p + 1):
            r=(n*cl[0] + m*cl[1] + p*cl[2])
            for b in basis:
                pos = r + b
                a, b, f = surface_coords(pos)
                if f < -1e-6:
                    continue                                                            
                if -1e-6 <= a < n1 - 1e-6 and -1e-6 <= b < n2 - 1e-6:
                    possible.append((round(f, 6), pos))
 
for f, pos in possible:
    layers.setdefault(f, []).append(pos)


layer_numbers = sorted(layers.keys())[:number_layers]           
for key in layer_numbers:
    print("layer:", key)
    print(layers[key])

for key in layer_numbers:
    for pos in layers[key]:
        basis1_x.append(pos[0])
        basis1_y.append(pos[1])
        basis1_z.append(pos[2])

print(layer_numbers)

print(f" hello {spv}")

# this part is the plot

fig = mp.figure(figsize=(12, 5))

ax1 = fig.add_subplot(221, projection="3d")

ax1.scatter(spv_x, spv_y, spv_z, s=50, color="black", label=" lattice points of plane ")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")
ax1.legend()

ax2 = fig.add_subplot(122, projection="3d")

ax2.scatter(basis1_x, basis1_y, basis1_z, s=70, color="red", label="atoms")
ax2.scatter(spv_x, spv_y, spv_z, s=50, color="black", label="surface lattice points")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("z")
ax2.legend()
ax2.set_title(f"({h}{k}{l}) surface view")

X = []
Y = []
Z = []

for layer_key in layer_numbers:
    for atom in layers[layer_key]:
        X.append(atom[0])
        Y.append(atom[1])
        Z.append(atom[2])

ax3 = fig.add_subplot(223, projection="3d")
ax3.scatter(X, Y, Z)
mp.show()

