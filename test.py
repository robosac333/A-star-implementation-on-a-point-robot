import numpy as np
# moves, costs = [(np.cos(np.radians(60)), np.sin(np.radians(60))), (np.cos(np.radians(30)), np.sin(np.radians(30))), (1, 0), (np.cos(np.radians(-30)), np.sin(np.radians(-30))), (np.cos(np.radians(-60)), np.sin(np.radians(-60)))], [1, 1, 1, 1, 1, 1]
# for index, (move, c2c_step) in enumerate(zip(moves, costs)):
#     print(index, move, c2c_step)

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

def obstacle_space(x, y):
    if check_for_rect(x, y) or check_for_hexagon(x, y) or check_for_rect1(x, y) or check_for_right_half_square(x, y) or check_for_maze(x, y):
        # print("The point is in the obstacle space")
        return True
    else:
        return False
    
def give_inputs():
    x_initial = int(input("Provide the initial x coordinate: "))
    y_initial = int(input("Provide the initial y coordinate: "))
    thetas = int(input("Provide the thetas value: "))

    x_goal = int(input("Provide the goal x coordinate: "))
    y_goal = int(input("Provide the goal y coordinate: "))
    if obstacle_space(x_initial, y_initial) or obstacle_space(x_goal, y_goal):
        print("The initial and goal points are in the obstacle space. Please provide different points.")
        return give_inputs()
    elif thetas < 0 or thetas > 30 :
        print("The value of thetas is not in the range. Please provide a value between 0 and 30")
        return give_inputs()
    else:
        return x_initial, y_initial, thetas, x_goal, y_goal
    
x_initial, y_initial, thetas, x_goal, y_goal = give_inputs()