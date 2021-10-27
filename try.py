time_limit, grid_size, no_of_trees = map(int,input().split())

trees = []
temp1 =[]
temp2 = []
temp3 = []
temp4 = []
uProfit = 0
lProfit = 0
rProfit = 0
dProfit = 0

# calculate_profit function
def cal_profit(trees_dict,tree):
    currentProfit = 0

    # calculating upprofit
    upProfit(trees_dict,tree)
    currentProfit = uProfit
    direction = 0

    downProfit(trees_dict,tree)
    if dProfit > currentProfit:
        currentProfit = dProfit
        direction = 1

    rightProfit(trees_dict,tree)
    if rProfit > currentProfit:
        currentProfit = rProfit
        direction = 2

    leftProfit(trees_dict,tree)
    if lProfit > currentProfit:
        currentProfit = lProfit
        direction = 3

    return direction,currentProfit


#upProfit function
def upProfit(trees_dict,near_tree):
    global uProfit
    uptrees = sorted([i for i in trees_dict if near_tree["x"] == i["x"] and near_tree["y"] < i["y"]],key=lambda j: j["y"])
    for i in uptrees:
        if near_tree["h"] > abs(i["position"] - near_tree["position"]) and near_tree["weight"] > i["weight"]:
            uProfit += i["value"]
            temp1.append(i)
            near_tree = i
        else:
            break


#downProfit function
def downProfit(trees_dict,near_tree):
    global dProfit
    downtrees = sorted([i for i in trees_dict if near_tree["x"] == i["x"] and near_tree["y"] > i["y"]],key=lambda j: -j["y"])
    for i in downtrees:
        if near_tree["h"] > abs(i["position"] - near_tree["position"]) and near_tree["weight"] > i["weight"]:
            dProfit += i["value"]
            temp2.append(i)
            near_tree = i
        else:
            break


# rightProfit function
def rightProfit(trees_dict,near_tree):
    global rProfit
    righttrees = sorted([i for i in trees_dict if near_tree["y"] == i["y"] and near_tree["x"] < i["x"]],key=lambda j: j["x"])
    for i in righttrees:
        if near_tree["h"] > abs(i["position"] - near_tree["position"]) and near_tree["weight"] > i["weight"]:
            rProfit += i["value"]
            temp3.append(i)
            near_tree = i
        else:
            break

# leftProfit function
def leftProfit(trees_dict,near_tree):
    global lProfit
    lefttrees = sorted([i for i in trees_dict if near_tree["y"] == i["y"] and near_tree["x"] > i["x"]],key = lambda j: -j["x"])
    for i in lefttrees:
        if near_tree["h"] > abs(i["position"] - near_tree["position"]) and near_tree["weight"] > i["weight"]:
            lProfit += i["value"]
            temp4.append(i)
            near_tree = i
        else:
            break

def path1():
    list = [i for i in trees if abs(i["x"]-current_x)+abs(i["y"]-current_y)+i["d"] <= t]
    list.sort(key = lambda x: (-((x["value"]+x["tree_profit"])/(abs(x["x"]-current_x)+abs(x["y"]-current_y)+x["d"])),-(x["value"])))
    if len(list) != 0:
        return list
    else:
        return []

def path2():
    list = [i for i in trees2 if abs(i["x"]-current_x)+abs(i["y"]-current_y)+i["d"] <= t]
    list.sort(key = lambda x: (-(x["value"]/(abs(x["x"]-current_x)+abs(x["y"]-current_y)+x["d"])),-(x["value"])))
    if len(list) != 0:
        return list
    else:
        return []


#-----------------------------------------------------------------------------------------------------------------

# taking input of properties for each tree in a list of dicts
for i in range(no_of_trees):
    x, y, h, d, c, p = map(int,input().split())
    trees += [{"position":x+y,"x":x,"y":y,"h":h,"d":d,"c":c,"p":p, "value":p*h*d, "weight":c*d*h, "tree_profit":0}]

trees2 = trees.copy()

time = 0
current_x = 0
current_y = 0
t = time_limit
final_profit1 = 0
directions1 = []
# path1
for i in trees:
    i["tree_profit"] = cal_profit(trees,i)[1]
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    uProfit = 0
    lProfit = 0
    rProfit = 0
    dProfit = 0

trees.sort(key = lambda x: x["position"])

