import math

dog=(2,5)
wolf=(5,9)

dx=wolf[0]-dog[0]
dy=wolf[1]-dog[1]

distance=math.sqrt(dx**2+dy**2)
print(distance)