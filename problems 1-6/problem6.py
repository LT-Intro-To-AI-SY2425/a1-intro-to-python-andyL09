# ### 6. **AI Concept: Random Walk Simulation**:
#    - Create a simple program that simulates a 
#       "random walk." The idea is that a point starts at 
#       the origin (0,0) and randomly moves either up, 
#       down, left, or right. Run this simulation for 
#       1000 steps and plot the final position (you can 
#       use `matplotlib` for plotting).

import random

xValue = 0
yValue = 0

# random_number movement guidelines
# 1 == up +1 on yValue
# 2 == down -1 on yValue
# 3 == right +1 on xValue
# 4 == left -1 on xValue

for steps in range(11):
    steps = steps + 1
    
    random_number = random.randint(1, 4)

    if random_number == 1:
        print("up")
        yValue = yValue + 1
    elif random_number == 2:
        print("down")
        yValue = yValue - 1
    elif random_number == 3:
        print("right")
        xValue = xValue + 1
    elif random_number == 4:
        print("left")
        xValue = xValue - 1

print(xValue)
print(yValue)
