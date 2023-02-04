from queue import PriorityQueue

f = open("day1_input.txt", "r")

## Part 1

# maxCalories = 0
# food = []
# for line in f.readlines():
#     line = line.replace("\n", "")
#     if not line.isnumeric():
#         calories = sum(food)
#         if calories > maxCalories:
#             maxCalories = calories
#         food = []
#     else: 
#         food.append(int(line))

# print(maxCalories)

## Part 2

pq = PriorityQueue()

food = []
for line in f.readlines():
    line = line.replace("\n", "")
    if not line.isnumeric():
        calories = sum(food)

        # Python priority queues return the lowest values first, so in order to get the highest values later we store
        # the negative representation.
        pq.put(-calories)
        food = []
    else: 
        food.append(int(line))

first = pq.get()
second = pq.get()
third = pq.get()

total = -(first + second + third)
print(total)


