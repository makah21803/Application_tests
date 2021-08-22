import os
import json

dirname = os.path.dirname(__file__)
file = open(dirname+"/test-input.txt", "r")

# list = file.readlines()[0]
input_list = json.load(file)
input_list = [int(i) for i in input_list]

def solution(A):
    def solution(A):
        """
        More efficient solution would be to count the same numbers after sort,
        and just use combinatorics to get the result. That way we itterate just once for each number.
        """
        A.sort()
        count = 0
        for i, n in enumerate(A):
            for j in range(i + 1, len(A)):
                if A[i] == A[j]:
                    count += 1
                else:
                    break

        return count


print(solution(input_list))