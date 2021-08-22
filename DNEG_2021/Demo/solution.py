import os
import json

dirname = os.path.dirname(__file__)
file = open(dirname+"/test-input.txt", "r")

# list = file.readlines()[0]
input_list = json.load(file)
input_list = [int(i) for i in input_list]

def solution(A):
    # write your code in Python 3.6
    for i, a in enumerate(A):
        if a < 0:
            A.pop(i)
            continue

    maxA = max(A)
    if maxA >= 0 and len(A) > 0:
        for n in range(1, maxA):
            if n in A:
                continue
            return n
        return maxA + 1
    else:
        return 1

print(solution(input_list))
