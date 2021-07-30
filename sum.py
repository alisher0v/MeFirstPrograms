number = int(input())

def sum(number):
    answer = 0

    if number == 0:
        return 1

    if number < 0:
        for i in range(number, 1):
            answer += i
    else:
        for i in range(1, number+1):
            answer += i

    return answer

print(sum(number))

