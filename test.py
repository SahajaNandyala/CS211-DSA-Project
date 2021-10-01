# taking input
time_limit, grid_size, no_of_trees = map(int,input().split())

trees = []
track = []

# print Path function
def path(direction):
    if (direction == 1) : print('cut down')
    elif (direction == 0) : print('cut up')
    elif (direction == 2) : print('cut right')
    elif (direction == 3) : print('cut left')
    elif (direction == -1) : return
# calculate_profit function
def cal_profit(near_tree):
    uProfit = rProfit = dProfit = lProfit = 0
    currentProfit = -1
    direction = -1
    # calculating upprofit
    temp,uProfit = upProfit(near_tree)
    currentProfit = uProfit
    track = temp
    if uProfit != 0 :
        direction = 0

    temp,dProfit = downProfit(near_tree)
    if dProfit > currentProfit:
        currentProfit = dProfit
        track = temp
        direction = 1

    temp,rProfit = rightProfit(near_tree)
    if rProfit > currentProfit:
        currentProfit = rProfit
        track = temp
        direction = 2

    temp,lProfit = leftProfit(near_tree)
    if lProfit > currentProfit:
        currentProfit = lProfit
        track = temp
        direction = 3
    path(direction)
    return track,currentProfit

#upProfit function
def upProfit(near_tree):
    temp = []
    profit = 0
    uptrees = sorted([i for i in trees if near_tree["x"] == i["x"] and near_tree["y"] < i["y"]],key=lambda j: j["y"])
    if len(uptrees) != 0:
        #print("i")
        if near_tree["h"] > abs(uptrees[0]["position"] - near_tree["position"]) and near_tree["weight"] > uptrees[0]["weight"]:
            profit += uptrees[0]["value"]
            temp += [uptrees[0]]
            profit1 = upProfit(uptrees[0])
            profit += profit1[1]
            return temp,profit
        else:return 0,0
    else: return 0,0

#downProfit function
def downProfit(near_tree):
    temp = []
    profit = 0
    downtrees = sorted([i for i in trees if near_tree["x"] == i["x"] and near_tree["y"] > i["y"]],key=lambda j: j["y"])
    if len(downtrees) != 0:
        if near_tree["h"] > abs(downtrees[0]["position"] - near_tree["position"]) and near_tree["weight"] > downtrees[0]["weight"]:
            profit += downtrees[0]["value"]
            temp += [downtrees[0]]
            profit1 = downProfit(downtrees[0])
            profit += profit1[1]
            return temp,profit
        else:return 0,0
    else: return 0,0


#rightProfit function
def rightProfit(near_tree):
    temp = []
    profit = 0
    righttrees = sorted([i for i in trees if near_tree["y"] == i["y"] and near_tree["x"] < i["x"]],key=lambda j: j["x"])
    if len(righttrees) != 0:
        if near_tree["h"] > abs(righttrees[0]["position"] - near_tree["position"]) and near_tree["weight"] > righttrees[0]["weight"]:
            profit += righttrees[0]["value"]
            temp += [righttrees[0]]
            profit1 = rightProfit(righttrees[0])
            profit += profit1[1]
            return temp,profit
        else:return 0,0
    else: return 0,0

#leftProfit function
def leftProfit(near_tree):
    temp = []
    profit = 0
    lefttrees = sorted([i for i in trees if near_tree["y"] == i["y"] and near_tree["x"] > i["x"]],key=lambda j: j["x"])
    if len(lefttrees) != 0:
        if near_tree["h"] > abs(lefttrees[0]["position"] - near_tree["position"]) and near_tree["weight"] > lefttrees[0]["weight"]:
            profit += lefttrees[0]["value"]
            temp += [lefttrees[0]]
            profit1 = leftProfit(lefttrees[0])
            profit += profit1[1]
            return temp,profit
        else: return 0,0
    else: return 0,0

#-----------------------------------------------------------------------------------------------------------------

# taking input of properties for each tree in a list of dicts
for i in range(no_of_trees):
    x, y, h, d, c, p = map(int,input().split())
    trees += [{"position":x+y,"x":x,"y":y,"h":h,"d":d,"c":c,"p":p, "value":p*h*d, "weight":c*d*h}]

# sorting based on position of tree from origin
trees.sort(key=lambda x:x["position"])

time = 0
total_price = 0
current_x = current_y = 0

# moving
while time < time_limit:
    a,final_profit = cal_profit(trees[0])
    #print(a)
    time += trees[0]["position"] - current_x - current_y

    if time + trees[0]["d"] < time_limit:
        total_price += trees[0]["value"] + final_profit
        time += trees[0]["d"]
        if current_x < trees[0]["x"]:
            print("move right\n"* (trees[0]["x"]-current_x ),end="")
        else:
            print("move left\n"* (current_x-trees[0]["x"]),end="")

        if current_y < trees[0]["y"]:
            print("move up\n"* (trees[0]["y"]-current_y ),end="")
        else:
            print("move down\n"* (current_y-trees[0]["y"]),end="")

        current_x = trees[0]["x"]
        current_y = trees[0]["y"]

        trees.remove(trees[0])
    if a != 0 :
        for i in a:
            trees.remove(i)
print(trees)

    #print(final_profit,total_price)
    #if near_tree["weight"] > x[0]["weight"] and near_tree["h"]>x[0]["h"]:
