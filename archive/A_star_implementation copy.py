# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:49:50 2024

@author: Sachin
"""

'''
Importing the required libraries
'''
import heapq as hq
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math

'''
Defining the Environment
'''
# create a figure and axis object
fig, ax = plt.subplots(figsize=(10,5.5))

# create a Rectangle object
rect = patches.Rectangle((100, 100), 75, 400, linewidth=1, edgecolor='r', facecolor='none')
rect1 = patches.Rectangle((275, 0), 75, 400, linewidth=1, edgecolor='r', facecolor='none')

# Create a hexagon for another obstacle
center_hexagon = (650, 250)
num_vertices_hexagon = 6
hexagon = patches.RegularPolygon(center_hexagon, num_vertices_hexagon, radius=150, orientation=0, linewidth=1, edgecolor='g', facecolor='none')

# Polygon patch for the right half of the square
vertices_right_half_square = [(900, 50), (1100, 50), (1100, 450), (900, 450), (900, 375), (1020, 375), (1020, 125), (900, 125)]

right_half_square = patches.Polygon(vertices_right_half_square, linewidth=1, edgecolor='orange', facecolor='none')


'''
Checking for Obstacles
'''
def check_for_rect(x, y):
    return (x >= 100-5 and x <= 175+5) and (y >= 100-5 and y <= 500)

def check_for_rect1(x, y):
    return (x >= 275-5 and x <= 350+5) and (y >= 0 and y <= 400+5)

def check_for_hexagon(x, y):
    # Define the vertices of the hexagon
    vertices_hexagon = [
        (650 + 155 * np.cos(np.pi/3 * i + np.pi/2), 250 + 155 * np.sin(np.pi/3 * i + np.pi/2)) 
        for i in range(6)
    ]

    # Check if the point (x, y) is inside the hexagon
    # Using the ray-casting algorithm
    count = 0
    for i in range(6):
        x1, y1 = vertices_hexagon[i]
        x2, y2 = vertices_hexagon[(i + 1) % 6]
        if y1 != y2:
            if min(y1, y2) < y <= max(y1, y2) and x <= max(x1, x2):
                x_intersect = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                if x1 == x2 or x <= x_intersect:
                    count += 1
        elif y == y1 and x <= x1:
            count += 1
    return count % 2 == 1

def check_for_right_half_square(x, y):
    if (y >= 45  and y<=130) or (y>=370 and y<=455):
        return (x >= 895 and x <= 1105)
    elif (y>=130 and y<=370):
        return (x >= 1015  and x <= 1105)
    else:
        return False

def check_for_maze(x, y):
    return (x <= 5 or x >= 1195) or (y <= 5 or y >= 495)

def is_move_legal(x, y):
    if check_for_rect(x, y) or check_for_hexagon(x, y) or check_for_rect1(x, y) or check_for_right_half_square(x, y) or check_for_maze(x, y):
        # print("The point is in the obstacle space")
        return False
    else:
        return True

'''
Ask the user for the initial and goal points
'''
def give_inputs():
    x_initial = int(input("Provide the initial x coordinate: "))
    y_initial = int(input("Provide the initial y coordinate: "))
    thetas = int(input("Provide the thetas value: "))

    x_goal = int(input("Provide the goal x coordinate: "))
    y_goal = int(input("Provide the goal y coordinate: "))
    if is_move_legal(x_initial, y_initial) or is_move_legal(x_goal, y_goal):
        print("The initial and goal points are in the obstacle space. Please provide different points.")
        return give_inputs()
    elif thetas < 0 or thetas > 30 :
        print("The value of thetas is not in the range. Please provide a value between 0 and 30")
        return give_inputs()
    else:
        return x_initial, y_initial, thetas, x_goal, y_goal
    


def check_open_list(node, pq):
    for open_node in open_list:
        if node[1][0] == open_node[1][0] and  node[1][1] == open_node[1][1]:
            return True
    return False


'''
When the goal is found, we look for the path
'''
def get_path(predecessor, start, goal):
    path = []
    while goal != start:
        # print("Goal before entering get_path:", goal)
        path.append(goal)
        goal = predecessor[(goal[0], goal[1])]
    path.append(start)
    path.reverse()
    print(path)
    # Plot the path nodes
    for node in path:
        ax.plot(node[0], node[1], 'ro', alpha=0.3, markersize=1)
    return path

def possible_moves(tup , step_size):
    x_old, y_old, theta_old = tup
    move_list = []
    angles = [0, 30, 60, -30, -60]

    for angle in angles:
        theta = (theta_old + angle)
        if (theta == 0):
            theta = 0
        elif (theta == 360):
            theta = 360
        else :
            theta = theta % 360
        x = x_old + step_size * math.cos(np.radians(theta))
        y = y_old + step_size * math.sin(np.radians(theta))  # Use sin for y-coordinate

        # if not is_move_legal(x_int, y_int) and (x_int, y_int) in visited_nodes and abs(theta - theta_old) < 15:
        #     ax.plot(x_int, y_int, 'go', alpha=0.3, markersize=1)
        move_list.append((x, y, theta))
    # print("The move list is: ", move_list)

    return move_list

# def possible_moves(tup , step_size, RPM1, RPM2):
#     Xi, Yi, Thetai = tup
#     move_list = [(0, RPM1), (RPM1, 0), (RPM1, RPM1), (0, RPM2), (RPM2, 0), (RPM2, RPM2), (RPM1, RPM2), (RPM2, RPM1)]

#     moves = []
    
#     for move in move_list:
#         UL,UR= move
#         t = 0
#         r = 0.038
#         L = 0.354
#         dt = 0.1
#         Xn=Xi
#         Yn=Yi
#         Thetan = 3.14 * Thetai / 180

#     # Xi, Yi,Thetai: Input point's coordinates
#     # Xs, Ys: Start point coordinates for plot function
#     # Xn, Yn, Thetan: End point coordintes

#         D=0
#         while t<1:
#             t = t + dt
#             Xs = Xn
#             Ys = Yn
#             Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
#             Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
#             Thetan += (r / L) * (UR - UL) * dt
#             Thetan = 180 * (Thetan) / 3.14
#             if (Thetan == 0):
#                 Thetan = 0
#             elif (Thetan == 360):
#                 Thetan = 360
#             else :
#                 Thetan = Thetan % 360
#             # plt.plot([Xs, Xn], [Ys, Yn], color="blue")

            
#         moves.append((Xn,Yn, Thetan))

def is_in_check(tup , is_in_checker):
    x , y , theta = tup
    if ((x , y)) in is_in_checker :
            thetas = is_in_checker[x, y]
            for theta_c in thetas:
                if abs(theta_c - theta) < 30:
                    # print("theta_c: ", theta_c)
                    # print("theta: ", theta)
                    print("True", thetas)
                    return True
    # print("False", is_in_checker)
    return False

if __name__ == "__main__":

    '''
    Set the time to 0
    '''
    start_time = time.time()
    '''
    Plotting the Environment
    '''
    # Add the patch to the Axes
    ax.add_patch(hexagon)
    ax.add_patch(rect)
    ax.add_patch(rect1)
    ax.add_patch(right_half_square)

    '''
    Specify the initial and goal points here
    '''
    # x_initial, y_initial, thetas, x_goal, y_goal = give_inputs()
    # x_initial = 90
    # y_initial = 400
    x_initial = 60
    y_initial = 200   
    thetas = 0
    # x_goal = 950
    # y_goal = 300
    # x_goal = 100
    # y_goal = 20
    x_goal = 200
    y_goal = 200
    thetag = thetas
    step_size = 1.0

    '''
    Defining the A star Algorithm
    '''
    is_in_checker = {}
    open_list = []
    hq.heapify(open_list)
    c2c = 0
    start = (c2c, (x_initial, y_initial, thetas))
    goal = (c2c, (x_goal, y_goal, thetag))

    # Add a circle around the goal point
    circle_radius = 1.5
    goal_circle = patches.Circle((x_goal, y_goal), circle_radius, edgecolor='b', facecolor='none', linestyle='--')
    ax.add_patch(goal_circle)

    # Set axis labels and limits
    ax.set_xlabel('X-axis $(m)$')
    ax.set_ylabel('Y-axis $(m)$')

    ax.set_xlim(0, 1200)
    ax.set_ylim(0, 500)

    # Plot the initial and goal points
    ax.plot(x_initial, y_initial, 'bo', label='Initial Point')
    ax.plot(x_goal, y_goal, 'ro', label='Goal Point')

    '''
    Initializing the data structures
    '''
    predecessor = {(start[1][0], start[1][1]): None}
    visited_nodes = [(start[1][0], start[1][1])]

    # Add the start node to the open list
    hq.heappush(open_list, start)
    # print(open_list)
    iteration = 0

    c2c_list = {start[1]: 0}
    c2g = np.sqrt((start[1][0] - x_goal)**2 + (start[1][1] - y_goal)**2)

    start = (c2g, (x_initial, y_initial, thetas))
    goal = (c2c, (x_goal, y_goal, thetas))

    # while the open list is not empty
    while not len(open_list)==0 :

        # Pop the node with the smallest cost from the open list
        node = hq.heappop(open_list)
        # if iteration == 4:
        #     print(iteration)
        #     break
        print(node)
        # Iteration to display the visited nodes after every 10000 iterations
        iteration += 1 
        # Distance from the current node to the goal node
        distance_from_goal = np.sqrt((node[1][0] - x_goal)**2 + (node[1][1] - y_goal)**2)

        Thetan = node[1][2] % 360
        x_int = int(round(node[1][0]))
        y_int = int(round(node[1][1]))

        if (x_int, y_int) in is_in_checker:
            thetas = is_in_checker[x_int, y_int]
            thetas.append(Thetan)
            # print("is_in_checker",is_in_checker)
        else:
            thetas = []
            thetas.append(Thetan)
            is_in_checker[x_int, y_int] = thetas
            # print("not is_in_checker",is_in_checker)

        # Check if the node is the goal node, if yes then break the loop and find the path
        if distance_from_goal <= circle_radius and abs(node[1][2] - goal[1][2]) <= 15:
            predecessor[(goal[1][0], goal[1][1])] = (node[1][0], node[1][1])
            path = get_path(predecessor, (start[1][0], start[1][1]), (goal[1][0], goal[1][1]))
            break
        else:
            # print("The iteration is: ", iteration)
            # Setting all the physical constraints of the turtlebot
            # RPM1 = 5
            # RPM2 = 10
            # Sets the cost to move from one node to another
            # move_list = [(0, RPM1), (RPM1, 0), (RPM1, RPM1), (0, RPM2), (RPM2, 0), (RPM2, RPM2), (RPM1, RPM2), (RPM2, RPM1)]
            move_list = possible_moves(node[1], step_size)
            # print("The move list is: ", move_list)
            costs = [step_size, step_size, step_size, step_size, step_size]            
            for move, c2c_step in zip(move_list, costs):
                # print("The move is: ", move)
                Xn, Yn, Thetan = move
                # r = 0.038
                # L = 0.354
                # dt = 0.1
                # t = 0
                # while t<1:
                #     t = t + dt
                #     Xs = Xn
                #     Ys = Yn
                #     Xn += 0.5*r * (move[0] + move[1]) * math.cos(Thetan) * dt
                #     Yn += 0.5*r * (move[0] + move[1]) * math.sin(Thetan) * dt
                #     Thetan += (r / L) * (move[1] - move[0]) * dt
                #     # ax.plot([Xs, Xn], [Ys, Yn], color="blue")
                #     # plt.pause(0.01)
                # print("The Xn and Yn are: ", Xn, Yn, Thetan)

                # Keep the angle in the range of 0 to 360
                # Thetan = 180 * (Thetan) / 3.14
                # if (Thetan == 0):
                #     Thetan = 0
                # elif (Thetan == 360):
                #     Thetan = 360
                # else :
                #     Thetan = Thetan % 360

                # Calculate the new node
                neighbor_x = int(round(Xn))
                neighbor_y = int(round(Yn))


                if is_in_check((neighbor_x, neighbor_y, Thetan), is_in_checker):      
                        # distance from the current node to the goal node
                        c2g = np.sqrt((neighbor_x - x_goal)**2 + (neighbor_y - y_goal)**2)
                        
                        # adding the new node with its costs to be updated
                        new_node = (c2c_step, (Xn, Yn, Thetan))
                        # print("The new node is: ", new_node)

                        # Check if the node is in closed list and if it is in the obstacle space and open list
                        if (neighbor_x, neighbor_y) not in predecessor and is_move_legal(neighbor_x, neighbor_y):
                        # if (neighbor_x, neighbor_y) not in visited_nodes:
                                # if not in closed list, add the node to the closed list
                                predecessor[(neighbor_x, neighbor_y)] = (node[1][0], node[1][1])
                                
                                # update the cost from start to the current node
                                c2c = node[0] + c2c_step
                                c2c_list[(neighbor_x, neighbor_y, Thetan)] = c2c
                                f_value = c2c + c2g

                                # update the node with the new cost
                                new_node = (f_value, (Xn, Yn, Thetan))

                                # Push the new node to the open list
                                hq.heappush(open_list, new_node)
                                # print("The new node is: ", new_node.node)

                                # Add the visited node to the list
                                visited_nodes.append((neighbor_x, neighbor_y))

                                # Plotting the visited nodes
                                if iteration % 3000 == 0:  # Plot every 100th node
                                    visited_x = [node[0] for node in visited_nodes]
                                    visited_y = [node[1] for node in visited_nodes]
                                    ax.plot(visited_x, visited_y, 'go', alpha=0.3, markersize=0.2)
                                    plt.pause(0.01)

                        else:
                            # If the node is in the open list, check if the cost to move from the current node to the neighbor node is less than the cost to move from the start node to the neighbor node
                            if is_move_legal(neighbor_x, neighbor_y):
                                # Check if the sample array is present in the list of tuples
                                for i in range(len(open_list)):
                                    if new_node[1][0] == open_list[i][1][0] and  new_node[1][1] == open_list[i][1][1] and open_list[i][0] > node[0] + c2c_step + c2g:
                                            predecessor[(neighbor_x, neighbor_y)] = (node[1][0], node[1][1])
                                            # distance from the current node to the goal node
                                            c2g = np.sqrt((neighbor_x - x_goal)**2 + (neighbor_y - y_goal)**2)
                                            c2c = node[0] + c2c_step
                                            c2c_list[(neighbor_x, neighbor_y, Thetan)] = c2c
                                            f_value = c2c + c2g
                                            new_node = (f_value, (Xn, Yn, Thetan))
                                            hq.heappush(open_list, new_node)
                                # continue
               
    # Record the end time
    end_time = time.time()

    # Print the time taken to find the path
    print("Time taken to find the path:", (end_time - start_time)/60, "minutes")

    # set the x and y limits of the axis
    ax.set_xlim(0, 1200)
    ax.set_ylim(0, 500)

    # Plot the initial and goal points
    ax.plot(x_initial, y_initial, 'bo', label='Initial Point')
    ax.plot(x_goal, y_goal, 'go', label='Goal Point')

    # plt.pause(0.001)
    # display the plot
    plt.show()


