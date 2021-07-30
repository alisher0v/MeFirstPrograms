a = int(input())
b = int(input())


def resault(a, b):
    if a < b:
        return "<"
    elif a > b: 
        return ">"
    else:
        return "="


print(resault(a, b))