import numpy as np
import cv2
import matplotlib.pyplot as plt
import heapq
import math
from matplotlib.animation import FuncAnimation

'''
Function to plot all the Visited Nodes
'''
def animate_search(visited, circle_center):
    fig, ax = plt.subplots(figsize=(9, 3)) #set animate to 12:5 match map shape
    ax.set_xlim(0, 6000) #set animate x axis
    ax.set_ylim(0, 2000) #set animate y axis

    #show obstacles
    for polygons in obstacles:
        polygon = plt.Polygon(polygons, facecolor="red", edgecolor='black')
        ax.add_patch(polygon)

    # Draw circle
    circle = plt.Circle(circle_center, radius=600, color='red', alpha=0.5)  # Adjust radius as needed
    ax.add_artist(circle)

    points = ax.scatter([], [], s=1, color='blue') 

    def init():
        points.set_offsets(np.empty((0, 2))) 
        return points,

    def update(frame):
        skip = 50000 #set flames skip
        frame *= skip 
        visited_points = np.array(visited[:frame+1])
        points.set_offsets(visited_points)
        return points,

    ani = FuncAnimation(fig, update, frames=len(visited), init_func=init, blit=True, interval=1)
    plt.show()


'''
Animate the path
'''
def animate_path(path, circle_center):
    fig, ax = plt.subplots(figsize=(9,3))
    ax.set_xlim(0, 6000)
    ax.set_ylim(0, 2000)

    for polygons in obstacles:
        polygon = plt.Polygon(polygons, facecolor="gray", edgecolor='black')
        ax.add_patch(polygon)

    # Draw circle
    circle = plt.Circle(circle_center, radius=600, color='black', alpha=0.5)  # Adjust radius as needed
    ax.add_artist(circle)

    line, = ax.plot([], [], 'b-', lw=2)  # Path line

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        skip = 20 #set flames skip
        frame *= skip
        x, y = zip(*path[:frame+1]) #get path
        line.set_data(x, y)
        return line,

    ani = FuncAnimation(fig, update, frames=len(path), init_func=init, blit=True, interval=50)
    plt.show()

obstacles = [
    [(1500, 1000), (1500, 2000), (1750, 2000), (1750, 1000)],

    [(2500, 0), (2500, 1000), (2750, 1000), (2750, 0)]
]

move_list = [
    (0, 5), (5, 0), (5, 5), (0, 10), (10, 0), (10, 10), (5, 10), (10, 5)
]

coord_list = []

circle_center = (4200, 1200)

animate_search(move_list, circle_center)

animate_path(coord_list, circle_center)