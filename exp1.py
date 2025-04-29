import numpy as np
c=[ [1,1,1,1], [1,-1,1,-1], [1,1,-1,-1], [1,-1,-1,1] ]
d=[int(input(f"Enter D{i+1}: ")) for i in range(4)]
r=sum(np.multiply(c[i],d[i]) for i in range(4))
print("Resultant Channel:", r)
ch=int(input("Enter station (1-4): "))-1
data=sum(np.multiply(r,c[ch]))/4
print("Data bit that was sent:", data)
