def solution(d, budget):
    d.sort()
    count = 0
    for i in d:
        if i <= budget:
            count += 1
            budget -= i
    return count


print(solution([1, 3, 2, 5, 4], 9))
