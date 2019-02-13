num = -5
result = None

def negative(num):
    if num < 0:
        result = True
    else:
        result = False
    return result

result = negative(num)
print(result)
