# taking input
time_limit, grid_size, no_of_trees = map(int,input().split())

trees = []

# calculate_profit function
def cal_profit(near_tree):
    uProfit = rProfit = dProfit = lProfit = 0
    currentProfit = 0
    direction = -1

    # calculating upprofit
    temp,uProfit = upProfit(near_tree)
    currentProfit = uProfit
    if uProfit != 0:
        direction = 0

    # calculating downProfit
    temp,dProfit = downProfit(near_tree)
    if dProfit > currentProfit:
        currentProfit = dProfit
        direction = 1

    # calculating rightProfit
    temp,rProfit = rightProfit(near_tree)
    if rProfit > currentProfit:
        currentProfit = rProfit
        direction = 2

    # calculating leftProfit
    temp,lProfit = leftProfit(near_tree)
    if lProfit > currentProfit:
        currentProfit = lProfit
        direction = 3

    return direction,currentProfit

#upProfit function
def upProfit(near_tree):
    temp = []
    profit = 0
    uptrees = sorted([i for i in trees if near_tree["x"] == i["x"] and near_tree["y"] < i["y"]],key=lambda j: j["y"])
    if len(uptrees) != 0:
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

# leftProfit function
def leftProfit(near_tree):
    temp = []
    profit = 0
    lefttrees = sorted([i for i in trees if near_tree["y"] == i["y"] and near_tree["x"] > i["x"]],key = lambda j: j["x"])
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
    trees += [{"position":x+y,"x":x,"y":y,"h":h,"d":d,"c":c,"p":p, "value":p*h*d, "weight":c*d*h, "full_profit":0}]

# sorting all tree values based on position
trees.sort(key=lambda x:(x["position"]))

time = 0
total_price = 0
current_x = current_y = 0
t = time_limit

# moving
if time < time_limit and len(trees)>0:
    direction,final_profit = cal_profit(trees[0])

    # printing directions to move
    if current_x < trees[0]["x"] and t >= 0:
        print("move right\n"*min(t,trees[0]["x"]-current_x),end="")
        t -= trees[0]["x"]-current_x
    elif current_x > trees[0]["x"] and t >= 0:
        print("move left\n"* min(t,current_x-trees[0]["x"]),end="")
        t -= current_x-trees[0]["x"]
    if current_y < trees[0]["y"] and t >= 0:
        print("move up\n"* min(t,trees[0]["y"]-current_y ),end="")
        t -= trees[0]["y"]-current_y
    elif current_y > trees[0]["y"] and t >= 0:
        print("move down\n"* min(t,current_y-trees[0]["y"]),end="")
        t -= current_y-trees[0]["y"]

#-------------------------printing direction to cut tree------------------------
    if direction == 0 and t >= 0:
        print("cut up")
        t -= trees[0]["d"]
    elif abs(direction) == 1 and t >= 0:
        print("cut down")
        t -= trees[0]["d"]
    elif direction == 2 and t >= 0:
        print("cut right")
        t -= trees[0]["d"]
    elif direction == 3 and t >= 0:
        print("cut left")
        t -= trees[0]["d"]