# moving
while time <= time_limit and len(trees)>0:

    direction, full_profit = cal_profit(trees,trees[0])

    if current_x < trees[0]["x"]:
        directions1.append("move right\n"*(trees[0]["x"]-current_x))
        t -= trees[0]["x"]-current_x

    elif current_x > trees[0]["x"]:
        directions1.append("move left\n"*(current_x-trees[0]["x"]))
        t -= current_x-trees[0]["x"]

    if current_y < trees[0]["y"]:
        directions1.append("move up\n"*(trees[0]["y"]-current_y))
        t -= trees[0]["y"]-current_y

    elif current_y > trees[0]["y"]:
        directions1.append("move down\n"*(current_y-trees[0]["y"]))
        t -= current_y-trees[0]["y"]

#------------------- cutting trees ------------

    if direction == 0 and (t - trees[0]["d"]) >= 0 :
        directions1.append("cut up\n")
        a = temp1
        t -= trees[0]["d"]
        final_profit1 += full_profit + trees[0]["value"]

    elif direction == 1 and (t - trees[0]["d"]) >= 0:
        directions1.append("cut down\n")
        a = temp2
        t -= trees[0]["d"]
        final_profit1 += full_profit + trees[0]["value"]

    elif direction == 2 and (t - trees[0]["d"]) >= 0:
        directions1.append("cut right\n")
        a = temp3
        t -= trees[0]["d"]
        final_profit1 += full_profit + trees[0]["value"]

    elif direction == 3 and (t - trees[0]["d"]) >= 0:
        directions1.append("cut left\n")
        a = temp4
        t -= trees[0]["d"]
        final_profit1 += full_profit + trees[0]["value"]

    time += trees[0]["d"] + abs(trees[0]["x"]-current_x)+abs(trees[0]["y"]-current_y)

    current_x = trees[0]["x"]
    current_y = trees[0]["y"]

    trees.remove(trees[0])

    if len(a) != 0 and len(trees) != 0:
        for i in a:
            trees.remove(i)
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    uProfit = 0
    lProfit = 0
    rProfit = 0
    dProfit = 0

    trees = path1()

# path2
time = 0
current_x = 0
current_y = 0
t = time_limit
directions2 = []
final_profit2 = 0

temp1 = []
temp2 = []
temp3 = []
temp4 = []
uProfit = 0
lProfit = 0
rProfit = 0
dProfit = 0
a = []
trees2.sort(key = lambda x: x["position"])

# moving
while time <= time_limit and len(trees2)>0:

    direction, full_profit = cal_profit(trees2,trees2[0])

    if current_x < trees2[0]["x"]:
        directions2.append("move right\n"*(trees2[0]["x"]-current_x))
        t -= trees2[0]["x"]-current_x

    elif current_x > trees2[0]["x"]:
        directions2.append("move left\n"*(current_x-trees2[0]["x"]))
        t -= current_x-trees2[0]["x"]

    if current_y < trees2[0]["y"]:
        directions2.append("move up\n"*(trees2[0]["y"]-current_y))
        t -= trees2[0]["y"]-current_y

    elif current_y > trees2[0]["y"]:
        directions2.append("move down\n"*(current_y-trees2[0]["y"]))
        t -= current_y-trees2[0]["y"]

#------------------- cutting trees2 ------------

    if direction == 0 and (t - trees2[0]["d"]) >= 0 :
        directions2.append("cut up\n")
        a = temp1
        t -= trees2[0]["d"]
        final_profit2 += full_profit + trees2[0]["value"]

    elif direction == 1 and (t - trees2[0]["d"]) >= 0:
        directions2.append("cut down\n")
        a = temp2
        t -= trees2[0]["d"]
        final_profit2 += full_profit + trees2[0]["value"]

    elif direction == 2 and (t - trees2[0]["d"]) >= 0:
        directions2.append("cut right\n")
        a = temp3
        t -= trees2[0]["d"]
        final_profit2 += full_profit + trees2[0]["value"]

    elif direction == 3 and (t - trees2[0]["d"]) >= 0:
        directions2.append("cut left\n")
        a = temp4
        t -= trees2[0]["d"]
        final_profit2 += full_profit + trees2[0]["value"]

    time += trees2[0]["d"] + abs(trees2[0]["x"]-current_x)+abs(trees2[0]["y"]-current_y)

    current_x = trees2[0]["x"]
    current_y = trees2[0]["y"]

    trees2.remove(trees2[0])
    if len(a) != 0 and len(trees2) != 0:
        for i in a:
            trees2.remove(i)
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    uProfit = 0
    lProfit = 0
    rProfit = 0
    dProfit = 0

    trees2 = path2()

if final_profit1 > final_profit2:
    for i in directions1:
        print(i, end="")
else:
    for i in directions2:
        print(i, end="")
