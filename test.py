# taking input
time_limit, grid_size, no_of_trees = map(int,input().split())

trees = []
track = []
temp = []
# calculate_profit function
def cal_profit(near_tree):
    uProfit = rightProfit = downProfit = leftProfit = 0
    currentProfit = 0
    # calculating upprofit
    uProfit = upProfit(near_tree)
    currentProfit = upProfit
    track = temp
    temp.clear()

    downProfit = downProfit(near_tree)
    if downProfit > currentProfit:
        currentProfit = downProfit
        track = temp
        temp.clear()

    rightProfit = rightProfit(near_tree)
    if rightProfit > currentProfit:
        currentProfit = rightProfit
        track = temp
        temp.clear()

    leftProfit = leftProfit(near_tree)
    if leftProfit > currentProfit:
        currentProfit = leftProfit
        track = temp
        temp.clear()

#upProfit function
def upProfit(near_tree):
    near_tree = trees[0]
    profit = 0
    uptrees = sorted([i for i in trees if near_tree["x"] == i["x"] and near_tree["y"] < i["y"]],key=lambda j: j["y"])
    if len(uptrees) != 0:
        if near_tree["h"] > abs(uptrees[0]["position"] - near_tree["position"]) and near_tree["weight"] > uptrees[0]["weight"]:
            profit += uptrees[0]["price"]
            temp += [uptrees[0]]
            temp1 = upProfit(uptrees[0])
            profit += temp1
    return profit

#downProfit function
def downProfit(near_tree):
    near_tree = trees[0]
    profit = 0
    downtrees = sorted([i for i in trees if near_tree["x"] == i["x"] and near_tree["y"] > i["y"]],key=lambda j: j["y"])
    if len(downtrees) != 0:
        if near_tree["h"] > abs(downtrees[0]["position"] - near_tree["position"]) and near_tree["weight"] > downtrees[0]["weight"]:
            profit += downtrees[0]["price"]
            temp += [downtrees[0]]
            temp1 = downProfit(downtrees[0])
            profit += temp1
    return profit

#rightProfit function
def rightProfit(near_tree):
    near_tree = trees[0]
    profit = 0
    righttrees = sorted([i for i in trees if near_tree["y"] == i["y"] and near_tree["x"] < i["x"]],key=lambda j: j["y"])
    if len(righttrees) != 0:
        if near_tree["h"] > abs(righttrees[0]["position"] - near_tree["position"]) and near_tree["weight"] > righttrees[0]["weight"]:
            profit += righttrees[0]["price"]
            temp += [righttrees[0]]
            temp1 = rightProfit(righttrees[0])
            profit += temp1
    return profit

#leftProfit function
def leftProfit(near_tree):
    near_tree = trees[0]
    profit = 0
    lefttrees = sorted([i for i in trees if near_tree["y"] == i["y"] and near_tree["x"] > i["x"]],key=lambda j: j["y"])
    if len(lefttrees) != 0:
        if near_tree["h"] > abs(lefttrees[0]["position"] - near_tree["position"]) and near_tree["weight"] > lefttrees[0]["weight"]:
            profit += lefttrees[0]["price"]
            temp += [lefttrees[0]]
            temp1 = leftProfit(lefttrees[0])
            profit += temp1
    return profit



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
    cal_profit(trees[0])
    time += trees[0]["position"] - current_x - current_y

    if time + trees[0]["d"] < time_limit:
        total_price += trees[0]["value"]
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

    #if near_tree["weight"] > x[0]["weight"] and near_tree["h"]>x[0]["h"]:
