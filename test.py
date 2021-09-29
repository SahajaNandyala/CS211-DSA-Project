# taking input
time_limit, grid_size, no_of_trees = map(int,input().split())

trees = []

for i in range(no_of_trees):
    x, y, h, d, c, p = map(int,input().split())
    trees += [{"position":x+y,"x":x,"y":y,"h":h,"d":d,"c":c,"p":p, "value":p*h*d, "weight":c*d*h}]

trees.sort(key=lambda x:x["position"])

time = 0
total_price = 0
current_x = current_y = 0

while time < time_limit:
    time += trees[0]["position"] - current_x - current_y

    if time + trees[0]["d"] < time_limit:
        total_price += trees[0]["price"]
        time += trees[0]["d"]
        current_x = trees[0]["x"]
        current_y = trees[0]["y"]
        print("total_price:", total_price)
        trees.remove(trees[0])
