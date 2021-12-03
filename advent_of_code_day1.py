# Advent of Code 2021 Day 1

# To open the file
with open("./data/input-day1.txt") as f:
    depths = []

    for line in f:
        depths.append(int(line))

increases = 0

for i in range(1, len(depths)):
    if depths[i] > depths [i-1]:
        increases += 1

print(increases)

increases = 0

for i in range(3, len(depths)):
    if sum(depths[i-3:i]) > sum(depths[i-4:i-1]):
        increases += 1

print(increases)
