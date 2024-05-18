# A-star-implementation-on-a-turtlebot
Hello. Our implementation of A-star expects as inputs from the user the radius of the robot, the clearance from the walls, and the boundaries of the maze, the step size for the robot, the start x position, the start y position, the start orientation, the goal x position, the goal y position and the goal orientation.

![A_Star_on_a_Point_Robot](https://github.com/robosac333/A-star-implementation-on-a-point-robot/blob/main/test.gif)

Recommended to run the code in VSCode and just press the Run Python File button to run it.

The goal and start orientation can be kept anything between 0 and 360 inclusive of 0 and 360(please don't enter negative angle values), that is 0 and 360 are treated as different values. The distance threshold where the algorithm concludes that it has found the goal is 1.5 and the angular threshold where the algorithm concludes that it has found a node that is rightfully orientated with respect to the required goal orientation is 15 degrees. 

Please input appropriate start and goal locations taking into mind the size of the maze and the radius of the robot, although we believe that inappropriate locations should be pointed out by the code.

Packages used in the code:

```sh
1. numpy
2. cv2
3. matplotlib.pyplot
4. heapq
5. math
6. matplotlib.animation.FuncAnimation
```

Also please note that our code has functions for visualization of the exploration space and visualization of the path, but other then these functions it also had some logic that will write an output video to your system that will also show the exploration and path. While running the code you might need to change the video driver to the driver that is supported in your system and the output path as well such that video generated will get stored at the desired path. 

Team Members:
1. Navdeep Singh 
	UID - 120098024
	Directory ID - nsingh19
2. Sachin Jadhav 
	UID - 119484524
	Directory ID - sjd3333

