import time

t_0 = time.time()


def b_to_i(binary_num: list) -> int:
    total = 0
    for i in range(len(binary_num)):
        if binary_num[len(binary_num) - 1 - i] == 1:
            total += 2 ** i
    return total


with open("./data/input-day3.txt") as f:
    nums = [line.strip() for line in f]

gamma = [0] * len(nums[0])
sigma = [0] * len(nums[0])

for num in nums:
    for i in range(len(num)):
        gamma[i] += 1 if num[i] == "1" else 0

for i in range(len(gamma)):
    gamma[i] = 1 if gamma[i] > len(nums) - gamma[i] else 0
    sigma[i] = 0 if gamma[i] == 1 else 1

print(b_to_i(gamma) * b_to_i(sigma))

print(len(nums))

# Go through all nums and keep ones with most
# for i in range(len(nums)):
#     if int(nums[i][0]) == gamma[0]:
#         print(nums[i][0], gamma[0])
#
#         del(nums[i])

for i in range(len(nums[0])):
    nums = [num for num in nums if int(num[i]) == gamma[i]]

print(len(nums))
nums = [int(num) for num in nums[0]]
num_a = []

for num in nums:
    num_a.append(0 if num == 1 else 1)

result = b_to_i(nums) * b_to_i(num_a)
print(result)