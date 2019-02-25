import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import style
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import axes3d

a11 = np.array([[1,-2,1], [3,1,-2], [7,-6,-1]])
b4 = np.array([6,4,10])

hasil = np.linalg.solve(a11,b4)
print(hasil)
print('x= ', hasil[0])
print('y= ', round(hasil[1]))
print('z= ', hasil[2])


# plt.figure('3D Plotting',figsize=(10,5))
# custom=plt.subplot(111,projection='3d')
# custom.bar3d(xalas,yalas,zalas,xdinding,ydinding,zdinding)
# plt.show()

plt.figure('Ujian 2 SPLTV',figsize=(18,5))

custom1=plt.subplot(131,projection='3d')
x1=np.array([6,0,0])
y1=np.array([0,-3,0])
z1=np.array([0,0,6])
custom1.plot_trisurf(x1,y1,z1,color='r',alpha=0.6)
custom1.scatter(x1,y1,z1,color='b')
custom1.text2D(0.2, 0.8, "x -2y +z = 6", transform=custom1.transAxes)
custom1.set_xlabel('Nilai X')
custom1.set_ylabel('Nilai Y')
custom1.set_zlabel('Nilai Z')

custom2=plt.subplot(132,projection='3d')
x2=np.array([4/3,0,0])
y2=np.array([0,4,0])
z2=np.array([0,0,4/-2])
custom2.plot_trisurf(x2,y2,z2,color='yellow',alpha=0.6)
custom2.scatter(x2,y2,z2,color='red')
custom2.text2D(0.4, 0.6, "3x + y - 2z = 4", transform=custom2.transAxes)
custom2.set_xlabel('Nilai X')
custom2.set_ylabel('Nilai Y')
custom2.set_zlabel('Nilai Z')

custom3=plt.subplot(133,projection='3d')
x3=np.array([10/7,0,0])
y3=np.array([0,10/-6,0])
z3=np.array([0,0,-10])
custom3.plot_trisurf(x3,y3,z3,color='blue',alpha=0.6)
custom3.scatter(x3,y3,z3,color='green')
custom3.text2D(0.2, 0.8, "7x - 6y -z = 10", transform=custom3.transAxes)
custom3.set_xlabel('Nilai X')
custom3.set_ylabel('Nilai Y')
custom3.set_zlabel('Nilai Z')
plt.show()

