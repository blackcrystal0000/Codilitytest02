import random

def solution(A, F, M):
    N = len(A) 
    total_known = sum(A)  
    total_missing = M * (N + F) - total_known  

    if total_missing < F or total_missing > F * 6:
        return [0]  

    possible_values = [] 

    def generate_rolls(remaining):
        if len(possible_values) == F:
            return
        for roll in range(1, 7):
            if remaining - roll >= 0:
                possible_values.append(roll)
                generate_rolls(remaining - roll)
                possible_values.pop()

    generate_rolls(total_missing)
    return possible_values

print(solution([3, 2, 4, 3], 2, 4))