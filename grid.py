GRID_SIZE=5
START = (0,0)
GOAL = (4,4)
OBSTACLES=[(1,2),(2,2),(3,2)]
def print_grid(agent):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i,j) == agent:
                print('A',end =" ")
            elif (i,j) == START:
                print('S',end=" ")
            elif (i,j) == GOAL:
                print('G',end=" ")
            elif (i,j) in OBSTACLES:
                print('X',end =" ")
            else:
                print('.', end =" ")
        print()
    print()
def valid(x,y):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and (x,y) not in OBSTACLES
agent = START
path =[agent]
print("INITIAL GRID:")
print_grid(agent)
while agent!= GOAL:
    x,y= agent
    if valid(x+1,y):
        agent=(x+1,y)
    elif valid(x,y+1):
        agent=(x,y+1)
    else:
        print("AGENT IS STUCK!!!")
        break
    path.append(agent)
    print_grid(agent)
print("Path Taken:",path)
    