import numpy as np
from matplotlib.pyplot import imshow, show

r = 43
s = 41
m = 2

# generate C_r(I)
C_r_I = np.zeros(r) - 1
C_s_J = np.zeros(s) - 1
for x in range(1, r):
	C_r_I[x**2 % r] = 1
for y in range(1, s):
	C_s_J[y**2 % s] = 1
	
# generate A_IJ
A_IJ = np.zeros([r,s])
for I in range(r):
	for J in range(s):
		if I == 0:
			A_IJ[I,J] = 0
		elif J == 0:
			A_IJ[I,J] = 1
		elif C_r_I[I] * C_s_J[J] == 1:
			A_IJ[I,J] = 1
		
# generate A_ij
A_ij = np.zeros([m*r,m*s])
for i in range(m*r):
	for j in range(m*s):
		A_ij[i,j] = A_IJ[i%r,j%s]
A_ij = np.roll(A_ij, int((r+1)/2), axis=0)
A_ij = np.roll(A_ij, int((s+1)/2), axis=1)

# display
imshow(A_ij, cmap="binary_r")
show()