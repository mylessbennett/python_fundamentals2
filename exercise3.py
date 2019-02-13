num = 6
result = None

def is_even(num):
    if num % 2 == 0:
        result = True
    else:
        result = False
    return result

result = is_even(num)
print(result)
