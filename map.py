import numpy as np
import cv2
import matplotlib.pyplot as plt
import heapq
import math
from matplotlib.animation import FuncAnimation

def algorithm (start , goal, step_size, img_check, total_clearence):
    print('Algorithm is running')
    
'''
First Plotting the Bloated Figure
'''
# step_size = float((input("Enter the step size: ")))
# radius = int(input("Enter the radius of the robot: "))
# cle = int(input("Enter the clearence: "))
step_size = 1
radius = 5
cle = 5
total_clearence = cle + radius

# Coordinates of the first polygon
x1_polygon1, x2_polygon1, y1_polygon1, y2_polygon1 = 1500 - cle , 1000 + cle , 1750 - cle , 2000 + cle

# Coordinates of the second polygon
x1_polygon2, x2_polygon2, y1_polygon2, y2_polygon2 = 2500 - cle , 0 + cle , 2750 , 1000 + cle

# Create a blank image with size 1190x490
img_check = np.zeros((6000, 2000 , 3), dtype=np.uint8)

# Define the vertices of the first polygon
pts_polygon1 = np.array([[x1_polygon1, y1_polygon1], [x2_polygon1, y1_polygon1], [x2_polygon1, y2_polygon1], [x1_polygon1, y2_polygon1]], np.int32)
pts_polygon1 = pts_polygon1.reshape((-1, 1, 2))

# Define the vertices of the second polygon
pts_polygon2 = np.array([[x1_polygon2, y1_polygon2], [x2_polygon2, y1_polygon2], [x2_polygon2, y2_polygon2], [x1_polygon2, y2_polygon2]], np.int32)
pts_polygon2 = pts_polygon2.reshape((-1, 1, 2))


# Fill the first polygon with white color
cv2.fillPoly(img_check, [pts_polygon1], (255 , 255 , 255))

# Fill the second polygon with white color
cv2.fillPoly(img_check, [pts_polygon2], (255 , 255 , 255))



'''
Now Plotting the Maze on top of the bloated figure
'''

# Coordinates of the first polygon
x1_polygon1, x2_polygon1, y1_polygon1, y2_polygon1 = 1500 , 1000 , 1750 , 2000

# Coordinates of the second polygon
x1_polygon2, x2_polygon2, y1_polygon2, y2_polygon2 = 2500 , 0 , 2750 , 1000


# Create a blank image with size 1190x490
img_ori = np.zeros((6000, 2000 ,3), dtype=np.uint8)

# Define the vertices of the first polygon
pts_polygon1 = np.array([[x1_polygon1, y1_polygon1], [x2_polygon1, y1_polygon1], [x2_polygon1, y2_polygon1], [x1_polygon1, y2_polygon1]], np.int32)
pts_polygon1 = pts_polygon1.reshape((-1, 1, 2))

# Define the vertices of the second polygon
pts_polygon2 = np.array([[x1_polygon2, y1_polygon2], [x2_polygon2, y1_polygon2], [x2_polygon2, y2_polygon2], [x1_polygon2, y2_polygon2]], np.int32)
pts_polygon2 = pts_polygon2.reshape((-1, 1, 2))

# Fill the first polygon with white color
cv2.fillPoly(img_check, [pts_polygon1], (255 , 0 , 0))

# Fill the second polygon with white color
cv2.fillPoly(img_check, [pts_polygon2], (255 , 0 , 0))


'''
To check if the point is in the free region or not

'''
def is_move_legal(tup , img_check, total_clearence):
    x , y = tup
    #pixel_value = img_check[y, x]
#     pixel_value = tuple(pixel_value)
    if x < total_clearence  or x > 1199 - total_clearence or y < total_clearence or y > 499 - total_clearence:
        return False
    elif tuple(img_check[int(round(y)), int(round(x))]) == (255 , 255 , 255) :
        #print(f"Point {point} is in the free region.(here 6)")
        return False
    else :
        return True


start_x = 500
start_y = 1000
start_theta = 0
goal_x = 600
goal_y = 1000
goal_theta = 0

start = (start_x , start_y, start_theta)
goal = (goal_x , goal_y, goal_theta)
Bool1 = is_move_legal((start[0] , start[1]) , img_check, total_clearence)
Bool2 = is_move_legal((goal[0] , goal[1]) , img_check, total_clearence)

if Bool1 == True and Bool2 == True :
    print('correct positions entered algo is executing')
    visited_parent , reached, path, move_list = algorithm (start , goal, step_size, img_check, total_clearence)
    if reached == 1 :
        print('Path is available')
    else  :
        print('Did not reach')
else :
    print('please run the code cell again and enter valid start and goal positions')